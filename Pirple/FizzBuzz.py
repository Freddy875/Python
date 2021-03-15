number = 0

print("Loop BuzzFizz")

for number in range(101):
    if number%3 == 0 and number%5 == 0:
        print('FizzBuzz')
    elif number%3 == 0:
        print('Fizz')
    elif number%5 == 0:
        print('Buzz')
    else:
        print(number)

#prime
print("\nLoop Prime")

number = 101

for n in range(2,number):
    x = 2
    flag = True

    while flag and x < n:

        if n % x == 0:
            flag = False
        else:
            x += 1
    if flag:
        print('prime')
    else:
        print(n)


