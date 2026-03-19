nums = (1,4,9,16,25,35,49,64,81,100)

#? While Loop
# i=0
# while i<len(nums):
#   if(nums[i]==16):
#     print(i)
#   i+=1

#? For Loop

# for ele in nums:
#   print(ele,end=" ")

#!Range()
# range function returns a sequence of numbers,starting from 0 by default,and inreaments by 1(by default), and stops before a specified number  
# range(start?,stop,step?)

n = int(input())
i=1
for i in range(1,11): #range(stop)
  print(n*i)

# for el in range(5,10):#range(start,stop)
#   print(el)

# for el in range(1,10,2):#range(start,stop,step)
#   print(el)
