# 세 자리 수
a = int(input())
b = str(input())
print(a*int(b[2]), a*int(b[1]), a*int(b[0]), a*int(b[2])+a*int(b[1])*10+a*int(b[0])*100, sep='\n')
