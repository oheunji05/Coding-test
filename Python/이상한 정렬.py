# https://dgsw.goorm.io/exam/132233/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B81/quiz/12 #

def sort1(s):
    #리스트 컴프리헨션
    s1=[a for a in s if a<0] #음수
    s2=[b for b in s if b>=0] #양수
    return s1+s2

li=list(map(int,input().split()))
r=sort1(li)
print(*r)