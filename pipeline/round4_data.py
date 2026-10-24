#!/usr/bin/env python3
"""第4回（第4回小テスト用 / Chapter 5, part 3 の残り：本文 p.57 l.17〜p.58）の課題データを各JSONに追記する。

第3回のセットは p.57 l.16 までだったので、その続き（On the other hand, … から
p.58 の終わりまで）を入れる。p.58 最後の "And when parties of" は p.59 に続く文なので入れない。
下線部訳は第3回の課題のうち p.57 l.17 以降の7問。
対訳プリントで赤太字になっている語句（授業で重要とされたもの）は必ず単語に含める。
文は対訳プリントから機械的に抜き出したもの（ページをまたぐ文だけ手でつないだ）。
一度きりのマージ用。同じ回の二重追加は拒否する。
"""
import json

CH = 5
ROUND = '第4回'

S = {
    'IDEA': ("On the other hand, I don't think many girls of her age would invent that idea for themselves.",
        'その一方で、あの子くらいの年の女の子で、そんな考えを自分で思いつく子はあまりいないと思う。'),
    'PRETENDING': ('If she had been pretending, she would have hidden for a reasonable time before coming out and telling her story."',
        'もしふりをしていたのなら、出てきて話をする前に、それらしく思えるだけの時間は隠れていただろうからね」'),
    'MEAN': ('"But do you really mean, sir," said Peter, "that there could be other worlds - all over the place, just round the corner - like that?"',
        '「でも先生、本当に」とピーターは言った。「そんなふうに別の世界が――あちこちに、すぐそこの角を曲がったところに――ありうるとおっしゃるんですか？」'),
    'PROBABLE': ('"Nothing is more probable," said the Professor, taking off his spectacles and beginning to polish them, while he muttered to himself, "I wonder what they do teach them at these schools."',
        '「これほどありそうなことはないよ」と教授は言い、眼鏡を外して磨き始めながら、「近ごろの学校では、いったい何を教えているのやら」とひとりつぶやいた。'),
    'ARE': ('"But what are we to do?" said Susan.',
        '「でも、私たちはどうすればいいんでしょう？」とスーザンは言った。'),
    'POINT': ('She felt that the conversation was beginning to get off the point.',
        '話が本題からそれ始めているような気がしたのだ。'),
    'PLAN': ('"My dear young lady," said the Professor, suddenly looking up with a very sharp expression at both of them, "there is one plan which no one has yet suggested and which is well worth trying."',
        '「お嬢さん」と教授は、急にとても鋭い顔つきで二人を見上げて言った。「まだ誰も言い出していないが、試してみる価値の大いにある方法が一つあるよ」'),
    'WHATS': ('"What\'s that?" said Susan.',
        '「何ですか？」とスーザンは言った。'),
    'MINDING': ('"We might all try minding our own business," said he.',
        '「みんなで、他人のことに口出しせず、自分のことだけを気にかけるようにしてみてはどうかね」と教授は言った。'),
    'END': ('And that was the end of that conversation.',
        'そして、その話はそれで終わりになった。'),
    'BETTER': ('After this, things were a good deal better for Lucy.',
        'それからは、ルーシーにとって状況はずいぶん良くなった。'),
    'SAW': ('Peter saw to it that Edmund stopped jeering at her, and neither she nor anyone else felt inclined to talk about the wardrobe at all.',
        'ピーターは、エドマンドがルーシーをからかうのをやめるように気をつけて見張っていたし、ルーシーもほかの誰も、洋服だんすのことを話す気にはまったくならなかった。'),
    'ALARMING': ('It had become a rather alarming subject.',
        'それは、どちらかというと気味の悪い話題になっていたのだ。'),
    'ADVENT': ('And so for a time it looked as if all the adventures were coming to an end; but that was not to be.',
        'こうしてしばらくの間は、冒険はすべて終わりに近づいているかのように見えた。しかし、そうはならなかった。'),
    'HOUSE': ("This house of the Professor's - which even he knew so little about - was so old and famous that people from all over England used to come and ask permission to see over it.",
        'この教授の家は――教授自身でさえほとんど何も知らないのだが――とても古くて有名だったので、イギリス中から人々がやって来ては、中を見学させてほしいと頼んだものだった。'),
    'SORT': ('It was the sort of house that is mentioned in guide books and even in histories; and well it might be, for all manner of stories were told about it, some of them even stranger than the one I am telling you now.',
        'それは旅行案内書や、歴史の本にさえ出てくるような家だった。それももっともなことで、この家についてはありとあらゆる話が伝わっていて、中には今私がお話ししているこの物語よりも、もっと不思議なものさえあったのだ。'),
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
    v("be to do", "〜すべきだ、〜することになっている（What are we to do?＝私たちはどうすればいいのか）", 'ARE', ["are we to do"]),
    v("get off the point", "本題からそれる", 'POINT', ["get off the point"]),
    v("no one has yet done", "まだ誰も〜していない（yet は否定の意味の文で「まだ」）", 'PLAN', ["no one has yet suggested"]),
    v("mind one's own business", "他人のことに口出ししない、自分のことだけを気にかける", 'MINDING', ["minding our own business"]),
    v("see to it that 〜", "〜するように取り計らう、必ず〜するようにする（it は that 以下を指す）", 'SAW', ["saw to it that"]),
    v("alarming", "気味の悪い、不安にさせる", 'ALARMING'),
    v("be not to be", "そうなる運命ではない、そうはならない（be to 不定詞の「運命」）", 'ADVENT', ["was not to be"]),
    v("may well 〜", "〜するのももっともだ（well it might be＝it might well be の倒置）", 'SORT', ["well", "might be"]),
    v("for ＋文（接続詞）", "というのも〜だから（理由をあとから付け加える）", 'SORT', ["for"]),
    v("all manner of 〜", "あらゆる種類の〜", 'SORT', ["all manner of"]),
    # --- そのほか p.57 l.17〜p.58 の重要表現 ---
    v("on the other hand", "その一方で、他方では", 'IDEA', ["On the other hand"]),
    v("invent", "（話・考えを）作り出す、でっち上げる", 'IDEA'),
    v("for oneself", "自分で、独力で", 'IDEA', ["for themselves"]),
    v("reasonable", "それなりの、妥当な（for a reasonable time＝それらしく思えるだけの時間）", 'PRETENDING'),
    v("all over the place", "あちこちに、至る所に", 'MEAN'),
    v("probable", "ありそうな、起こりそうな（Nothing is more probable＝これほどありそうなことはない）", 'PROBABLE'),
    v("take off", "（眼鏡・服などを）外す、脱ぐ", 'PROBABLE', ["taking off"]),
    v("polish", "磨く", 'PROBABLE'),
    v("mutter to oneself", "ひとりつぶやく", 'PROBABLE', ["muttered to himself"]),
    v("be worth -ing", "〜する価値がある（well worth trying＝試してみる価値が大いにある）", 'PLAN', ["worth trying"]),
    v("a good deal＋比較級", "ずっと〜、かなり〜（比較級の強調）", 'BETTER', ["a good deal better"]),
    v("neither A nor B", "AもBも〜ない", 'SAW', ["neither", "nor"]),
    v("feel inclined to do", "〜したい気がする、〜する気になる", 'SAW', ["felt inclined to"]),
    v("for a time", "しばらくの間", 'ADVENT'),
    v("it looks as if 〜", "まるで〜のように見える", 'ADVENT', ["it looked as if"]),
    v("come to an end", "終わる", 'ADVENT', ["coming to an end"]),
    v("used to do", "以前はよく〜したものだ", 'HOUSE', ["used to"]),
    v("see over 〜", "（建物など）を見て回る、見学する", 'HOUSE', ["see over"]),
]

