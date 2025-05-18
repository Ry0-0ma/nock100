# ニューラルネットワークモデルの作り方

# ニューラルネットワークは、レイヤー（もしくはモジュール）と呼ばれるデータ操作の固まりで構成
# PyTorchの全てのモジュールは、nn.Moduleを継承

import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# 訓練に使用するデバイス(使用可能なGPU)
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print('Using {} device'.format(device))

# クラスの定義
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten() #平滑化(次元を減らす)
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
            nn.ReLU()
        )
    # 順伝搬
    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits


model = NeuralNetwork().to(device) #インスタンス生成
print(model)


# 入力データをモデルに投入すると、forward関数で処理されるとともに、いくつかのbackground operationsが実行
# model.forward() と記載して入力データを処理しない
# モデルに入力を与えると、各クラスの生の予測値を含む10次元のテンソルが返されます
# nn.Softmaxモジュールにこの出力結果を与えることで、入力データが各クラスに属する確率の予測値を求める

X = torch.rand(1, 28, 28, device=device) #ランダムな入力
logits = model(X) #forward関数を呼び出す
pred_probab = nn.Softmax(dim=1)(logits)
y_pred = pred_probab.argmax(1)
print(f"Predicted class: {y_pred}")

# モデルレイヤー
# サイズ28x28の3枚の画像からなるミニバッチのサンプルを用意し、このミニバッチをネットワークに入力し、各処理による変化を確認
input_image = torch.rand(3,28,28)
print(input_image.size())

# nn.Flatten
# 2次元（28x28）の画像を、1次元の784ピクセルの値へと変換
# ミニバッチの0次元目は、サンプル番号を示す次元で、この次元はnn.Flattenを通しても変化しません（1次元目以降がFlattenされます）。
flatten = nn.Flatten()
flat_image = flatten(input_image)
print(flat_image.size())

# nn.Linear
# linear layerは重みとバイアスのパラメータを保持
layer1 = nn.Linear(in_features=28*28, out_features=20)
hidden1 = layer1(flat_image) #線形変換
# 784次元の入力を20次元の出力に変換
print(hidden1.size())

# nn.ReLU
print(f"Before ReLU: {hidden1}\n\n")
hidden1 = nn.ReLU()(hidden1) #活性化関数
# ReLUは、負の値を0に変換し、正の値はそのまま出力
print(f"After ReLU: {hidden1}")

# nn.Sequential
seq_modules = nn.Sequential(
    flatten,
    layer1,
    nn.ReLU(),
    nn.Linear(20, 10)
)
input_image = torch.rand(3,28,28)
logits = seq_modules(input_image)

# nn.Softmax
# ニューラルネットワークの最後のlinear layerはlogits [- ∞, ∞] を出力
# nn.Softmax に渡す→採取的な値は[0, 1]の範囲となり、これは各クラスである確率を示し
# dimパラメータは次元を示しており、dim=1の次元で和を求めると確率の総和なので1になります。
softmax = nn.Softmax(dim=1)
pred_probab = softmax(logits)

# nn.Moduleの継承により
# parameters() や named_parameters() メソッドを使って、モデルの各レイヤーのすべてのパラメータにアクセス

print("Model structure: ", model, "\n\n")

for name, param in model.named_parameters():
    print(f"Layer: {name} | Size: {param.size()} | Values : {param[:2]} \n")




