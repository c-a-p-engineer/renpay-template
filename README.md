# Ren'Py Template (renpay-template)

このリポジトリは、ビジュアルノベルエンジン [Ren'Py](https://www.renpy.org/) を使用した開発のための DevContainer テンプレートです。

## 🚀 概要

- **Ren'Py SDK** を DevContainer 内に自動インストール
- **日本語フォント対応済み**（IPAフォント）
- **GUIアプリケーション対応（X11）**
- **VSCode DevContainers 対応**
- **Windows / WSL2 / Linux 向け**

---

## 🧩 前提条件

以下のツールをインストールしてください：

- [Visual Studio Code](https://code.visualstudio.com/)
- [Dev Containers 拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- （Windows の場合）[VcXsrv](https://sourceforge.net/projects/vcxsrv/) または [X410](https://x410.dev/)

---

## 📦 セットアップ手順

1. このリポジトリをクローン：

    ```bash
    git clone https://github.com/your-name/renpay-template.git
    cd renpay-template
    ```

2. VS Code で開く → 「Reopen in Container」を選択

3. 自動でDevContainerが構築され、Ren'Pyやフォントが導入されます

---

## 🖥️ Ren'Pyの起動方法

コンテナ内で以下のコマンドを実行してください：

```bash
renpy .
```

または、X11が無効な場合は以下でも可：

```bash
xvfb-run --auto-servernum renpy .
```

※プロジェクトのルートが `renpy` に渡されることで、ゲームが即実行されます。

---

## 🌐 X11表示の確認方法（Windows / Linux）

### Windows + VcXsrv の場合：

1. `XLaunch` を実行 → 以下の設定で起動：

   * ✔ Multiple windows
   * ✔ Start no client
   * ✔ Disable access control

2. DevContainerが以下を含んでいればOK：

```jsonc
"runArgs": [
  "--env", "DISPLAY=${localEnv:DISPLAY}",
  "--volume", "/tmp/.X11-unix:/tmp/.X11-unix:rw"
],
"containerEnv": {
  "DISPLAY": "${localEnv:DISPLAY}"
}
```

3. 実行テスト：

```bash
xeyes
```

→ 目が表示されれば成功です

---

## 🔤 日本語フォント対応について

本テンプレートにはIPAフォントが導入済みです。

### 🗂️ IPAフォント一覧（表示名付き）

| 📄 ファイルパス            | 💬 フォント名（英語）  | 🈁 日本語名     |
| -------------------- | ------------- | ----------- |
| `./fonts/ipam.ttf`   | `IPAMincho`   | `IPA明朝`     |
| `./fonts/ipaexg.ttf` | `IPAexGothic` | `IPAexゴシック` |
| `./fonts/ipagp.ttf`  | `IPAPGothic`  | `IPA Pゴシック` |
| `./fonts/ipaexm.ttf` | `IPAexMincho` | `IPAex明朝`   |
| `./fonts/ipamp.ttf`  | `IPAPMincho`  | `IPA P明朝`   |
| `./fonts/ipag.ttf`   | `IPAGothic`   | `IPAゴシック`   |


### フォント設置場所：

```
game/
└── fonts/
    └── ipaexg.ttf
```

### `options.rpy` の設定（自動適用済み）：

```renpy
        ## ゲーム内で使われるデフォルトフォント

        ## デフォルトフォントを含むファイル
        style.default.font = "fonts/ipam.ttf"
```

### 文字化け対策：

* `.rpy` ファイルは UTF-8 で保存
* 上記フォント指定が正しく行われていることを確認

---

## 📁 ディレクトリ構成

```
game/
├── script.rpy      # ゲーム本編スクリプト
├── screens.rpy     # UI定義（メインメニューなど）
├── options.rpy     # 設定
├── fonts/
│    └── ipaexg.ttf # 日本語対応フォント
├── images/         # 画像素材（任意）
├── audio/          # 音声素材（任意）
└── saves/          # セーブデータ保存先
```

---

## 🧪 テスト用コード

### `script.rpy`

```renpy
define z = Character("ずんだもん")

label start:
    scene black
    z "こんにちは、マスター。日本語フォントのテストです。"
    return
```

### `screens.rpy`

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

## 📚 よくある質問

### Q: Ren'Pyのランチャー画面を起動したい

A: `renpy.sh` を使って以下のように指定できます：

```bash
/opt/renpy/renpy.sh
```

ただし GUI ランチャーは基本的に必要ありません。通常は `renpy .` で即起動します。

---

## 🧰 補足情報

* Ren'Py公式ドキュメント: [https://www.renpy.org/doc/html/](https://www.renpy.org/doc/html/)
* IPAフォント: [https://moji.or.jp/ipafont/](https://moji.or.jp/ipafont/)

---

## 📝 ライセンス

本テンプレートはMITライセンスです。IPAフォントの使用はIPAの配布条件に準じてください。
