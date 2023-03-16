import sys
sys.stdin = open('input.txt')

ran_ = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
resu = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

# result = 0 # res * ran / N
N = 0 # 나눠줄 수강 학점
sumV = 0
for i in range(20):
    sub, res, ran = input().split()
    ress = float(res)
    if ran != 'P':
        N += ress
        sumV += ress * resu[ran_.index(ran)]

result = sumV / N
# print(N)
# print(sumV)
print('{: 2f}'.format(round(result, 6)))