# https://dgsw.goorm.io/exam/132233/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B81/quiz/2

n=list(map(int,input().split()))
n=set(n) #중복 제거
n=sorted(n)
print(*n) # *를 쓰면 반복이 된다   =   for i in n: print(i,end=' ')