# coding: utf-8
# 必要なモジュールのインポート
from torchvision import transforms
import pytorch_lightning as pl
import torch.nn as nn
#学習時に使ったのと同じ学習済みモデルをインポート
from torchvision.models import resnet18 

# 学習済みモデルに合わせた前処理を追加
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# ネットワークの定義
class Net(pl.LightningModule):

    def __init__(self):
        super().__init__()

        ### 特徴抽出器（ファインチューニング）：ResNe
        self.feature = resnet18(pretrained=True)

        ###   全結合層(1000分類⇒2分類)
        self.fc0 = nn.Linear(1000, 2)


    ###  順伝播 
    def forward(self, x):

        ### 特徴抽出器（ファインチューニング）：ResNe
        h = self.feature(x)

        ### 線形変換 全結合層
        h = self.fc0(h)

        return h