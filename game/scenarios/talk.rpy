# =========================================================
# talk.rpy
# 会話メニュー
# =========================================================

label talk_menu:

    menu:
        "今日の天気は？":
            voice "voices/zundamon_weather.wav"
            z "ずんだもんがいるところはずんずんだよ"
            jump talk_menu

        "好きな食べ物は？":
            voice "voices/zundamon_food.wav"
            z "もちろん、ずんだもち～！"
            jump talk_menu

        "もう帰る（最初に戻る）":
            voice "voices/zundamon_byebye.wav"
            z "またね！ばいばい～"
            jump start
