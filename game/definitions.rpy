# =========================================================
# definitions.rpy
# キャラクター、画像、トランジション等の定義
# =========================================================

# ----------------------
# キャラ定義
# ----------------------
define z = Character("ずんだもん", image="zundamon")
define u = Character("マスター")

# ----------------------
# 画像・背景・効果用定義
# ----------------------
# 立ち絵
image zundamon = Transform("characters/zundamon/default.png", zoom=0.4)

# 背景（画面サイズに合わせて拡大縮小）
image bg_room = im.Scale("backgrounds/room.png", 1280, 720)

# フラッシュ用真っ白画像
image white = Solid("#fff")

# ----------------------
# トランジション
# ----------------------
define fade     = Fade(0.3, 0.3, 0.3)
define dissolve = Dissolve(0.3)
define flash    = Fade(0.05, 0.0, 0.2, color="#fff")

# ----------------------
# Transform（ATL）
# ----------------------
transform shake:
    xalign 0.5 yalign 0.5
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    repeat 5

transform zoom_in:
    zoom 0.2
    linear 0.4 zoom 1.0

transform slide_left:
    xalign 1.0
    linear 0.4 xalign 0.5

transform vpunch_tiny:
    ypos 0.0
    linear 0.05 ypos -10
    linear 0.05 ypos 0
    repeat 3
