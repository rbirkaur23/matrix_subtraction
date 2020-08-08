n=int(input("Enter number of rows: "))
m=int(input("Enter number of columns: "))
m1=[]
m2=[]
ans=[]
for i in range(n):
    m1.append([0]*m)
for i in range(n):
    m2.append([0]*m)    
for i in range(n):
    ans.append([0]*m)
print("\nEnter elements for first matrix: ")    
for i in range(n):
    for j  in range(m):
        m1[i][j]=int(input("Enter value at row " +str(i+1)+ " col "+str(j+1)+ ":"))
print("\nEnter elements for second matrix : ")
for i in range(n):
    for j  in range(m):
        m2[i][j]=int(input("Enter value at row " +str(i+1)+ " col "+str(j+1)+ ":"))
for i in range(n):
    for j  in range(m):
        ans[i][j]=m1[i][j]-m2[i][j]
for i in range(n):
        print(m1[i] ,"-" ,m2[i], "=", ans[i])
  
