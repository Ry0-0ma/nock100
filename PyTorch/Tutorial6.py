# パラメータの最適化

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda
# データ準備
training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)

train_dataloader = DataLoader(training_data, batch_size=64)
test_dataloader = DataLoader(test_data, batch_size=64)
# モデル構築
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

model = NeuralNetwork()

# ハイパーパラメータ
# 訓練用のハイパーパラメータとして以下の値を使用します。
#    # Number of Epochs：イテレーション回数
#    # Batch Size：ミニバッチサイズを構成するデータ数
#    # Learning Rate：パラメータ更新の係数。値が小さいと変化が少なく、大きすぎると訓練に失敗する可能性が生まれる
learning_rate = 1e-3
batch_size = 64
epochs = 5

# 最適化ループ
# 各エポックでは2種類のループから構成されます。
#    # 訓練ループ：データセットに対して訓練を実行し、パラメータを収束させます
#    # 検証 / テストループ：テストデータセットでモデルを評価し、性能が向上しているか確認します

# Loss function
# 一般的な損失関数としては、回帰タスクではnn.MSELoss(Mean Square Error)、分類タスクではnn.NLLLoss(Negative Log Likelihood) が使用されます。
# nn.CrossEntropyLossは、nn.LogSoftmax と nn.NLLLossを結合した損失関数
# モデルが出力するlogit値をnn.CrossEntropyLossに与えて正規化し、予測誤差を求めます。

# loss functionの初期化、定義
loss_fn = nn.CrossEntropyLoss()


# Optimizer: 各訓練ステップにおいてモデルの誤差を小さくなるように、モデルパラメータを調整するプロセス
# Optimization algorithm: 最適化プロセスの具体的な手続き(ex:SGD, Adam, RMSprop)
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

# 訓練ループ内で、最適化（optimization）は3つのステップから構成されます。
#    # [1] optimizer.zero_grad()を実行し、モデルパラメータの勾配をリセットします。
#       # 勾配の計算は蓄積されていくので、毎イテレーション、明示的にリセットします。
#    # [2] 続いて、loss.backwards()を実行し、バックプロパゲーションを実行します。
#       # PyTorchは損失に対する各パラメータの偏微分の値（勾配）を求めます。
#    # [3] 最後に、optimizer.step()を実行し、各パラメータの勾配を使用してパラメータの値を調整


def train_loop(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset) #全訓練データのサンプル数
    # batchはバッチ番号, （X:入力, y:ラベル(真値)）
    for batch, (X, y) in enumerate(dataloader):
        # 予測と損失の計算
        pred = model(X) #入力と予測値
        loss = loss_fn(pred, y) #損失関数の計算

        # バックプロパゲーション
        optimizer.zero_grad()  # 勾配をリセット
        loss.backward()        # 勾配を計算
        optimizer.step()       # パラメータを更新

        # 100バッチごとに損失値と進捗を表示
        if batch % 100 == 0:
            loss, current = loss.item(), batch * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")


