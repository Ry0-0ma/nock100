# Automatic differentiation with torch.autograd

# 学習アルゴリズム: backpropagation
# モデルの重みなどの各パラメータは、損失関数に対するその変数の微分値（勾配）に応じて調整
# 勾配の値を計算するために、PyTorchにはtorch.autograd という微分エンジン

import torch

x = torch.ones(5)  # input tensor
y = torch.zeros(3)  # expected output
w = torch.randn(5, 3, requires_grad=True)
b = torch.randn(3, requires_grad=True)
z = torch.matmul(x, w)+b #x*w+b
loss = torch.nn.functional.binary_cross_entropy_with_logits(z, y)

#w, b を最適にする-> 微分を可能にするために、requires_grad属性をこれらのテンソルに追記
#requires_gradはテンソルを定義する際、もしくはその後に、x.requires_grad_(True)を実行するなどして指定

# 勾配は、テンソルの grad_fn プロパティに格納
print('Gradient function for z =',z.grad_fn)
print('Gradient function for loss =', loss.grad_fn)

# 勾配の計算
# 偏微分値を求めるためにloss.backward()を実行し、w.gradとb.gradの値を導出
loss.backward()
print(w.grad)
print(b.grad)

# gradは計算グラフのleaf node（かつ、requires_gradがTrueの変数）のみで求める
# 勾配の計算は各計算グラフに対して、backwardを実行し、1度だけ計算できます


# 勾配計算をしない方法
# 勾配計算が不要なケース:例えば訓練済みモデルで推論するケースなど
# すなわち、ネットワークの順伝搬関数のみを使用する場合
# 実装コードで勾配計算を不要にするには、torch.no_grad()のブロックにそれらのコードを記載

z = torch.matmul(x, w)+b
print(z.requires_grad) # True

with torch.no_grad(): # 勾配計算をしない
    z = torch.matmul(x, w)+b
print(z.requires_grad) # False


z = torch.matmul(x, w)+b
z_det = z.detach() #detach() によりテンソルに勾配計算をしないようにする
print(z_det.requires_grad) # False

# 勾配の計算、追跡を不能にしたいケース
    # ネットワークの一部のパラメータを固定したい（frozen parameters）ケース
    # 順伝搬の計算スピードを高速化したいケース。


# 計算グラフについて補足
# autogradはテンソルとそれらに対する演算処理をFunctionを構成単位として、DAG（a directed acyclic graph）の形で保存したグラフ

# 各leafは入力テンソル、そしてrootは出力テンソル
# rootから各leafまでchain rule（微分の連鎖律）で追跡することによって各変数に対する偏微分の値を求める

# 順伝搬では autograd は2つの処理を同時に行っています。
    # 指定された演算を実行し、計算結果のテンソルを求める
    # DAGの各操作のgradient function を更新する

# 逆伝搬では、.backward()がDAGのrootのテンソルに対して実行されると、autogradは、
    # 各変数の .grad_fnを計算する
    # 各変数の.grad属性に微分値を代入する
    # 微分の連鎖律を使用して、各leafのテンソルの微分値を求める

# PyTorchではDAGは動的
# PyTorchは Define-by-run 形式であり、事前に計算グラフを定義するのではなく、計算を実行する際に、柔軟に計算グラフを作ってくれます。
# 一方で、Define-and-run形式のディープラーニングフレームワークは、事前に計算グラフを定義する必要があるため、for文やif文といった制御フローの構文を柔軟に使いづらい


# 補注：テンソルに対する勾配とヤコビ行列
# 多くの場合、スカラー値を出力する損失関数に対して、とある変数の勾配を計算
# 関数の出力がスカラー値ではなく、任意のテンソルであるケースもある
    # このような場合、PyTorchでは実際の勾配ではなく、いわゆるヤコビ行列（Jacobian matrix）を計算

inp = torch.eye(5, requires_grad=True) #5×5の単位行列（対角成分が1、それ以外が0）を作成し、勾配計算を有効
out = (inp+1).pow(2) #各要素に1を足して2乗
out.backward(torch.ones_like(inp), retain_graph=True) #1度目の勾配計算
print("First call\n", inp.grad)
out.backward(torch.ones_like(inp), retain_graph=True) #2度目の勾配計算(勾配累積)
print("\nSecond call\n", inp.grad)
inp.grad.zero_() #勾配をゼロにする
out.backward(torch.ones_like(inp), retain_graph=True)
print("\nCall after zeroing gradients\n", inp.grad)

# 計算グラフの全leafのgradには、勾配が足し算されます。
# 適切に勾配を計算するには、gradを事前に0にリセットする必要があります。
# なお実際にPyTorchでディープラーニングモデルの訓練を行う際には、オプティマイザー（optimizer）が、勾配をリセットする役割を担ってくれます。


"""
Gradient function for z = <AddBackward0 object at 0x7f66f093a110>
Gradient function for loss = <BinaryCrossEntropyWithLogitsBackward0 object at 0x7f66f093a110>
tensor([[0.0792, 0.0938, 0.0927],
        [0.0792, 0.0938, 0.0927],
        [0.0792, 0.0938, 0.0927],
        [0.0792, 0.0938, 0.0927],
        [0.0792, 0.0938, 0.0927]])
tensor([0.0792, 0.0938, 0.0927])
True
False
False
First call
 tensor([[4., 2., 2., 2., 2.],
        [2., 4., 2., 2., 2.],
        [2., 2., 4., 2., 2.],
        [2., 2., 2., 4., 2.],
        [2., 2., 2., 2., 4.]])

Second call
 tensor([[8., 4., 4., 4., 4.],
        [4., 8., 4., 4., 4.],
        [4., 4., 8., 4., 4.],
        [4., 4., 4., 8., 4.],
        [4., 4., 4., 4., 8.]])

Call after zeroing gradients
 tensor([[4., 2., 2., 2., 2.],
        [2., 4., 2., 2., 2.],
        [2., 2., 4., 2., 2.],
        [2., 2., 2., 4., 2.],
        [2., 2., 2., 2., 4.]])
"""