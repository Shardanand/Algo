def printJobScheduling(arr,t):
    n=len(arr)
    for i in range(n):
          for j in range(n-1-i):
               if arr[j][2] < arr[j+1][2]:
                     arr[j], arr[j+i] = arr[j+1],arr[j]
    result = [False] * t
    job = ["-1"] * t
    for i in range (len(arr)):
              for j in range (min(t-1,arr[i][1] - 1),-1,-1):
                   if result[j] is False:
                       result[j] = True
                       job[j]= arr[i][0]
                       break
    print(job)
arr = [["a", 2 ,150],
       ["b",1,196],
       ["c",2,267],
       ["d",1,265],
       ["e",3,156]]
print("Following is the maximum profit sequence of jobs")
printJobScheduling(arr,4)
