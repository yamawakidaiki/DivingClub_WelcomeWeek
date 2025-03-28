# 概要
このコードは，Pythonを使用して作成されたプログラムです．  
対象はプログラミング初心者の方で，WindowsおよびMacのどちらでも動作するように構成されています．  
以下の手順に従って，環境を構築し，プログラムを実行してください．

---

## 1. 必要な環境

- **Python**  
  動作確認できているのは，Python 3.12.4 です．  
  ※ Pythonが既にインストールされている場合は，次の「Pythonのインストール手順」はスキップして構いません．

---

## 2. Pythonのインストール手順

### Windowsの場合

1. [Python公式サイト](https://www.python.jp/install/windows/install.html) にアクセスし，これに従ってパッケージをインストールしてください。
2. ダウンロードしたインストーラーを実行します．  
   インストール時に「Add Python 3.x to PATH」にチェックを入れることを忘れないでください．
3. インストールが完了したら，`コマンドプロンプト`を開き，以下のコマンドでインストールが成功したか確認します．
```
   python --version
```
バージョン番号が表示されれば成功です。

### Macの場合
#### Python公式サイトからインストールする
同様にPython公式サイトにアクセスして，ダウンロードした`.pkg`ファイルを開いて、画面に表示される指示に従いインストールを進めてください。
#### Homebrewを利用してインストールする
Homebrewを利用してインストールする方法もあります。
HomebrewとはMac用のパッケージ管理ツールで、コマンドラインから簡単に様々なソフトウェアをインストールできます。

1. `ターミナル.app`を開きます。
2. Homebrewをインストールします。ターミナル.appで以下のコマンドをコピー・ペーストしてください。
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
3. インストールが成功したら，次のコマンドを実行してください。：`brew install python`
4. インストールの確認をします。`python --version`でバージョン番号が表示されれば成功です。



## 3. Pythonプログラムの実行
### 3.1 事前準備
フォルダを新規作成して，そこにGitHubで共有されているPythonファイルと器材管理用のエクセルファイルを入れます。
こんなかんじ。
```
.
├── EquipManagement_2024_adjustment.xlsx（器材管理用エクセルファイル）
├── EquipmentManagement_DivingClub.py：（GitHubで共有したpython file）
├── README.md
```

`ターミナル.app`で先ほど新規作成したフォルダに移動して，`python <ファイル名>.py`で実行できる。
例：`python EquipmentManagement_DivingClub.py`

※エクセルファイルのファイル名称を変更した場合，Pythonファイルがうまく実行できません。ファイル名を変更した場合は，pythonファイル14行目：`    input_file ="EquipManagement_2024_adjustment.xlsx"`の`EquipManagement_2024_adjustment.xlsx`部分を変更してください。その際，""は削除しないよう気をつけてください。

### 3.2 プログラム実行方法
上記手順に従って実行すると，以下のように出力される（Macの場合）。ターミナル.appで`python <ファイル名>.py`を実行すると，以下のようになる。
身長体重ブーツサイズが聞かれるので，そこにそれぞれ新入生のデータを入力すると，
-  身長：±5
-  体重：±10
-  ブーツ：±3

の範囲にある今までの先輩の器材が名前と共に出力される。
ある新入生に対して，身長・体重・ブーツサイズが似ている先輩を出力してくれるわけだ。
※ これは，pythonが先輩方の身長体重ブーツサイズが記載されているエクセルファイルを読み込んで，処理している。

```
(base) yama＠MacBook-Air urdc% EquipmentManagement_DivingClub.py
新入生の身長を入力してください (cm): 171
新入生の体重を入力してください (kg): 73
新入生のブーツサイズを入力してください (cm): 26.5
ファイルに含まれる列名:
Index(['名前', '身長', '体重', 'ブーツ', 'オプチ', '適正(ジャケ有)', '適正(ジャケ無)', '期', '学部/コース',
    '性', 'Unnamed: 10', 'マスク', 'シュノーケル', 'ロングジョン', 'ジャケット', 'ナイフ', 'ブーツ.1',
    'グローブ'],
    dtype='object')

マッチング結果:
条件に一致するデータ数: 4

以下のデータが新入生の条件に近いです:
	名前    身長   体重  ブーツ        オプチ 適正(ジャケ有)  適正(ジャケ無)    期
	name 1 173.0 71.0 26.5        度無し        5       3.0 51.0
	name 2 166.0 64.0 26.5        度無し      NaN       NaN 53.0
	name 3 176.0 68.0 28.5 左-6.0右-5.5      NaN       NaN 54.0
	name 4 174.0 72.5 27.0     両方-4.0      NaN       NaN 54.0
'''
```
