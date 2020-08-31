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