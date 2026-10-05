#!/usr/bin/env python3
"""第2回授業（Chapter 5, part 2 / 本文 p.53〜55）の課題データを各JSONに追記する。

対訳プリントで赤太字になっている語句（授業で重要とされたもの）は必ず単語に含める。
p.53〜54 の課題文（第1回と同じ問題）は第1回のデータに入っているので、
下線部訳・文法などの問題は p.55 の新しい課題を中心に追加する。
一度きりのマージ用。同じ回の二重追加は拒否する。
"""
import json

CH = 5
ROUND = '第2回'

S = {
    'GOOD': ('But whichever it is, what good do you think you\'ll do by jeering and nagging at her one day and encouraging her the next?"',
        'でも、そのどちらだとしても、ある日は冷やかしていじめておいて、次の日にはけしかける(励ます)ようなことをして、一体それが何の役に立つと思っているんだ?」'),
    'THOUGHT': ('"I thought - I thought—" said Edmund; but he couldn\'t think of anything to say.',
        '「僕はただ――僕はただ――」エドマンドはそう言ったが、あとが続かなかった。'),
    'SPITE': ('"You didn\'t think anything at all," said Peter; "it\'s just spite.',
        '「お前は何も考えちゃいなかったんだ」とピーターは言った。「ただの意地悪だ。'),
    'BEASTLY': ('You\'ve always liked being beastly to anyone smaller than yourself; we\'ve seen that at school before now."',
        'お前は昔から、自分より小さい相手にひどいことをするのが好きだった。学校でもそういうところを何度も見てきたんだからな」'),
    'ROW': ('"Do stop it," said Susan; "it won\'t make things any better having a row between you two.',
        '「もうやめてよ」とスーザンが言った。「二人で口けんかしたって、何も良くなりはしないわ。'),
    'FIND': ('Let\'s go and find Lucy."',
        'ルーシーを捜しに行きましょう」'),
    'SURPRISING': ('It was not surprising that when they found Lucy, a good deal later, everyone could see that she had been crying.',
        'しばらく経ってようやくルーシーを見つけたとき、彼女が泣いていたのが誰の目にも明らかだったのも、無理のないことだった。'),
    'NOTHING': ('Nothing they could say to her made any difference.',
        'みんなが何を言っても、ルーシーの様子は少しも変わらなかった。'),
    'STUCK': ('She stuck to her story and said: "I don\'t care what you think, and I don\'t care what you say.',
        '彼女は自分の話を曲げず、こう言った。「みんながどう思おうとかまわないし、何を言おうとかまわない。'),
    'TELL': ('You can tell the Professor or you can write to Mother or you can do anything you like.',
        '教授に言いつけてもいいし、お母さんに手紙を書いてもいいし、好きなようにすればいいわ。'),
    'FAUN': ('I know I\'ve met a Faun in there and - I wish I\'d stayed there and you are all beasts, beasts."',
        '私はあそこでフォーンに会ったんだから――あそこに残っていればよかった。みんなひどい、ひどい人よ」'),
    'EVENING': ('It was an unpleasant evening.',
        '気まずい晩になった。'),
    'MISERABLE': ("Lucy was miserable and Edmund was beginning to feel that his plan wasn't working as well as he had expected.",
        'ルーシーはみじめな気分で、エドマンドは自分の計画が思ったほどうまくいっていないと感じ始めていた。'),
    'MIND': ('The two older ones were really beginning to think that Lucy was out of her mind.',
        '上の二人は、ルーシーが本当に頭がおかしくなってしまったのではないかと、真剣に思い始めていた。'),
    'WHISPERS': ('They stood in the passage talking about it in whispers long after she had gone to bed.',
        'ルーシーが寝てしまってからもずいぶん長いあいだ、二人は廊下に立ち、そのことをひそひそと話し合っていた。'),
    'RESULT': ('The result was the next morning they decided that they really would go and tell the whole thing to the Professor.',
        'その結果、翌朝二人は、本当にこのことを全部教授に話しに行こうと決めた。'),
    'BEYOND': ('"He\'ll write to Father if he thinks there is really something wrong with Lu," said Peter; "it\'s getting beyond us."',
        '「ルーに本当に何かおかしなところがあると思ったら、教授がお父さんに手紙を書いてくれるだろう」とピーターは言った。「もう僕たちの手には負えないよ」'),
    'DISPOSAL': ('So they went and knocked at the study door, and the Professor said, "Come in," and got up and found chairs for them and said he was quite at their disposal.',
        'そこで二人は書斎のドアをノックしに行った。すると教授は「お入り」と言い、立ち上がって椅子を用意し、何でも遠慮なく話してくれてかまわないと言った。'),
    'TIPS': ('Then he sat listening to them with the tips of his fingers pressed together and never interrupting, till they had finished the whole story.',
        'それから教授は、指先を合わせるようにして座り、二人が話を全部終えるまで、一度も口を挟まずに耳を傾けていた。'),
    'AFTER': ('After that he said nothing for quite a long time.',
        'そのあと、教授はかなり長いあいだ、何も言わなかった。'),
    'LAST': ('Then he cleared his throat and said the last thing either of them expected: "How do you know," he asked, "that your sister\'s story is not true?"',
        'それから咳払いをすると、二人が最も予想していなかったことを口にした。「妹さんの話が本当ではないと、どうして分かるんだね?」と教授は尋ねた。'),
    'OHBUT': ('"Oh, but—" began Susan, and then stopped.',
        '「まあ、でも――」とスーザンは言いかけて、そこで口をつぐんだ。'),
    'SERIOUS': ("Anyone could see from the old man's face that he was perfectly serious.",
        '老教授の顔を見れば、彼が大まじめであることは誰の目にも明らかだった。'),
    'PULLED': ('Then Susan pulled herself together and said, "But Edmund said they had only been pretending."',
        'それからスーザンは気を取り直して言った。「でも、エドマンドは、二人でただふりをしていただけだって言ったんです」'),
    'POINT': ('"That is a point," said the Professor, "which certainly deserves consideration; very careful consideration.',
        '「それは確かに考えてみる価値のある点だね」と教授は言った。「それも、よくよく考えてみるべき点だ。'),
    'INSTANCE': ('For instance - if you will excuse me for asking the question - does your experience lead you to regard your brother or your sister as the more reliable?',
        'たとえば――こんなことを尋ねるのを許してもらえるなら――これまでの経験からして、君たちは弟さんと妹さんのどちらのほうが信用できると思うかね?'),
    'IMEAN': ('I mean, which is the more truthful?"',
        'つまり、どちらのほうが正直かということだが」'),
    'FUNNY': ('"That\'s just the funny thing about it, sir," said Peter.',
        '「そこがまさに妙なところなんです、先生」とピーターは言った。'),
    'UPTILL': ('"Up till now, I\'d have said Lucy every time."',
        '「これまでだったら、いつだってルーシーのほうだと答えていたでしょう」'),
    'DEAR': ('"And what do you think, my dear?" said the Professor, turning to Susan.',
        '「では、君はどう思うかね?」と教授はスーザンのほうを向いて言った。'),
    'GENERAL': ('"Well," said Susan, "in general, I\'d say the same as Peter, but this couldn\'t be true - all this about the wood and the faun."',
        '「そうですね」とスーザンは言った。「ふだんならピーターと同じ意見です。でも、今度のことは本当のはずがありません――森だとかフォーンだとか、そういう話は全部」'),
    'MORETHAN': ('"That is more than I know," said the Professor,',
        '「それは私にも分からないね」と教授は言った。'),
    'CHARGE': ('"and a charge of lying against someone whom you have always found truthful is a very serious thing; a very serious thing indeed."',
        '「それに、これまでずっと正直だと分かっている人を嘘つき呼ばわりするのは、とても重大なことだよ。本当に重大なことだ」'),
    'AFRAID': ('"We were afraid it mightn\'t even be lying," said Susan; "we thought there might be something wrong with Lucy."',
        '「私たち、ひょっとすると嘘ですらないのではと心配していたんです」とスーザンは言った。「ルーシーはどこかおかしいのかもしれないと思って」'),
    'MADNESS': ('"Madness, you mean?" said the Professor quite',
        '「気が変になっている、ということかね?」と教授は実に……(p.56へ続く)'),
}


