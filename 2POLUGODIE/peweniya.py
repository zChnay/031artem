#5 ЗАДАЧА 
for N in range(516):
  b=f'{N:b}'
  if N % 2 == 0:
    b += '10'
  else:
    b = '1' + b + '10'
  if int(b,2) > 516:
    print(N)
    break
    
    
#8 ЗАДАЧА
print(int('...',5)+1)
