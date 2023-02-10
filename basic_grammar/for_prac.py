for i in range(10):
  print(i)

l = ['zero','one','two','three','four','five','six','seven','eight','nine','ten',]
for i in l:
  print(i)

print(len(l))
for i in range(len(l)):
  print(i)

l = [1,2,3,4,5,6,7,8,9]

print('break check...')
for i in l:
  if i > 5:
    print(i, "中断")
    break
  print(i, '継続')

else:
  print('完了')

print('continue check...')
for i in l:
  if i < 5:
    print(i, 'スキップ')
    continue
  print(i, '継続')
else:
  print('完了')