def v(term, gloss, key, marks=None, html=None):
    en, jp = S[key]
    if html is None:
        html = en
        for m in (marks or [term]):
            assert m in html, (m, en)
            html = html.replace(m, f'<mark>{m}</mark>', 1)
    return {"term": term, "enHtml": html, "jp": jp, "chapter": CH, "gloss": gloss, "round": ROUND}


REGARD_HTML = S['INSTANCE'][0].replace('lead you to', '<mark>lead you to</mark>', 1).replace('regard', '<mark>regard</mark>', 1).replace(' as the more', ' <mark>as</mark> the more', 1)

VOCAB = [
    # --- 対訳プリントで赤太字（授業で重要）の語句：必ず含める ---
    v("do good", "役に立つ（what good …? ＝一体何の役に立つのか）", 'GOOD', ["good"]),
    v("jeer at 〜", "〜をあざける、冷やかす", 'GOOD', ["jeering"]),
    v("nag at 〜", "〜にがみがみ言う、小言を言う", 'GOOD', ["nagging"]),
    v("encourage", "励ます、けしかける", 'GOOD', ["encouraging"]),
    v("row", "口げんか、口論（発音は［ráu］）", 'ROW', ["row"]),
    v("stick to 〜", "〜を曲げない、〜に固執する（stick-stuck-stuck）", 'STUCK', ["stuck to"]),
    v("at one's disposal", "〜の自由に使える、何でも力になる", 'DISPOSAL', ["at their disposal"]),
    v("the last thing", "最も〜しそうにないこと（the last thing 人 expected＝まったく予想外のこと）", 'LAST', ["last thing"]),
    v("pull oneself together", "気を取り直す、落ち着きを取り戻す", 'PULLED', ["pulled herself together"]),
    v("deserve consideration", "考慮に値する、考えてみる価値がある", 'POINT', ["deserves consideration"]),
    v("lead 人 to do", "人に〜させる（経験が人を〜へ導く→経験から〜と考える）", 'INSTANCE', html=REGARD_HTML),
    v("regard A as B", "AをBとみなす", 'INSTANCE', html=REGARD_HTML),
    v("more than I know", "私には分からない（直訳：私が知っている以上のこと）", 'MORETHAN'),
    v("charge", "非難、告発（a charge of lying against 〜＝〜を嘘つきだと責めること）", 'CHARGE', ["charge"]),
    # --- そのほか p.53〜55 の重要表現 ---
    v("before now", "これまでに（何度も）", 'BEASTLY', ["before now"]),
    v("a good deal later", "かなりたってから", 'SURPRISING', ["a good deal later"]),
    v("make a difference", "違いを生む、効き目がある（not any difference＝まったく効果がない）", 'NOTHING', ["made any difference"]),
    v("miserable", "みじめな、ひどく落ち込んだ", 'MISERABLE'),
    v("out of one's mind", "頭がおかしくなって、正気を失って", 'MIND', ["out of her mind"]),
    v("in whispers", "ひそひそ声で", 'WHISPERS'),
    v("get beyond 人", "人の手に負えなくなる", 'BEYOND', ["getting beyond us"]),
    v("interrupt", "（話に）口を挟む、さえぎる", 'TIPS', ["interrupting"]),
    v("clear one's throat", "咳払いをする", 'LAST', ["cleared his throat"]),
    v("for instance", "たとえば", 'INSTANCE', ["For instance"]),
    v("reliable", "信頼できる", 'INSTANCE'),
    v("truthful", "正直な、嘘をつかない", 'IMEAN'),
    v("up till now", "今までは", 'UPTILL', ["Up till now"]),
    v("in general", "ふだんは、一般的に", 'GENERAL'),
]

