# 犬猫判定アプリ
## 【仕様】
GoogleColabにて「犬猫の画像判定用機械モデル」を２種作成、このモデル予測精度の高い方のモデル（ファインチューニングで作成）と「Flask」を利用し、Python3にてコードを作成。その後、「Render」でWeb公開しています。
## 【Web公開URL】
[犬猫判定アプリ](https://animal-app-zdb9.onrender.com/)  https://animal-app-zdb9.onrender.com/
## 【使用可能画像（拡張子）】
- png
- jpg
- gif
- jpeg
## 【アプリ使用方法】
1. 判定する画像をご用意をおねがいいたします。
2. 上記【Web公開URL】よりURLをクリック、または、直接ご入力をお願いいたします。
3. 「ファイルをアップロードして犬か猫かを判定しよう」と表示がでましたら、「ファイル選択」ボタンをクリックし、ご用意していただいた画像のご選択をお願いいたします。
4. 「判定」ボタンをクリックをお願いいたします。
5. 判定が出ます。

※ご使用の環境により、表示までにお時間がかかる場合がございます。ご容赦いただけますと幸いです。

## 画像処理(犬猫判定)モデルコード　　※GoogleColabにて
### ファインチューニング　　※今回はこちらを元にアプリを作成しております。
※torchvision.modelsのresnet18元にしました。
[ファインチューニングで画像処理モデル(犬猫判定)](https://colab.research.google.com/drive/1Yz7s6m0otORxifKz0lJmUmzJt2EzvhpH?usp=sharing)
https://colab.research.google.com/drive/1Yz7s6m0otORxifKz0lJmUmzJt2EzvhpH?usp=sharing
### 自作モデルコード　　※参考までにこちらもどうぞ。
[自作画像処理モデル(犬猫判定)](https://colab.research.google.com/drive/1yDl4A23vdDDBR51HGtdifECI6UKol3J8?usp=sharing)
https://colab.research.google.com/drive/1yDl4A23vdDDBR51HGtdifECI6UKol3J8?usp=sharing

## 【利用したツールなど】
- GoogleColab
- Visual Studio Code
- FLask
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
  - resnet18
  - glob
  - natsort
  - warnings
## 【animal_APP　ファイル解説】
- animal_APP/src
  - /animal.py　：モジュールインポート、学習済みモデル対応の前処理、ネットワーク定義（モデルの構想）
  - /appy.py　　：モジュールインポート、学習済みモデルでの推論、犬猫判定、データ入力および結果の（Flaskによる）Web表示
  - /dog_cat.pt ：モデルの学習結果（重みなど）
  - 
- animal_APP/src/templates
  - /index.html ：Web表示時の初期画面用のフォーマット（入力画面）
  - /result.html：Web表示時の結果表示画面用のフォーマット（出力画面）
  - 
- animal_APP
  - /requirements.txt：使用ライブラリーバージョン設定
  - /README.md：このanimal_APPの説明書
#### ＜おまけ＞
※よろしければ、こちらもご覧いただけると幸いです。
色々学んだことをブログにまとめてます。

[まぬねこの足跡。。。](https://manulcat280.hatenablog.com/entry/2023/06/06/Python_%E7%9B%AE%E6%AC%A1)　https://manulcat280.hatenablog.com/entry/2023/06/06/Python_%E7%9B%AE%E6%AC%A1
