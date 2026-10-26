#!/usr/bin/env python3
"""第5回（Chapter 5, part 3 の続き / 本文 p.59〜61）の課題データを各JSONに追記する。

p.58 の終わりから p.59 に続く文（And when parties of sightseers …）から、p.61 の終わり
（… never shut yourself up in a wardrobe.）まで。ページをまたぐ文は手でつないだ。
下線部訳は第4回の課題（p.59〜60 の6問）。
対訳プリントで赤太字になっている語句（授業で重要とされたもの）は必ず単語に含める。
一度きりのマージ用。同じ回の二重追加は拒否する。
"""
import json

CH = 5
ROUND = '第5回'

S = {
    'SIGHT': ('And when parties of sightseers arrived and asked to see the house, the Professor always gave them permission, and Mrs Macready, the housekeeper, showed them round, telling them about the pictures and the armour, and the rare books in the library.',
        'そして、見学者の一行がやって来て家を見せてほしいと頼むと、教授はいつも許可を与えた。そして家政婦のマクレディ夫人が一行を案内して回り、絵や甲冑、図書室の珍しい本について説明して聞かせるのだった。'),
    'FOND': ('Mrs Macready was not fond of children, and did not like to be interrupted when she was telling visitors all the things she knew.',
        'マクレディ夫人は子どもが好きではなく、自分の知っていることを残らず見学者に話して聞かせているときに、邪魔をされるのを嫌った。'),
    'SAID': ('She had said to Susan and Peter almost on the first morning (along with a good many other instructions),',
        '夫人は、ほとんど最初の朝のうちに、スーザンとピーターに（ほかのたくさんの言いつけと一緒に）こう言ってあった。'),
    'KEEP': ('"And please remember you\'re to keep out of the way whenever I\'m taking a party over the house."',
        '「それから、私がお客様の一行をお屋敷の中にご案内しているときは、いつでも邪魔にならないところにいること。覚えておいてくださいね」'),
    'ASIF': ('"Just as if any of us would want to waste half the morning trailing round with a crowd of strange grown-ups!" said Edmund, and the other three thought the same.',
        '「まるで僕たちの誰かが、知らない大人の集団のあとにぞろぞろついて回って、午前中の半分をむだにしたがるとでもいうみたいだ！」とエドマンドが言うと、ほかの三人も同じように思った。'),
    'HOW': ('That was how the adventures began for the third time.',
        'こうして、冒険が三度目に始まったのだった。'),
    'FEW': ('A few mornings later Peter and Edmund were looking at the suit of armour and wondering if they could take it to bits when the two girls rushed into the room and said, "Look out!',
        '数日後の朝、ピーターとエドマンドが甲冑を眺めながら、これをばらばらに分解できないだろうかと考えていると、女の子二人が部屋に駆け込んできて言った。「気をつけて！'),
    'HERE': ('Here comes the Macready and a whole gang with her."',
        'あのマクレディさんが、大勢の人を引き連れてやって来るわ」'),
    'SHARP': ('"Sharp\'s the word," said Peter, and all four made off through the door at the far end of the room.',
        '「急げ！」とピーターが言い、四人とも部屋のいちばん奥のドアから急いで逃げ出した。'),
    'BUTWHEN': ('But when they had got out into the Green Room and beyond it, into the Library, they suddenly heard voices ahead of them, and realized that Mrs Macready must be bringing her party of sightseers up the back stairs - instead of up the front stairs as they had expected.',
        'ところが、緑の間に出て、さらにその先の図書室まで来たところで、急に前方から話し声が聞こえてきた。それで四人は、マクレディ夫人が見学者の一行を、思っていたように表階段からではなく、裏階段から連れて上がってきているにちがいないと気づいた。'),
    'AFTER': ('And after that - whether it was that they lost their heads, or that Mrs Macready was trying to catch them, or that some magic in the house had come to life and was chasing them into Narnia - they seemed to find themselves being followed everywhere, until at last Susan said, "Oh, bother those trippers!',
        'そしてそれからは――四人があわてて冷静さを失ったせいなのか、マクレディ夫人が四人を捕まえようとしていたのか、それとも、この家の何かの魔法が目を覚まして四人をナルニアへ追い立てていたのか――どこへ行っても後をつけられているような気がして、とうとうスーザンが言った。「もう、あの見物の人たちったら！'),
    'HEREGO': ("Here - let's go into the Wardrobe Room till they've passed.",
        'ねえ――あの人たちが通り過ぎるまで、洋服だんすの部屋に入っていましょうよ。'),
    'NOONE': ('No one will follow us in there."',
        'あそこなら誰もついてこないわ」'),
    'MOMENT': ('But the moment they were inside they heard the voices in the passage - and then someone fumbling at the door - and then they saw the handle turning.',
        'ところが、中に入ったとたん、廊下で話し声が聞こえ――それから誰かがドアを手探りしている音がして――そして取っ手が回るのが見えた。'),
    'QUICK': ('"Quick!" said Peter.',
        '「早く！」とピーターが言った。'),
    'NOWHERE': ('"There\'s nowhere else," and flung open the wardrobe.',
        '「ほかに逃げ場はない」と言って、ピーターは洋服だんすの扉をさっと開けた。'),
    'BUNDLED': ('All four of them bundled inside it and sat there, panting, in the dark.',
        '四人ともその中にどやどやと転がり込み、暗闇の中で息を切らしながら座っていた。'),
    'HELD': ('Peter held the door closed but did not shut it; for, of course, he remembered, as every sensible person does, that you should never, never shut yourself up in a wardrobe.',
        'ピーターは扉を押さえて閉じておいたが、ぴったり閉め切りはしなかった。というのも、もちろんピーターは、分別のある人なら誰でもそうであるように、洋服だんすの中に自分を閉じ込めるようなことは絶対に、絶対にしてはいけないと覚えていたからだ。'),
}


