a='ABCBDABA'
b='BDCABAA'
def LCS(x,y):
    x_len = len(x)
    y_len = len(y)
    c = [[0 for _ in range(y_len+1)]for _ in range(x_len+1)]
    res = ""
    i = 0
    for i in range(x_len):
        for j in range(y_len):
            if x[i] == y[j]:
                c[i][j] = c[i-1][j-1]+1
            else:
                c[i][j] = max(c[i-1][j],c[i][j-1])
    print c[x_len-1][y_len-1]
LCS(a,b)
