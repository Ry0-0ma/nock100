# Transforms

from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda

ds = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
    target_transform=Lambda(lambda y: torch.zeros(10, dtype=torch.float).scatter_(0, torch.tensor(y), value=1))
    # 最初に大きさ10のゼロテンソルを作成し（10はクラス数に対応）、scatter_ を用いて、ラベルyの値のindexのみ1のワンホットエンコーディングに変換
)
"""
    ラベル y(例えば、クラス 3)
    を受け取る。
    長さ 10 のゼロテンソルを作成。
    scatter_ を使って、y 番目の要素を 1 に設定。
    例えば、y=3 の場合、結果は [0, 0, 0, 1, 0, 0, 0, 0, 0, 0] となります。
    これにより、ラベルがワンホットエンコーディング形式に変換されます。
"""

# https://docs.pytorch.org/vision/stable/transforms.html

