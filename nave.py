
#list6 = list(map(lambda x :'0' if x == 0 ('홀수' if x %2 == 1 else '짝수'). range(11)))
#print(list6)

list6 = list(map(lambda x: '0' if x == 0 else ('홀수' if x % 2 == 1 else '짝수'), range(11)))

# 결과 출력
print(list6)
