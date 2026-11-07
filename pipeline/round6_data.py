#!/usr/bin/env python3
"""第6回（Chapter 6, part 1 / 本文 p.62〜64）の課題データを各JSONに追記する。

Chapter 6 の対訳（ナルニア国物語_対訳_Chapter6.docx）の p.62〜64。p.64 最後の
"Well, of all the" は p.65 の続きとつないだ。下線部訳は第5回の課題（8問）。
この回は対訳に赤太字がない（授業で引けなかった）ので、単語は重要表現を選んで入れた。
一度きりのマージ用。同じ回の二重追加は拒否する。
"""
import json

CH = 6
ROUND = '第6回'

S = {
    'WISH': ('"I wish the Macready would hurry up and take all these people away," said Susan presently.',
        '「マクレディさん、早くあの人たちをみんな連れて行ってくれないかしら」と、しばらくしてスーザンが言った。'),
    'CRAMPED': ('"I\'m getting horribly cramped."',
        '「ひどく窮屈になってきたわ」'),
    'EXPECT': ('"I expect the pockets of these coats are full of it," said Susan, "to keep away the moths."',
        '「きっと、このコートのポケットに樟脳がいっぱい入っているのよ」とスーザンは言った。「虫よけにね」'),
    'STICK': ('"There\'s something sticking into my back," said Peter.',
        '「何かが背中に刺さってるぞ」とピーターが言った。'),
    'NOWTHAT': ('"Now that you mention it, it is cold," said Peter, "and hang it all, it\'s wet too.',
        '「言われてみると、確かに寒いね」とピーターは言った。「それに、ちくしょう、濡れてもいるぞ。'),
    'MATTER': ("What's the matter with this place?",
        'ここはいったいどうなってるんだ？'),
    'WETTER': ('It\'s getting wetter every minute."',
        'どんどん濡れてくるぞ」'),
    'STRUGGLED': ('He struggled to his feet.',
        'ピーターはやっとのことで立ち上がった。'),
    'AGAINST': ('"I\'m sitting against a tree," said Susan, "and look!',
        '「私、木に寄りかかって座ってるわ」とスーザンは言った。「それに見て！'),
    'AFTERALL': ('Why, I do believe we\'ve got into Lucy\'s wood after all."',
        'なんだ、やっぱり僕たち、ルーシーの森に入ってきたんだ」'),
    'MISTAKING': ('And now there was no mistaking it and all four children stood blinking in the daylight of a winter day.',
        'そして今や、それはもう間違えようがなかった。四人の子どもたちはみな、冬の日の昼の光の中で目をぱちぱちさせながら立っていた。'),
    'BEHIND': ('Behind them were coats hanging on pegs, in front of them were snow-covered trees.',
        '後ろには掛けくぎに掛かったコートがあり、前には雪をかぶった木々があった。'),
    'APOLOGIZE': ('"I apologize for not believing you," he said.',
        '「信じなくてごめん」とピーターは言った。'),
    'SHAKE': ('Will you shake hands?"',
        '握手してくれるかい？」'),
    'DID': ('"Of course," said Lucy, and did.',
        '「もちろんよ」とルーシーは言って、握手をした。'),
    'UGH': ('"Ugh!" said Susan, stamping her feet.',
        '「うう！」とスーザンは足踏みしながら言った。'),
    'WHATABOUT': ('What about putting on some of these coats?"',
        'ここのコートを何着か着たらどうかしら？」'),
    'DOUBTFULLY': ('"They\'re not ours," said Peter doubtfully.',
        '「僕たちのじゃないよ」とピーターはためらいがちに言った。'),
    'MIND': ('"I am sure nobody would mind," said Susan; "it isn\'t as if we wanted to take them out of the house; we shan\'t take them even out of the wardrobe."',
        '「誰も気にしないに決まってるわ」とスーザンは言った。「家の外に持ち出そうっていうわけじゃないんだし。洋服だんすの外にさえ持ち出さないんだから」'),
    'PUTIT': ('"Of course, now you put it that way, I see.',
        '「もちろん、そう言われてみると、なるほどと思うよ。'),
    'BAGGED': ('No one could say you had bagged a coat as long as you leave it in the wardrobe where you found it.',
        '見つけた洋服だんすの中に置いておく限り、コートを盗んだなんて誰にも言えないものね。'),
    'CARRIED': ("They immediately carried out Susan's very sensible plan.",
        '四人はすぐに、スーザンのとても賢明な案を実行に移した。'),
    'COATS': ('The coats were rather too big for them so that they came down to their heels and looked more like royal robes than coats when they had put them on.',
        'コートは四人には少し大きすぎたので、着てみるとかかとまで届き、コートというよりは王様の衣装のように見えた。'),
    'WARMER': ('But they all felt a good deal warmer and each thought the others looked better in their new get-up and more suitable to the landscape.',
        'それでも、みんなずっと暖かくなったし、それぞれが、ほかのみんなは新しい身なりのほうが似合っていて、この景色にもふさわしいと思った。'),
    'EXCITING': ('"This is going to be exciting enough without pretending," said Peter, as he began leading the way forward into the forest.',
        '「つもりにならなくても、これから十分わくわくすることになるさ」とピーターは言い、先に立って森の中へと進み始めた。'),
    'CLOUDS': ('There were heavy, darkish clouds overhead and it looked as if there might be more snow before night.',
        '頭上には重く黒っぽい雲が垂れこめていて、夜になる前にまた雪が降りそうだった。'),
    'ISAY': ('"I say," began Edmund presently, "oughtn\'t we to be bearing a bit more to the left, that is, if we are aiming for the lamp-post?"',
        '「ねえ」としばらくしてエドマンドが言い出した。「もう少し左のほうへ進んだほうがいいんじゃないかな。つまり、街灯を目指しているならだけど」'),
    'FORGOTTEN': ('He had forgotten for the moment that he must pretend never to have been in the wood before.',
        'エドマンドは、前にこの森に来たことなど一度もないふりをしなければならないことを、その時はうっかり忘れていたのだ。'),
    'MOMENT': ('The moment the words were out of his mouth he realized that he had given himself away.',
        'その言葉が口から出たとたん、エドマンドは自分で秘密をばらしてしまったことに気づいた。'),
    'SOYOU': ('"So you really were here," he said, "that time Lu said she\'d met you in here - and you made out she was telling lies."',
        '「じゃあ、お前は本当にここに来ていたんだな」とピーターは言った。「ルーがここでお前に会ったと言った、あの時に――それなのに、お前はルーが嘘をついていることにしたんだ」'),
    'BEASTS': ('"Well, of all the poisonous little beasts—" said Peter, and shrugged his shoulders and said no more.',
        '「まったく、ありとあらゆる意地の悪いちびのけだものの中でも――」とピーターは言いかけて、肩をすくめ、それ以上は何も言わなかった。'),
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
    v("cramped", "窮屈な、（狭くて）身動きがとれない", 'CRAMPED'),
    v("keep away 〜", "〜を寄せつけない（keep away the moths＝虫よけにする）", 'EXPECT', ["keep away"]),
    v("stick into 〜", "〜に突き刺さる", 'STICK', ["sticking into"]),
    v("now that 〜", "今や〜なので、〜した以上は（Now that you mention it＝言われてみると）", 'NOWTHAT', ["Now that"]),
    v("hang it all", "ちくしょう、くそっ（いらだちの間投詞）", 'NOWTHAT'),
    v("What's the matter with 〜?", "〜はどうなっているのか、〜はどうしたのか", 'MATTER', ["What's the matter with"]),
    v("比較級＋every minute", "刻一刻と〜、どんどん〜（getting wetter every minute＝どんどん濡れてくる）", 'WETTER', ["wetter every minute"]),
    v("struggle to one's feet", "やっとのことで立ち上がる", 'STRUGGLED', ["struggled to his feet"]),
    v("after all", "やっぱり、結局（予想に反して）", 'AFTERALL'),
    v("there is no -ing", "〜することはできない（there was no mistaking it＝間違えようがなかった）", 'MISTAKING', ["there was no mistaking"]),
    v("apologize for 〜", "〜のことで謝る（apologize for not believing you＝信じなかったことを謝る）", 'APOLOGIZE', ["apologize for"]),
    v("shake hands", "握手する", 'SHAKE'),
    v("What about -ing?", "〜するのはどうですか（提案）", 'WHATABOUT', ["What about putting"]),
    v("doubtfully", "ためらいがちに、疑わしそうに", 'DOUBTFULLY'),
    v("it isn't as if 〜", "〜というわけではない", 'MIND', ["it isn't as if"]),
    v("put it that way", "そういうふうに言う（put＝言い表す）", 'PUTIT', ["put it that way"]),
    v("bag", "（口語）くすねる、自分のものにする", 'BAGGED', ["bagged"]),
    v("as long as 〜", "〜する限りは、〜しさえすれば（条件）", 'BAGGED', ["as long as"]),
    v("carry out", "実行する", 'CARRIED', ["carried out"]),
    v("sensible", "賢明な、分別のある", 'CARRIED'),
    v("more like A than B", "BというよりはむしろAのような", 'COATS', ["more like royal robes than coats"]),
    v("get-up", "（口語）身なり、服装", 'WARMER'),
    v("lead the way", "先に立って進む、案内する", 'EXCITING', ["leading the way"]),
    v("bear (to the left)", "（左へ）進む、曲がる", 'ISAY', ["bearing a bit more to the left"]),
    v("aim for 〜", "〜を目指す", 'ISAY', ["aiming for"]),
    v("give oneself away", "（うっかり）正体・秘密をばらす、ぼろを出す", 'MOMENT', ["given himself away"]),
    v("make out (that) 〜", "〜だと（事実でないのに）言い張る、見せかける", 'SOYOU', ["made out"]),
    v("of all the＋複数名詞", "あらゆる〜の中で（後ろに最上級が続く）", 'BEASTS', ["of all the"]),
]

