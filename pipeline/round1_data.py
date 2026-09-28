#!/usr/bin/env python3
"""第1回授業（Chapter 5, part 2 / 本文 p.52〜54）の課題データを各JSONに追記する。

一度きりのマージ用。再実行すると重複するので注意（重複チェックあり）。
"""
import json

CH = 5
ROUND = '第1回'

S_SUPERIOR = "And Edmund gave a very superior look as if he were far older than Lucy (there was really only a year's difference) and then a little snigger and said,"
J_SUPERIOR = "するとエドマンドは、まるで自分がルーシーよりずっと年上であるかのように、いかにも人を見下したような顔つきをして（実際にはたった一つしか違わなかったのだが）、それから小さくくすっと忍び笑いをして言った。"
S_RUSH = "Poor Lucy gave Edmund one look and rushed out of the room."
J_RUSH = "かわいそうに、ルーシーはエドマンドをひとにらみすると、部屋から飛び出していった。"
S_NASTY = "Edmund, who was becoming a nastier person every minute, thought that he had scored a great success, and went on at once to say, \"There she goes again."
J_NASTY = "刻一刻といやな人間になりつつあったエドマンドは、うまくやってやったと思い、すぐさま続けてこう言った。「ほら、また始まった。"
S_WORST = "That's the worst of young kids, they always—\""
J_WORST = "ちびっ子ってやつはこれだから困るんだ、いつも――」"
S_LOOK = "\"Look here,\" said Peter, turning on him savagely, \"shut up!"
J_LOOK = "「いいか」とピーターは、荒々しく彼に食ってかかった。「黙れ！"
S_BEASTLY = "You've been perfectly beastly to Lu ever since she started this nonsense about the wardrobe, and now you go playing games with her about it and setting her off again."
J_BEASTLY = "ルーがあの洋服だんすのばかげた話を言い出してからというもの、お前はずっとルーにひどい態度を取ってきた。それなのに今度は、よりによってそのことでルーをからかって遊んで、また泣き出させるなんて。"
S_SPITE = "I believe you did it simply out of spite.\""
J_SPITE = "お前がそんなことをしたのは、ただの意地悪からだと思うよ」"
S_ABACK = "\"But it's all nonsense,\" said Edmund, very taken aback."
J_ABACK = "「でも、あれは全部でたらめじゃないか」すっかり面食らって、エドマンドが言った。"
S_POINT = "\"Of course it's all nonsense,\" said Peter, \"that's just the point."
J_POINT = "「もちろん全部でたらめさ」とピーターは言った。「まさにそこが問題なんだ。"


def v(term, gloss, en, jp, marks=None):
    html = en
    for m in (marks or [term]):
        assert m in html, (m, en)
        html = html.replace(m, f'<mark>{m}</mark>', 1)
    return {"term": term, "enHtml": html, "jp": jp, "chapter": CH, "gloss": gloss, "round": ROUND}


# 本文 p.52 の範囲のみ（p.53・54 の語は次回以降）
VOCAB = [
    v("superior look", "見下したような顔つき", S_SUPERIOR, J_SUPERIOR, ["superior look"]),
    v("as if", "まるで〜であるかのように（＋仮定法）", S_SUPERIOR, J_SUPERIOR),
    v("snigger", "（小ばかにした）忍び笑い", S_SUPERIOR, J_SUPERIOR),
    v("rush out of", "〜から飛び出す", S_RUSH, J_RUSH, ["rushed out of"]),
    v("nasty", "いやな、意地の悪い", S_NASTY, J_NASTY, ["nastier"]),
    v("every minute", "刻一刻と", S_NASTY, J_NASTY),
    v("score a great success", "大成功を収める、してやったりとなる", S_NASTY, J_NASTY, ["scored a great success"]),
    v("go on to do", "（続けて）次に〜する", S_NASTY, J_NASTY, ["went on at once to say"]),
    v("There she goes again.", "ほら、また始まった", S_NASTY, J_NASTY, ["There she goes again."]),
    v("That's the worst of 〜", "〜はそこが困る", S_WORST, J_WORST, ["That's the worst of"]),
    v("Look here", "いいか、おい（注意を促す）", S_LOOK, J_LOOK),
    v("turn on 〜", "〜に食ってかかる", S_LOOK, J_LOOK, ["turning on"]),
    v("savagely", "荒々しく", S_LOOK, J_LOOK),
    v("shut up", "黙れ", S_LOOK, J_LOOK),
    v("beastly", "ひどい、意地悪な", S_BEASTLY, J_BEASTLY),
    v("nonsense", "ばかげた話、でたらめ", S_BEASTLY, J_BEASTLY),
    v("go playing", "（よりによって）〜なんかする（go＋-ing：非難）", S_BEASTLY, J_BEASTLY, ["go playing"]),
    v("play games with 〜", "〜をからかう、もてあそぶ", S_BEASTLY, J_BEASTLY, ["playing games with"]),
    v("set 〜 off", "〜を（また泣き）出させる", S_BEASTLY, J_BEASTLY, ["setting her off"]),
    v("out of spite", "意地悪で、悪意から", S_SPITE, J_SPITE),
    v("take aback", "面食らわせる（be taken aback：面食らう）", S_ABACK, J_ABACK, ["taken aback"]),
    v("that's just the point", "まさにそこが問題だ", S_POINT, J_POINT),
]

