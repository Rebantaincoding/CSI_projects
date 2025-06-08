#Rebanta Sarkar
#Celebal user_id:CT_CSI_DS_4841 
#Program to print Lower triangle,Upper Triangle and Pyramid 
print("\n Enter size of triangle \n")
n=int(input())
print("\nLower Triangle:\n")
for i in range (0,n):
    for j in range(0,i+1):
        print('*',end='')
    print() 
print("\nUpper triangle:\n")
for i in range(0,n):
    for j in range(0,i+1):
        print(' ',end='') 
    for k in range(n-i,0,-1):
        print('*',end='') 
    print()
print("\nPyramid:\n")
for i in range(0,n):
    for j in range(n-i,0,-1):
        print(' ',end='')
    for k in range(0,i+1):
        print('* ',end='')
    print()
