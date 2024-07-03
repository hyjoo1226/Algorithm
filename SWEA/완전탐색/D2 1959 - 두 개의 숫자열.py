T = int(input())
#for i in T:
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
if N > M:
    N, M = M, N
    A, B = B, A
 
sum = 0
for i in range(M - N + 1):
    j = 0
    temp = 0
    for j in range(M - N + 1):
        temp += A[j] * B[i]
        i = i + 1
    print(temp)
    if temp > sum:
        sum = temp
#print(sum)
         
         
    #print("#t ", answer)