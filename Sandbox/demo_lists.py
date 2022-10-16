
shopping_list = []
shopping_list.append('bread')
shopping_list.append('butter')
shopping_list.extend(['apples', 'kiwis'])
shopping_list.insert(0, 'beer')
shopping_list.append(99)
shopping_list.pop()
shopping_list.remove('beer')

print(shopping_list)

shopping_list.sort()

print(shopping_list)

print(len(shopping_list))

#-----------------------------------------------

numbers = [1.0, 5.3, 3, 4, 7, 2]

for number in numbers:
    print(number)

print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print(numbers[0])

numbers.append([1, 3])
print(numbers)


squared = []
for n in numbers:
    squared.append(n ** 2)


squared = [n ** 2 for n in numbers]



print(squared)
