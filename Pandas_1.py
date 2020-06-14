import pandas as pd
import numpy as np

# データフレームの作成
d0 = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']
d1 = np.random.rand(9)
d_t = np.array([d0, d1]).T

df = pd.DataFrame(d_t, columns=['lot', 'col_1'])
df.set_index('lot', inplace=True)
print("データフレーム df = \n{}".format(df))

# ファイルの読み込み
#df = pd.read_csv('test.csv',encoding='cp932')



df.info()  #「有効データ数」「データ型」「メモリ使用量」などの総合的な情報を表示
df.shape  #縦横の形を調べる
df.count()  #各カラムの有効データ数を表示
df.dtypes  #各カラムのデータ型を表示
len(df) - df.count()  #すべてのカラムに対して、欠損値の数を計算
