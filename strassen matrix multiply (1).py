#define arrays
a = [[1,2],[3,4]]
b = [[4,3],[2,1]]
c = [[0,0],[0,0]]

m1= (a[0][0] + a[1][1]) * (b[0][0] + b[1][1])
m2= (a[1][0] + a[1][1] * b[1][0])
m3=a[0][0] *(b[0][1] - b[1][1])
m4=a[1][1] * (b[1][0] - b[0][0])
m5=(a[0][0] + a[0][1]) * b[1][1]
m6=(a[1][0] - a[0][0]) * (b[0][0] + b[0][1])
m7=(a[0][1] - a[1][1]) * (b[1][0] + b[1][1])

#assign to m values
c[0][0]=m1+m4-m5+m7
c[0][1]=m3+m5
c[1][0]=m2+m4
c[1][1]=m1 - m2+m3+m6
print("matrix values are :",m1,m2,m3,m4,m5,m6,m7)
print("Resulting matrix:")
print(a)
print(b)
print(c)

