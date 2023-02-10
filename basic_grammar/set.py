print('-- START')
d1 = set('ABBAACCCCCD')
print('d1', d1)

print('-- 存在確認')
print('A', 'A' in d1)
print('K', 'K' in d1)

d2 = set('ADDNNB')
print('d2', d2)

print('-- 差集合')
print(d1 - d2)

print('-- 和集合')
print(d1 | d2)

print('-- 共通')
print(d1 & d2)

print('-- 対称差')
print(d1 ^ d2)

