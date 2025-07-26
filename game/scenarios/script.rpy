# =========================================================
# script.rpy  (Ren'Py 8.x 想定)
# =========================================================

# =========================================================
# スタート
# =========================================================
label start:

    # BGM開始
    play music "bgm/frog_piano.mp3" fadein 1.0 loop

    scene bg_room with fade
    show zundamon at center

    voice "voices/zundamon_hello.wav"
    z "Hello! World!!"

    u "おお、元気そうだな。"

    jump main_loop


# =========================================================
# メインループ
# =========================================================
label main_loop:

    menu:
        "何をする？"

        "エフェクトを試す":
            jump effect_menu

        "会話メニュー":
            jump talk_menu

        "最初からやり直す":
            jump start

        "終了（ゲーム終了）":
            return