# 下線部訳：第3回の課題のうち p.57 l.17 以降のもの（答えは課題の解答と同じ内容）
UNDERLINE = [
    {"underline": "that idea", "task": "1. 訳しましょう　2. それでは、教授は、ルーシーくらいの女の子はどのように振る舞うのが普通だと言っているか？",
     "enHtml": "On the other hand, I don't think many girls of her age would invent <u>that idea</u> for themselves.",
     "jp": "その一方で、あの子くらいの年の女の子で、そんな考えを自分で思いつく子が多いとは思わない。",
     "note": "that idea＝直前の「別の世界にはこちらとは別の独自の時間が流れていて、向こうにどれだけ長くいても、こちらの時間はまったくたたない」という考え。I don't think 〜 は「〜とは思わない」と否定を後ろに回して訳すと自然。for oneself「自分で」、invent「作り出す」。2. 普通の振る舞い：ふりをしているのなら、出てきて話をする前に、それらしく思えるだけの時間は隠れているはずだ（If she had been pretending, she would have hidden for a reasonable time before coming out and telling her story.＝仮定法過去完了）。だから1分で戻って何時間も行っていたと言うのは作り話として不自然＝本当らしい。"},
    {"underline": "（全文）", "task": "probableの後に省略されているものを同じページから抜き出しましょう",
     "enHtml": "'Nothing is more probable.'",
     "jp": "「（そんなふうに別の世界があちこちに、すぐそこの角を曲がったところにあるということ）ほどありそうなことはないよ。」",
     "note": "省略されているもの：Nothing is more probable (than that there could be other worlds - all over the place, just round the corner - like that).　直前のピーターの質問 \"But do you really mean, sir, that there could be other worlds - all over the place, just round the corner - like that?\" の that 以下。Nothing is more＋形容詞 (than 〜)「〜ほど…なものはない」（比較級で最上級の意味）。"},
    {"underline": "（全文）", "task": None,
     "enHtml": "She felt that the conversation was beginning to get off the point.",
     "jp": "スーザンは、話が本題からそれ始めているような気がした。",
     "note": "get off the point「本題からそれる」。the point は「要点、本題」（第1回の that's just the point と同じ point）。スーザンが知りたいのは「これからどうすればいいか（What are we to do?）」なのに、教授は論理や「学校で何を教えているのやら」という話をしているので、そう感じた。"},
    {"underline": "（全文）", "task": "1. 訳しましょう　2. planの内容を説明しましょう",
     "enHtml": "There is one plan which no one has yet suggested and which is well worth trying.",
     "jp": "まだ誰も言い出していないが、試してみる価値の大いにある方法が一つあるよ。",
     "note": "which no one has yet suggested と which is well worth trying の2つの関係代名詞節が、どちらも one plan にかかる（1つ目は目的格、2つ目は主格）。be worth -ing「〜する価値がある」、well は worth を強める。2. plan の内容：直後の \"We might all try minding our own business.\"＝みんなが他人のことに口出しせず、自分のことだけを気にかけるようにしてみること（ルーシーの話を詮索したり問い詰めたりせず、そっとしておくこと）。"},
    {"underline": "（全文）", "task": None,
     "enHtml": "Peter saw to it that Edmund stopped jeering at her.",
     "jp": "ピーターは、エドマンドがルーシーをからかうのをやめるように気をつけて取り計らった。",
     "note": "see to it that 〜「〜するように取り計らう、必ず〜するようにする（ensure）」。it は形式目的語で that 以下を指す。stop -ing「〜するのをやめる」（stop to do は「〜するために立ち止まる」）。jeer at 〜「〜をあざける」（第2回の単語）。課題プリントでは see だが本文は saw。"},
    {"underline": "but that was not to be", "task": "thatの内容を明らかにして下線部を訳しましょう",
     "enHtml": "And so for a time it looked as if all the adventures were coming to an end; <u>but that was not to be</u>.",
     "jp": "こうしてしばらくの間は、冒険はすべて終わりに近づいているかのように見えた。しかし、冒険がすべて終わってしまうということにはならなかった（そうなる運命ではなかった）。",
     "note": "that＝直前の「冒険がすべて終わりに近づいている（終わってしまう）」ということ。be not to be は be to 不定詞の「運命」の用法で「そうなる運命ではなかった、そうはならなかった」。it looked as if 〜「〜であるかのように見えた」。come to an end「終わる」。"},
    {"underline": "it / it", "task": "下線部の指すものを明らかにして訳しましょう",
     "enHtml": "It was the sort of house that is mentioned in guide books and even in histories; and well <u>it</u> might be, for all manner of stories were told about <u>it</u>, some of them even stranger than the one I am telling you now.",
     "jp": "それは旅行案内書や歴史の本にさえ出てくるような家だった。そして、教授の家がそういう本に出てくるのも当然のことだった。というのも、その家についてはありとあらゆる話が伝わっていて、中には今私がお話ししているこの物語よりもっと不思議なものさえあったからだ。",
     "note": "どちらの it も「教授の家（This house of the Professor's）」。1つ目は well it might be (mentioned in guide books and histories) と省略されている。well it might be は it might well be の倒置で、may / might well 〜「〜するのももっともだ」。for は接続詞で「というのも〜だから」。all manner of 〜「あらゆる種類の〜」。the one＝the story。I は語り手（作者）。"},
]
for u in UNDERLINE:
    u["chapter"] = CH
    u["round"] = ROUND
    if u["task"] is None:
        del u["task"]

