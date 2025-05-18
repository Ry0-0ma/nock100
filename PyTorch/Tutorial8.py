import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda, Compose
import matplotlib.pyplot as plt

# PyTorchには以下に示すようなドメイン固有のライブラリが存在し、それぞれにデータセットが用意されています。
#   #TorchText
#   #TorchVision
#   #TorchAudio

# torchvision.datasets モジュールには、画像データの Dataset オブジェクトがたくさん用意
#   #CIFAR, COCO, FahionMNIST

# 訓練データをdatasetsからダウンロード
training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
)

# テストデータをdatasetsからダウンロード
test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor(),
)

batch_size = 64
# データローダーの作成(イテレート処理できる)
train_dataloader = DataLoader(training_data, batch_size=batch_size)
test_dataloader = DataLoader(test_data, batch_size=batch_size)

for X, y in test_dataloader:
    print("Shape of X [N, C, H, W]: ", X.shape)
    print("Shape of y: ", y.shape, y.dtype)
    break


# モデルの構築
# 訓練に際して、可能であればGPU（cuda）を設定します。GPUが搭載されていない場合はCPUを使用します
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using {} device".format(device))

# modelを定義します
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
            nn.ReLU()
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

model = NeuralNetwork().to(device)
print(model)


# モデルパラメータの最適化
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        # 損失誤差を計算
        pred = model(X)
        loss = loss_fn(pred, y)

        # バックプロパゲーション
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 100 == 0:
            loss, current = loss.item(), batch * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")

def test(dataloader, model):
    size = len(dataloader.dataset)
    model.eval() # モデルを評価モードにする
    test_loss, correct = 0, 0
    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
    test_loss /= size
    correct /= size
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")


# モデルパラメータの最適化
epochs = 5
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train(train_dataloader, model, loss_fn, optimizer)
    test(test_dataloader, model)
print("Done!")

# モデルの保存
torch.save(model.state_dict(), "Tuto8_model.pth")
print("Saved PyTorch Model State to Tuto8_model.pth")

# モデルの読み込み
model = NeuralNetwork()
model.load_state_dict(torch.load("Tuto8_model.pth"))

classes = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]

model.eval()
x, y = test_data[0][0], test_data[0][1]
with torch.no_grad():
    pred = model(x)
    predicted, actual = classes[pred[0].argmax(0)], classes[y]
    print(f'Predicted: "{predicted}", Actual: "{actual}"')


"""
Shape of X [N, C, H, W]:  torch.Size([64, 1, 28, 28])
Shape of y:  torch.Size([64]) torch.int64
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
Epoch 1
-------------------------------
loss: 2.301979  [    0/60000]
loss: 2.291653  [ 6400/60000]
loss: 2.281521  [12800/60000]
loss: 2.279319  [19200/60000]
loss: 2.266802  [25600/60000]
loss: 2.258501  [32000/60000]
loss: 2.242954  [38400/60000]
loss: 2.225652  [44800/60000]
loss: 2.230237  [51200/60000]
loss: 2.214223  [57600/60000]
Test Error: 
 Accuracy: 57.3%, Avg loss: 0.034622 

Epoch 2
-------------------------------
loss: 2.219101  [    0/60000]
loss: 2.204568  [ 6400/60000]
loss: 2.171695  [12800/60000]
loss: 2.175508  [19200/60000]
loss: 2.144600  [25600/60000]
loss: 2.107833  [32000/60000]
loss: 2.116682  [38400/60000]
loss: 2.064735  [44800/60000]
loss: 2.083147  [51200/60000]
loss: 2.030536  [57600/60000]
Test Error: 
 Accuracy: 61.2%, Avg loss: 0.031838 

Epoch 3
-------------------------------
loss: 2.064008  [    0/60000]
loss: 2.033675  [ 6400/60000]
loss: 1.951393  [12800/60000]
loss: 1.971459  [19200/60000]
loss: 1.904943  [25600/60000]
loss: 1.840830  [32000/60000]
loss: 1.863329  [38400/60000]
loss: 1.768143  [44800/60000]
loss: 1.821840  [51200/60000]
loss: 1.704236  [57600/60000]
Test Error: 
 Accuracy: 61.8%, Avg loss: 0.027030 

Epoch 4
-------------------------------
loss: 1.794362  [    0/60000]
loss: 1.747299  [ 6400/60000]
loss: 1.610735  [12800/60000]
loss: 1.662907  [19200/60000]
loss: 1.609250  [25600/60000]
loss: 1.510284  [32000/60000]
loss: 1.553289  [38400/60000]
loss: 1.437907  [44800/60000]
loss: 1.552842  [51200/60000]
loss: 1.380287  [57600/60000]
Test Error: 
 Accuracy: 63.1%, Avg loss: 0.022527 

Epoch 5
-------------------------------
loss: 1.543521  [    0/60000]
loss: 1.495954  [ 6400/60000]
loss: 1.334987  [12800/60000]
loss: 1.413276  [19200/60000]
loss: 1.417993  [25600/60000]
loss: 1.285616  [32000/60000]
loss: 1.343172  [38400/60000]
loss: 1.228626  [44800/60000]
loss: 1.391157  [51200/60000]
loss: 1.187912  [57600/60000]
Test Error: 
 Accuracy: 64.2%, Avg loss: 0.019849 

Done!
Saved PyTorch Model State to Tuto8_model.pth
Predicted: "Ankle boot", Actual: "Ankle boot"
"""