def v(term, gloss, key, marks=None):
    """marks の語句を、文の前から順に探して <mark> で囲む。"""
    en, jp = S[key]
    html, pos = '', 0
    for m in (marks or [term]):
        j = en.find(m, pos)
        assert j >= 0, (m, en)
        html += en[pos:j] + f'<mark>{m}</mark>'
        pos = j + len(m)
    html += en[pos:]
    return {"term": term, "enHtml": html, "jp": jp, "chapter": CH, "gloss": gloss, "round": ROUND}


VOCAB = [
    # --- 対訳プリントで赤太字（授業で重要）の語句：必ず含める ---
    v("keep out of the way", "邪魔にならないところにいる、近寄らない", 'KEEP'),
    v("trail round", "（人のあとに）だらだらついて回る", 'ASIF', ["trailing round"]),
    v("a crowd of 〜", "大勢の〜、〜の群れ（a crowd of strange grown-ups＝知らない大人の集団）", 'ASIF', ["crowd of strange grown-ups"]),
    v("take 〜 to bits", "〜をばらばらに分解する（bit＝小片）", 'FEW', ["take it to bits"]),
    v("Sharp's the word", "急げ、ぐずぐずするな（決まり文句）", 'SHARP'),
    v("make off", "急いで逃げる、立ち去る（make-made-made）", 'SHARP', ["made off"]),
    v("the back stairs", "裏階段（⇔ the front stairs 表階段）", 'BUTWHEN', ["the back stairs", "the front stairs"]),
    v("find oneself -ing", "気がつくと〜されて（して）いる（find themselves being followed＝後をつけられている気がする）", 'AFTER', ["find themselves being followed everywhere"]),
    v("bother 〜!", "〜なんていまいましい、うるさいなあ（いらだちを表す）", 'AFTER', ["bother"]),
    v("tripper", "（日帰りの）観光客、行楽客（やや見下した言い方）", 'AFTER', ["trippers"]),
    v("fumble at 〜", "〜を手探りする、ごそごそいじる", 'MOMENT', ["fumbling at the door"]),
    v("handle", "取っ手、ハンドル（the handle turning＝取っ手が回る）", 'MOMENT', ["handle turning"]),
    v("fling open 〜", "〜をさっと（勢いよく）開ける（fling-flung-flung）", 'NOWHERE', ["flung open the wardrobe"]),
    v("pant", "あえぐ、息を切らす", 'BUNDLED', ["panting"]),
    v("hold 〜 closed", "〜を閉じた状態で押さえておく（hold O C：OをCの状態に保つ）", 'HELD', ["held the door closed but did not shut it"]),
    # --- そのほか p.59〜61 の重要表現 ---
    v("show 人 round", "人を案内して回る", 'SIGHT', ["showed them round"]),
    v("be fond of 〜", "〜が好きだ", 'FOND', ["fond of"]),
    v("along with 〜", "〜と一緒に、〜に加えて", 'SAID', ["along with"]),
    v("a good many 〜", "かなり多くの〜", 'SAID', ["a good many"]),
    v("just as if 〜", "まるで〜であるかのように（as if＋仮定法）", 'ASIF', ["Just as if"]),
    v("waste 時間 -ing", "〜して時間をむだにする", 'ASIF', ["waste half the morning trailing"]),
    v("Here comes 〜", "〜がやって来る（倒置）", 'HERE', ["Here comes"]),
    v("lose one's head", "冷静さを失う、あわてる", 'AFTER', ["lost their heads"]),
    v("come to life", "生き返る、活動し始める", 'AFTER', ["come to life"]),
    v("instead of 〜", "〜の代わりに、〜ではなく", 'BUTWHEN', ["instead of"]),
    v("the moment 〜", "〜するとすぐに（接続詞のように使う）", 'MOMENT', ["the moment"]),
    v("bundle", "どやどやと入る、ごちゃごちゃと押し込む", 'BUNDLED', ["bundled"]),
    v("shut oneself up in 〜", "〜に閉じこもる", 'HELD', ["shut yourself up in"]),
]