def test_loop(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    test_loss, correct = 0, 0 #損失と正解数をカウント

    # テスト時はパラメータ更新しない
    with torch.no_grad():
        for X, y in dataloader:
            pred = model(X)
            test_loss += loss_fn(pred, y).item() #損失を計算し、.item()でスカラー値に変換
            # pred.argmax(1) は、各サンプルについて最もスコアが高いクラス（＝モデルの予測クラス）のインデックスを取得
            # .type(torch.float) でTrue→1.0, False→0.0に変換。
            # .sum() でバッチ内の正解数を合計。
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()

    test_loss /= size
    correct /= size
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")


# モデルの性能を向上させるために、epoch数は自由に変えて
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

epochs = 10
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train_loop(train_dataloader, model, loss_fn, optimizer)
    test_loop(test_dataloader, model, loss_fn)
print("Done!")


"""
Epoch 1
-------------------------------
loss: 2.304773  [    0/60000]
loss: 2.289492  [ 6400/60000]
loss: 2.283064  [12800/60000]
loss: 2.283863  [19200/60000]
loss: 2.269354  [25600/60000]
loss: 2.272359  [32000/60000]
loss: 2.270423  [38400/60000]
loss: 2.258389  [44800/60000]
loss: 2.282936  [51200/60000]
loss: 2.259048  [57600/60000]
Test Error: 
 Accuracy: 30.5%, Avg loss: 0.035257 

Epoch 2
-------------------------------
loss: 2.254249  [    0/60000]
loss: 2.232351  [ 6400/60000]
loss: 2.201711  [12800/60000]
loss: 2.229116  [19200/60000]
loss: 2.189451  [25600/60000]
loss: 2.186262  [32000/60000]
loss: 2.201424  [38400/60000]
loss: 2.157880  [44800/60000]
loss: 2.218282  [51200/60000]
loss: 2.195665  [57600/60000]
Test Error: 
 Accuracy: 36.8%, Avg loss: 0.033843 

Epoch 3
-------------------------------
loss: 2.158784  [    0/60000]
loss: 2.127866  [ 6400/60000]
loss: 2.061152  [12800/60000]
loss: 2.139946  [19200/60000]
loss: 2.057133  [25600/60000]
loss: 2.056817  [32000/60000]
loss: 2.102714  [38400/60000]
loss: 2.021773  [44800/60000]
loss: 2.133122  [51200/60000]
loss: 2.122735  [57600/60000]
Test Error: 
 Accuracy: 38.4%, Avg loss: 0.032053 

Epoch 4
-------------------------------
loss: 2.034218  [    0/60000]
loss: 1.999052  [ 6400/60000]
loss: 1.895393  [12800/60000]
loss: 2.037977  [19200/60000]
loss: 1.926516  [25600/60000]
loss: 1.932843  [32000/60000]
loss: 1.993184  [38400/60000]
loss: 1.876132  [44800/60000]
loss: 2.003767  [51200/60000]
loss: 2.012055  [57600/60000]
Test Error: 
 Accuracy: 39.0%, Avg loss: 0.029798 

Epoch 5
-------------------------------
loss: 1.865779  [    0/60000]
loss: 1.830860  [ 6400/60000]
loss: 1.718587  [12800/60000]
loss: 1.899894  [19200/60000]
loss: 1.721863  [25600/60000]
loss: 1.776795  [32000/60000]
loss: 1.779975  [38400/60000]
loss: 1.682932  [44800/60000]
loss: 1.799819  [51200/60000]
loss: 1.840212  [57600/60000]
Test Error: 
 Accuracy: 49.4%, Avg loss: 0.027107 

Epoch 6
-------------------------------
loss: 1.656709  [    0/60000]
loss: 1.646050  [ 6400/60000]
loss: 1.551913  [12800/60000]
loss: 1.758092  [19200/60000]
loss: 1.547032  [25600/60000]
loss: 1.648440  [32000/60000]
loss: 1.589852  [38400/60000]
loss: 1.535068  [44800/60000]
loss: 1.636061  [51200/60000]
loss: 1.689397  [57600/60000]
Test Error: 
 Accuracy: 53.1%, Avg loss: 0.024980 

Epoch 7
-------------------------------
loss: 1.493047  [    0/60000]
loss: 1.508031  [ 6400/60000]
loss: 1.427181  [12800/60000]
loss: 1.644915  [19200/60000]
loss: 1.420494  [25600/60000]
loss: 1.550562  [32000/60000]
loss: 1.452252  [38400/60000]
loss: 1.433183  [44800/60000]
loss: 1.524521  [51200/60000]
loss: 1.585904  [57600/60000]
Test Error: 
 Accuracy: 53.9%, Avg loss: 0.023426 

Epoch 8
-------------------------------
loss: 1.375264  [    0/60000]
loss: 1.409020  [ 6400/60000]
loss: 1.331622  [12800/60000]
loss: 1.563614  [19200/60000]
loss: 1.327853  [25600/60000]
loss: 1.471692  [32000/60000]
loss: 1.356388  [38400/60000]
loss: 1.358889  [44800/60000]
loss: 1.440302  [51200/60000]
loss: 1.511951  [57600/60000]
Test Error: 
 Accuracy: 55.4%, Avg loss: 0.022235 

Epoch 9
-------------------------------
loss: 1.286818  [    0/60000]
loss: 1.334444  [ 6400/60000]
loss: 1.255768  [12800/60000]
loss: 1.505001  [19200/60000]
loss: 1.258789  [25600/60000]
loss: 1.406621  [32000/60000]
loss: 1.286406  [38400/60000]
loss: 1.302734  [44800/60000]
loss: 1.374314  [51200/60000]
loss: 1.456086  [57600/60000]
Test Error: 
 Accuracy: 56.7%, Avg loss: 0.021285 

Epoch 10
-------------------------------
loss: 1.217064  [    0/60000]
loss: 1.271600  [ 6400/60000]
loss: 1.194619  [12800/60000]
loss: 1.461143  [19200/60000]
loss: 1.204940  [25600/60000]
loss: 1.352715  [32000/60000]
loss: 1.232833  [38400/60000]
loss: 1.258434  [44800/60000]
loss: 1.320335  [51200/60000]
loss: 1.413019  [57600/60000]
Test Error: 
 Accuracy: 58.0%, Avg loss: 0.020508 

Done!
"""
