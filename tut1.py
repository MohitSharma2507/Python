# i=1
# while i<=5 :
#     print("Mysirji")
#     i+=1

n = int(input("Enter a number : "))
i=2
while i<n:
    if n%i==0:
      break
    i+=1
if i==n:
 print("PRIME")
else:
  print("NOT PRIME")

