string = 'abcdefghijklmn'

print(len(string))

print(string[1:])

# 文字数を超える数を後ろのインデックスに指定→文字列全てを返す
print(string[:100])

# 文字列を超える数を始めのインデックスに指定→文字列を何も返さない
print(string[100:])

# 文字列にないインデックスを指定→IndexError
# print(string[100])

# 文字列を部分的に書き換え→TypeError
# string[0] = 'A'

print()
string = 'a'
print(ord(string))
print(chr(100))

string = 'GHDAKTSB'
for s in string:
  print(s, end='')

print()
string2 = ''
for s in sorted(string):
  string2 += s
print(string2)

for s1, s2 in zip(string, string2):
  print(s1, s2)

for s3 in zip(string, string2):
  print(s3)

