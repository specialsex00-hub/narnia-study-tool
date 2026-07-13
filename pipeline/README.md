# narnia_study_tool.html 生成パイプライン

`narnia_study_tool.html`（Downloads直下）は、以下のスクリプトで
`英語(Writing&Reading).docx`（OneDrive上の元教材）から自動生成しています。
教材が更新された場合は、このパイプラインを再実行してください。

## 再実行手順

```bash
cd narnia_tool_pipeline
python3 -m pip install python-docx   # 初回のみ

# 1. docxのハイライト（灰色=語彙, 黄色=注釈）と下線を直接パースして抽出
python3 extract_from_docx.py "/path/to/英語(Writing&Reading).docx" .
# -> data.json が生成される（vocab / underline / quiz / yellow_sentences）

# 2. 語彙547語分の簡潔な日本語訳（gloss）をマージ
python3 merge_glosses.py data.json

# 3. data.json + grammar.json から最終HTMLを組み立てる
python3 build_html.py ../narnia_study_tool.html
```

## ファイルの役割

- `extract_from_docx.py` — docxのXMLをrun単位で読み、ハイライト色・下線を
  正確に抽出する。以前のpandoc経由の変換で発生していた「1語の下線が
  抜け落ちる」「入れ子タグが途中で切れる」問題を解消済み。
- `glosses.py` — 語彙547語（用語→簡潔な日本語訳）の手動作成辞書。
  新しい章を追加した場合、`merge_glosses.py` 実行時に未対応語が
  警告表示されるので、そのぶんを追記する。
- `merge_glosses.py` — `data.json` の各語彙エントリに `gloss` フィールドを追加する。
- `grammar.json` — 文法問題モード用に手作業で作成した30問（本文中の
  実際の文を使用）。教材更新時に流用・追加可能。
- `build_html.py` — 上記データをテンプレートに埋め込み、最終的な
  `narnia_study_tool.html` を書き出す。CSS/HTML/JS本体もこのファイル内に
  直接記述されている（単一ファイルで完結させる方針を踏襲）。

## データ保存形式（window.storage）

進捗は `narnia-progress` というキーに1つのJSONとしてまとめて保存される。
`version: 2` のスキーマ：

```
{
  version: 2,
  vocab: { [語彙配列のindex]: {box: 0-6, due: <ms timestamp>} },  // Leitner式間隔反復
  underlineDone: { [下線配列のindex]: true },
  underlineWrong: { [下線配列のindex]: true },  // 復習タブ用
  quizWrong: { [クイズ配列のindex]: true },      // 復習タブ用
  quizScore: {correct, total},
  grammarWrong: { [文法配列のindex]: true },     // 復習タブ用
  grammarScore: {correct, total},
}
```

進捗はVOCAB/UNDERLINE/QUIZ/GRAMMAR配列の **index** をキーにしている。
つまりこのパイプラインを再実行してデータの並び・件数が変わると、
既存の学習進捗との対応関係がずれる（実質リセットに近い扱いになる）。
教材が大きく変わらない限りは頻繁に再実行しない想定。
