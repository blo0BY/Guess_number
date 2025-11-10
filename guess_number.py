from random import randint


number = randint(0, 100)
print("Угадай от 1 до 100")

while True:
    guess = int(input("введите число: "))
    
    if guess < number:
        print("Число больше")
    
    if guess > number:
        print("Число меньше")

    if guess == number:
        print("Кгадал! Число", number)
        break

print("число угадано!")