# Word 教材の編集ツール（tools/docx）

`~/英語/` にある授業用の Word ファイルを、書式を崩さずに編集するためのスクリプト。

| ファイル | 中身 |
|---|---|
| `ナルニア国物語_対訳.docx` | 予習プリント。ページ見出し（52, 53, …）の下に「英文の段落（字下げなし）」と「和訳の段落（字下げあり）」が交互に並ぶ |
| `ナルニア国物語_課題.docx` | 授業ワークの解答。「授業ワーク（第N回・…）」見出しの下に、場所（茶色太字）→英文（下線部は下線）→【指示】（赤）→【訳】【注意点】など |

## 使い方

```bash
cd tools/docx
python3 narnia_docx.py dump ~/英語/第3回課題.docx          # 課題を下線つきで読む（[U]下線 [R]赤太字 [M]マーカー）
python3 narnia_docx.py yaku-add pages.json                 # 対訳にページを追記
python3 narnia_docx.py yaku-new pages.json                 # 章ごとの新しい対訳ファイルを作る（"file" 必須）
python3 narnia_docx.py kadai-add section.json              # 課題ファイルに解答を追記
python3 narnia_docx.py mark marks.json                     # 対訳の課題の文にマーカー
```

- Word で開いているファイルは触らない（`~$…` ロックファイルを検出して中止）。
- 書き換える前に `~/英語/.narnia_backup/` に日時つきのコピーを残す。
- `mark` は本文の文字が1文字でも変わる場合は中止する。
- テストするときは `NARNIA_EIGO_DIR=/tmp/xxx` で別フォルダのコピーを対象にできる。

## JSON の書き方

### pages.json（yaku-add）
```json
{"title": "ナルニア国物語 対訳 (52〜61)",
 "replace": [["…と教授は言い、眼鏡を外して磨き始めながら……（p.58へ続く）", "直した訳"]],
 "pages": {"59": [["英文1", "和訳1"], ["英文2", "和訳2"]]}}
```
- 1文ごとに英文と和訳のペア。ページをまたぐ文は前ページに「……（p.60へ続く）」、次ページに「（p.59から続く）」と注記する。
- `replace` は任意（前ページの「続く」の訳を完成させるときなど）。
- **Chapter 6 からは章ごとに別ファイル**：`"file": "ナルニア国物語_対訳_Chapter6.docx"` を付ける（`yaku-add`・`mark` 共通。`mark` は `{"file": …, "marks": [...]}` の形）。`file` を省くと Chapter 5 の `ナルニア国物語_対訳.docx`。
- 新しい章のファイルは `yaku-new`（既存の対訳をひな形に、同じ書式で作る。例：`examples/yaku_ch6_pages_62-64.json`）。

### section.json（kadai-add）
```json
{"heading": "授業ワーク（第3回・Chapter 5, part 3）",
 "note": "※ p.56〜57 の2問は第2回と同じ問題です。",
 "copy_items_from": ["p. 55 l. 3", "Writing Practice"],
 "items": [
   {"loc": "p. 56 l. 2", "en": "One has only to __look at her__ …", "instr": "下線部に注意して訳しましょう",
    "sections": [["訳", ["…"]], ["注意点", ["…", "…"]]]},
   {"loc": "p. 54 l. 12", "en": "…", "instr": "この状態を絵に描いてみましょう",
    "sections": [["訳", ["…"]], ["絵のポイント", ["…"]]], "drawing_box": true}
 ],
 "writing": {"jp": "和文", "en": ["英訳例", "（別解）…"], "points": ["…"]}}
```
- `__…__` で囲んだ部分に下線。
- ラベルが「訳」「1. 訳」「2. 訳」の行は本文段落、それ以外は「・」付きの箇条書き。
- `copy_items_from`（任意）：前の回と同じ問題が出たとき、既存の解答を「この場所見出し」から「この見出しの直前」まで書式ごと複製する。

### marks.json（mark）
```json
[{"page": "56", "start": "\"Logic!\"", "highlight": "*"},
 {"page": "57", "start": "\"That is the very thing", "highlight": "\"That is the very thing that makes her story so likely to be true,\"", "underline": "the very thing"}]
```
- `start`：英文段落の書き出し（そのページ内で1つに決まる長さ）。
- `highlight`：マーカーを引く範囲（段落内の文字列そのまま）。`"*"` で段落全体。
- `underline`：課題で下線が引かれている語句（任意）。複数あるときは出てくる順にリスト（例 `["that", "it"]`）。単語単位で一致するので、`it` が `with` の中に引かれることはない。

実際に使った JSON は `examples/` にある（第3回の解答・マーカー、p.56〜58 の対訳）。ひな形としてコピーして使う。
