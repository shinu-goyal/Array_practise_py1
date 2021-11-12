list1=[]
number=int(input("enter list size here"))
print("enter numbers")
for i in range(number):
  data=int(input())
  list1.append(data)

print("sum of the numbers:",sum(list1))
