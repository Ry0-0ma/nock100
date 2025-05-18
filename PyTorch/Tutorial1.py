import torch
import numpy as np


# テンソルの初期化
# numpy torch 相互に変換可能
data = [[1, 2],[3, 4]]
x_data = torch.tensor(data)

data = [[1, 2],[3, 4]]
x_data = torch.tensor(data)


# 他のテンソルから作成
x_ones = torch.ones_like(x_data) # x_dataのプロパティ（サイズ、データ型）を引き継ぐ
print(f'Ones Tensor: {x_ones}\n')

x_rand = torch.rand_like(x_data, dtype=torch.float) # x_dataのdatatypeを上書き更新
print(f"Random Tensor: \n {x_rand} \n")


# ランダム地や定数のテンソルの作成
    # テンソルのサイズを決めてから
shape = (2,3,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f"Random Tensor: \n {rand_tensor} \n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor}")


# テンソルの属性変数
tensor = torch.rand(3, 4)
print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")


# テンソルの操作
if torch.cuda.is_available():
    tensor = tensor.to('cuda') # GPUに移動
print(tensor.device)
tensor = torch.ones(4, 4)
print('First row: ',tensor[0])
print('First column: ', tensor[:, 0])
print('Last column:', tensor[..., -1])
tensor[:,1] = 0 # 2列目を0にする
print(tensor)


# テンソルの結合
t1 = torch.cat([tensor, tensor, tensor], dim=1) #torch.stack では次元を増やして結合
print(t1)
#cat: 結合する次元以外のサイズがそろっている必要あり, stack: サイズ同じでないとダメ


# 算術演算
# 2つのテンソル行列のかけ算です。 y1, y2, y3 は同じ結果になります。
y1 = tensor @ tensor.T
y2 = tensor.matmul(tensor.T)

y3 = torch.rand_like(tensor) #tensorと同じサイズのテンソルを作成
torch.matmul(tensor, tensor.T, out=y3) #既存のテンソルに結果を格納
print("行列の掛け算の結果")
print(y1)


# こちらは、要素ごとの積を求めます。 z1, z2, z3 は同じ値になります。
z1 = tensor * tensor
z2 = tensor.mul(tensor)

z3 = torch.rand_like(tensor)
torch.mul(tensor, tensor, out=z3)
print("要素ごとの積の結果")
print(z1)


# 1要素のテンソル
agg = tensor.sum()
agg_item = agg.item()
print(agg, type(agg)) # tensor
print(agg_item, type(agg_item))


# インプレース操作
print(tensor, "\n")
tensor.add_(5)
print(tensor)


# NumPyとの変換
# テンソルをNumPy配列に変換
t = torch.ones(5)
print(f"t: {t}")
n = t.numpy()
print(f"n: {n}")

# テンソルが変化すると、Numpy側も変化します。
t.add_(1)
print(f"t: {t}")
print(f"n: {n}")

# NumPy配列をテンソルに変換
n = np.ones(5)
t = torch.from_numpy(n)

# NumPy arrayの変化はテンソル側にも反映されます。
np.add(n, 1, out=n)
print(f"t: {t}")
print(f"n: {n}")

# この場合でも、テンソルの変化はNumPy側に反映されます。
t.add_(1)
print(f"t: {t}")
print(f"n: {n}")