# 下線部訳：第4回の課題（p.59〜60）。答えは課題の解答と同じ内容
UNDERLINE = [
    {"underline": "（全文）", "task": "最初の部分（just as ifの前）に省略された語を補いましょう",
     "enHtml": "'Just as if any of us would want to waste half the morning trailing round with a crowd of strange grown-ups!'",
     "jp": "「（あの人の言い方ときたら、）まるで僕たちの誰かが、知らない大人の集団のあとにぞろぞろついて回って、午前中の半分をむだにしたがるとでもいうみたいだ！」",
     "note": "補う語：(She talks / She said that) just as if any of us would want to …。直前のマクレディ夫人の言いつけ「私がお客様を案内しているときは、邪魔にならないところにいること」を受けたエドマンドの文句。as if＋仮定法（would want）「まるで〜であるかのように」（実際は誰もそんなことをしたくない）。waste 時間 -ing「〜して時間をむだにする」、trail round「だらだらついて回る」。"},
    {"underline": "take it to bits", "task": None,
     "enHtml": "Peter and Edmund were looking at the suit of armour and wondering if they could <u>take it to bits</u>.",
     "jp": "ピーターとエドマンドは甲冑を眺めながら、それをばらばらに分解できないだろうかと考えていた。",
     "note": "take 〜 to bits「〜をばらばらに分解する」（bit＝小片。take 〜 to pieces も同じ）。it は the suit of armour（ひとそろいの甲冑）。wonder if 〜「〜だろうかと思う」。"},
    {"underline": "（全文）", "task": None,
     "enHtml": "'Look out! Here comes the Macready and a whole gang with her.'",
     "jp": "「気をつけて！ あのマクレディさんが、大勢の人を引き連れてやって来るわ」",
     "note": "Look out!「気をつけて！」。Here comes 〜「〜がやって来る」（倒置）。the Macready は人名に the を付けて「あの（おっかない）マクレディ」と、からかい・反感をこめた言い方。a whole gang「一団、大勢」（くだけた、やや悪口っぽい言い方）。"},
    {"underline": "（全文）", "task": None,
     "enHtml": "'Sharp's the word,' said Peter.",
     "jp": "「急げ！」とピーターは言った。",
     "note": "Sharp's the word「急げ、ぐずぐずするな」という決まり文句（口語・イギリス英語）。sharp は「すばやい」、直訳は「合言葉は『すばやく』だ」。このあと all four made off through the door …（make off＝急いで逃げる）。"},
    {"underline": "（全文）", "task": "この理由として考えられるものを挙げなさい",
     "enHtml": "They seemed to find themselves being followed everywhere.",
     "jp": "四人は、どこへ行っても後をつけられているような気がした。",
     "note": "考えられる理由（直前のダッシュの間）：① 四人があわてて冷静さを失ったから（they lost their heads）② マクレディ夫人が四人を捕まえようとしていたから ③ この家の何かの魔法が目を覚まし、四人をナルニアへ追い立てていたから。find oneself＋過去分詞/-ing「気がつくと〜されて（して）いる」、being followed は受け身の進行形。"},
    {"underline": "（全文）", "task": None,
     "enHtml": "At last Susan said, 'Oh, bother those trippers!'",
     "jp": "とうとうスーザンが言った。「もう、あの見物の人たちったら、うっとうしい！」",
     "note": "bother 〜!「〜なんていまいましい、うるさいなあ」。tripper「（日帰りの）観光客」で、やや見下した言い方（マクレディ夫人が案内している見学者たちのこと）。at last「とうとう」。"},
]
for u in UNDERLINE:
    u["chapter"] = CH
    u["round"] = ROUND
    if u["task"] is None:
        del u["task"]

