from datetime import datetime
print(datetime.now())
print('Student name: Vatslav Zhdanovich')
print('--------------------------------')
print('Prime Time!\n')
prime= False
def isPrime(num):
    amount= num
    if amount > 1:
        for i in range(2,amount):
            if (amount % i) == 0:
                print(amount,'is not prime.')
                break
        else:
            print(amount, 'is prime.')
    else:
        print(amount,'is not prime.')
isPrime(int(input('Enter a number: ')))
















