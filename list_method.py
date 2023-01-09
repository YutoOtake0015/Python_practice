from collections import deque

l = list('18974321167')
print('-- START')
print(l)

print('-- append')
l.append('Z')
print(l)
s = 'XXXX'
l.append(s)
print(l)

print('-- extend')
l2 = list('abcdef')
l.extend(l2)
print(l)
# 文字列を結合→1文字ずつ配列の要素として結合
s1 = 'ABCD'
l.extend(s1)
print(l)

print('-- insert')
l.insert(1, 9999)
print(l)

print('-- remove')
l.remove(9999)
print(l)

print('-- popleft')
l3 = deque(l)
string = l3.popleft()
print(string)

print('-- pop')
string = l.pop()
print(string)

print('-- index')
print(l.index('3'))

print('-- count')
print(l.count('1'))

print('-- sort')
# l.sort()
# print(l.sort())
l.sort()
print(l)

print('-- reverse')
l.reverse()
print(l)

print('-- clear')
l.clear()
print(l)

# print('-- del list')
# del l
# print(l)

print('-- リスト内包表記')
l4 = [x for x in range(5)]
print(l4)

l5 = [x*2 for x in range(10)]
print(l5)

l6 = [x**2 for x in range(10) if x % 2 == 0]
print(l6)
  