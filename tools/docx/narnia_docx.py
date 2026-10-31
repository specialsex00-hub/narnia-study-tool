#!/usr/bin/env python3
"""ナルニア国物語の Word 教材（~/英語/）を編集するための道具。

  python3 narnia_docx.py dump  FILE.docx            本文を表示（下線=[U]…[/U]、赤太字=[R]…[/R]、マーカー=[M]…[/M]）
  python3 narnia_docx.py yaku-add  PAGES.json       対訳に新しいページを追記（"file" で章ごとの別ファイルも指定可）
  python3 narnia_docx.py yaku-new  PAGES.json       章ごとの新しい対訳ファイルを作る（書式は既存の対訳と同じ）
  python3 narnia_docx.py kadai-add SECTION.json     課題ファイルに授業ワーク（解答）を追記
  python3 narnia_docx.py mark  MARKS.json           対訳の課題の文に黄色マーカー（＋下線）を引く

共通の安全策:
  - Word で開いている（~$ロックファイルがある）ファイルは触らない
  - 書き換える前に ~/英語/.narnia_backup/ に日時つきでコピーを残す
  - 書き換え後に XML の妥当性と、本文テキストが意図どおり変わったかを確認する

JSON の形式は tools/docx/README.md と tools/docx/examples/（実際に使ったもの）を参照。
"""
import datetime
import json
import os
import re
import shutil
import sys
import tempfile
import zipfile
from xml.sax.saxutils import escape, unescape
import xml.dom.minidom

EIGO = os.environ.get('NARNIA_EIGO_DIR') or os.path.expanduser('~/英語')   # テスト時は別フォルダを指定できる
YAKU = os.path.join(EIGO, 'ナルニア国物語_対訳.docx')
KADAI = os.path.join(EIGO, 'ナルニア国物語_課題.docx')
BACKUP_DIR = os.path.join(EIGO, '.narnia_backup')
MARK_FILL = 'FFF176'   # 黄色マーカー（Word の蛍光ペンは Mac のプレビューで見えないので網かけを使う）


# ---------------- docx I/O ----------------
def ensure_closed(path):
    lock = os.path.join(os.path.dirname(path), '~$' + os.path.basename(path)[2:])
    if os.path.exists(lock):
        sys.exit(f'Word で開かれています。閉じてから実行してください: {os.path.basename(path)}')


def read_xml(path):
    with zipfile.ZipFile(path) as z:
        return z.read('word/document.xml').decode('utf-8')


def write_xml(path, xml_text, backup=True):
    xml.dom.minidom.parseString(xml_text.encode('utf-8'))   # validity check
    if backup:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S-%f')[:-3]
        shutil.copy2(path, os.path.join(BACKUP_DIR, f'{stamp}_{os.path.basename(path)}'))
    fd, tmp = tempfile.mkstemp(suffix='.docx'); os.close(fd)
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = xml_text.encode('utf-8') if item.filename == 'word/document.xml' else zin.read(item.filename)
            zout.writestr(item, data)
    shutil.copymode(path, tmp)   # keep the original file permissions
    shutil.move(tmp, path)
    print(f'保存しました: {path}' + (f'（バックアップ: {BACKUP_DIR}）' if backup else ''))


PARA_RE = re.compile(r'<w:p[ >](?:(?!</w:p>).)*?</w:p>', re.S)
RUN_RE = re.compile(r'<w:r>(?:<w:rPr>(.*?)</w:rPr>)?((?:<w:lastRenderedPageBreak/>)?)<w:t(?: [^>]*)?>(.*?)</w:t></w:r>|<w:r[ >].*?</w:r>', re.S)


