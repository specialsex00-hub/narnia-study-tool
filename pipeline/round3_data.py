#!/usr/bin/env python3
"""第3回授業（Chapter 5, part 3 / 本文 p.56〜57 l.16）の課題データを各JSONに追記する。

範囲はユーザーが予習を済ませた p.56 の始め〜p.57 l.16（... so that however long you
stayed there it would never take up any of our time. まで）。
対訳プリントで赤太字になっている語句（授業で重要とされたもの）は必ず単語に含める。
文は対訳プリントから機械的に抜き出したもの。
一度きりのマージ用。同じ回の二重追加は拒否する。
"""
import json

CH = 5
ROUND = '第3回'

S = {
    'EASY': ('"Oh, you can make your minds easy about that.',
        '「ああ、その点なら安心していい。'),
    'ONLY': ('One has only to look at her and talk to her to see that she is not mad."',
        'あの子を見て、話をしてみさえすれば、気が変になっていないことはすぐに分かる」'),
    'BUTTHEN': ('"But then," said Susan, and stopped.',
        '「でも、それなら――」とスーザンは言いかけて、口をつぐんだ。'),
    'DREAMED': ("She had never dreamed that a grown-up would talk like the professor and didn't know what to think.",
        '大人が教授のような話し方をするなんて夢にも思っていなかったので、スーザンはどう考えたらいいのか分からなかった。'),
    'LOGIC': ('"Logic!" said the Professor half to himself.',
        '「論理だよ！」と教授は半ばひとりごとのように言った。'),
    'TEACH': ('"Why don\'t they teach logic at these schools?',
        '「近ごろの学校では、どうして論理を教えないのかね？'),
    'THREE': ('There are only three possibilities.',
        '可能性は三つしかない。'),
    'EITHER': ('Either your sister is telling lies, or she is mad, or she is telling the truth.',
        '妹さんが嘘をついているか、気が変になっているか、本当のことを言っているかのどれかだ。'),
    'OBVIOUS': ("You know she doesn't tell lies and it is obvious that she is not mad.",
        '妹さんが嘘をつかないことは君たちも知っているし、気が変になっていないことも明らかだ。'),
    'MOMENT': ('For the moment then and unless any further evidence turns up, we must assume that she is telling the truth."',
        'だとすれば、さしあたっては、そして何かほかの証拠が出てこない限りは、妹さんは本当のことを言っていると考えるべきなのだよ」'),
    'HARD': ('Susan looked at him very hard and was quite sure from the expression on his face that he was not making fun of them.',
        'スーザンは教授をじっと見つめ、その顔つきから、教授が自分たちをからかっているのではないとはっきり分かった。'),
    'HOW': ('"But how could it be true, sir?" said Peter.',
        '「でも、どうしてそれが本当だなんてことがありうるんですか、先生？」とピーターは言った。'),
    'WHYSAY': ('"Why do you say that?" asked the Professor.',
        '「どうしてそう言うのかね？」と教授は尋ねた。'),
    'ONETHING': ('"Well, for one thing," said Peter, "if it was real why doesn\'t everyone find this country every time they go to the wardrobe?',
        '「ええと、一つには」とピーターは言った。「もしそれが本当なら、どうして誰でも洋服だんすに行くたびにその国を見つけられないんでしょう？'),
    'IMEAN': ('I mean, there was nothing there when we looked; even Lucy didn\'t pretend there was."',
        'つまり、僕たちが見たときには何もなかったんです。ルーシーでさえ、何かあるふりはしませんでした」'),
    'TODO': ('"What has that to do with it?" said the Professor.',
        '「それがこの話と何の関係があるのかね？」と教授は言った。'),
    'ALLTIME': ('"Well, sir, if things are real, they\'re there all the time."',
        '「だって先生、本当にあるものなら、いつだってそこにあるはずです」'),
    'ARE': ('"Are they?" said the Professor; and Peter did not know quite what to say.',
        '「そうかね？」と教授が言うと、ピーターは何と言っていいのかよく分からなくなった。'),
    'NOTIME': ('"But there was no time," said Susan.',
        '「でも、時間がなかったんです」とスーザンは言った。'),
    'HADHAD': ('"Lucy had had no time to have gone anywhere, even if there was such a place.',
        '「たとえそんな場所があったとしても、ルーシーにはどこかへ行っている時間なんてなかったんです。'),
    'RUNNING': ('She came running after us the very moment we were out of the room.',
        '私たちが部屋を出たまさにその瞬間に、あの子は走って追いかけてきました。'),
    'MINUTE': ('It was less than a minute, and she pretended to have been away for hours."',
        '1分もたっていなかったのに、あの子は何時間も向こうに行っていたようなふりをしたんです」'),
    'VERY': ('"That is the very thing that makes her story so likely to be true," said the Professor.',
        '「まさにそのことが、あの子の話をいかにも本当らしくしているのだよ」と教授は言った。'),
    'DOOR': ('"If there really is a door in this house that leads to some other world (and I should warn you that this is a very strange house, and even I know very little about it) - if, I say, she had got into another world, I should not be at all surprised to find that the other world had a separate time of its own; so that however long you stayed there it would never take up any of our time.',
        '「もしこの家に、本当にどこか別の世界へ通じる扉があるとしたら（言っておくが、ここはとても不思議な家で、私でさえほとんど何も知らないのだよ）――いいかね、もしあの子が別の世界に入ったのだとしたら、その世界にはこちらとは別の独自の時間が流れていると分かっても、私は少しも驚かないだろう。だから、向こうにどれだけ長くいても、こちらの時間は少しもたたないというわけだ。'),
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
    v("make one's mind easy (about 〜)", "（〜について）安心する", 'EASY', ["make your minds easy"]),
    v("have only to do (to 〜)", "…しさえすれば（〜できる）（One has only to look at her … to see 〜＝あの子を見さえすれば〜が分かる）", 'ONLY', ["has only to", "to see"]),
    v("for the moment", "さしあたって、今のところは", 'MOMENT', ["For the moment"]),
    v("then", "それなら、だとすれば（前の話を受けて）", 'MOMENT', ["then"]),
    v("unless", "〜しない限り", 'MOMENT', ["unless"]),
    v("turn up", "（物・証拠などが）現れる、出てくる", 'MOMENT', ["turns up"]),
    v("have A to do with B", "AがBと関係がある（What has A to do with B?＝AがBと何の関係があるのか→関係ない）", 'TODO', ["has", "to do with"]),
    v("of one's own", "自分自身の、独自の（a separate time of its own＝独自の別の時間）", 'DOOR', ["of its own"]),
    # --- そのほか p.56〜57 l.16 の重要表現 ---
    v("dream that 〜", "〜ということを想像する（had never dreamed that 〜＝〜とは夢にも思っていなかった）", 'DREAMED', ["never dreamed that"]),
    v("half to oneself", "半ばひとりごとのように", 'LOGIC', ["half to himself"]),
    v("possibility", "可能性", 'THREE', ["possibilities"]),
    v("either A or B (or C)", "AかBか（Cか）のどれか", 'EITHER', ["Either", "or", "or"]),
    v("obvious", "明らかな（it is obvious that 〜＝〜は明らかだ）", 'OBVIOUS'),
    v("evidence", "証拠（any further evidence＝何かそれ以上の証拠）", 'MOMENT'),
    v("assume that 〜", "（証拠はないが）〜だと考える、〜と仮定する", 'MOMENT', ["assume that"]),
    v("look at 〜 hard", "〜をじっと見つめる", 'HARD', ["looked at him very hard"]),
    v("expression", "表情、顔つき", 'HARD'),
    v("make fun of 〜", "〜をからかう", 'HARD', ["making fun of"]),
    v("for one thing", "一つには（理由を挙げるときの前置き）", 'ONETHING'),
    v("pretend", "ふりをする（pretend to have been 〜＝〜していたふりをする）", 'MINUTE', ["pretended"]),
    v("all the time", "いつも、常に", 'ALLTIME'),
    v("the very moment 〜", "〜したまさにその瞬間に（接続詞のように使う）", 'RUNNING', ["the very moment"]),
    v("be likely to do", "〜しそうだ、〜らしい（so likely to be true＝いかにも本当らしい）", 'VERY', ["likely to"]),
    v("lead to 〜", "〜へ通じる", 'DOOR', ["leads to"]),
    v("warn 人 that 〜", "人に〜だと警告する、前もって言っておく", 'DOOR', ["warn you that"]),
    v("not 〜 at all", "少しも〜ない", 'DOOR', ["not be at all"]),
    v("however long 〜", "どんなに長く〜しても", 'DOOR', ["however long"]),
    v("take up", "（時間・場所を）とる、使う", 'DOOR', ["take up"]),
]

