#4-3 Counting to Twenty : 숫자 1~20까지 for loop 이용해서 출력하기

for val in range(1,21):
  print (val)

#4-4 너무 길게 나와서 패스
#4-5 summing a miliion : 1에서 1백만까지 리스트 만들고 min, max 출력해서
#list의 시작과 끝이 똑바른지 확인하고 sum()이용해서 리스트의 모든숫자를 더한 값 출력하기
numbers = list(range(1,1000001))
min_num = min(numbers)
max_num = max(numbers)

print("Minimum: ", min_num, "\nMaximum: ", max_num)

print(sum(numbers)) #와 이거는 신세계다 진짜

#4-6 Odd numbers : range의 3번째 argument 이용해서 1에서 20까지 숫자중
#홀수만 담고 있는 리스트를 만들고 for 루프 이용해서 출력하라

odd_nums = list(range(1,21,2))
for n in odd_nums:
   print(n)

#4-7 Three : Make a list of 3의 배수 from 3 to 30, use for loop

threes = list(range(3,31,3))
for x in threes:
    print(x)


#4-8 Cubes : 1에서 10 숫자의 3의 지수, use for loop to print out
cubesList = []
for i in range(1,11):
    cubesList.append(i**3)

for j in cubesList:
    print(j)

#4-9 Cube Comprehension : use a list comprehension to generate
#a list of the first 10cubes
cubes = [value**3 for value in range(1,11)]

for xy in cubes:
    print(xy)
  
#4-10 Slice : using one of the programs you wrote in this chapter, add several lines to the end of
#the progrma that do the fllowings:


food_list = ["coffee", "soda", "burgers","coke", "noodles"]
print("The first three items in the list are: ", food_list[0:3])
print("Three items from middle of the list are: ", food_list[1:4])
print("The last three items in the list are: ", food_list[-3:])

#4-11 My pizzas, your pizzas
pizzas = ["cheese pizza", "bulgogi pizza", "combination pizza"]
friend_pizzas = pizzas[:] #copy pizzas list
pizzas.append("original pizza")
friend_pizzas.append("hawaiian pizza")

print("My favorite pizzas are :")
for pizza in pizzas:
    print(pizza)

print ("\n")
print("My friend's fav pizzas are")
for pizza in friend_pizzas:
    print(pizza)

#skip 4-12
#4-13
print("The original menu")
buffet_food = ("김밥","잡채","떡볶이","튀김","과일")
for food in buffet_food:
    print(food)

#buffet_food[0] = "짜장면" this is not working. tuple is not allowed to be changed.
#buffet_food.pop() =>AttributeError: 'tuple' object has no attribute 'pop'
print ("\nafter changing the menu")
buffet_food=("pizza","burgers","떡볶이","튀김","과일")
for food in buffet_food:
    print(food)