# 読解クイズ（日本語訳を選ぶ）
QUIZ = [{"en": S[k][0], "jp": S[k][1], "chapter": CH, "round": ROUND} for k in [
    'SIGHT', 'FOND', 'SAID', 'KEEP', 'ASIF', 'HOW', 'FEW', 'SHARP', 'BUTWHEN', 'AFTER', 'MOMENT', 'NOWHERE', 'BUNDLED', 'HELD',
]]

COMPREHENSION = [
    {"q": "見学者が来たとき、家の中を案内したのは誰か？",
     "choices": ["家政婦のマクレディ夫人", "教授", "ピーター", "見学者が自分たちで見て回った"],
     "answer": "家政婦のマクレディ夫人",
     "explain": "\"the Professor always gave them permission, and Mrs Macready, the housekeeper, showed them round\"。教授は許可を与えただけ。"},
    {"q": "マクレディ夫人が嫌がったことは？",
     "choices": ["見学者に説明しているときに邪魔をされること", "教授が見学を許可すること", "子どもたちが図書室で本を読むこと", "見学者が質問をすること"],
     "answer": "見学者に説明しているときに邪魔をされること",
     "explain": "\"did not like to be interrupted when she was telling visitors all the things she knew.\" 夫人は子ども好きでもなかった（not fond of children）。"},
    {"q": "マクレディ夫人が最初の朝に子どもたちに言いつけたことは？",
     "choices": ["見学者を案内しているときは、邪魔にならないところにいること", "見学者の案内を手伝うこと", "図書室には入らないこと", "甲冑に触らないこと"],
     "answer": "見学者を案内しているときは、邪魔にならないところにいること",
     "explain": "\"you're to keep out of the way whenever I'm taking a party over the house.\""},
    {"q": "冒険が三度目に始まった日の朝、ピーターとエドマンドは何をしていたか？",
     "choices": ["甲冑を眺めて、分解できないかと考えていた", "図書室で本を読んでいた", "洋服だんすを調べていた", "庭で遊んでいた"],
     "answer": "甲冑を眺めて、分解できないかと考えていた",
     "explain": "\"Peter and Edmund were looking at the suit of armour and wondering if they could take it to bits\""},
    {"q": "四人が図書室まで逃げたところで、困ったことになったのはなぜか？",
     "choices": ["マクレディ夫人が、予想と違って裏階段から一行を連れて上がってきたから", "図書室のドアに鍵がかかっていたから", "教授に見つかったから", "エドマンドが迷子になったから"],
     "answer": "マクレディ夫人が、予想と違って裏階段から一行を連れて上がってきたから",
     "explain": "\"Mrs Macready must be bringing her party of sightseers up the back stairs - instead of up the front stairs as they had expected.\""},
    {"q": "スーザンが洋服だんすの部屋に入ろうと言ったのはなぜか？",
     "choices": ["あそこなら誰もついてこないと思ったから", "ナルニアに行きたかったから", "コートを着たかったから", "教授がそこにいると思ったから"],
     "answer": "あそこなら誰もついてこないと思ったから",
     "explain": "\"let's go into the Wardrobe Room till they've passed. No one will follow us in there.\""},
    {"q": "洋服だんすの部屋に入ったあと、四人が洋服だんすに隠れることになったのはなぜか？",
     "choices": ["誰かがドアを手探りして、取っ手が回るのが見えたから", "マクレディ夫人に命令されたから", "ルーシーがナルニアを見せたがったから", "部屋がとても寒かったから"],
     "answer": "誰かがドアを手探りして、取っ手が回るのが見えたから",
     "explain": "\"someone fumbling at the door - and then they saw the handle turning.\" ピーターが \"There's nowhere else\" と言って洋服だんすを開けた。"},
    {"q": "ピーターが洋服だんすの扉をぴったり閉めなかったのはなぜか？",
     "choices": ["洋服だんすの中に自分を閉じ込めてはいけないと覚えていたから", "外の様子を見たかったから", "扉が壊れていたから", "ルーシーに頼まれたから"],
     "answer": "洋服だんすの中に自分を閉じ込めてはいけないと覚えていたから",
     "explain": "\"he remembered, as every sensible person does, that you should never, never shut yourself up in a wardrobe.\""},
]
for c in COMPREHENSION:
    c["chapter"] = CH
    c["round"] = ROUND

