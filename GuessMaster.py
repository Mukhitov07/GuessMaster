import random
easy=1
normal=2
hard=3
while True:
    choice=int(input("Выберите сложность (1-easy, 2-normal, 3-hard):"))
    if choice == 1:
        pc = random.randint(1,10)
        attempts = 5
        while attempts > 0:
            num= int(input('Введите число:'))
            if num == pc:
                print("you win!")
                break
            elif num < pc:
                print("more")
            elif num > pc:
                print("less")
            attempts -= 1
            print(f"Осталось попыток: {attempts}")            
            if attempts == 0:
                print(f"Вы проиграли! Загаданное число было {pc}")       
    elif choice == 2:
        pc = random.randint(1,50)
        attempts = 5
        while attempts > 0:
            num= int(input('Введите число:'))
            if num == pc:
                print("you win!")
                break
            elif num < pc:
                print("more")
            elif num > pc:
                print("less")
            attempts -= 1
            print(f"Осталось попыток: {attempts}")            
        if attempts == 0:
            print(f"Вы проиграли! Загаданное число было {pc}")        
    elif choice == 3:
        pc = random.randint(1,100)
        attempts = 3
        while attempts > 0:
            num= int(input('Введите число:'))
            if num == pc:
                print("you win!")
                break
            elif num < pc:
                print("more")
            elif num > pc:
                print("less")
            attempts -= 1
            print(f"Осталось попыток: {attempts}") 
        if attempts == 0:
            print(f"Вы проиграли! Загаданное число было {pc}")
    again = input("Хотите сыграть еще?:") 
    if again != "да":    
        break
input("Press Enter to exit")