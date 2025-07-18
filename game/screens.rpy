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