"""
Using cuda device
NeuralNetwork(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (linear_relu_stack): Sequential(
    (0): Linear(in_features=784, out_features=512, bias=True)
    (1): ReLU()
    (2): Linear(in_features=512, out_features=512, bias=True)
    (3): ReLU()
    (4): Linear(in_features=512, out_features=10, bias=True)
    (5): ReLU()
  )
)
Predicted class: tensor([2], device='cuda:0')
torch.Size([3, 28, 28])
torch.Size([3, 784])
torch.Size([3, 20])
Before ReLU: tensor([[ 0.3893, -0.2822,  0.0093,  0.1540,  0.0052,  0.4749, -0.1554,  0.1046,
         -0.0513,  0.1357, -0.0666,  0.0466,  0.1882, -0.4081,  0.1218,  0.1984,
          0.3006, -0.3642, -0.1535, -0.0708],
        [ 0.1730, -0.5735,  0.5285, -0.0100,  0.2497,  0.3658, -0.0437,  0.3489,
          0.0313, -0.2782,  0.0725,  0.0188, -0.1053,  0.0930,  0.0188,  0.0583,
          0.1865, -0.3037,  0.0856, -0.3912],
        [ 0.2396, -0.2962,  0.4047,  0.0522,  0.2114,  0.5587, -0.1047,  0.1719,
         -0.0523,  0.1847, -0.1729,  0.0562,  0.2556, -0.4840,  0.0555,  0.4172,
          0.1185, -0.1958, -0.3090, -0.2005]], grad_fn=<AddmmBackward0>)


After ReLU: tensor([[0.3893, 0.0000, 0.0093, 0.1540, 0.0052, 0.4749, 0.0000, 0.1046, 0.0000,
         0.1357, 0.0000, 0.0466, 0.1882, 0.0000, 0.1218, 0.1984, 0.3006, 0.0000,
         0.0000, 0.0000],
        [0.1730, 0.0000, 0.5285, 0.0000, 0.2497, 0.3658, 0.0000, 0.3489, 0.0313,
         0.0000, 0.0725, 0.0188, 0.0000, 0.0930, 0.0188, 0.0583, 0.1865, 0.0000,
         0.0856, 0.0000],
        [0.2396, 0.0000, 0.4047, 0.0522, 0.2114, 0.5587, 0.0000, 0.1719, 0.0000,
         0.1847, 0.0000, 0.0562, 0.2556, 0.0000, 0.0555, 0.4172, 0.1185, 0.0000,
         0.0000, 0.0000]], grad_fn=<ReluBackward0>)
Model structure:  NeuralNetwork(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (linear_relu_stack): Sequential(
    (0): Linear(in_features=784, out_features=512, bias=True)
    (1): ReLU()
    (2): Linear(in_features=512, out_features=512, bias=True)
    (3): ReLU()
    (4): Linear(in_features=512, out_features=10, bias=True)
    (5): ReLU()
  )
) 


Layer: linear_relu_stack.0.weight | Size: torch.Size([512, 784]) | Values : tensor([[-0.0153, -0.0292,  0.0147,  ..., -0.0081, -0.0008,  0.0126],
        [ 0.0162, -0.0006, -0.0054,  ..., -0.0020,  0.0112,  0.0106]],
       device='cuda:0', grad_fn=<SliceBackward0>) 

Layer: linear_relu_stack.0.bias | Size: torch.Size([512]) | Values : tensor([-0.0177,  0.0215], device='cuda:0', grad_fn=<SliceBackward0>) 

Layer: linear_relu_stack.2.weight | Size: torch.Size([512, 512]) | Values : tensor([[-0.0176,  0.0274, -0.0334,  ...,  0.0088, -0.0377, -0.0184],
        [-0.0069,  0.0134,  0.0153,  ..., -0.0237,  0.0139, -0.0091]],
       device='cuda:0', grad_fn=<SliceBackward0>) 

Layer: linear_relu_stack.2.bias | Size: torch.Size([512]) | Values : tensor([ 0.0315, -0.0171], device='cuda:0', grad_fn=<SliceBackward0>) 

Layer: linear_relu_stack.4.weight | Size: torch.Size([10, 512]) | Values : tensor([[-0.0339,  0.0040, -0.0250,  ...,  0.0157,  0.0348,  0.0026],
        [ 0.0085,  0.0272,  0.0310,  ...,  0.0137, -0.0138,  0.0070]],
       device='cuda:0', grad_fn=<SliceBackward0>) 

Layer: linear_relu_stack.4.bias | Size: torch.Size([10]) | Values : tensor([ 0.0071, -0.0152], device='cuda:0', grad_fn=<SliceBackward0>) 
"""