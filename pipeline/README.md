# narnia_study_tool.html 生成パイプライン

`narnia_study_tool.html`（リポジトリ直下）は、以下のスクリプトで元教材
`英語(Writing&Reading).docx` と各JSONから生成します。教材が更新された場合や、
新しい小テストの内容を追加したい場合は、このパイプラインを再実行してください。

> **現在の状態**：前回（第1〜5章）の問題データは削除済みで、現在は授業の
> 回ごとに手作業でデータを追加している。第1回ぶんは `round1_data.py` で
> `data.json`（vocab / underline / quiz）・`grammar.json`・`comprehension.json`
> に追記済み（`kotest.json` は空）。
>
> **下の docx 抽出手順（手順1）を実行すると `data.json` が丸ごと上書きされ、
> 手作業で追加した回のデータが消える**ので注意。回を追加するときは
> `round1_data.py` と同じ形で `roundN_data.py` を作って実行し、
> `build_html.py` だけを再実行する：
>
> ```bash
> cd pipeline
> python3 round2_data.py          # 各JSONに追記（同じ回の二重追加は拒否される）
> python3 build_html.py ../narnia_study_tool.html
> ```
>
> 各項目には `round`（"第1回" など）を付ける。単語タブの回の選択肢は
> 語彙の `round` から自動で作られる。下線部訳の項目は任意で `task`
> （課題の指示文）と `note`（解答後に表示する解説）を持てる。`enHtml`
> に `<u>` が無い項目は「全文を訳す」問題として表示される。
>
> なお `add_kotest_tags.py` 内の `NEW_ENTRIES`（前回の小テスト由来の
> 補足語彙）はスクリプトに直書きされているため、手順3を実行すると
> それらが語彙に追加されます。不要なら `NEW_ENTRIES` を空にしてください。

## 再実行手順

```bash
cd pipeline
python3 -m pip install python-docx   # 初回のみ

# 1. docxのハイライト（灰色=語彙, 黄色=注釈）と下線を直接パースして抽出
python3 extract_from_docx.py "/path/to/英語(Writing&Reading).docx" .
# -> data.json が生成される（vocab / underline / quiz / yellow_sentences）

# 2. 語彙のうち本文由来のものに簡潔な日本語訳（gloss）をマージ
python3 merge_glosses.py data.json

# 3. 小テスト（kotest.json）で出た語句を語彙にタグ付け・追加
python3 add_kotest_tags.py data.json kotest.json

# 4. data.json + grammar.json + comprehension.json + summary_data.json
#    + kotest.json から最終HTMLを組み立てる
python3 build_html.py ../narnia_study_tool.html
```

## ファイルの役割

- `extract_from_docx.py` — docxのXMLをrun単位で読み、ハイライト色・下線を
  正確に抽出する。以前のpandoc経由の変換で発生していた「1語の下線が
  抜け落ちる」「入れ子タグが途中で切れる」問題を解消済み。
- `glosses.py` — 本文由来の語彙（用語→簡潔な日本語訳）の手動作成辞書。
  新しい章を追加した場合、`merge_glosses.py` 実行時に未対応語が
  警告表示されるので、そのぶんを追記する。
- `merge_glosses.py` — `data.json` の各語彙エントリに `gloss` フィールドを追加する。
- `kotest.json` — 授業の小テストで実際に出た穴埋め問題（生徒が貼り付けた
  ものをそのまま収録）。「小テスト対策」タブの4択問題として出題される。
  各項目は `{en, answer, jp, explain}`（空欄は`___`）。`jp`は問題文と一緒に
  最初から表示され、`explain`は解答後に表示される。新しい小テストを
  追加する場合は `en`/`answer` を追記したうえで `add_kotest_jp.py` と
  同じ要領で `jp`/`explain` を書き足す（このスクリプト自体は一度きりの
  マージ用に書いたもので、そのまま再実行はできないので参考用）。
- `add_kotest_tags.py` — `kotest.json` の各解答を `data.json` の語彙リストと
  突き合わせ、一致した語彙に `exam:true` を付与する（単語タブの
  「小テストの語のみ」フィルタに使われる）。一致しない解答のうち
  学習価値のあるもの（mustache/whiskerなど本文に無い補足語彙も含む）は
  `NEW_ENTRIES` として新規語彙に追加する。**docxを再抽出すると
  `exam` フラグは消えるので、抽出のたびに必ずこのスクリプトを再実行する。**
- `grammar.json` — 文法4択問題（本文中の実際の文を使用）。各項目は
  `{chapter, en, choices, answer, point, explain}`。現在は空。
- `comprehension.json` — 内容理解4択クイズ（訳ではなく、本文の
  出来事・事実を問う設問）。読解クイズタブの「内容理解」サブタブで使用。
  各項目は `{chapter, q, choices, answer, explain}`。現在は空。
- `summary_data.json` — 「まとめ」タブ用の章あらすじ・登場人物データ。
  各章の「重要文法ポイント」（`grammar_points`）と「キーワード」
  （`keywords`）も章ごとにこのファイルに直接持たせており、`grammar.json`
  や語彙データとは独立している（問題データを削除しても「まとめ」タブの
  内容が変わらないようにするため）。
  章バナーやキャラクターアバターのSVGはハードコードせずbuild_html.py内の
  `BANNER_SVG` / `CHAR_ICON` に定義されており、`summary_data.json` 側は
  どのSVGキーを使うか（`svg` フィールド）を指定するだけ。
- `build_html.py` — 上記データをテンプレートに埋め込み、最終的な
  `narnia_study_tool.html` を書き出す。CSS/HTML/JS本体もこのファイル内に
  直接記述されている（単一ファイルで完結させる方針を踏襲）。

## データ保存形式（localStorage）

進捗はブラウザの `localStorage` に `narnia-progress` というキーで1つの
JSONとしてまとめて保存される（`window.storage` が使える特殊な環境では
そちらも併用するが、GitHub Pagesなど通常のブラウザではlocalStorageのみが
実際に効く）。`version: 5` のスキーマ：
（問題データを削除した際に `version` を 4→5 に上げ、古い進捗はリセットした）

```
{
  version: 5,
  vocab: { [語彙配列のindex]: {box: 0-6, due: <ms timestamp>} },  // Leitner式間隔反復
  underlineDone: { [下線配列のindex]: true },
  underlineWrong: { [下線配列のindex]: true },        // 復習タブ用
  quizWrong: { [クイズ配列のindex]: true },            // 復習タブ用
  quizScore: {correct, total},
  grammarWrong: { [文法配列のindex]: true },           // 復習タブ用
  grammarScore: {correct, total},
  comprehensionWrong: { [内容理解配列のindex]: true }, // 復習タブ用
  comprehensionScore: {correct, total},
  kotestWrong: { [小テスト配列のindex]: true },        // 復習タブ用
  kotestScore: {correct, total},
}
```

進捗はVOCAB/UNDERLINE/QUIZ/GRAMMAR/COMPREHENSION/KOTEST配列の **index** を
キーにしている。つまりこのパイプラインを再実行してデータの並び・件数が
変わると、既存の学習進捗との対応関係がずれる（実質リセットに近い扱いになる、
スキーマ変更時は`version`を上げて明示的にリセットする方針）。教材が
大きく変わらない限りは頻繁に再実行しない想定。

なお、単語マッチゲーム（Quizletスタイル。全タイルが最初から表向きで、
正しいペアをタップすると消える）は進捗を保存しない一発勝負のミニゲームとして
実装しており、SRS（間隔反復）には影響しない。
