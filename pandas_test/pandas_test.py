import pandas as pd

# df1 = pd.DataFrame({
#   'Name': ['Taro', 'Ichiro', 'Jiro'],
#   'Add': ['Tokyo', 'Osaka', 'Tokyo'],
#   'Age': [20, 21, 20]
# })
# print(df1)

# print(' 1:********** ')
# s1 = pd.Series(
#   ['Ken', 'Taro', 'Hanako'],
#   index=[1,2,3]
# )
# print(s1)

print(' 2:********** ')
df = pd.read_excel('pandas_test/data.xlsx')
print(df)

# インデックスとカラム名を指定して取得
print(' 3:********** ')
print(df.loc[[0, 1, 4], ['Name', 'Age']])

# 全インデックスを対象としてNameカラムの値指定
print(' 4:********** ')
print(df.loc[:, ['Name']])

# 範囲で指定
print(' 5:********** ')
print(df.loc[0:3, 'Name':'Age'])

print(' 6:********** ')
print(df.iloc[1:3, 1:3])
print(' 7:********** ')
print(df.iloc[[1,2], [1,3]])

print(' 8:********** ')
print(df['Name'])

# ブールインデックス１
print(' 9:********** ')
print(df[[True, True, False, False, True]])

# ブールインデックス２
print(' 10:********** ')
# 複数条件は()で囲まないとエラーになる
print(df[(df['Address'] == 'Tokyo') | (df['Age'] > 20)])