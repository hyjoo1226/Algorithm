https://programmers.co.kr/learn/courses/30/lessons/42839
모든 순열조합을 만들어 per에 저장한다. per를 int로 바꾸는 과정을 통해 맨 앞에 0이오는 경우를 없앤다.

리스트를 제곱근보다 작은 숫자까지 순회하며 하나라도 나누어떨어지는 경우 check는 거짓이 된다.
check가 참인 경우만 골라서 개수를 리턴 

```
from itertools import permutations

def solution(numbers):
    answer = []                                   
    nums = [n for n in numbers]                  
    per = []                                      
    for i in range(1, len(numbers)+1):            
        per += list(permutations(nums, i))       
    new_nums = [int(("").join(p)) for p in per]  

    for n in new_nums:                           
        if n < 2:                                 
            continue
        check = True            
        for i in range(2,int(n**0.5) + 1):       
            if n % i == 0:                       
                check = False
                break
        if check:
            answer.append(n)                    

    return len(set(answer))  
```