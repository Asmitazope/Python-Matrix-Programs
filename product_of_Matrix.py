A = [[1,2],
    [3,4]]

B = [[5,6],
    [7,8]]

C = [[0,0],
    [0,0]]

# iterate by row of A
for i in range(len(A)):

    # iterate by column in B
    for j in range(len(B[0])):

        # iterate by rows of B
        for k in range(len(B)):

            C[i][j] = A[i][k] * B[k][j]

for r in C:
    print(C)