# 下線部訳タブ：授業ワークの「訳しましょう」系の課題
UNDERLINE = [
    {"underline": "（全文）", "task": "文の構造に注意して訳しましょう",
     "enHtml": "And Edmund gave a very superior look as if he were far older than Lucy (there was really only a year's difference) and then a little snigger and said.",
     "jp": J_SUPERIOR,
     "note": "gave の目的語は a very superior look と a little snigger の2つ（give＋動作名詞＝〜する）。as if he were …：as if＋仮定法過去「まるで〜であるかのように」。far は比較級の強調「ずっと」。( ) 内は語り手の皮肉な補足。"},
    {"underline": "（全文）", "task": None,
     "enHtml": "Edmund, who was becoming a nastier person every minute, thought that he had scored a great success, and went on at once to say, 'There she goes again.'",
     "jp": J_NASTY + "」",
     "note": ", who … ,：非制限用法の関係代名詞。was becoming a nastier person every minute：「刻一刻と（ますます）いやなやつになっていった」。go on to do：「続けて〜する」（go on doing「〜し続ける」と区別）。There she goes again.：「ほら、また始まった」。"},
    {"underline": "go", "task": "文の構造に注意して訳しましょう",
     "enHtml": "and now you <u>go</u> playing games with her about it and setting her off again. I believe you did it simply out of spite.",
     "jp": "それなのに今度は、よりによってそのことでルーをからかって遊んで、また泣き出させるなんて。お前がそんなことをしたのは、ただの意地悪からだと思うよ。",
     "note": "go は playing と setting の両方にかかる。この go は「行く」ではなく、go＋-ing で「（よりによって）〜なんかする」という非難を表す口語表現。play games with 〜「〜をからかう」、set 〜 off「〜を泣き出させる」、out of spite「意地悪で」。"},
    {"underline": "whichever it is", "task": "下線部の内容を明らかにして訳しましょう",
     "enHtml": "But <u>whichever it is</u>, what good do you think you'll do by jeering and nagging at her one day and encouraging her the next?",
     "jp": "でも、ルーの頭がおかしくなりかけているにせよ、とんでもない嘘つきになりかけているにせよ、ある日はあの子をあざ笑ってがみがみ責め立て、次の日には（話を信じるふりをして）調子に乗らせるようなことをして、一体何の役に立つと思っているんだ。（何の役にも立ちはしない）",
     "note": "whichever it is＝直前の either going queer in the head（頭がおかしくなりかけている）or else turning into a most frightful liar（ひどい嘘つきになりかけている）の「どちらであっても」。what good do you think you'll do：修辞疑問で「何の役にも立たない」。one day … the next (day)「ある日は…次の日は」。"},
    {"underline": "（全文）", "task": None,
     "enHtml": "Nothing they could say to her made any difference.",
     "jp": "みんながどんな言葉をかけても、まったく効き目がなかった。（ルーシーは少しも態度を変えなかった）",
     "note": "Nothing (that) they could say to her が主語。否定語が主語の文は「何を言っても…しなかった」と訳すと自然。make a difference「効果がある」。"},
    {"underline": "（全文）", "task": None,
     "enHtml": "'it's getting beyond us.'",
     "jp": "「もう僕たちの手には負えなくなってきているよ。」",
     "note": "it は漠然と「事態」（ルーシーの件）。beyond 〜「〜の手に負えない」。進行形 is getting で「だんだん〜になってきている」。"},
    {"underline": "（全文）", "task": None,
     "enHtml": "[The Professor] said he was quite at their disposal.",
     "jp": "教授は、何でも遠慮なく相談してくれてかまわないと言った。",
     "note": "at 〜's disposal「〜の自由に使える」。直訳「自分は完全に君たちの自由に使ってよい」。said he was …は時制の一致なので「〜だと言った」と訳す。"},
    {"underline": "he sat listening to them with the tips of his fingers pressed together", "task": "この状態を絵に描いてみましょう",
     "enHtml": "Then <u>he sat listening to them with the tips of his fingers pressed together</u> and never interrupting.",
     "jp": "それから教授は、両手の指先を合わせたまま座って二人の話に耳を傾け、一度も口を挟まなかった。",
     "note": "絵：椅子に座った教授が、胸の前で手のひらは離したまま両手の指先だけを突き合わせ（山形・steepled fingers）、黙って聞いている。sit＋-ing「〜しながら座っている」。with＋O＋過去分詞「Oが〜された状態で」（付帯状況）。"},
    {"underline": "the last thing either of them expected", "task": "1. 訳しましょう　2. 下線部の具体的な内容を説明しましょう",
     "enHtml": "Then he cleared his throat and said <u>the last thing either of them expected</u>.",
     "jp": "それから教授は咳払いをして、二人のどちらもまったく予想していなかったことを言った。",
     "note": "下線部の内容：「How do you know that your sister's story is not true?（妹さんの話が本当ではないと、どうして分かるのかね？）」という言葉。二人は教授もルーシーがおかしいと同意してくれると思っていたのに、逆に自分たちの思い込みを問われた。the last＋名詞＋関係詞節「最も〜しそうにないもの」。"},
]
for u in UNDERLINE:
    u["chapter"] = CH
    u["round"] = ROUND
    if u["task"] is None:
        del u["task"]

