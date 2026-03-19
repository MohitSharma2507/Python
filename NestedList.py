# list1=[1,2,3,[4,5,6,7,8],9]
# print(len(list1))

# print(list1[3])  #[4,5,6,7,8]
# print(list1[3][2]) #6
# print(list1[3][0:2])

size= (input("Enter the position you want to access : "))
row=int(size[0])
col=int(size[1])

list1=[[1,2,3],[4,5,6],[7,8,9]]
list1[row-1][col-1]="X"

print(list1)

