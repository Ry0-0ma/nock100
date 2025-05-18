import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda
import matplotlib.pyplot as plt

# Dataset の読み込み
# FahionMNIST: 28*28のグレースケール画像, 10クラス
# 60,000個の訓練データ
training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True, #root にデータが存在しない場合は、インターネットからデータをダウンロードを指定
    transform=ToTensor() #特徴量とラベルの変換を指定
)
# 10,000個のテストデータ
test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)

# データの可視化
# ランダムにサンプルして、画像を表示
labels_map = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}
figure = plt.figure(figsize=(8, 8))
cols, rows = 3, 3
for i in range(1, cols * rows + 1):
    sample_idx = torch.randint(len(training_data), size=(1,)).item() #0~len(training_data)-1の数, .itemでスカラー値
    img, label = training_data[sample_idx]
    figure.add_subplot(rows, cols, i)
    plt.title(labels_map[label])
    plt.axis("off")
    plt.imshow(img.squeeze(), cmap="gray")
# plt.show()
plt.savefig('Ex_FashonMnist.png')  # 画像ファイルとして保存
plt.close()  # メモリ解放のためにプロットを閉じる


# カスタムデータセットの作成
# 自分でカスタムしたDatasetクラスを作る際には、 __init__、__len__、__getitem__の3つの関数は必ず実装する必要があります。
# FashionMNISTの画像データをimg_dirフォルダに、ラベルはCSVファイルannotations_fileとして保存
import os
import pandas as pd
from torchvision.io import read_image

class CustomImageDataset(Dataset):
    # __init__関数はDatasetオブジェクトがインスタンス化される際に1度だけ実行されます。
    # 画像、アノテーションファイル、そしてそれらに対する変換処理（transforms：次のセクションで解説します）の初期設定を行います。
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file)
        self.img_dir = img_dir
        self.transform = transform #デフォルトはNone=そのまま
        self.target_transform = target_transform

    # データセットのサンプル数を返す関数
    def __len__(self):
        return len(self.img_labels)

    # 指定されたidxに対応するサンプルをデータセットから読み込んで返す関数
    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0]) #img_labelsの0列目に画像ファイル名
        image = read_image(img_path)
        label = self.img_labels.iloc[idx, 1] #img_labelsの1列目にラベル
        if self.transform: #Noneでなければ変換処理を実行
            image = self.transform(image) 
        if self.target_transform:
            label = self.target_transform(label)
        sample = {"image": image, "label": label}
        return sample

# DataLoaderの使用方法
# モデルの訓練時にはミニバッチ単位でデータを扱いたく、また各epochでデータはシャッフルされて欲しい
# multiprocessingを使用し、複数データの取り出しを高速化したい

# 以上を実現でいるのがDataLoader: データセットを反復処理することができます
from torch.utils.data import DataLoader

train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=64, shuffle=True)

# Display image and label.
train_features, train_labels = next(iter(train_dataloader)) #イテレータに変化し、先頭のバッチを取得
print(f"Feature batch shape: {train_features.size()}") #torch.Size([64, 1, 28, 28])
print(f"Labels batch shape: {train_labels.size()}") # torch.Size([64])
img = train_features[0].squeeze()  #.squeeze()で不要な次元を削除
label = train_labels[0]
plt.imshow(img, cmap="gray")
# plt.show()
plt.savefig('Dataloader.png')  # 画像ファイルとして保存
plt.close()  # メモリ解放のためにプロットを閉じる
print(f"Label: {label}") # 画像のラベルを表示


