import pandas as pd
import numpy as np

d0 = ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']
d1 = np.random.rand(9)
d_t = np.array([d0, d1]).T
df = pd.DataFrame(d_t, columns=['lot', 'col_1'])
df.set_index('lot', inplace=True)
print(df)
#iiiprint(df)print(df)print(df)print(df)print(df)
# 2233
# test
# test3