# 下線部訳：第5回の課題（p.62〜64）。答えは課題の解答と同じ内容
UNDERLINE = [
    {"underline": "（全文）", "task": None, "enHtml": "'Now that you mention it, it is cold,' said Peter, 'and hang it all, it's wet too.'", "jp": "「言われてみると、確かに寒いね」とピーターは言った。「それに、ちくしょう、濡れてもいるぞ」", "note": "now that 〜：「今や〜なので、〜した以上は」。Now that you mention it＝「あなたがそう言ったので（言われてみると）」。it は直前のスーザンの \"And isn't it cold?\"（寒くない？）という発言。 it is cold の is は強く読み、「（言われてみると）確かに寒い」と強調している。 hang it all：「ちくしょう、くそっ」といういらだちの間投詞（古風な口語）。 洋服だんすの中なのに寒くて濡れている → もうナルニアの雪の上にいる、という伏線。"},
    {"underline": "（全文）", "task": None, "enHtml": "He struggled to his feet.", "jp": "ピーターはやっとのことで立ち上がった。", "note": "struggle to one's feet：「苦労して（やっとのことで）立ち上がる」。struggle は「もがく」、to one's feet は「立った状態へ」（get to one's feet＝立ち上がる）。 狭い洋服だんすの中で四人が押し合っていて、しかも座っている所がどんどん濡れてきたので、もがくようにして立ち上がった。"},
    {"underline": "（全文）", "task": "itの内容を明らかにして訳しましょう。", "enHtml": "And now there was no mistaking it.", "jp": "そして今や、自分たちがルーシーの森に入ってしまったということは、もう間違えようがなかった（四人の子どもたちはみな、冬の日の昼の光の中で目をぱちぱちさせながら立っていた）。", "note": "it の内容：四人がルーシーの言っていた森（ナルニア）に入ってしまったということ。直前でピーターが \"It's trees all round. And this wet stuff is snow. Why, I do believe we've got into Lucy's wood after all.\"（周りじゅう木だらけだ。この濡れたものは雪だ。やっぱりルーシーの森に来たんだ）と言っている。 There is no -ing：「〜することはできない」（＝It is impossible to do）。mistake は「取り違える、見誤る」。"},
    {"underline": "did", "task": None, "enHtml": "'Of course,' said Lucy, and <u>did</u>.", "jp": "「もちろんよ」とルーシーは言って、握手をした。", "note": "did は代動詞で、直前のピーターの \"Will you shake hands?\"（握手してくれるかい？）を受けて shook hands の代わり。 ピーターは「信じなくてごめん」とルーシーに謝り、仲直りの握手を求めた。ルーシーはそれに快く応じた。"},
    {"underline": "you put it that way,", "task": "下線部の具体的な内容を説明しましょう", "enHtml": "Of course, now <u>you put it that way,</u> I see.", "jp": "「もちろん、君にそう言われてみると、なるほどと思うよ。」", "note": "下線部の内容：直前のスーザンの言い分：「コートを家の外に持ち出すわけではないし、洋服だんすの外にさえ持ち出さないのだから、（寒いので）コートを着ても誰も気にしないだろう」ということ。 now (that) 〜：「〜した今となっては」。put：「言い表す、表現する」。put it that way＝「そういうふうに言う」。 I see.：「なるほど、分かった」。 ピーターは最初「僕たちのコートじゃない（They're not ours）」とためらっていたが、スーザンの理屈に納得した。続けて「見つけた洋服だんすの中に置いておく限り、コートを盗んだとは誰も言えない」と言っている。"},
    {"underline": "（全文）", "task": None, "enHtml": "This is going to be exciting enough without pretending.", "jp": "「（北極探検家の）つもりにならなくても、これから十分わくわくすることになるさ。」", "note": "直前のルーシーの \"We can pretend we are Arctic explorers.\"（北極探検家になったつもりになれるわね）を受けたピーターのことば。without pretending＝without pretending (that we are Arctic explorers)。 be going to do：ここでは「（今の状況から見て）〜することになる」という予測。This＝これから始まる森の探検。 形容詞＋enough：「十分に〜」。enough は形容詞・副詞の後ろに置く（exciting enough）。名詞に付くときは前（enough time）。 without -ing：「〜しなくても、〜せずに」。本物のナルニアにいるのだから、ごっこ遊び（pretend）は必要ない、ということ。"},
    {"underline": "the words / he had given himself away", "task": "1. the wordsの内容を説明しなさい　2. he had given himself awayとは具体的にどういうことか？", "enHtml": "The moment <u>the words</u> were out of his mouth he realized that <u>he had given himself away</u>.", "jp": "その言葉が口から出たとたん、エドマンドは自分で秘密をばらしてしまったことに気づいた。", "note": "1. the words の内容：直前のエドマンドの発言 \"oughtn't we to be bearing a bit more to the left, that is, if we are aiming for the lamp-post?\"（街灯を目指しているなら、もう少し左のほうへ進んだほうがいいんじゃないか）ということ。 2. he had given himself away の内容：街灯の場所を知っているということは、前にこの森（ナルニア）に来たことがあるということ。それを自分の口でばらしてしまった、ということ。 つまり、以前ルーシーと一緒にナルニアに来ていたのに、「ルーシーと二人でふりをしていただけ」と嘘をついていたことがばれた。直前の He had forgotten for the moment that he must pretend never to have been in the wood before. がその説明。 the moment S V：「〜するとすぐに、〜したとたん」（接続詞のように使う。第5回単語の the moment 〜 と同じ）。 give oneself away：「（うっかり）正体・秘密をばらす、ぼろを出す」。 このあとピーターが \"So you really were here\"（じゃあ本当にここに来ていたんだな）と言う。"},
    {"underline": "（全文）", "task": "beastsの後に続く文章はどのようなものでしょうか？自分で作ってみましょう", "enHtml": "'Well, of all the poisonous little beasts—' said Peter.", "jp": "「まったく、ありとあらゆる意地の悪いちびのけだものの中でも――」とピーターは言った。", "note": "作文例：Well, of all the poisonous little beasts (I have ever known), you are the worst!（今まで会ったありとあらゆる意地の悪いちびのけだものの中でも、お前が最悪だ！） （別解）Well, of all the poisonous little beasts in the world, you are the most poisonous! of all the＋複数名詞：「あらゆる〜の中で」。後ろに最上級（the worst / the most 〜）を続けて「〜の中でいちばん…だ」と言う形になる。 poisonous は「毒のある」→ ここでは「意地の悪い、たちの悪い」。little beast は「ちびのけだもの」で、弟エドマンドをののしることば。 本文では、ピーターはあまりの腹立たしさにここで言葉を切り、shrugged his shoulders and said no more（肩をすくめて、それ以上何も言わなかった）。だから文が最後まで書かれていない。"},
]
for u in UNDERLINE:
    u["chapter"] = CH
    u["round"] = ROUND
    if u["task"] is None:
        del u["task"]

