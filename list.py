l = ['a','b','c','d','e','f','g','h','i','j','k',]

print(f'配列l の要素数は、{len(l)}')

print(l)
l[0] = 'A'
print(l)

l[4:]='たまごやき'
print(l)

l.append('追加要素1')
print(l)

weekdays = [['Sanday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',],[1,2,3,4,5,6,7]]
print(weekdays)
print(len(weekdays))
print(weekdays[0][2])