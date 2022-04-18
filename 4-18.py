

# salesList = ['삼각김밥','바나나','도시락','삼각김밥','삼각김밥','도시락','삼각김밥']
# print(set(salesList))
# print(type(salesList))

# numList = []
# for num in range(1,6):
#     numList.append(num)
# print(numList)

# numList = [num for num in range(1,6)]
# print(numList)

# foods = ['떡볶이','짜장면','라면','피자','맥주','치킨','삼겹살']
# sides = ['오뎅','단무지','김치']
# for food, side in zip(foods,sides):
#     print(food,'-->',side)

# a = ['one','two','three']
# b = ['a','b','c']
# for val1, val2 in zip(a,b):
#     print(val1,val2)

# A = ['name','age','phone','gender']
# B = ['CHAN', 28, '010-XXXX-YYYY','male']
# d = dict(zip(A,B))
# print(d)

a = ['a','b','c','d','e']
b = [1,2,3]

for s in zip(a,b):
    print(s)
    print(list(s))