GRAMMAR = [
    {"point": "be fond of（〜が好きだ）", "en": "Mrs Macready was not fond ___ children.",
     "choices": ["of", "with", "for", "to"], "answer": "of",
     "explain": "be fond of 〜「〜が好きだ」。"},
    {"point": "受け身の不定詞（to be＋過去分詞）", "en": "… and did not like to be ___ when she was telling visitors all the things she knew.",
     "choices": ["interrupted", "interrupt", "interrupting", "to interrupt"], "answer": "interrupted",
     "explain": "to be＋過去分詞「〜されること」。like to be interrupted＝邪魔されるのを好む（ここでは did not なので嫌う）。"},
    {"point": "be to 不定詞（義務）", "en": "\"And please remember you're ___ keep out of the way whenever I'm taking a party over the house.\"",
     "choices": ["to", "for", "going", "able"], "answer": "to",
     "explain": "be to do「〜すること（になっている）」と指示・義務を表す。keep out of the way「邪魔にならないところにいる」。"},
    {"point": "as if＋仮定法", "en": "\"Just as if any of us ___ want to waste half the morning trailing round with a crowd of strange grown-ups!\"",
     "choices": ["would", "will", "can", "shall"], "answer": "would",
     "explain": "as if の後は仮定法（過去形）。実際には誰もそうしたくないので would want。"},
    {"point": "That is how 〜（こうして〜した）", "en": "That was ___ the adventures began for the third time.",
     "choices": ["how", "what", "which", "why"], "answer": "how",
     "explain": "That is how 〜「そのようにして〜」。関係副詞 how（先行詞 the way と同時には使わない）。"},
    {"point": "wonder if 〜（〜だろうかと思う）", "en": "… Peter and Edmund were looking at the suit of armour and wondering ___ they could take it to bits.",
     "choices": ["if", "that", "what", "so"], "answer": "if",
     "explain": "wonder if 〜「〜だろうかと思う」。if は「〜かどうか」の名詞節。"},
    {"point": "must be（〜にちがいない）", "en": "… and realized that Mrs Macready ___ be bringing her party of sightseers up the back stairs.",
     "choices": ["must", "should", "would", "need"], "answer": "must",
     "explain": "must be 〜「〜にちがいない」（推量）。must be bringing は進行形「連れて上がってきているにちがいない」。"},
    {"point": "find oneself＋受け身の進行形", "en": "… they seemed to find themselves ___ followed everywhere.",
     "choices": ["being", "been", "be", "to be"], "answer": "being",
     "explain": "find oneself＋-ing「気がつくと〜している」。受け身の進行形 being followed で「後をつけられている」。"},
    {"point": "知覚動詞＋O＋-ing", "en": "… and then they saw the handle ___.",
     "choices": ["turning", "turned", "to turn", "turns"], "answer": "turning",
     "explain": "see O -ing「Oが〜しているのを見る」。取っ手が回っている最中を見た。"},
    {"point": "hold O C（OをCの状態に保つ）", "en": "Peter held the door ___ but did not shut it.",
     "choices": ["closed", "closing", "close", "to close"], "answer": "closed",
     "explain": "hold O C「OをCの状態に保つ」。ドアは「閉じられた」状態なので過去分詞 closed。shut は「ぴったり閉め切る」。"},
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
