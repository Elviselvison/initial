#print("HELLO")

el = [1, 2, 3, 4] 
k =el.index(3)
print(k)
print(type(el))
list1 =  [10,20,30,40,50,60,70]
type(list1)
# slicing estrarre gli element della lista 
print(list1[0])
print(list1[0:3])
print(list1[:5])
print(list1[5:])
print(list1[::-1])
list1[0] = 15
print(list1[:])
print(list1[2:])
# mdifica elementi della lista 
list1.remove(70)
print(list1)
list1.append(150)
print(list1)
list1.append("gatto")
print(list1)
animal = list1.pop(-1)
print(animal)
animal.insert



