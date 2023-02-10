# l = ['a','b','c','d','e','f','g','h','i','j','k']

# print(f'配列l の要素数は、{len(l)}')

# print(l)
# l[0] = 'A'
# print(l)

# l[4:]='たまごやき'
# print(l)

# l.append('追加要素1')
# print(l)

# weekdays = [['Sanday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',],[1,2,3,4,5,6,7]]
# print(weekdays)
# print(len(weekdays))
# print(weekdays[0][2])

l2 = ['a','b','c','d','e','f','g','h','i','j','k']
print(l2)

# # 指定インデックスの要素を変更
# l2[0] = 'A'
# print(l2)

# # スライスで指定したインデックス位置に要素を追加
# l2[0:0] = 'B'
# print(l2)
# # スライスインデックス数＜要素のインデックス数で代入→配列の足りない分の要素は無視して値を代入
# l2[0:3] = 'Z'
# print(l2)
# # スライスインデックス数＜要素のインデックス数で代入→要素のインデックス-1の値を配列に代入
# l2[0:1] = 'XXXXXXXX'

# l2[-2] = 'C'
# print(l2)

l2[-2:-2] = 'D'
print(l2)

l2 = ['a','b','c','d','e','f','g','h','i','j','k']
l2[-2:-3] = 'D'
print(l2)

# l2[-2:-1] = 'G'
# print(l2)