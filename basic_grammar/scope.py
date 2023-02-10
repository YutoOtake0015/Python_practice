print('-- START')
print(globals())

string='aiueo'
def sample(n):
  loc = '関数内'
  print(f'入力した値は{n}')
  
  print()
  print('-- LOCAL')
  print(locals())

sample(10)

print()
print('-- GLOBAL')
print(globals())

print()
print('-- BUILTIN')
print(dir(__builtins__))