# 下線部訳：第3回の課題のうち p.57 l.16 までのもの（答えは課題の解答と同じ内容）
UNDERLINE = [
    {"underline": "that", "task": "下線部の指す内容を簡単に答えなさい",
     "enHtml": "'Oh, you can make your minds easy about <u>that</u>.'",
     "jp": "「ああ、その点なら安心していい。」",
     "note": "下線部 that＝直前のスーザンの心配「ルーシーはどこかおかしい（頭が変になっている）のではないか」ということ。教授の \"Madness, you mean?\" を受けて「その点なら安心していい」と言っている。make one's mind easy (about 〜)「（〜について）安心する」。理由は直後の One has only to look at her and talk to her to see that she is not mad.（あの子を見て話してみれば、気が変になっていないことはすぐ分かる）。"},
    {"underline": "（全文）", "task": "とあるが、それぞれどのようなものかまとめましょう。",
     "enHtml": "There are only three possibilities.",
     "jp": "可能性は三つしかない。",
     "note": "三つの可能性：① ルーシーが嘘をついている（Either your sister is telling lies,）② ルーシーの頭がおかしくなっている（or she is mad,）③ ルーシーが本当のことを言っている（or she is telling the truth.）。教授の論理：ルーシーは嘘をつかない子だと二人とも認めている（①は否定）、気が変になっていないのも明らか（②も否定）→ 残る③「本当のことを言っている」と考えるしかない。"},
    {"underline": "（全文）", "task": None,
     "enHtml": "For the moment then and unless any further evidence turns up, we must assume that she is telling the truth.",
     "jp": "だとすれば、さしあたっては、そして何かほかの証拠が出てこない限りは、妹さんは本当のことを言っていると考えなければならないのだよ。",
     "note": "for the moment「さしあたって」。then「それなら、だとすれば」（前の三つの可能性の話を受ける）。unless 〜「〜しない限り」。any further evidence「それ以上の（何か新しい）証拠」。turn up「現れる、出てくる」。assume that 〜「（証拠はないが）〜だと考える」。must＝論理的にそう考えるしかない。"},
    {"underline": "that / it", "task": "下線部の内容を明らかにして訳しなさい",
     "enHtml": "'What has <u>that</u> to do with <u>it</u>?'",
     "jp": "「僕たちが見たときには洋服だんすの中に何もなかったということが、ルーシーの話が本当かどうかということと、いったい何の関係があるのかね？」（＝何の関係もない）",
     "note": "that＝直前のピーターの発言「もし本当なら、どうして誰でも洋服だんすに行くたびにその国を見つけられないのか。僕たちが見たときには何もなかった」ということ。it＝今問題になっていること、つまり「ルーシーの話が本当かどうか」。have to do with 〜「〜と関係がある」。What has A to do with B? は修辞疑問で「関係ない」の意味。have something / nothing / a lot to do with 〜 もセットで。"},
    {"underline": "（全文）", "task": "theyの後に省略されたものを補いましょう",
     "enHtml": "'Are they?' said the Professor.",
     "jp": "「（本当にあるものは）いつもそこにあるのかね？」と教授は言った。",
     "note": "補うもの：Are they (there all the time)?　直前のピーターの \"if things are real, they're there all the time.\" を受けた疑問文。they＝things（本当にあるもの）。教授は「本当にあるものでも、いつもそこにあるとは限らないのではないか」と問い返している。だからピーターは何と言っていいか分からなくなった。"},
    {"underline": "That / that", "task": "1. 最初のthatの内容を答えなさい　2. 訳しましょう",
     "enHtml": "'<u>That</u> is the very thing <u>that</u> makes her story so likely to be true,' said the Professor.",
     "jp": "「まさにそのこと（1分もたっていないのに何時間も行っていたと言ったこと）が、あの子の話をいかにも本当らしくしているのだよ」と教授は言った。",
     "note": "最初の That＝直前のスーザンの発言「ルーシーには時間がなかった。私たちが部屋を出た瞬間に追いかけてきて、1分もたっていなかったのに、何時間も向こうに行っていたふりをした」ということ。2つ目の that は関係代名詞（主格）で、先行詞は the very thing（まさにその〜）。make O C「OをCにする」、be likely to do「〜しそうだ」。スーザンは「時間がなかった」ことを嘘の証拠だと思ったが、教授は逆に本当らしい理由だと言っている（続きで、別の世界には独自の時間がある、と説明する）。"},
]
for u in UNDERLINE:
    u["chapter"] = CH
    u["round"] = ROUND
    if u["task"] is None:
        del u["task"]