# 下線部訳：第2回で新しく出た p.55 の課題
UNDERLINE = [
    {"underline": "（全文）", "task": None,
     "enHtml": "Then Susan pulled herself together and said.",
     "jp": "それからスーザンは気を取り直して言った。",
     "note": "pull oneself together「気を取り直す、落ち着きを取り戻す」。直前で教授の予想外の質問に驚いて言葉に詰まった（\"Oh, but—\"）スーザンが、立ち直って話し始める場面。"},
    {"underline": "（全文）", "task": None,
     "enHtml": "'That is a point,' said the Professor, 'which certainly deserves consideration.'",
     "jp": "「それは確かに考えてみる価値のある点だね」と教授は言った。",
     "note": "which の先行詞は a point（said the Professor が間に挟まって離れている）。deserve consideration「考慮に値する」。That＝スーザンの言った「エドマンドは、二人でふりをしていただけだと言った」こと。"},
    {"underline": "（全文）", "task": "文構造に気をつけて、訳しましょう",
     "enHtml": "For instance, --if you will excuse me for asking the question--does your experience lead you to regard your brother or your sister as the more reliable?",
     "jp": "たとえば――こんなことを尋ねるのを許してもらえるなら――これまでの経験からすると、君たちは弟さん（エドマンド）と妹さん（ルーシー）のどちらのほうが信頼できると思うかね？",
     "note": "ダッシュの間は挿入（if you will …：will は相手の意志「〜してくれるなら」）。your experience lead(s) you to do は無生物主語→「経験から〜と考える」。regard A as B「AをBとみなす」。二者の比較なので the more reliable。ピーターの答え：これまでならいつもルーシー。スーザンの答え：ふだんならルーシーだが、森とフォーンの話は本当のはずがない。"},
    {"underline": "That", "task": "1. 下線部の内容は？　2. 訳しましょう",
     "enHtml": "'<u>That</u> is more than I know,' said the Professor, 'and a charge of lying against someone whom you have always found truthful is a very serious thing; a very serious thing indeed.'",
     "jp": "「それは私には分からないね」と教授は言った。「それに、これまでずっと正直だと分かっている人に対して、嘘をついていると責めるのは、とても重大なことだよ。本当に、とても重大なことだ」",
     "note": "下線部 That＝スーザンの「森やフォーンの話が本当であるはずがない」ということ。more than I know「私には分からない」（＝本当ではないとは言い切れない）。a charge of lying against 〜「〜を嘘つきだと責めること」が主語。someone whom you have always found truthful は find O C の O が関係代名詞 whom になった形。"},
]
for u in UNDERLINE:
    u["chapter"] = CH
    u["round"] = ROUND
    if u["task"] is None:
        del u["task"]

