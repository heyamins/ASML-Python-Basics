# Exercise 5.6 from Crash Course for Python

age = int(input('What age? : '))

if age < 2:
    print('A baby')

elif 2 <= age < 4:
    print('A toddler')

elif 3 <= age < 13:
    print('A kid')

elif age >= 13 and age < 20:
    print('A teenager')

elif 20 <= age < 65:
    print('An adult')

else:
    print('An elder')








lijst = [{'bounds': [0, 2], 'stage': 'A baby'},
         {'bounds': [2, 4], 'stage': 'A toddler'},
         {'bounds': [4, 12], 'stage': 'A kid'},
         {'bounds': [13, 20], 'stage': 'A teenager'},
         {'bounds': [21, 65], 'stage': 'An adult'},
         {'bounds': [65, 110], 'stage': 'An elder'}]

for d in lijst:
   lower, upper = d['bounds']
   if lower <= age < upper:
       print(d['stage'])
       break







d = {'A baby': [0, 2],
     'A toddler': [2, 4],
     'A kid': [4, 12],
     'A teenager': [13, 20],
     'An adult': [21, 65],
     'An elder': [65, 110]}

for k, v in d.items():
    lower, upper = v
    if lower <= age < upper:
        print(k)
        break
