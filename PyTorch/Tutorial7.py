import torch
import torch.onnx as onnx
import torchvision.models as models

# 学習したパラメータを内部に状態辞書（state_dict）として保持
# パラメータの値は torch.save を使用することで、永続化
# model = models.vgg16(pretrained=True) #Error: バージョンエラーの警告が生じた
model = models.vgg16(weights=models.VGG16_Weights.DEFAULT)
torch.save(model.state_dict(), 'Tuto7_model_weights.pth')

# モデルの重みを読み込み
model = models.vgg16() # pretrained=Trueを引数に入れていないので、デフォルトのランダムな値になっています
model.load_state_dict(torch.load('Tuto7_model_weights.pth'))
model.eval() #評価モード, これを忘れると、推論結果が正確ではなくなります。

# モデルクラスの構造も一緒に保存したい場合もあるかと思います。
# その際は保存時に、model.state_dict()ではなくmodelを渡します。
torch.save(model, 'Tuto7_model.pth')
model = torch.load('Tuto7_model.pth') #モデルの読み込み
model.eval()

# モデルのモジュールに独自クラスを定義して使用している場合、torch.loadを実行する前に、その独自クラスをimportするか宣言するかして、使用可能な状態にしておく必要がある

# ONNX形式でのモデル出力
# ONNXモデルを使用することで、異なるプラットフォームや異なるプログラミング言語でディープラーニングモデルの推論を実行させるなど、様々なことが可能です。
# https://github.com/onnx/tutorials

input_image = torch.zeros((1,3,224,224))
onnx.export(model, input_image, 'Tuto7_model.onnx')

