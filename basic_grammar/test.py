import sys
# import test2

# print('test')
# print('test2')

print(sys.path)
sys.path.append("sub/")
print(sys.path)

import test2

print(test2.add5(10))