# 読解クイズ（日本語訳を選ぶ）：p.53〜55 の第1回で出していない文
QUIZ = [{"en": S[k][0], "jp": S[k][1], "chapter": CH, "round": ROUND} for k in [
    'ROW', 'SURPRISING', 'STUCK', 'MISERABLE', 'MIND', 'WHISPERS', 'PULLED', 'POINT', 'INSTANCE', 'UPTILL', 'GENERAL', 'CHARGE', 'AFRAID',
]]

COMPREHENSION = [
    {"q": "スーザンが「二人でけんかしないで」と止めたあと、提案したことは？",
     "choices": ["ルーシーを捜しに行くこと", "教授に相談しに行くこと", "お母さんに手紙を書くこと", "洋服だんすをもう一度調べること"],
     "answer": "ルーシーを捜しに行くこと",
     "explain": "\"Do stop it … Let's go and find Lucy.\"。教授に相談するのは翌朝になってから決めたこと。"},
    {"q": "その晩、エドマンドが感じ始めていたことは？",
     "choices": ["自分の計画が思ったほどうまくいっていない", "ルーシーの話は本当かもしれない", "ピーターに謝らなければならない", "教授に叱られるかもしれない"],
     "answer": "自分の計画が思ったほどうまくいっていない",
     "explain": "\"Edmund was beginning to feel that his plan wasn't working as well as he had expected.\""},
    {"q": "ルーシーが寝たあと、ピーターとスーザンはどうしていたか？",
     "choices": ["廊下に立って、ひそひそ声で長いあいだ話し合っていた", "すぐに教授の書斎へ行った", "洋服だんすの部屋を調べに行った", "エドマンドと一緒にトランプをしていた"],
     "answer": "廊下に立って、ひそひそ声で長いあいだ話し合っていた",
     "explain": "\"They stood in the passage talking about it in whispers long after she had gone to bed.\" in whispers＝ひそひそ声で。"},
    {"q": "教授の質問（話が本当でないとどうして分かるのか）に、スーザンが最初に持ち出した反論は？",
     "choices": ["エドマンドが「二人でふりをしていただけ」と言ったこと", "洋服だんすの奥は板で行き止まりだったこと", "ルーシーが前にも嘘をついたことがあること", "フォーンなどいるはずがないこと"],
     "answer": "エドマンドが「二人でふりをしていただけ」と言ったこと",
     "explain": "\"But Edmund said they had only been pretending.\" 教授はそれを「考えてみる価値のある点だ」と受け止め、では二人のどちらが信頼できるかと尋ねる。"},
    {"q": "「弟と妹のどちらが信頼できるか」と聞かれて、ピーターはどう答えたか？",
     "choices": ["これまでなら、いつもルーシーと答えていた", "これまでなら、いつもエドマンドと答えていた", "どちらも同じくらい信頼できる", "どちらも信頼できない"],
     "answer": "これまでなら、いつもルーシーと答えていた",
     "explain": "\"That's just the funny thing about it, sir. Up till now, I'd have said Lucy every time.\" だからこそ今回のことが「妙」だと言っている。"},
    {"q": "同じ質問へのスーザンの答えとして正しいものは？",
     "choices": ["ふだんならピーターと同じ（ルーシー）だが、森とフォーンの話は本当のはずがない", "エドマンドのほうがずっと信頼できる", "ルーシーの話は全部本当だと思う", "分からないので教授に決めてほしい"],
     "answer": "ふだんならピーターと同じ（ルーシー）だが、森とフォーンの話は本当のはずがない",
     "explain": "\"in general, I'd say the same as Peter, but this couldn't be true - all this about the wood and the faun.\""},
    {"q": "教授が「とても重大なことだ」と言ったのは何について？",
     "choices": ["いつも正直だと分かっている人を、嘘つきだと責めること", "子どもが夜遅くまで起きていること", "洋服だんすに勝手に入ること", "親に手紙を書かずに済ませること"],
     "answer": "いつも正直だと分かっている人を、嘘つきだと責めること",
     "explain": "\"a charge of lying against someone whom you have always found truthful is a very serious thing\"。charge＝非難。"},
    {"q": "スーザンたちが「嘘ですらないかもしれない」と心配していたのは、どういうことか？",
     "choices": ["ルーシーの頭がどこかおかしくなっているかもしれないこと", "ルーシーが本当に別の国に行ったかもしれないこと", "エドマンドが嘘をついているかもしれないこと", "教授が話を信じてくれないかもしれないこと"],
     "answer": "ルーシーの頭がどこかおかしくなっているかもしれないこと",
     "explain": "\"we thought there might be something wrong with Lucy.\" 教授は \"Madness, you mean?\"（狂気、ということかね）と聞き返す。"},
]
for c in COMPREHENSION:
    c["chapter"] = CH
    c["round"] = ROUND