# 読解クイズ（日本語訳を選ぶ）
QUIZ = [{"en": S[k][0], "jp": S[k][1], "chapter": CH, "round": ROUND} for k in [
    'PRETENDING', 'MEAN', 'PROBABLE', 'ARE', 'MINDING', 'END', 'BETTER', 'SAW', 'ALARMING', 'ADVENT', 'HOUSE', 'PLAN',
]]

COMPREHENSION = [
    {"q": "教授が「あの子くらいの女の子が自分で思いつくとは思えない」と言った考えとは？",
     "choices": ["別の世界には独自の時間があり、向こうにどれだけいてもこちらの時間はたたない", "洋服だんすの奥に別の国がある", "フォーンという生き物がいる", "教授の家はとても不思議な家だ"],
     "answer": "別の世界には独自の時間があり、向こうにどれだけいてもこちらの時間はたたない",
     "explain": "that idea は直前の \"the other world had a separate time of its own; so that however long you stayed there it would never take up any of our time.\" を指す。"},
    {"q": "教授によると、もしルーシーがふりをしていたのなら、どうしたはずか？",
     "choices": ["それらしく思えるだけの時間隠れてから、出てきて話をした", "すぐに部屋から出てきた", "洋服だんすのことは話さなかった", "エドマンドと口裏を合わせた"],
     "answer": "それらしく思えるだけの時間隠れてから、出てきて話をした",
     "explain": "\"If she had been pretending, she would have hidden for a reasonable time before coming out and telling her story.\"（仮定法過去完了）"},
    {"q": "\"Nothing is more probable\" と言いながら、教授は何をしていたか？",
     "choices": ["眼鏡を外して磨いていた", "本棚から本を取り出していた", "窓の外を眺めていた", "パイプに火をつけていた"],
     "answer": "眼鏡を外して磨いていた",
     "explain": "\"taking off his spectacles and beginning to polish them, while he muttered to himself …\""},
    {"q": "スーザンが「話が本題からそれ始めている」と感じたのはなぜか？",
     "choices": ["知りたいのは「どうすればいいか」なのに、教授は論理や学校の話をしていたから", "教授が急に昔の思い出話を始めたから", "ピーターが別の質問を始めたから", "教授が居眠りを始めたから"],
     "answer": "知りたいのは「どうすればいいか」なのに、教授は論理や学校の話をしていたから",
     "explain": "スーザンは \"But what are we to do?\" と聞いている。get off the point「本題からそれる」。"},
    {"q": "教授が「試してみる価値が大いにある」と言った方法は？",
     "choices": ["みんなが他人のことに口出ししないようにすること", "もう一度洋服だんすを調べること", "ルーシーを医者に連れて行くこと", "両親に手紙を書くこと"],
     "answer": "みんなが他人のことに口出ししないようにすること",
     "explain": "\"We might all try minding our own business.\" mind one's own business「他人のことに口出ししない」。"},
    {"q": "その後、ルーシーにとって状況がずいぶん良くなったのはなぜか？",
     "choices": ["ピーターが、エドマンドがルーシーをからかうのをやめるように取り計らったから", "エドマンドがルーシーに謝ったから", "教授がルーシーの話を信じると皆に言ったから", "ルーシーが洋服だんすの話をやめたから"],
     "answer": "ピーターが、エドマンドがルーシーをからかうのをやめるように取り計らったから",
     "explain": "\"Peter saw to it that Edmund stopped jeering at her\" see to it that 〜「〜するように取り計らう」。"},
    {"q": "洋服だんすの話題は、その後どうなったか？",
     "choices": ["誰も話す気にならない、どちらかというと気味の悪い話題になった", "みんなが毎日話す楽しい話題になった", "教授だけが話題にした", "エドマンドがいつも持ち出した"],
     "answer": "誰も話す気にならない、どちらかというと気味の悪い話題になった",
     "explain": "\"neither she nor anyone else felt inclined to talk about the wardrobe at all. It had become a rather alarming subject.\""},
    {"q": "イギリス中から人々が教授の家にやって来たのはなぜか？",
     "choices": ["家がとても古くて有名で、中を見学させてほしかったから", "教授の講義を聞きたかったから", "家が売りに出されていたから", "教授が客を招待していたから"],
     "answer": "家がとても古くて有名で、中を見学させてほしかったから",
     "explain": "\"was so old and famous that people from all over England used to come and ask permission to see over it.\" so … that 〜「とても…なので〜」。"},
]
for c in COMPREHENSION:
    c["chapter"] = CH
    c["round"] = ROUND

