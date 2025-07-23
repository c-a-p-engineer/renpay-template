## このファイルにはあなたのゲームをカスタマイズするために
## 変更できるオプションが書かれています。
## ここには一般的なオプションだけが並んでいますが、
## 他にもたくさんのカスタマイズができます。
##
## 「#」2つから始まっている行はコメント行です。
## コメントアウトしないでください。
## 「#」1つから始まっている行はコメントアウトされたコードです。
## 必要であれば適宜「#」を外して使ってください。

define config.name = _("ずんだもんゲーム")     # 表示用（日本語でもOK）
init python:
    build.name = "zundamon_game"              # exe/zipに使う実際のファイル名用(ASCIIのみ推奨)

init -1:
    python hide:

        ## 開発者向けツールを使う。
        ## ユーザにチート（ずる）をさせないために
        ## リリース時には False にしましょう。
        config.developer = True

        ## 画面の幅と高さ
        config.screen_width = 1280
        config.screen_height = 720

        ## ウィンドウモードで実行している時のウィンドウタイトル。
        config.window_title = u"A Ren'Py Game"

        ## テーマ関数を呼び出します。
        ## themes.roundrect は角の丸い長方形を使えるようにします。
        ## 現在サポートされているのはこのテーマだけです。
        ##
        ## テーマ関数は色をカスタマイズするためのパラメータを
        ## 引数に取ります。

        theme.roundrect(

            ## 非アクティブなウィジェット
            widget = "#003c78",

            ## アクティブなウィジェット
            widget_hover = "#0050a0",

            ## ウィジェット内のテキスト
            widget_text = "#c8ffff",

            ## 選択されたウィジェット内のテキスト
            ## （たとえば設定の現在の値）
            widget_selected = "#ffffc8",

            ## 無効なウィジェット
            disabled = "#404040",

            ## 無効なウィジェット内のテキスト
            disabled_text = "#c8c8c8",

            ## 情報ラベル
            label = "#ffffff",

            ## ウィジェットを含んでいるフレーム
            frame = "#6496c8",

            ## True  - ゲームメニューを画面の中心に表示
            ## False - ゲームメニューを画面下部のウィンドウ内に表示 
            button_menu = True,

            ## True  - ゲームメニューの角を丸く
            ## False - ゲームメニューの角を直角に
            rounded_window = False,

            ## メインメニューの背景。
            ## 色または画像ファイル名を指定。
            ## 画像を使う場合、画面と同じサイズのものを用意する。
            mm_root = "#dcebff",

            ## ゲームメニューの背景。
            ## あとは上の mm root と同じ。
            gm_root = "#dcebff",

            ## ボタンのフォントサイズ
            # text_size = 16,
            )


        #########################################
        ## 会話とナレーションを含むウィンドウのカスタマイズ。
        ## 背景に画像を使う。

        ## フレーム内では 2つの数字はそれぞれ
        ## 上下、左右の枠線のサイズ。
        # style.window.background = Frame("frame.png", 12, 12)

        ## ウィンドウを囲むスペースのマージン。
        ## 背景は描かれない。

        # style.window.left_margin = 6
        # style.window.right_margin = 6
        # style.window.top_margin = 6
        # style.window.bottom_margin = 6

        ## ウィンドウの内側のパディング。
        ## 背景は描かれる。

        # style.window.left_padding = 6
        # style.window.right_padding = 6
        # style.window.top_padding = 6
        # style.window.bottom_padding = 6

        ## ウィンドウの高さの最小値。
        ## マージンとパディングを含む。
        # style.window.yminimum = 250


        #########################################
        ## メインメニューの配置。
        
        ## 表示領域（displayable）内のアンカー（anchor）ポイントと
        ## 画面上の位置（pos）ポイントを使う。
        ## 2つの点が同じ位置で重なるように配置する。

        ## anchor、pos は整数または小数で指定。
        ## 整数 - 左上からのピクセル数
        ## 小数 - 表示領域（displayable）または画面のサイズの比

        # style.mm_menu_frame.xpos = 0.5
        # style.mm_menu_frame.xanchor = 0.5
        # style.mm_menu_frame.ypos = 0.75
        # style.mm_menu_frame.yanchor = 0.5


        #########################################
        ## ゲーム内で使われるデフォルトフォント

        ## デフォルトフォントを含むファイル
        style.default.font = "fonts/ipam.ttf"

        ## デフォルトのテキストサイズ
        # style.default.size = 22

        ## 注）これで変更できるのはすべてのテキストではなく、
        ## ボタンは独自のスタイルで表示される。


        #########################################
        ## 音声の設定

        ## 効果音を使わない場合は False にする。
        config.has_sound = True

        ## BGMを使わない場合は False にする。
        config.has_music = True

        ## 声を使わない場合は False にする。
        config.has_voice = True

        ## ボタンとイメージマップをクリックした時の音
        # style.button.activate_sound = "click.wav"
        # style.imagemap.activate_sound = "click.wav"

        ## ゲームメニューに入る時、出る時の音。
        # config.enter_sound = "click.wav"
        # config.exit_sound = "click.wav"

        ## 音量チェックで鳴らす音。
        # config.sample_sound = "click.wav"

        ## メインメニューのBGM。
        # config.main_menu_music = "main_menu_theme.ogg"

        #########################################
        ## Transitions.
        ## 画像切り替え

        ## ゲーム中にゲームメニューへ
        config.enter_transition = None

        ## ゲームメニューからゲームへ戻る
        config.exit_transition = None

        ## ゲームメニューでの画面切り替え
        config.intra_transition = None

        ## メインメニューからゲームメニューへ
        config.main_game_transition = None

        ## ゲームからメインメニューに戻る
        config.game_main_transition = None

        ## スプラッシュスクリーンからメインメニューへ
        config.end_splash_transition = None

        ## ゲーム終了（エンディング）からメインメニューへ
        config.end_game_transition = None
        
        
        #########################################
        ## 設定の初期値

        ## 注）これらのオプション値は初回ゲームプレイ時にのみ
        ## 評価される。
        ## 2回目でもこれらの値を使いたい場合は
        ## game/saves/persistent を消去する。
       
        ## フルスクリーンモードで始める
        config.default_fullscreen = False

        ## デフォルトのテキスト表示スピード（文字数/秒）
        ## 0 で無限（最速）
        config.default_text_cps = 0