# 読解クイズ（日本語訳を選ぶ）
QUIZ = [{"en": en, "jp": jp, "chapter": CH, "round": ROUND} for en, jp in [
    ("And Edmund gave a very superior look as if he were far older than Lucy (there was really only a year's difference) and then a little snigger and said,", J_SUPERIOR),
    ("Edmund, who was becoming a nastier person every minute, thought that he had scored a great success, and went on at once to say, \"There she goes again.\"", J_NASTY + "」"),
    ("And now you go playing games with her about it and setting her off again. I believe you did it simply out of spite.", "それなのに今度は、よりによってそのことでルーをからかって遊んで、また泣き出させるなんて。お前がそんなことをしたのは、ただの意地悪からだと思うよ。"),
    ("\"Of course it's all nonsense,\" said Peter, \"that's just the point.\"", "「もちろん全部でたらめさ」とピーターは言った。「まさにそこが問題なんだ。」"),
    ("But whichever it is, what good do you think you'll do by jeering and nagging at her one day and encouraging her the next?", "でも、どちらにせよ、ある日はあの子をあざ笑ってがみがみ責め立て、次の日には調子に乗らせるようなことをして、一体何の役に立つと思っているんだ。"),
    ("Nothing they could say to her made any difference.", "みんながどんな言葉をかけても、まったく効き目がなかった。"),
    ("\"It's getting beyond us.\"", "「もう僕たちの手には負えなくなってきているよ。」"),
    ("The Professor said he was quite at their disposal.", "教授は、何でも遠慮なく相談してくれてかまわないと言った。"),
    ("Then he sat listening to them with the tips of his fingers pressed together and never interrupting.", "それから教授は、両手の指先を合わせたまま座って二人の話に耳を傾け、一度も口を挟まなかった。"),
    ("Then he cleared his throat and said the last thing either of them expected.", "それから教授は咳払いをして、二人のどちらもまったく予想していなかったことを言った。"),
]]

