# 시간 합산
# A시 B분
# C분
# A = [0 ~ 23], B = [0~59], C=[0~1000]

# a,b = map(int, input().split())
# c = int(input())
#
# c_clock = c//60
# c_min = c % 60
#
# ai = a+c_clock
# bi = b+c_min
# if bi > 59:
#     m = bi//60
#     ai = ai+m
#     bi = bi%60
# if ai > 23:
#     ai = ai%24
#
# print('%d %d' %(ai, bi))

a,b = map(int, input().split())
c = int(input())
t = (a*60+b+c)//60
tt = (a*60+b+c)%60
if t>23:
    t = t%24
print('%d %d'%(t, tt))

