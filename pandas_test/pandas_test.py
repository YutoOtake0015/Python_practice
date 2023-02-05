import pandas as pd

df1 = pd.DataFrame({
  'Name': ['Taro', 'Ichiro', 'Jiro'],
  'Add': ['Tokyo', 'Osaka', 'Tokyo'],
  'Age': [20, 21, 20]
})
print(df1)

print(' ********** ')
s1 = pd.Series(
  ['Ken', 'Taro', 'Hanako'],
  index=[1,2,3]
)
print(s1)

print(' ********** ')
df = pd.read_excel('pandas_test/data.xlsx')
print(df)