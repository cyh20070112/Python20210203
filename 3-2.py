math = []
total = 0
high = 0
low = 100
n = int(input('班上人數?'))
for i in range(n):
    score = int(input('成績'))
    total = total+score
    if high < score:
        high = score
    if low > score:
        low = score
    math.append(score)
average = total / n
print(score)
print('average:',average)    
print('high:',high)
print('low:',low)