# 内容理解
COMPREHENSION = [
    {"q": "ピーターが \"Of course it's all nonsense, that's just the point.\" と言ったとき、「まさにそこが問題だ」と考えているのはどんなことか？",
     "choices": ["話がでたらめである以上、ルーシーは頭がおかしくなりかけているか、ひどい嘘つきになりかけているかのどちらかだということ",
                 "エドマンドがルーシーの話を本気で信じ始めていること",
                 "洋服だんすの奥に本当に別の国があるかもしれないこと",
                 "教授がルーシーの話をまったく聞いてくれないこと"],
     "answer": "話がでたらめである以上、ルーシーは頭がおかしくなりかけているか、ひどい嘘つきになりかけているかのどちらかだということ",
     "explain": "直後で \"she seems to be either going queer in the head or else turning into a most frightful liar\" と続く。家では何ともなかった妹がそうなっていること自体が深刻な問題で、だからエドマンドがからかうのは状況を悪くするだけだと責めている。"},
    {"q": "ピーターがルーシーの話を「でたらめ」だと考える根拠として最も適切なものは？",
     "choices": ["以前4人で洋服だんすを調べたとき、コートが掛かっているだけの普通の洋服だんすで、奥は行き止まりだったから",
                 "教授が「そんな国はない」と言ったから",
                 "ルーシー自身が冗談だったと認めたから",
                 "スーザンが夜中に一人で洋服だんすを調べたから"],
     "answer": "以前4人で洋服だんすを調べたとき、コートが掛かっているだけの普通の洋服だんすで、奥は行き止まりだったから",
     "explain": "4人で確かめたときは何の変哲もない洋服だんすだった。そもそも洋服だんすの中に別の国があるなど常識的にありえない、というのがピーターの考え。"},
    {"q": "ルーシーを見つけたあと、みんなが声をかけるとルーシーはどうしたか？",
     "choices": ["何を言っても効き目がなく、自分の話を曲げなかった",
                 "話は嘘だったと認めて謝った",
                 "エドマンドとすぐに仲直りした",
                 "自分から教授に話しに行くと言い出した"],
     "answer": "何を言っても効き目がなく、自分の話を曲げなかった",
     "explain": "\"Nothing they could say to her made any difference. She stuck to her story …\"。stick to 〜「〜を曲げない、固守する」。"},
    {"q": "ピーターとスーザンが教授に相談しに行くことにしたのはなぜか？",
     "choices": ["ルーシーの様子がおかしく、自分たちの手に負えなくなってきたと思ったから",
                 "エドマンドを罰してもらいたかったから",
                 "洋服だんすのある部屋の鍵を借りたかったから",
                 "屋敷を探検する許可をもらいたかったから"],
     "answer": "ルーシーの様子がおかしく、自分たちの手に負えなくなってきたと思ったから",
     "explain": "ピーターは \"it's getting beyond us\"（もう僕たちの手には負えない）と言い、ルーに本当に何かおかしなところがあると教授が思えば、お父さんに手紙を書いてくれるだろうと考えた。"},
    {"q": "教授は二人の話をどのように聞いていたか？",
     "choices": ["両手の指先を合わせて座り、一度も口を挟まずに聞いていた",
                 "腕を組んで立ったまま、ときどき質問しながら聞いていた",
                 "本を読みながら、半分うわの空で聞いていた",
                 "何度も笑いながら、首を振って聞いていた"],
     "answer": "両手の指先を合わせて座り、一度も口を挟まずに聞いていた",
     "explain": "\"he sat listening to them with the tips of his fingers pressed together and never interrupting\"。with＋O＋過去分詞（付帯状況）で「指先を押し合わせた状態で」。"},
    {"q": "教授が言った「二人のどちらもまったく予想していなかったこと（the last thing either of them expected）」とは？",
     "choices": ["「妹さんの話が本当ではないと、どうして分かるのかね？」",
                 "「ルーシーはお父さんのところへ帰したほうがいい」",
                 "「エドマンドは私から厳しく叱っておこう」",
                 "「ルーシーは医者に診てもらうべきだ」"],
     "answer": "「妹さんの話が本当ではないと、どうして分かるのかね？」",
     "explain": "\"How do you know that your sister's story is not true?\"。二人は教授もルーシーがおかしいと同意すると思っていたのに、逆に「話が本当かもしれない」と自分たちの思い込みを問われた。"},
]
for c in COMPREHENSION:
    c["chapter"] = CH
    c["round"] = ROUND