GRAMMAR = [
    {"point": "動名詞（〜することは）", "en": "\"It won't make things any better ___ a row between you two.\"",
     "choices": ["having", "to have", "had", "have"], "answer": "having",
     "explain": "it は形式主語で、後ろの having a row（口げんかをすること）を指す口語の形。「二人で口げんかしても、何も良くならない」。"},
    {"point": "It is … that 〜（〜なのは…だ）", "en": "It was not surprising ___ when they found Lucy, a good deal later, everyone could see that she had been crying.",
     "choices": ["that", "what", "which", "if"], "answer": "that",
     "explain": "It は形式主語で、that 以下が本当の主語。「〜なのも無理はなかった」。"},
    {"point": "再帰代名詞（pull oneself together）", "en": "Then Susan pulled ___ together and said, \"But Edmund said they had only been pretending.\"",
     "choices": ["herself", "her", "she", "hers"], "answer": "herself",
     "explain": "pull oneself together「気を取り直す」。主語 Susan と同じ人なので再帰代名詞 herself。"},
    {"point": "関係代名詞 which（先行詞が離れている）", "en": "\"That is a point,\" said the Professor, \"___ certainly deserves consideration.\"",
     "choices": ["which", "what", "who", "where"], "answer": "which",
     "explain": "先行詞は a point（物）。said the Professor が挟まって離れているが、a point which certainly deserves consideration とつながる。what は先行詞を含むので不可。"},
    {"point": "if you will …（相手の意志：〜してくれるなら）", "en": "For instance - if you ___ excuse me for asking the question - does your experience lead you to regard your brother or your sister as the more reliable?",
     "choices": ["will", "shall", "must", "should"], "answer": "will",
     "explain": "条件節の will は未来ではなく相手の意志。「こんな質問をすることを許してくれるなら」という丁寧な前置き。"},
    {"point": "lead O to do（Oに〜させる）", "en": "… does your experience lead you ___ regard your brother or your sister as the more reliable?",
     "choices": ["to", "for", "into", "at"], "answer": "to",
     "explain": "lead O to do「Oを〜するように導く、Oに〜させる」。無生物主語なので「経験から〜と考える」と訳すと自然。"},
    {"point": "regard A as B（AをBとみなす）", "en": "… does your experience lead you to regard your brother or your sister ___ the more reliable?",
     "choices": ["as", "for", "to", "like"], "answer": "as",
     "explain": "regard A as B「AをBとみなす」。同じ形に think of A as B、look on A as B など。"},
    {"point": "the＋比較級（二者のうち〜なほう）", "en": "… regard your brother or your sister as ___ more reliable?",
     "choices": ["the", "a", "most", "much"], "answer": "the",
     "explain": "2人のうち「より信頼できるほう」と特定するので the＋比較級。I mean, which is the more truthful? も同じ形。"},
    {"point": "関係代名詞 whom（find O C の O）", "en": "\"and a charge of lying against someone ___ you have always found truthful is a very serious thing\"",
     "choices": ["whom", "whose", "what", "which"], "answer": "whom",
     "explain": "you have always found someone truthful（その人が正直だと分かっている）の someone が先行詞になり、目的格の whom が使われている。"},
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
