# キャラ定義（キャラ画像も同時に指定）
define z = Character("ずんだもん", image="zundamon")
define u = Character("マスター")

# キャラ画像の登録（立ち絵ファイル名に合わせて）
# image zundamon = "characters/zundamon/default.png"  # 例: 笑顔の立ち絵
# キャラ画像スケール
image zundamon = Transform("characters/zundamon/default.png", zoom=0.4)

# 背景画像を画面にフィット（例：1280x720に収める）
image bg_room = im.Scale("backgrounds/room.png", 1280, 720)

# スタートシナリオ
label start:

    # ループで再生
    play music "bgm/frog_piano.mp3" fadein 1.0 loop

    scene bg_room        # 背景画像表示
    show zundamon        # キャラ立ち絵表示（中央）

    voice "voices/zundamon_hello.wav"  # 音声再生（セリフに同期）
    z "Hello! World!!"

    u "おお、元気そうだな。"

    menu:
        "今日の天気は？":
            voice "voices/zundamon_weather.wav"
            z "ずんだもんがいるところはずんずんだよ"
        "好きな食べ物は？":
            voice "voices/zundamon_food.wav"
            z "もちろん、ずんだもち～！"

    voice "voices/zundamon_byebye.wav"
    z "またね！ばいばい～"

    return