# 文法問題
GRAMMAR = [
    {"point": "as if＋仮定法過去", "en": "Edmund gave a very superior look as if he ___ far older than Lucy.",
     "choices": ["were", "is", "has been", "will be"], "answer": "were",
     "explain": "as if＋仮定法過去（be動詞は主語に関係なく were）で「まるで〜であるかのように」。実際には1歳しか違わないので、事実に反する内容＝仮定法。"},
    {"point": "非制限用法の関係代名詞", "en": "Edmund, ___ was becoming a nastier person every minute, thought that he had scored a great success.",
     "choices": ["who", "that", "which", "whom"], "answer": "who",
     "explain": "コンマで挟んで先行詞（人）を補足説明する非制限用法。that は非制限用法では使えない。主格なので whom も不可。"},
    {"point": "go on to do（続けて〜する）", "en": "… and went on at once ___ say, \"There she goes again.\"",
     "choices": ["to", "for", "with", "by"], "answer": "to",
     "explain": "go on to do は「（前のことに続けて）次に〜する」。go on doing（〜し続ける）とは意味が違うので注意。"},
    {"point": "go＋-ing（非難：よりによって〜する）", "en": "and now you go ___ games with her about it and setting her off again.",
     "choices": ["playing", "to play", "played", "play"], "answer": "playing",
     "explain": "go＋-ing で「（よりによって）〜なんかする」という非難を表す口語表現。後ろの setting と並列になっている（go は playing と setting の両方にかかる）。"},
    {"point": "out of（動機：〜から）", "en": "I believe you did it simply ___ of spite.",
     "choices": ["out", "because", "in", "for"], "answer": "out",
     "explain": "out of spite で「意地悪から、悪意で」。out of は動機・原因を表す（out of curiosity「好奇心から」など）。"},
    {"point": "修辞疑問（what good …?＝何の役にも立たない）", "en": "What ___ do you think you'll do by jeering and nagging at her one day and encouraging her the next?",
     "choices": ["good", "well", "best", "better"], "answer": "good",
     "explain": "do good で「役に立つ」。What good do you think you'll do …? は「何の役に立つと思うのか」＝「何の役にも立たない」という修辞疑問。do you think は疑問詞の直後に入る。"},
    {"point": "付帯状況 with＋O＋過去分詞", "en": "Then he sat listening to them with the tips of his fingers ___ together and never interrupting.",
     "choices": ["pressed", "pressing", "to press", "press"], "answer": "pressed",
     "explain": "with＋O＋過去分詞で「Oが〜された状態で」。指先は「押し合わされている」側なので受け身の意味の過去分詞 pressed。"},
    {"point": "the last＋名詞（最も〜しそうにない）", "en": "Then he cleared his throat and said the ___ thing either of them expected.",
     "choices": ["last", "first", "least", "latest"], "answer": "last",
     "explain": "the last thing (that) 〜 expected で「最も予想していなかったこと」。the last＋名詞＋関係詞節は「最も〜しそうにない…」という意味になる。"},
]
for g in GRAMMAR:
    g["chapter"] = CH
    g["round"] = ROUND


def main():
    data = json.load(open('data.json', encoding='utf-8'))
    grammar = json.load(open('grammar.json', encoding='utf-8'))
    comp = json.load(open('comprehension.json', encoding='utf-8'))
    if any(x.get('round') == ROUND for x in data['vocab']):
        raise SystemExit(f'{ROUND} は既に追加済みです')
    data['vocab'] += VOCAB
    data['underline'] += UNDERLINE
    data['quiz'] += QUIZ
    grammar += GRAMMAR
    comp += COMPREHENSION
    json.dump(data, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    json.dump(grammar, open('grammar.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    json.dump(comp, open('comprehension.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f'vocab+{len(VOCAB)} underline+{len(UNDERLINE)} quiz+{len(QUIZ)} grammar+{len(GRAMMAR)} comprehension+{len(COMPREHENSION)}')


if __name__ == '__main__':
    main()
