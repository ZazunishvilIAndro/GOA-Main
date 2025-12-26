                                                      #დავალება 2 

#list ები პითონში არის იგივე კოლექცია, ჩამონათვალი რაშიც ინახება მნიშვნელობები.

# array = ["ana , nata , elene , anano , gabro , gogia , nikusha"]
# for i in array:
#     print(i)


                                                       #დავალება 3

# animals = ["lion", "tiger" , "bear", "wolf", "monkey"]
# animals.remove("lion")
# del animals[1]
# print(animals)


                                                       #დავალება 4

# massive = ["bear", "wolf", "monkey",  "anano" , "gabro" , "gogia" , "nikusha"]
# print(massive[1:5])


                                                        #დავალება 5

real_password = 'Nino1234!'
attemps = 3

user_attempts = 0

while attemps > user_attempts: 
    remaining = attemps - user_attempts
    user_input = input(f'Guess the password again You have {remaining}, Attemp(s) left To Guess the password: ')
    user_attempts += 1

    if user_input == real_password:
        print('Congrats you have guessed the correct password!')
        break
    else:
        print('Wrong please try again later!')
else:
    print('You have reached the maximum number of attempts')
    