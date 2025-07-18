# キャラ定義（必ず先に）
define z = Character("ずんだもん")
define u = Character("マスター")

# スタートシナリオ
label start:

    scene bg room  # 背景（なければコメントアウトしてもよい）

    z "Hello!World!!"
    u "おお、元気そうだな。"

    menu:
        "今日の天気は？":
            z "ずんだもん地方は快晴だよ！"
        "好きな食べ物は？":
            z "もちろん、ずんだもち～！"

    z "またね！ばいばい～"

    return
