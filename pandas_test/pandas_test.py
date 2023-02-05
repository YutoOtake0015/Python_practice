import pandas as pd

df1 = pd.DataFrame({
  'Name': ['Taro', 'Ichiro', 'Jiro'],
  'Add': ['Tokyo', 'Osaka', 'Tokyo'],
  'Age': [20, 21, 20]
})
print(df1)

df = pd.read_excel('pandas_test/data.xlsx')
print(df)