# 読解クイズ（日本語訳を選ぶ）
QUIZ = [{"en": S[k][0], "jp": S[k][1], "chapter": CH, "round": ROUND} for k in [
    'WISH', 'EXPECT', 'AGAINST', 'BEHIND', 'APOLOGIZE', 'MIND', 'BAGGED', 'COATS', 'WARMER', 'CLOUDS', 'ISAY', 'FORGOTTEN', 'SOYOU', 'BEASTS',
]]

COMPREHENSION = [
    {"q": "洋服だんすの中でエドマンドが文句を言ったのは何について？",
     "choices": ["樟脳（防虫剤）のひどいにおい", "暗さ", "スーザンが押してくること", "コートが重いこと"],
     "answer": "樟脳（防虫剤）のひどいにおい",
     "explain": "\"And what a filthy smell of camphor!\" スーザンは、虫よけにコートのポケットに入っているのだろうと言う。"},
    {"q": "ピーターが「ここはどうなってるんだ」と言ったのはなぜか？",
     "choices": ["寒いうえに、座っている所がどんどん濡れてきたから", "背中に何かが刺さったから", "外から誰かの声が聞こえたから", "扉が開かなくなったから"],
     "answer": "寒いうえに、座っている所がどんどん濡れてきたから",
     "explain": "\"it's wet too. … I'm sitting on something wet. It's getting wetter every minute.\" 実はもうナルニアの雪の上にいた。"},
    {"q": "スーザンが「きゃあっ」と声を上げたとき、気づいたことは？",
     "choices": ["木に寄りかかって座っていて、向こうが明るくなってきていること", "コートが消えていること", "ルーシーがいなくなったこと", "マクレディ夫人が扉を開けたこと"],
     "answer": "木に寄りかかって座っていて、向こうが明るくなってきていること",
     "explain": "\"I'm sitting against a tree … and look! It's getting light - over there.\""},
    {"q": "自分たちがルーシーの森に来たと分かったとき、ピーターが最初にしたことは？",
     "choices": ["ルーシーに、信じなかったことを謝って握手を求めた", "すぐに洋服だんすに戻ろうと言った", "エドマンドを叱った", "森の探検に一人で出かけた"],
     "answer": "ルーシーに、信じなかったことを謝って握手を求めた",
     "explain": "\"Peter turned at once to Lucy. 'I apologize for not believing you … Will you shake hands?'\""},
    {"q": "コートを着ることについて、スーザンが「誰も気にしない」と考えた理由は？",
     "choices": ["家の外どころか、洋服だんすの外にさえ持ち出さないから", "コートはもともと自分たちのものだから", "教授が着てもいいと言ったから", "あとで洗って返すから"],
     "answer": "家の外どころか、洋服だんすの外にさえ持ち出さないから",
     "explain": "\"it isn't as if we wanted to take them out of the house; we shan't take them even out of the wardrobe.\" ピーターも \"now you put it that way, I see\" と納得する。"},
    {"q": "コートを着た四人の姿はどう見えたか？",
     "choices": ["大きすぎてかかとまで届き、コートというより王様の衣装のようだった", "小さすぎて腕が出てしまった", "北極探検家そのものだった", "おかしくてみんなで笑った"],
     "answer": "大きすぎてかかとまで届き、コートというより王様の衣装のようだった",
     "explain": "\"they came down to their heels and looked more like royal robes than coats\""},
    {"q": "エドマンドが「自分で秘密をばらしてしまった」のは、何を言ったからか？",
     "choices": ["街灯を目指すなら、もう少し左へ進むべきだと言った", "前にフォーンに会ったことがあると言った", "白い魔女を知っていると言った", "家に帰りたいと言った"],
     "answer": "街灯を目指すなら、もう少し左へ進むべきだと言った",
     "explain": "\"oughtn't we to be bearing a bit more to the left, that is, if we are aiming for the lamp-post?\" 街灯の場所を知っている＝前に来たことがある、とばれた。"},
    {"q": "ピーターがエドマンドを責めたのは、どんなことについてか？",
     "choices": ["本当はナルニアに来ていたのに、ルーシーが嘘をついていることにしたこと", "コートを勝手に着たこと", "道を間違えたこと", "マクレディ夫人に見つかったこと"],
     "answer": "本当はナルニアに来ていたのに、ルーシーが嘘をついていることにしたこと",
     "explain": "\"So you really were here … that time Lu said she'd met you in here - and you made out she was telling lies.\" make out＝（事実でないのに）言い張る。"},
]
for c in COMPREHENSION:
    c["chapter"] = CH
    c["round"] = ROUND

