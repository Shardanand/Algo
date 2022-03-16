def knapSack(W,wt,val,n):
    if n==0 or W==0:
        return 0
    if (wt[n-1]>W):
        return knapSack(W,wt,val,n-1)
    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1],wt,val,n-1),
            knapSack(W,wt,val,n-1))
val=[606,1400,120,150,30]
wt=[10,20,30,4,2]
W=100.90
n=len(val)
print (knapSack (W,wt,val,n))

