# ライブラリに親しむ
# 汎用コードをつくる
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

from l36WordFrequancy import RemoveMarkup, SortFrequancy

sys.path.append(os.path.abspath("../S3Normal"))
from l20ReadJson import Read_Json, ExtractJournal_byWord


def PlotFrequancy_doublelog(wordfrequancy:dict, TopNum:int=100, output_file:str="wordfrequancy.png"):
    x = np.arange(TopNum)
    y = np.array(list(wordfrequancy.values())[:TopNum])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(x, y)
    ax.set_xscale('log')
    ax.set_yscale('log')
    # plt.show()
    plt.savefig(output_file)  # 画像ファイルとして保存
    plt.close()  # メモリ解放のためにプロットを閉じる


if __name__ == "__main__":
    Journals = Read_Json("/home/ryoma/nock100/S3Normal/jawiki-country.json.gz")
    # Journals = ExtractJournal_byWord(dict_list, 'イギリス')
    RemoveMarkup(Journals)
    wordfrequancy = SortFrequancy(Journals)
    PlotFrequancy_doublelog(wordfrequancy, 500, 'wordfrequancy500.png')