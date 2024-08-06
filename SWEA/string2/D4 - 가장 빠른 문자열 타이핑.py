T = int(input())
 
for tc in range(1 , T + 1):
    A, B = input().split()
 
    i = 0   #A문자열 길이만큼 순회
    typing = 0  #타이핑의 합
    while i < len(A):
        if len(B) > len(A) - i: #B가 A의 남은 부분보다 긴 경우
            typing += (len(A) - i)
            break

        if A[i] == B[0]:    #두 문자열의 첫 문자가 같으면 체크
            check = 0
            for j in range(len(B)): #다른 문자가 있으면 check = 1, 브레이크
                if i + j >= len(A) or A[i + j] != B[j]:
                    check = 1
                    break
            if check == 1:
                i += 1
            else:
                i += len(B)
        else:
            i += 1
        typing += 1
 
    print(f'#{tc} {typing}')