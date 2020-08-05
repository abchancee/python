# 시 분 초 +d초(500,000)

a,b,c = map(int, input().split())
d = int(input())


t = (a*60*60+b*60+c+d)//(60*60)
tb = ((a*60*60+b*60+c+d)%(60*60))//60
tc = ((a*60*60+b*60+c+d)%(60*60))%60

if t>23:
    t = t%24

print('%d %d %d'%(t, tb, tc))






