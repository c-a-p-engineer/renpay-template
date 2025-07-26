# =========================================================
# effects.rpy
# エフェクト関連のメニューとラベル
# =========================================================

label effect_menu:

    menu:
        "どのエフェクトを試す？"

        "フェード + セリフ":
            jump eff_fade

        "画面フラッシュ":
            jump eff_flash

        "立ち絵シェイク":
            jump eff_shake

        "ズームイン演出":
            jump eff_zoom_in

        "スライド登場":
            jump eff_slide_in

        "戻る":
            jump main_loop


# --- 各エフェクトデモ ------------------------------------

label eff_fade:
    scene bg_room with fade
    voice "voices/zundamon_weather.wav"
    z "フェードインで登場したずんだもんだよ。"
    jump effect_menu

label eff_flash:
    show white
    with flash
    hide white
    z "まぶしいッ！ これがフラッシュ効果だよ。"
    jump effect_menu

label eff_shake:
    show zundamon at shake
    z "ガタガタ… 画面が揺れてるよ！"
    jump effect_menu

label eff_zoom_in:
    show zundamon at zoom_in
    z "ズームインしてインパクトを出すのだ！"
    jump effect_menu

label eff_slide_in:
    hide zundamon
    show zundamon at slide_left
    z "スライドして登場～。"
    jump effect_menu