GRAMMAR = [
    {"point": "I wish＋S would（〜してくれればいいのに）", "en": "\"I wish the Macready ___ hurry up and take all these people away,\" said Susan presently.",
     "choices": ["would", "will", "shall", "can"], "answer": "would",
     "explain": "I wish S would 〜「Sが〜してくれればいいのに」（相手の行動への不満・願望）。I wish の後は仮定法なので will ではなく would。"},
    {"point": "now that 〜（今や〜なので）", "en": "\"Now ___ you mention it, it is cold,\" said Peter.",
     "choices": ["that", "when", "if", "as"], "answer": "that",
     "explain": "now that 〜「今や〜なので、〜した以上は」。Now that you mention it＝言われてみると。"},
    {"point": "比較級＋every minute", "en": "I'm sitting on something wet. It's getting ___ every minute.",
     "choices": ["wetter", "wet", "wettest", "more wet"], "answer": "wetter",
     "explain": "get＋比較級「ますます〜になる」。every minute を付けて「刻一刻と、どんどん」。wet の比較級は t を重ねて wetter。"},
    {"point": "there is no -ing（〜できない）", "en": "And now there was no ___ it.",
     "choices": ["mistaking", "mistake", "to mistake", "mistaken"], "answer": "mistaking",
     "explain": "There is no -ing「〜することはできない」（＝It is impossible to do）。no の後なので動名詞。"},
    {"point": "前置詞＋動名詞の否定（not -ing）", "en": "\"I apologize for ___ believing you,\" he said.",
     "choices": ["not", "no", "don't", "never to"], "answer": "not",
     "explain": "動名詞の否定は not＋-ing。apologize for not believing you＝君を信じなかったことを謝る。"},
    {"point": "What about -ing?（〜するのはどう？）", "en": "\"It's pretty cold. What about ___ on some of these coats?\"",
     "choices": ["putting", "put", "to put", "puts"], "answer": "putting",
     "explain": "What about -ing?「〜するのはどうですか」。about は前置詞なので後ろは動名詞。How about -ing? も同じ。"},
    {"point": "as long as 〜（〜する限りは）", "en": "No one could say you had bagged a coat as ___ as you leave it in the wardrobe where you found it.",
     "choices": ["long", "far", "soon", "well"], "answer": "long",
     "explain": "as long as 〜「〜する限りは、〜しさえすれば」（条件）。as far as は「〜の範囲では」で意味が違う。"},
    {"point": "more A than B（BというよりA）", "en": "… they came down to their heels and looked more like royal robes ___ coats.",
     "choices": ["than", "as", "that", "to"], "answer": "than",
     "explain": "more A than B「BというよりはむしろA」。ここでは look like の like を使って more like royal robes than coats。"},
    {"point": "完了不定詞（to have＋過去分詞）", "en": "He had forgotten for the moment that he must pretend never to ___ been in the wood before.",
     "choices": ["have", "be", "has", "having"], "answer": "have",
     "explain": "pretend never to have been 〜「一度も〜に来たことがないふりをする」。完了不定詞で、pretend する時より前のことを表す。never は不定詞の前に置く。"},
    {"point": "再帰代名詞（give oneself away）", "en": "The moment the words were out of his mouth he realized that he had given ___ away.",
     "choices": ["himself", "him", "his", "he"], "answer": "himself",
     "explain": "give oneself away「（うっかり）正体・秘密をばらす」。主語 he と同じ人なので himself。"},
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
