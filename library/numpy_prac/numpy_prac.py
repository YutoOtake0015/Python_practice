import numpy as np

l1 = [1, 20, 34]
l2 = [9, 13, 23]

# ndarray配列作成
print('array')
x = np.array(l1)
y = np.array([l1, l2])
print(x)
print(y)

# 次元
print('ndim')
print(x.ndim)
print(y.ndim)

# 要素数
print('shape')
print(x.shape)
print(y.shape)

# 要素0配列
print('zeros')
z1 = np.zeros(3)
z2 = np.zeros((2, 3))
print(z1)
print(z2)

# 要素1配列
print('ones')
o1 = np.ones(3)
o2 = np.ones((2, 3))
print(o1)
print(o2)

# 要素ランダム配列
print('random.rand')
r1 = np.random.rand(3)
r2 = np.random.rand(2, 3)
print(r1)
print(r2)

# 要素をメモリ上から取得した配列
# 高速に配列を作成可能
print('empty')
e1 = np.empty(3)
e2 = np.empty((2, 3))
print(e1)
print(e2)
