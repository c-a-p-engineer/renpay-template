# game/screens.rpy

screen main_menu():

    tag menu

    window:
        style "main_menu_window"

    vbox:
        style_prefix "main_menu"

        spacing 20
        xalign 0.5
        yalign 0.6

        # ✅ メニューの日本語化
        textbutton "はじめから" action Start()
        textbutton "ロード" action ShowMenu("load")
        textbutton "設定" action ShowMenu("preferences")
        textbutton "終了" action Quit(confirm=True)


# ----------------------
# （任意）メニュー大量表示用スクロールスクリーン
# 使うときは、config.choice_screen = "choice_scroll" を有効化
# ----------------------
screen choice_scroll(items):
    modal True
    window:
        style "menu_window"

        viewport id "vp":
            draggable True
            mousewheel True

            vbox:
                spacing 6
                for i in items:
                    textbutton i.caption action i.action style "menu_choice_button"

        vbar value YScrollValue("vp") style "vscrollbar"

# ----------------------
# ユーティリティ（ページング例）
# ----------------------
init python:
    def paginate(seq, size=6):
        """
        seq を size 個ずつに分割したリストを返す
        """
        return [seq[i:i+size] for i in range(0, len(seq), size)]
