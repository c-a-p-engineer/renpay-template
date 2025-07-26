# Ren'Py DevContainer Template (renpay-template)

ビジュアルノベルエンジン [Ren'Py](https://www.renpy.org/) を VS Code Dev Containers 上で手早く使うためのテンプレートです。

## 🚀 特長

* **Ren'Py SDK 自動導入**
* **日本語フォント同梱（IPA系）**
* **GUI対応（X11 / PulseAudio）**
* **Windows / WSL2 / Linux 対応**
* **ビルド用スクリプト同梱（Windows / macOS / Linux 用パッケージ生成）**

---

## 🧩 前提ツール

* [Visual Studio Code](https://code.visualstudio.com/)
* [Dev Containers 拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
* [Docker Desktop](https://www.docker.com/products/docker-desktop)
* （Windowsのみ）Xサーバー（例： [VcXsrv](https://sourceforge.net/projects/vcxsrv/) / [X410](https://x410.dev/)）

---

## 📦 セットアップ

```bash
git clone https://github.com/your-name/renpay-template.git
cd renpay-template
```

VS Code で開き、**Reopen in Container** を選択 → 自動で DevContainer が構築されます。

---

## 🖥️ 実行方法

コンテナ内で:

```bash
renpy .
# うまく動かない場合:
/opt/renpy/renpy.sh .
```

> `.`(カレントディレクトリ) を渡せば、ゲームが即起動します。

---

## 🌐 X11 表示確認（Windows例）

1. `XLaunch` 起動

   * Multiple windows
   * Start no client
   * Disable access control

2. コンテナ内でテスト:

```bash
xeyes
```

→ 目が表示されればOK。

---

## 🔊 音声出力（PulseAudio）

コンテナ→ホストへ音を出す設定です。

### Windowsでの PulseAudio 起動

1. ダウンロード
   [PulseAudio for Windows](https://www.freedesktop.org/wiki/Software/PulseAudio/Ports/Windows/)

2. 展開（例：`C:\pulseaudio`）

3. コマンドプロンプト/PowerShell:

```powershell
cd C:\pulseaudio
.\pulseaudio.exe -D --exit-idle-time=-1 --load="module-native-protocol-tcp auth-anonymous=1 port=4713"
```

### コンテナ側での設定（自動化済み）

`PULSE_SERVER` が `host.docker.internal:4713` になっていればOK。
テスト:

```bash
ffplay -autoexit ./game/bgm/frog_piano.mp3
```

→ ホストから音が出れば成功。

---

## 🔤 日本語フォント

IPA系フォントを同梱済みで、`options.rpy` から自動指定しています。

| ファイル               | 英語名         | 日本語名      |
| ------------------ | ----------- | --------- |
| `fonts/ipam.ttf`   | IPAMincho   | IPA明朝     |
| `fonts/ipaexg.ttf` | IPAexGothic | IPAexゴシック |
| `fonts/ipagp.ttf`  | IPAPGothic  | IPA Pゴシック |
| `fonts/ipaexm.ttf` | IPAexMincho | IPAex明朝   |
| `fonts/ipamp.ttf`  | IPAPMincho  | IPA P明朝   |
| `fonts/ipag.ttf`   | IPAGothic   | IPAゴシック   |

`options.rpy`（抜粋）:

```renpy
# デフォルトフォント
style.default.font = "fonts/ipam.ttf"
```

* `.rpy` は UTF-8 で保存
* フォントパスの打ち間違いに注意

---

## 📁 ディレクトリ構成

```
game/
├── script.rpy
├── screens.rpy
├── options.rpy
├── fonts/
│   └── ipaexg.ttf
├── images/
├── audio/
└── saves/
```

---

## 🧪 最小テストコード

`script.rpy`

```renpy
define z = Character("ずんだもん")

label start:
    scene black
    z "こんにちは、マスター。日本語フォントのテストです。"
    return
```

`screens.rpy`

```renpy
screen main_menu():
    tag menu
    vbox:
        style_prefix "main_menu"
        spacing 20
        xalign 0.5
        yalign 0.6

        textbutton "はじめから" action Start()
        textbutton "ロード" action ShowMenu("load")
        textbutton "設定" action ShowMenu("preferences")
        textbutton "終了" action Quit(confirm=True)
```

---

## 📚 FAQ

**Q. ランチャー画面を出したい**
A. 通常は不要ですが、以下で起動可能です。

```bash
/opt/renpy/renpy.sh launcher .
```

**Q. X11が映らない / PulseAudioが鳴らない**

* Windows ファイアウォールでブロックされていないか確認
* `DISPLAY` / `PULSE_SERVER` 環境変数を確認
* Xサーバー側のアクセス制御を無効化する

---

## 🏗️ ビルド（配布パッケージ生成）

```bash
chmod +x build.sh
./build.sh
```

環境変数でカスタマイズ:

```bash
# 例: プロジェクト/出力先指定
PROJ=/path/to/proj DEST=/artifacts ./build.sh
```

---

## 🔗 参考

* Ren'Py 公式ドキュメント: [https://www.renpy.org/doc/html/](https://www.renpy.org/doc/html/)
* IPAフォント: [https://moji.or.jp/ipafont/](https://moji.or.jp/ipafont/)

---

## 📝 ライセンス

* 本テンプレート：MIT License
* IPAフォント：IPA配布条件に準拠してください
