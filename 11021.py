# 총 개수
# a b 입력

# n = int(input())
# a = []
# b = []
# for i in range(n):
#     aa,bb = map(int, input().split())
#     a.append(aa)
#     b.append(bb)
#     print('Case #%d: %d' % (i+1, int(a[i]) + int(b[i])))

# n = int(input())
# for i in range(n):
#     a,b = map(int, input().split())
#     print('Case #%d: %d'%(i+1,a+b))

import sys
n = int(input())
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    print('Case #%d: %d' %(i+1, a+b))

