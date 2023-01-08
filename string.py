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
string[0] = 'A'
