from unittest import result


X = [[1,2,3],
    [4,5,6],
    [7,8,9]]

Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

res=[[0,0,0],
    [0,0,0],
    [0,0,0]]

# iterate through rows
for i in range(len(X)):
    # iterate throgh columns
    for j in range(len(X[0])):
        res[i][j] = X[i][j] + Y[i][j]

for r in res:
    print(r)