GRAMMAR = [
    {"point": "for oneself（自分で）", "en": "On the other hand, I don't think many girls of her age would invent that idea ___ themselves.",
     "choices": ["for", "of", "to", "at"], "answer": "for",
     "explain": "for oneself「自分で、独力で」。主語 many girls を受けて themselves。"},
    {"point": "仮定法過去完了", "en": "If she had been pretending, she would have ___ for a reasonable time before coming out and telling her story.",
     "choices": ["hidden", "hid", "hide", "hiding"], "answer": "hidden",
     "explain": "If S had＋過去分詞, S would have＋過去分詞「（あのとき）もし〜していたなら、…しただろう」。hide-hid-hidden。"},
    {"point": "比較級で最上級の意味", "en": "\"Nothing is ___ probable,\" said the Professor.",
     "choices": ["more", "most", "much", "very"], "answer": "more",
     "explain": "Nothing is more＋形容詞 (than 〜)「〜ほど…なものはない」。than 以下（that there could be other worlds …）が省略されている。"},
    {"point": "be to 不定詞（予定・義務）", "en": "\"But what are we ___ do?\" said Susan.",
     "choices": ["to", "for", "going", "must"], "answer": "to",
     "explain": "be to do「〜すべきだ、〜することになっている」。What are we to do?「私たちはどうすればいいのか」。"},
    {"point": "関係代名詞 which（2つの節が並列）", "en": "\"there is one plan ___ no one has yet suggested and which is well worth trying.\"",
     "choices": ["which", "what", "who", "where"], "answer": "which",
     "explain": "先行詞 one plan に、which no one has yet suggested（目的格）と which is well worth trying（主格）の2つの節が and でかかっている。"},
    {"point": "be worth -ing（〜する価値がある）", "en": "\"there is one plan which no one has yet suggested and which is well worth ___.\"",
     "choices": ["trying", "to try", "try", "tried"], "answer": "trying",
     "explain": "be worth -ing「〜する価値がある」。worth の後ろは動名詞。well は「大いに」と worth を強める。"},
    {"point": "try -ing（試しに〜してみる）", "en": "\"We might all try ___ our own business,\" said he.",
     "choices": ["minding", "to mind", "mind", "minded"], "answer": "minding",
     "explain": "try -ing「試しに〜してみる」（try to do は「〜しようと努力する」）。mind one's own business「他人のことに口出ししない」。"},
    {"point": "比較級の強調（a good deal）", "en": "After this, things were a good deal ___ for Lucy.",
     "choices": ["better", "good", "best", "well"], "answer": "better",
     "explain": "a good deal＋比較級「ずっと〜」。much / far / a lot も比較級を強める。"},
    {"point": "neither A nor B（AもBも〜ない）", "en": "… and neither she ___ anyone else felt inclined to talk about the wardrobe at all.",
     "choices": ["nor", "or", "and", "but"], "answer": "nor",
     "explain": "neither A nor B「AもBも〜ない」。either A or B（AかBのどちらか）と区別する。"},
    {"point": "it looks as if 〜（まるで〜のように見える）", "en": "And so for a time it looked as ___ all the adventures were coming to an end.",
     "choices": ["if", "like", "so", "than"], "answer": "if",
     "explain": "it looks as if 〜「まるで〜のように見える」。as though も同じ意味。"},
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
