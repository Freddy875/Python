X = 'abcd'
for i in range(len(X)):
    print(i)
    
x = 2 
for i in range(x):
    for j in range(x):
        a = x - j  + 1
        print(a)

f = 1 
A = [[1,2,3],[2,3,4],[3,4,5]]
for i in range(0,3):
    f = f * i 
    for j in range(0,3):
        A[i][j] = f
print(A)