def para_text(p):
    return unescape(''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', p)))


# ---------------- paragraph builders (same formatting as the existing files) ----------------
def run(text, bold=False, color=None, size=None, underline=False):
    rpr = ''
    if bold: rpr += '<w:b/><w:bCs/>'
    if underline: rpr += '<w:u w:val="single"/>'
    if color: rpr += f'<w:color w:val="{color}"/>'
    if size: rpr += f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
    rpr = f'<w:rPr>{rpr}</w:rPr>' if rpr else ''
    return f'<w:r>{rpr}<w:t xml:space="preserve">{escape(text)}</w:t></w:r>'


def para(runs, ppr=''):
    return f"<w:p><w:pPr>{ppr}</w:pPr>{''.join(runs)}</w:p>"


def heading1(text, page_break=False):
    pb = '<w:pageBreakBefore/>' if page_break else ''
    return para([run(text)], f'<w:pStyle w:val="1"/>{pb}<w:pBdr><w:bottom w:val="single" w:sz="6" w:space="4" w:color="999999"/></w:pBdr><w:spacing w:before="400" w:after="200"/>')


def yaku_en(text):  return para([run(text)], '<w:spacing w:before="200" w:after="40"/>')
def yaku_jp(text):  return para([run(text)], '<w:spacing w:after="120"/><w:ind w:left="340"/>')
def k_loc(text):    return para([run(text, bold=True, color='8A5A3B')], '<w:keepNext/><w:spacing w:before="360" w:after="40"/>')
def k_note(text):   return para([run(text, color='7F7F7F', size=18)], '<w:spacing w:after="80"/>')


def k_en(text):
    """英文。__下線__ で囲んだ部分に下線。"""
    parts = text.split('__')
    return para([run(t, underline=(i % 2 == 1)) for i, t in enumerate(parts) if t], '<w:keepNext/><w:spacing w:before="40" w:after="60"/>')


def k_instr(text):
    return para([run('【指示】', bold=True, color='C0504D', size=20), run(text, color='C0504D', size=20)], '<w:keepNext/><w:spacing w:after="80"/>')


def k_label(text):
    return para([run(f'【{text}】', bold=True, size=20)], '<w:keepNext/><w:spacing w:before="80" w:after="20"/><w:ind w:left="340"/>')


def k_body(text, bullet):
    if bullet:
        return para([run('・' + text, size=20)], '<w:spacing w:after="40"/><w:ind w:left="567" w:hanging="227"/>')
    return para([run(text)], '<w:spacing w:after="80"/><w:ind w:left="340"/>')


def k_drawing_box():
    b = ''.join(f'<w:{s} w:val="single" w:sz="8" w:color="999999"/>' for s in ('top', 'left', 'bottom', 'right'))
    return (f'<w:tbl><w:tblPr><w:tblW w:w="5000" w:type="pct"/><w:tblBorders>{b}</w:tblBorders></w:tblPr>'
            '<w:tblGrid><w:gridCol w:w="9360"/></w:tblGrid><w:tr><w:trPr><w:trHeight w:val="3600" w:hRule="exact"/></w:trPr>'
            '<w:tc><w:tcPr><w:tcW w:w="5000" w:type="pct"/></w:tcPr>' + para([run('（ここに絵を描く）', color='999999', size=18)]) +
            '</w:tc></w:tr></w:tbl>' + para([], '<w:spacing w:after="80"/>'))


# ---------------- commands ----------------
def cmd_dump(path):
    d = read_xml(path)
    for p in PARA_RE.findall(d):
        out = ''
        for r in re.findall(r'<w:r[ >].*?</w:r>', p, re.S):
            t = unescape(''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', r)))
            if not t: continue
            if '<w:u ' in r and 'w:val="none"' not in r: t = f'[U]{t}[/U]'
            if re.search(r'<w:color w:val="(EE0000|FF0000|C00000)"', r) and '<w:b/>' in r: t = f'[R]{t}[/R]'
            if MARK_FILL in r or '<w:highlight' in r: t = f'[M]{t}[/M]'
            out += t
        if out: print(out)


def yaku_path(spec):
    """spec の "file"（~/英語/ の中のファイル名）。省略時は Chapter 5 の対訳。"""
    return os.path.join(EIGO, spec['file']) if isinstance(spec, dict) and spec.get('file') else YAKU


def pages_xml(pages):
    out = []
    for page, pairs in pages.items():
        out.append(heading1(page))
        for en, jp in pairs:
            out += [yaku_en(en), yaku_jp(jp)]
    return ''.join(out)


def cmd_yaku_new(spec_path):
    """PAGES.json: {"file": "ナルニア国物語_対訳_Chapter6.docx", "title": "ナルニア国物語 対訳 Chapter 6 (62〜64)",
                    "pages": {"62": [["英文", "和訳"], ...], ...}}
    既存の対訳（Chapter 5）をひな形に、スタイル・余白はそのままで本文だけ入れ替えた新しいファイルを作る。"""
    spec = json.load(open(spec_path, encoding='utf-8'))
    path = yaku_path(spec)
    if path == YAKU or os.path.exists(path): sys.exit(f'すでにあるファイルには作れません: {os.path.basename(path)}')
    d = read_xml(YAKU)
    b = d.index('<w:body>') + len('<w:body>')
    k = d.index('<w:sectPr')
    title = para([run(spec['title'])], '<w:pStyle w:val="a3"/>')   # a3 = 既存ファイルの表題スタイル
    shutil.copy2(YAKU, path)
    try:
        write_xml(path, d[:b] + title + pages_xml(spec['pages']) + d[k:], backup=False)
    except BaseException:
        os.remove(path); raise


def cmd_yaku_add(spec_path):
    """PAGES.json: {"file": "…docx"(任意: 省略時は Chapter 5 の対訳), "title": "ナルニア国物語 対訳 (52〜61)"(任意),
                    "replace": [["旧訳の文字列", "新訳の文字列"], ...](任意: 前ページの「続く」の訳を直すなど),
                    "pages": {"59": [["英文", "和訳"], ...], ...}}"""
    spec = json.load(open(spec_path, encoding='utf-8'))
    YAKU_ = yaku_path(spec)
    ensure_closed(YAKU_)
    d = read_xml(YAKU_)
    for page in spec['pages']:
        if f'>{page}</w:t>' in d:
            sys.exit(f'p.{page} はすでにあります')
    for old, new in spec.get('replace', []):
        if d.count(escape(old)) != 1: sys.exit(f'置き換え対象が1か所に特定できません: {old}')
        d = d.replace(escape(old), escape(new))
    if spec.get('title'):
        d = re.sub(r'(<w:t[^>]*>)ナルニア国物語 対訳 [^<]*\([^<]*\)(</w:t>)', lambda m: m.group(1) + escape(spec['title']) + m.group(2), d, count=1)
    k = d.index('<w:sectPr')
    write_xml(YAKU_, d[:k] + pages_xml(spec['pages']) + d[k:])


def cmd_kadai_add(spec_path):
    """SECTION.json:
    {"heading": "授業ワーク（第3回・Chapter 5, part 3）",
     "note": "※…（任意）",
     "copy_items_from": ["p. 53 l. 2", "Writing Practice"]  (任意: 既存の課題から、この見出し〜この見出しの直前までを書式ごと複製),
     "items": [{"loc": "p. 56 l. 2", "en": "…__下線__…", "instr": "…"(任意),
                "sections": [["訳", ["…"]], ["注意点", ["…", "…"]]], "drawing_box": false}],
     "writing": {"jp": "和文", "en": ["英訳例", "別解"], "points": ["…"]}  (任意)}
    「訳」「1. 訳」「2. 訳」のラベルは本文の段落、それ以外は「・」付きの箇条書きになる。"""
    spec = json.load(open(spec_path, encoding='utf-8'))
    ensure_closed(KADAI)
    d = read_xml(KADAI)
    if f'>{escape(spec["heading"])}</w:t>' in d:
        sys.exit('この見出しはすでにあります')
    out = [heading1(spec['heading'], page_break=True)]
    if spec.get('note'): out.append(k_note(spec['note']))
    if spec.get('copy_items_from'):
        a_txt, b_txt = spec['copy_items_from']
        def p_start(t):
            k = d.index(f'>{escape(t)}</w:t>')
            return max(d.rindex('<w:p>', 0, k), d.rfind('<w:p ', 0, k))
        out.append(d[p_start(a_txt):p_start(b_txt)])
    for it in spec.get('items', []):
        out += [k_loc(it['loc']), k_en(it['en'])]
        if it.get('instr'): out.append(k_instr(it['instr']))
        for label, lines in it['sections']:
            out.append(k_label(label))
            bullet = label not in ('訳', '1. 訳', '2. 訳')
            out += [k_body(l, bullet) for l in lines]
            if it.get('drawing_box') and label.startswith('絵'):
                out.append(k_drawing_box())
    w = spec.get('writing')
    if w:
        out += [heading1('Writing Practice'), k_loc('和文英訳'), k_en(w['jp']), k_label('英訳例')]
        out += [k_body(e, False) for e in w['en']]
        out.append(k_label('注意点'))
        out += [k_body(p, True) for p in w['points']]
    k = d.index('<w:sectPr')
    write_xml(KADAI, d[:k] + ''.join(out) + d[k:])


def _mark_paragraph(p, hl_text, ul_texts):
    """Split the runs of paragraph p so that hl_text gets the yellow shading and
    each of ul_texts (found in order, inside it) an underline. Existing run
    formatting is kept."""
    body_start = p.index('</w:pPr>') + len('</w:pPr>') if '</w:pPr>' in p else p.index('>') + 1
    prefix, body = p[:body_start], p[body_start:p.rindex('</w:p>')]
    pieces = []
    for m in RUN_RE.finditer(body):
        if m.group(3) is None:
            if '<w:t' in m.group(0): sys.exit('解析できない書式の段落があります: ' + para_text(p)[:40])
            continue   # proofErr などは捨てる
        pieces.append((m.group(1) or '', m.group(2), unescape(m.group(3))))
    full = ''.join(x[2] for x in pieces)
    s = full.find(hl_text)
    if s < 0: sys.exit(f'マーカー範囲が見つかりません: {hl_text[:40]}')
    e = s + len(hl_text)
    spans, pos = [], s
    for ul in ul_texts:
        # whole words only (so "it" never matches inside "with")
        m_ul = re.compile(r'(?<![A-Za-z])' + re.escape(ul) + r'(?![A-Za-z])').search(full, pos)
        if not m_ul: sys.exit(f'下線の語句が見つかりません: {ul}')
        us = m_ul.start()
        spans.append((us, us + len(ul))); pos = us + len(ul)
    cuts = sorted({s, e, *[c for sp in spans for c in sp]})
    out, off = [], 0
    for rpr, lrpb, t in pieces:
        a, b = off, off + len(t); off = b
        bounds = [a] + [c for c in cuts if a < c < b] + [b]
        for i in range(len(bounds) - 1):
            u, v = bounds[i], bounds[i + 1]
            seg = t[u - a:v - a]
            if not seg: continue
            extra = ''
            if any(a2 <= u and v <= b2 for a2, b2 in spans) and '<w:u ' not in rpr: extra += '<w:u w:val="single"/>'
            if s <= u and v <= e and MARK_FILL not in rpr: extra += f'<w:shd w:val="clear" w:color="auto" w:fill="{MARK_FILL}"/>'
            r_pr = f'<w:rPr>{rpr}{extra}</w:rPr>' if (rpr or extra) else ''
            out.append(f'<w:r>{r_pr}{lrpb if u == a else ""}<w:t xml:space="preserve">{escape(seg)}</w:t></w:r>')
    return prefix + ''.join(out) + '</w:p>'


def cmd_mark(spec_path):
    """MARKS.json: [{"page": "56", "start": "段落の書き出し", "highlight": "マーカーを引く範囲" または "*"(段落全体),
                     "underline": "下線を引く語句" または ["語句1", "語句2"](出てくる順。任意)}, ...]
    対象は英文の段落（字下げのない段落）だけ。page の見出しから次のページ見出しまでの範囲で探す。"""
    spec = json.load(open(spec_path, encoding='utf-8'))
    YAKU_ = yaku_path(spec)   # {"file": "…docx", "marks": [...]} の形なら別ファイル
    if isinstance(spec, dict): spec = spec['marks']
    ensure_closed(YAKU_)
    d = read_xml(YAKU_)
    for m in spec:
        page = m['page']
        k = d.index(f'>{page}</w:t>')
        nxt = re.search(r'>\d{2,3}</w:t>', d[k + 5:])
        end = k + 5 + nxt.start() if nxt else len(d)
        region = d[k:end]
        hits = [p for p in PARA_RE.findall(region) if 'w:ind' not in p and para_text(p).startswith(m['start'])]
        if len(hits) != 1: sys.exit(f'p.{page} の段落を1つに特定できません: {m["start"]}（{len(hits)}件）')
        p = hits[0]
        hl = para_text(p) if m['highlight'] == '*' else m['highlight']
        ul = m.get('underline') or []
        newp = _mark_paragraph(p, hl, [ul] if isinstance(ul, str) else ul)
        region = region.replace(p, newp, 1)
        d = d[:k] + region + d[end:]
    before = re.sub(r'\s+', '', ''.join(para_text(p) for p in PARA_RE.findall(read_xml(YAKU_))))
    after = re.sub(r'\s+', '', ''.join(para_text(p) for p in PARA_RE.findall(d)))
    if before != after: sys.exit('本文の文字が変わってしまうため中止しました')
    write_xml(YAKU_, d)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    cmd, arg = sys.argv[1], sys.argv[2]
    {'dump': cmd_dump, 'yaku-add': cmd_yaku_add, 'yaku-new': cmd_yaku_new, 'kadai-add': cmd_kadai_add, 'mark': cmd_mark}[cmd](arg)