# 読解クイズ（日本語訳を選ぶ）
QUIZ = [{"en": S[k][0], "jp": S[k][1], "chapter": CH, "round": ROUND} for k in [
    'ONLY', 'DREAMED', 'EITHER', 'OBVIOUS', 'MOMENT', 'HARD', 'ONETHING', 'IMEAN', 'TODO', 'ALLTIME', 'HADHAD', 'RUNNING', 'MINUTE', 'VERY',
]]

COMPREHENSION = [
    {"q": "教授が「ルーシーは気が変になっていない」と言える理由として挙げたことは？",
     "choices": ["あの子を見て話してみれば分かる", "医者に診てもらったから", "ルーシーが自分でそう言ったから", "エドマンドがそう証言したから"],
     "answer": "あの子を見て話してみれば分かる",
     "explain": "\"One has only to look at her and talk to her to see that she is not mad.\" have only to do「〜しさえすればよい」。"},
    {"q": "教授の話を聞いたスーザンがどう考えたらいいか分からなくなったのはなぜか？",
     "choices": ["大人が教授のような話し方をするとは夢にも思っていなかったから", "教授が怒り出したから", "教授の英語が難しすぎたから", "ピーターが教授に反論したから"],
     "answer": "大人が教授のような話し方をするとは夢にも思っていなかったから",
     "explain": "\"She had never dreamed that a grown-up would talk like the professor and didn't know what to think.\" 大人なら「ルーシーの作り話だ」と言うと思っていた。"},
    {"q": "教授が挙げた三つの可能性のうち、教授が「そう考えるべきだ」としたのはどれか？",
     "choices": ["ルーシーは本当のことを言っている", "ルーシーは嘘をついている", "ルーシーは気が変になっている", "エドマンドが嘘をついている"],
     "answer": "ルーシーは本当のことを言っている",
     "explain": "嘘をつく子ではない（①を否定）、気が変になっていないのも明らか（②を否定）→ \"we must assume that she is telling the truth.\""},
    {"q": "スーザンが教授の顔つきから確信したことは？",
     "choices": ["教授は自分たちをからかっているのではない", "教授は怒っている", "教授は何かを隠している", "教授は話をよく聞いていなかった"],
     "answer": "教授は自分たちをからかっているのではない",
     "explain": "\"was quite sure from the expression on his face that he was not making fun of them.\" make fun of「からかう」。"},
    {"q": "ピーターが「話が本当なはずがない」と考える理由として最初に挙げたことは？",
     "choices": ["本当なら、洋服だんすに行くたびに誰でもその国を見つけられるはずだ", "ルーシーは前にも嘘をついたことがある", "教授の家には洋服だんすが一つしかない", "フォーンなどこの世にいるはずがない"],
     "answer": "本当なら、洋服だんすに行くたびに誰でもその国を見つけられるはずだ",
     "explain": "\"if it was real why doesn't everyone find this country every time they go to the wardrobe?\" 自分たちが見たときには何もなかった。"},
    {"q": "スーザンが挙げた反論「時間がなかった」とは、どういうことか？",
     "choices": ["部屋を出た瞬間に追いかけてきたので、1分もたっていなかった", "ルーシーは学校に行く時間だった", "洋服だんすを調べる時間がなかった", "教授に相談する時間がなかった"],
     "answer": "部屋を出た瞬間に追いかけてきたので、1分もたっていなかった",
     "explain": "\"She came running after us the very moment we were out of the room. It was less than a minute, and she pretended to have been away for hours.\""},
    {"q": "「時間がなかった」という点について、教授はどう言ったか？",
     "choices": ["まさにそのことが、話をいかにも本当らしくしている", "だからルーシーの話は嘘だと分かる", "時計が壊れていたのだろう", "スーザンの勘違いだ"],
     "answer": "まさにそのことが、話をいかにも本当らしくしている",
     "explain": "\"That is the very thing that makes her story so likely to be true.\" 作り話なら、もっともらしく長く隠れていたはず。"},
    {"q": "教授は自分の家について何と言ったか？",
     "choices": ["とても不思議な家で、自分でさえほとんど何も知らない", "自分が建てた家なので隅々まで知っている", "最近買ったばかりの家だ", "何の変哲もない普通の家だ"],
     "answer": "とても不思議な家で、自分でさえほとんど何も知らない",
     "explain": "\"I should warn you that this is a very strange house, and even I know very little about it\""},
    {"q": "教授の考えでは、別の世界に独自の時間が流れているとすると、どうなるか？",
     "choices": ["向こうにどれだけ長くいても、こちらの時間は少しもたたない", "向こうの1日がこちらの1年になる", "向こうに行くと年をとらなくなる", "こちらに戻ってこられなくなる"],
     "answer": "向こうにどれだけ長くいても、こちらの時間は少しもたたない",
     "explain": "\"the other world had a separate time of its own; so that however long you stayed there it would never take up any of our time.\""},
]
for c in COMPREHENSION:
    c["chapter"] = CH
    c["round"] = ROUND

