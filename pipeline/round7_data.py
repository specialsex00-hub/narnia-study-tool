#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""第7回（Chapter 6, part 2 / 本文 p.65〜67）の課題データを各JSONに追記する。

Chapter 6 の対訳（ナルニア国物語_対訳_Chapter6.docx）の p.65〜67。p.65〜66 にまたがる
"Snow had drifted …" はつないだ。p.67 最後の "And it's getting colder every minute, and" は
p.68 に続くので入れない。下線部訳は第6回の課題（8問）。
対訳プリントで赤太字になっている語句（授業で重要とされたもの）は必ず単語に含める。
一度きりのマージ用。同じ回の二重追加は拒否する。
"""
import json

CH = 6
ROUND = '第7回'

S = {
    'RESUMED': ('There seemed, indeed, no more to say, and presently the four resumed their journey; but Edmund was saying to himself, "I\'ll pay you all out for this, you pack of stuck-up, self-satisfied prigs."',
        '実際、それ以上言うことはなさそうだったので、やがて四人はまた歩き始めた。しかしエドマンドは心の中でこうつぶやいていた。「このお返しは、みんなにきっとしてやるからな。お高くとまって、うぬぼれた、お上品ぶったやつらめ」'),
    'WHERE': ('"Where are we going anyway?" said Susan, chiefly for the sake of changing the subject.',
        '「ところで、私たちどこへ行くの？」とスーザンが言った。主に話題を変えるためだった。'),
    'LEADER': ('"I think Lu ought to be the leader," said Peter; "goodness knows she deserves it.',
        '「ルーがリーダーになるべきだと思うな」とピーターは言った。「ルーにはその資格が十分あるよ。'),
    'AGREED': ('Everyone agreed to this and off they went, walking briskly and stamping their feet.',
        'みんなこれに賛成して、足を踏み鳴らしながら、きびきびと歩いて出発した。'),
    'PROVED': ('Lucy proved a good leader.',
        'ルーシーはよいリーダーぶりを見せた。'),
    'ATFIRST': ("At first she wondered whether she would be able to find the way, but she recognized an odd-looking tree in one place and a stump in another and brought them on to where the ground became uneven and into the little valley and at last to the very door of Mr Tumnus's cave.",
        '初めのうちは、道が分かるかどうか自信がなかったが、ある所では変わった形の木に、別の所では切り株に見覚えがあったので、みんなを連れて地面がでこぼこになっている所まで進み、小さな谷に入り、とうとうタムナスさんのほら穴の戸口までたどり着いた。'),
    'SURPRISE': ('But there a terrible surprise awaited them.',
        'ところが、そこではとんでもない驚きが四人を待ち受けていた。'),
    'DOOR': ('The door had been wrenched off its hinges and broken to bits.',
        '扉はちょうつがいからもぎ取られ、こなごなに壊されていた。'),
    'INSIDE': ('Inside, the cave was dark and cold and had the damp feel and smell of a place that had not been lived in for several days.',
        'ほら穴の中は暗く冷え切っていて、何日も人が住んでいない場所の、じめじめした感じとにおいがした。'),
    'FLUNG': ('Someone had apparently flung it about the room and then stamped it out.',
        'どうやら誰かが、暖炉の火を部屋中にまき散らしてから、踏みつけて消したらしかった。'),
    'CROCKERY': ("The crockery lay smashed on the floor and the picture of the Faun's father had been slashed into shreds with a knife.",
        '瀬戸物は床の上で粉々に割れていて、フォーンのお父さんの肖像画はナイフでずたずたに切り裂かれていた。'),
    'WASHOUT': ('"This is a pretty good wash-out," said Edmund; "not much good coming here."',
        '「こりゃあ、まったくの期待はずれだな」とエドマンドは言った。「ここへ来たって、たいして意味がなかったね」'),
    'STOOP': ('"What is this?" said Peter, stooping down.',
        '「これは何だ？」とピーターはかがみこんで言った。'),
    'NAILED': ('He had just noticed a piece of paper which had been nailed through the carpet to the floor.',
        'ピーターは、じゅうたんの上から床にくぎで打ちつけられた一枚の紙に、ちょうど気づいたところだった。'),
    'NOTICE': ("The former occupant of these premises, the Faun Tumnus, is under arrest and awaiting his trial on a charge of High Treason against her Imperial Majesty Jadis, Queen of Narnia, Chatelaine of Cair Paravel, Empress of the Lone Islands, etc., also of comforting her said Majesty's enemies, harbouring spies and fraternizing with Humans.",
        'この住居の前の住人、フォーンのタムナスは、ナルニアの女王、ケア・パラベルの城主、離れ島諸島の女帝などであらせられる女帝陛下ジェイディスに対する大逆罪の容疑で逮捕され、裁判を待つ身である。あわせて、前記陛下の敵に力を貸し、スパイをかくまい、人間と親しく交わった罪にも問われている。'),
    'DONTKNOW': ('"I don\'t know that I\'m going to like this place after all," said Susan.',
        '「やっぱり私、この場所を好きになれるか分からないわ」とスーザンは言った。'),
    'WITCH': ('"She isn\'t a real queen at all," answered Lucy; "she\'s a horrible witch, the White Witch.',
        '「本物の女王なんかじゃ全然ないの」とルーシーは答えた。「恐ろしい魔女よ。白い魔女なの。'),
    'ENCHANT': ('She has made an enchantment over the whole country so that it is always winter here and never Christmas."',
        '国じゅうに魔法をかけて、ここをいつも冬なのに、クリスマスは決して来ないようにしてしまったの」'),
    'POINT': ('"I- I wonder if there\'s any point in going on," said Susan.',
        '「こ、このまま進んで、何か意味があるのかしら」とスーザンは言った。'),
    'IMEAN': ('"I mean, it doesn\'t seem particularly safe here and it looks as if it won\'t be much fun either.',
        '「つまり、ここはあまり安全そうじゃないし、それに、あんまり楽しくもなさそうだわ。'),
    'SNOW': ('Snow had drifted in from the doorway and was heaped on the floor, mixed with something black, which turned out to be the charred sticks and ashes from the fire.',
        '雪が戸口から吹き込んで床に積もり、何か黒いものが混じっていた。それは、暖炉の焦げた薪と灰だと分かった。'),
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
    v("pay 人 out (for 〜)", "人に（〜の）仕返しをする", 'RESUMED', ["pay you all out"]),
    v("a pack of 〜", "（軽蔑して）〜の一味、〜な連中", 'RESUMED', ["pack of"]),
    v("stuck-up", "お高くとまった、高慢な", 'RESUMED'),
    v("self-satisfied", "うぬぼれた、独りよがりの", 'RESUMED'),
    v("prig", "お上品ぶった人、道徳家ぶった人", 'RESUMED', ["prigs"]),
    v("chiefly", "主に", 'WHERE'),
    v("for the sake of -ing", "〜するために", 'WHERE', ["for the sake of"]),
    v("goodness knows 〜", "確かに〜だ（強調）。疑問詞が続くと「誰にも分からない」", 'LEADER', ["goodness knows"]),
    v("prove (＋C)", "〜であると分かる、〜になる（proved a good leader＝よいリーダーぶりを見せた）", 'PROVED', ["proved"]),
    v("bring 人 on (to 〜)", "人を（〜まで）連れて進む", 'ATFIRST', ["brought them on to"]),
    v("wrench 〜 off", "〜をもぎ取る、ねじり取る", 'DOOR', ["wrenched off"]),
    v("hinge", "ちょうつがい", 'DOOR', ["hinges"]),
    v("charred", "焦げた、炭になった", 'SNOW'),
    v("stick", "（名詞）棒きれ、小枝、薪", 'SNOW', ["sticks"]),
    v("ash", "灰（ふつう複数形 ashes）", 'SNOW', ["ashes"]),
    v("a pretty good 〜", "（強調）相当な〜、まったくの〜（good は「よい」ではない）", 'WASHOUT', ["pretty good"]),
    v("wash-out", "（口語）大失敗、期待はずれ", 'WASHOUT'),
    v("nail", "くぎで打ちつける", 'NAILED', ["nailed"]),
    v("premises", "建物、敷地（複数形で使う）", 'NOTICE'),
    v("on a charge of 〜", "〜の容疑で", 'NOTICE', ["on a charge of"]),
    v("comfort", "（ここでは）援助する、力を貸す（ふつうは「慰める」）", 'NOTICE', ["comforting"]),
    # --- そのほか p.65〜67 の重要表現 ---
    v("resume", "再開する（resumed their journey＝また歩き始めた）", 'RESUMED', ["resumed"]),
    v("change the subject", "話題を変える", 'WHERE', ["changing the subject"]),
    v("turn out to be 〜", "〜だと分かる", 'SNOW', ["turned out to be"]),
    v("apparently", "どうやら〜らしい", 'FLUNG'),
    v("stamp 〜 out", "〜を踏み消す", 'FLUNG', ["stamped it out"]),
    v("under arrest", "逮捕されて", 'NOTICE'),
    v("harbour", "かくまう（米 harbor）", 'NOTICE', ["harbouring"]),
    v("fraternize with 〜", "〜と親しく交わる", 'NOTICE', ["fraternizing with"]),
    v("there is no point in -ing", "〜しても無駄だ（any point in -ing＝〜することに意味がある）", 'POINT', ["any point in going"]),
]

# 下線部訳：第6回の課題（p.65〜67）。答えは課題の解答と同じ内容
UNDERLINE = [
    {"underline": "（全文）", "task": None, "enHtml": "but Edmund was saying to himself, 'I'll pay you all out for this, you pack of stuck-up, self-satisfied prigs.'", "jp": "しかしエドマンドは心の中でこうつぶやいていた。「このお返しは、みんなにきっとしてやるからな。お高くとまって、うぬぼれた、お上品ぶったやつらめ」", "note": "say to oneself：「心の中で思う、ひとりごとを言う」。 pay 人 out (for 〜)：「人に（〜の）仕返しをする」。you all は「君たちみんな」。 this＝嘘がばれてみんなに責められたこと。自分が悪いのに逆恨みしている。 you pack of 〜 は呼びかけで「〜な連中め」。pack は軽蔑をこめて「一味、連中」。 stuck-up：「お高くとまった」。self-satisfied：「うぬぼれた、独りよがりの」。prig：「お上品ぶった人、道徳家ぶった人」。"},
    {"underline": "（全文）", "task": None, "enHtml": "'Where are we going anyway?' said Susan, chiefly for the sake of changing the subject.", "jp": "「ところで、私たちどこへ行くの？」と、スーザンは主に話題を変えるために言った。", "note": "anyway：話を切り替えて「ところで、それはそうと」。 chiefly：「主に」。for the sake of -ing：「〜するために」。change the subject：「話題を変える」。 エドマンドの嘘がばれて気まずくなった空気を変えようとしている。"},
    {"underline": "it", "task": None, "enHtml": "'goodness knows she deserves <u>it</u>.'", "jp": "「ルーにはリーダーになる資格が、確かに十分あるよ」", "note": "下線部の内容：it＝リーダーになること。直前のピーターの \"I think Lu ought to be the leader\" を受けている。 goodness knows (that) 〜：「確かに〜だ、本当に〜だ」と強調する言い方。 Goodness knows where he is.（どこにいるのか誰にも分からない）のように疑問詞が続くと「誰にも分からない」の意味になるので区別する。 deserve：「〜に値する」。ルーシーは本当のことを言っていたのに信じてもらえなかったので、ピーターはその埋め合わせの気持ちも込めている。"},
    {"underline": "（全文）", "task": "とあるが、a terrible surpriseの具体的な内容を説明しなさい。", "enHtml": "But there a terrible surprise awaited them.", "jp": "ところが、そこではとんでもない驚きが四人を待ち受けていた。", "note": "a terrible surprise の内容：タムナスさんのほら穴が荒らされ、タムナスさんの姿がなかったこと。 扉はちょうつがいからもぎ取られて、こなごなに壊されていた。 中は暗く冷たく、何日も人が住んでいない様子で、雪が吹き込んで床に積もっていた。 暖炉の火がまき散らされて踏み消され、焦げた薪と灰が雪に混じっていた。 瀬戸物は割れ、フォーンのお父さんの肖像画はナイフでずたずたに切り裂かれていた。 there＝タムナスさんのほら穴の戸口で。 await：「〜を待ち受ける」（他動詞なので前置詞は不要。wait for と同じ意味）。"},
    {"underline": "it / it", "task": None, "enHtml": "Someone had apparently flung <u>it</u> about the room and then stamped <u>it</u> out.", "jp": "どうやら誰かが、暖炉の火を部屋中にまき散らしてから、踏みつけて消したらしかった。", "note": "下線部の内容：どちらの it も the fire（暖炉の火）。直前の the charred sticks and ashes from the fire の fire を指す。sticks and ashes は複数なので it では受けられない。 apparently：「どうやら〜らしい」。 fling 〜 about：「〜をまき散らす」（fling-flung-flung）。 stamp out：「踏み消す」。目的語が代名詞のときは stamp it out の語順になる。 had flung は過去完了で、子どもたちが来るより前に起きたことを表す。"},
    {"underline": "good / good", "task": None, "enHtml": "'This is a pretty <u>good</u> wash-out,' said Edmund; 'not much <u>good</u> coming here.'", "jp": "「こりゃあ、まったくの期待はずれだな」とエドマンドは言った。「ここへ来たって、たいして意味がなかったね」", "note": "下線部の違い：1つ目の good：形容詞で、wash-out（大失敗、期待はずれ）を強めて「相当な、まったくの」。「よい」という意味ではない。pretty は副詞で「かなり」。 2つ目の good：名詞で「役に立つこと、意味」（第2回の what good … do と同じ good）。 not much good coming here は (It is) not much good coming here の省略。It is no good -ing（〜しても無駄だ）と同じ形で、not much で「あまり意味がない」。 ※課題プリントでは washout になっているが、本文は wash-out。"},
    {"underline": "（全文）", "task": "文の構造に気をつけて訳しましょう。", "enHtml": "The former occupant of these premises, the Faun Tumnus, is under arrest and awaiting his trial on a charge of High Treason against her Imperial Majesty Jadis, Queen of Narnia, Chatelaine of Cair Paravel, Empress of the Lone Islands, etc., also of comforting her said Majesty's enemies, harbouring spies and fraternizing with Humans.", "jp": "この住居の前の住人、フォーンのタムナスは、ナルニアの女王、ケア・パラベルの城主、離れ島諸島の女帝などであらせられる女帝陛下ジェイディスに対する大逆罪の容疑で逮捕され、裁判を待つ身である。あわせて、前記陛下の敵に力を貸し、スパイをかくまい、人間と親しく交わった罪にも問われている。", "note": "文の構造：主語：The former occupant of these premises（＝the Faun Tumnus と同格） 述語：is under arrest and (is) awaiting his trial 容疑①：on a charge of High Treason against her Imperial Majesty Jadis Queen of Narnia, Chatelaine of Cair Paravel, Empress of the Lone Islands, etc. はすべて Jadis の同格（称号の列挙） 容疑②：also (on a charge) of ＋ comforting …, harbouring …, and fraternizing … の動名詞3つが並列 former：「前の」。occupant：「住人」。premises：「建物、敷地」（複数形で使う）。 under arrest：「逮捕されて」。await one's trial：「裁判を待つ」。on a charge of 〜：「〜の容疑で」（第2回の charge と同じ）。 High Treason：「大逆罪」。Her Imperial Majesty：「女帝陛下」。Chatelaine：「（女性の）城主」。 said：形容詞で「前述の」（公文書の言い方）。comfort：ここでは「力を貸す、援助する」。harbour：「かくまう」。fraternize with 〜：「〜と親しく交わる」。 ※課題プリントでは Tamnus、harboring になっているが、本文は Tumnus、harbouring。"},
    {"underline": "（全文）", "task": None, "enHtml": "'I wonder if there's any point in going on,' said Susan.", "jp": "「このまま進むことに、何か意味があるのかしら」とスーザンは言った。", "note": "wonder if 〜：「〜だろうかと思う」。 there is any point in -ing：「〜することに意味がある」。否定の there is no point in -ing（〜しても無駄だ）でよく使う。 go on：「先へ進む、続ける」。 スーザンの理由（直後）：ここはあまり安全そうではない、楽しくもなさそう、どんどん寒くなってくる。"},
]
for u in UNDERLINE:
    u["chapter"] = CH
    u["round"] = ROUND
    if u["task"] is None:
        del u["task"]

# 読解クイズ（日本語訳を選ぶ）
QUIZ = [{"en": S[k][0], "jp": S[k][1], "chapter": CH, "round": ROUND} for k in [
    'RESUMED', 'WHERE', 'AGREED', 'ATFIRST', 'DOOR', 'INSIDE', 'SNOW', 'FLUNG', 'CROCKERY', 'WASHOUT', 'NAILED', 'DONTKNOW', 'ENCHANT', 'IMEAN',
]]

COMPREHENSION = [
    {"q": "嘘がばれたあと、エドマンドが心の中で思っていたことは？",
     "choices": ["みんなに仕返しをしてやる", "ルーシーに謝りたい", "家に帰りたい", "フォーンに会いたい"],
     "answer": "みんなに仕返しをしてやる",
     "explain": "\"I'll pay you all out for this, you pack of stuck-up, self-satisfied prigs.\" 自分が悪いのに逆恨みしている。"},
    {"q": "スーザンが「どこへ行くの？」と尋ねたのはなぜか？",
     "choices": ["主に話題を変えるため", "道に迷ったから", "家に帰りたかったから", "ルーシーを試すため"],
     "answer": "主に話題を変えるため",
     "explain": "\"chiefly for the sake of changing the subject.\" エドマンドの件で気まずくなった空気を変えたかった。"},
    {"q": "ピーターがリーダーにしようと言ったのは誰か？",
     "choices": ["ルーシー", "スーザン", "エドマンド", "ピーター自身"],
     "answer": "ルーシー",
     "explain": "\"I think Lu ought to be the leader … goodness knows she deserves it.\""},
    {"q": "ルーシーはどうやってタムナスさんのほら穴までの道を見つけたか？",
     "choices": ["変わった形の木や切り株に見覚えがあった", "地図を持っていた", "足跡をたどった", "フォーンが迎えに来た"],
     "answer": "変わった形の木や切り株に見覚えがあった",
     "explain": "\"she recognized an odd-looking tree in one place and a stump in another\""},
    {"q": "ほら穴の扉はどうなっていたか？",
     "choices": ["ちょうつがいからもぎ取られ、こなごなに壊されていた", "鍵がかかっていた", "開け放しになっていた", "新しい扉に替わっていた"],
     "answer": "ちょうつがいからもぎ取られ、こなごなに壊されていた",
     "explain": "\"The door had been wrenched off its hinges and broken to bits.\""},
    {"q": "ほら穴の床に雪と混じっていた黒いものは何だったか？",
     "choices": ["暖炉の焦げた薪と灰", "泥", "焼けた本", "割れた瀬戸物"],
     "answer": "暖炉の焦げた薪と灰",
     "explain": "\"something black, which turned out to be the charred sticks and ashes from the fire.\""},
    {"q": "ピーターが見つけた紙はどこにあったか？",
     "choices": ["じゅうたんの上から床にくぎで打ちつけられていた", "扉に貼られていた", "暖炉の中に落ちていた", "肖像画の裏に隠されていた"],
     "answer": "じゅうたんの上から床にくぎで打ちつけられていた",
     "explain": "\"a piece of paper which had been nailed through the carpet to the floor.\""},
    {"q": "告示によると、タムナスさんはどうなっているか？",
     "choices": ["逮捕されて、裁判を待っている", "国外に追放された", "すでに処刑された", "どこかへ逃げた"],
     "answer": "逮捕されて、裁判を待っている",
     "explain": "\"is under arrest and awaiting his trial on a charge of High Treason\""},
    {"q": "ルーシーによると、白い魔女はナルニアをどうしてしまったか？",
     "choices": ["いつも冬なのに、クリスマスが決して来ないようにした", "いつも夜のままにした", "動物が話せないようにした", "森を全部焼いてしまった"],
     "answer": "いつも冬なのに、クリスマスが決して来ないようにした",
     "explain": "\"She has made an enchantment over the whole country so that it is always winter here and never Christmas.\""},
]
for c in COMPREHENSION:
    c["chapter"] = CH
    c["round"] = ROUND

GRAMMAR = [
    {"point": "pay 人 out（人に仕返しをする）", "en": "\"I'll pay you all ___ for this, you pack of stuck-up, self-satisfied prigs.\"",
     "choices": ["out", "off", "back", "up"], "answer": "out",
     "explain": "pay 人 out (for 〜)「人に（〜の）仕返しをする」（イギリス英語の口語）。pay 人 back も「仕返しをする」の意味で使うが、本文は out。"},
    {"point": "for the sake of -ing（〜するために）", "en": "\"Where are we going anyway?\" said Susan, chiefly for the sake of ___ the subject.",
     "choices": ["changing", "change", "to change", "changed"], "answer": "changing",
     "explain": "for the sake of 〜「〜のために」。of は前置詞なので後ろは動名詞。"},
    {"point": "prove＋C（〜であると分かる）", "en": "Lucy ___ a good leader.",
     "choices": ["proved", "approved", "provided", "improved"], "answer": "proved",
     "explain": "prove (to be) C「Cであると分かる、結果的にCになる」。proved a good leader＝よいリーダーぶりを見せた。"},
    {"point": "wonder whether 〜（〜かどうか）", "en": "At first she wondered ___ she would be able to find the way.",
     "choices": ["whether", "that", "what", "which"], "answer": "whether",
     "explain": "wonder whether / if 〜「〜かどうかと思う」。that は wonder の後には使わない。"},
    {"point": "過去完了の受け身（had been＋過去分詞）", "en": "The door had been ___ off its hinges and broken to bits.",
     "choices": ["wrenched", "wrenching", "wrench", "to wrench"], "answer": "wrenched",
     "explain": "had been＋過去分詞「（それより前に）〜されていた」。子どもたちが着く前に扉はもぎ取られていた。"},
    {"point": "関係代名詞 which（非制限用法）", "en": "… mixed with something black, ___ turned out to be the charred sticks and ashes from the fire.",
     "choices": ["which", "what", "that", "who"], "answer": "which",
     "explain": "コンマの後で先行詞 something black に説明を加える非制限用法。that は非制限用法では使えない。"},
    {"point": "代名詞の位置（stamp it out）", "en": "Someone had apparently flung it about the room and then stamped ___.",
     "choices": ["it out", "out it", "out", "it"], "answer": "it out",
     "explain": "動詞＋副詞の句動詞で目的語が代名詞のときは、stamp it out のように動詞と副詞の間に置く。"},
    {"point": "lie＋C（〜の状態で横たわっている）", "en": "The crockery lay ___ on the floor.",
     "choices": ["smashed", "smashing", "smash", "to smash"], "answer": "smashed",
     "explain": "lie C「Cの状態である」（lie-lay-lain）。瀬戸物は割られた状態なので過去分詞 smashed。"},
    {"point": "so that（結果：それで〜）", "en": "She has made an enchantment over the whole country ___ that it is always winter here and never Christmas.",
     "choices": ["so", "such", "as", "in"], "answer": "so",
     "explain": "so that 〜「その結果〜、〜するように」。魔法をかけた結果、いつも冬でクリスマスが来ない。"},
    {"point": "there is any point in -ing", "en": "\"I- I wonder if there's any point in ___ on,\" said Susan.",
     "choices": ["going", "go", "to go", "gone"], "answer": "going",
     "explain": "there is (no) point in -ing「〜することに意味がある（ない）」。in は前置詞なので動名詞。"},
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
