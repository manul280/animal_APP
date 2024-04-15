# 犬猫判定アプリ
## 目次
- [仕様](https://github.com/manul280/animal_APP/edit/master/README.md#%E4%BB%95%E6%A7%98)　
- Web公開URL
- 使用可能画像（拡張子）
- アプリ使用方法
- コード
- 利用したツールなど
- 使用言語・ライブラリ
- おまけ

## 【仕様】
GoogleColabにて「犬猫の画像判定用機械モデル」を作成、このモデルの重み等を利用し、Python3にてコードを作成。その後、「Render」でWeb公開しています。
## 【Web公開URL】
[犬猫判定アプリ](https://animal-app-zdb9.onrender.com/)  https://animal-app-zdb9.onrender.com/
## 【使用可能画像（拡張子）】
- png
- jpg
- gif
- jpeg
## 【アプリ使用方法】
1. 上記【Web公開URL】よりURLをクリック、または、直接ご入力をお願いいたします。
2. 「ファイルをアップロードして犬か猫かを判定しよう」と表示がでましたら、「ファイル選択」ボタンをクリックし、ご用意していただいた画像のご選択をお願いいたします。
3. 「判定」ボタンをクリックをお願いいたします。
4. 判定が出ます。

※ご使用の環境により、表示までにお時間がかかる場合がございます。ご容赦いただけますと幸いです。

## 【コード】
### 画像処理(犬猫判定)モデルコード　　※GoogleColabにて
https://colab.research.google.com/drive/1yDl4A23vdDDBR51HGtdifECI6UKol3J8?usp=sharing
## 【利用したツールなど】
- GoogleColab
- Visual Studio Code
- Render
- GitHub
## 【使用言語・ライブラリ】
- Python3
  ‐ numpy
  - pandas
  - matplotlib
  - OpenCV
  - PIL
  - torch
  - pytorch_lightning
  - torchmetrics
  - torchvision
  - glob
  - natsort
  - warnings

#### ＜おまけ＞
※よろしければ、こちらもご覧いただけると幸いです。
色々学んだことをブログにまとめてます。

[まぬねこの足跡。。。](https://manulcat280.hatenablog.com/entry/2023/06/06/Python_%E7%9B%AE%E6%AC%A1)　https://manulcat280.hatenablog.com/entry/2023/06/06/Python_%E7%9B%AE%E6%AC%A1