GRAMMAR = [
    {"point": "have only to do（〜しさえすればよい）", "en": "One has only to look at her and talk to her ___ see that she is not mad.",
     "choices": ["to", "for", "and", "in"], "answer": "to",
     "explain": "have only to do「〜しさえすればよい」。後ろの to see は結果・目的の不定詞で「見て話しさえすれば、〜が分かる」。"},
    {"point": "either A or B（AかBのどれか）", "en": "___ your sister is telling lies, or she is mad, or she is telling the truth.",
     "choices": ["Either", "Neither", "Both", "Whether"], "answer": "Either",
     "explain": "either A or B (or C)「AかBか（Cか）のどれか」。Neither は nor と、Both は and と組む。"},
    {"point": "形式主語 it（it is … that 〜）", "en": "You know she doesn't tell lies and it is obvious ___ she is not mad.",
     "choices": ["that", "what", "which", "if"], "answer": "that",
     "explain": "it は形式主語で、that 以下が本当の主語。「彼女が気が変になっていないことは明らかだ」。"},
    {"point": "unless（〜しない限り）", "en": "For the moment then and ___ any further evidence turns up, we must assume that she is telling the truth.",
     "choices": ["unless", "if", "until", "since"], "answer": "unless",
     "explain": "unless「〜しない限り」（≒ if … not）。「何かほかの証拠が出てこない限り、本当のことを言っていると考えるべきだ」。if だと意味が逆になる。"},
    {"point": "make fun of（〜をからかう）", "en": "… was quite sure from the expression on his face that he was not making fun ___ them.",
     "choices": ["of", "at", "with", "to"], "answer": "of",
     "explain": "make fun of 〜「〜をからかう」。同じ意味の laugh at、第2回の jeer at と前置詞の違いに注意。"},
    {"point": "have A to do with B（AがBと関係がある）", "en": "\"What has that to do ___ it?\" said the Professor.",
     "choices": ["with", "for", "of", "about"], "answer": "with",
     "explain": "have A to do with B「AがBと関係がある」。What has A to do with B? は「AがBと何の関係があるのか（関係ない）」という修辞疑問。"},
    {"point": "完了不定詞（to have＋過去分詞）", "en": "It was less than a minute, and she pretended to have ___ away for hours.",
     "choices": ["been", "be", "being", "was"], "answer": "been",
     "explain": "to have been は完了不定詞で、pretended（ふりをした）時点より前のこと「何時間も行っていた」を表す。"},
    {"point": "関係代名詞 that（先行詞に the very）", "en": "\"That is the very thing ___ makes her story so likely to be true,\" said the Professor.",
     "choices": ["that", "what", "where", "whom"], "answer": "that",
     "explain": "先行詞 the very thing（まさにそのこと）を受ける主格の関係代名詞。先行詞に the very・the only・最上級などが付くと that が好まれる。what は先行詞を含むので不可。"},
    {"point": "of one's own（独自の）", "en": "… I should not be at all surprised to find that the other world had a separate time of ___ own.",
     "choices": ["its", "it", "it's", "their"], "answer": "its",
     "explain": "of one's own「自分自身の、独自の」。the other world を受けるので its。it's は it is の短縮形。"},
    {"point": "however（どんなに〜しても）", "en": "… so that ___ long you stayed there it would never take up any of our time.",
     "choices": ["however", "whatever", "whenever", "although"], "answer": "however",
     "explain": "however＋形容詞・副詞＋S V「どんなに〜しても」。however long you stayed there＝向こうにどれだけ長くいても。"},
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
