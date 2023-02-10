# パターン1
print('パターン1')
a = 0
b = 1

while a < 10:
  print(a, end=' ')
  c = a + b
  a = b
  b = c

# パターン2
print()
print('パターン2')
a = 0
b = 1

while a < 10:
  print(a, end=' ')

  a, b = b, a+b
