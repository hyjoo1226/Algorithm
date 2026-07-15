n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
m_l = []
m = 0
m_i = -1
while m_i != 0:
    if m_i == -1:
        for i in range(n):
            if m < a[i]:
                m_i = i
                m = a[i]
        m_l.append(m_i)
        m = 0
    else:
        for i in range(m_i):
            if m < a[i]:
                m_i = i
                m = a[i]
        m_l.append(m_i)
        m = 0

for m in m_l:
    print(m + 1, end = ' ')
