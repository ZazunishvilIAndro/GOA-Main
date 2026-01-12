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

# real_password = 'Nino1234!'       #შევქმენით ცვლადი სადაც წერია რეალური პაროლი
# attemps = 3              #3 ცდა აქვს მომხმარებელს

# user_attempts = 0        #ჯერ არ აქვს შემოტანილი პაროლი ამიტომ 0 იქნება attempts

# while attemps > user_attempts:         #სანამ 3 მეტია 0 ზე 
#     remaining = attemps - user_attempts       #ჯამში მცდელობის საშვალებას უნდა გამოვაკლოთ მომხმარებლის ცდების რაოდენობა რადგან მცდელობების რაოდენობა შემცირდეს ულიმიტოდ როარ გაგრძელდეს.
#     user_input = input(f'Guess the password again You have {remaining}, Attemp(s) left To Guess the password: ')              #მომხმარებელს შემოვატანინოთ პაროლი პირველ მცდელობისას ექნება 3 ცდა 1 ცდის მერე 2 და ეგრე
#     user_attempts += 1      #დაემატება 1 მომხმარებლის მცდელობებს სანამ 3 არ გახდება 

#     if user_input == real_password:          #თუ მომხმარებლის პაროლი ემთხვევა პაროლს მაშინ გამოიცნო პაროლი
#         print('Congrats you have guessed the correct password!')
#         break       #break რო არ იყოს სწორი პაროლის ჩაწერის შემთვევაში კოდი კიდე გაგრძელდებოდა და რო არის თუ გამოიცნო მომხმარებელმა გამოიტანს მილოცვას და დამტავრდება კოდი
#     else:           #სხვა შემთხვევაში გამოიტანს რო არასწორია
#         print('Wrong please try again later!')
# else:
#     print('You have reached the maximum number of attempts')       #თუ ამოიწურა მცდელობის რაოდენობა ამას გამოიტანს  Wrong please try again later! ამასთან ერთად
    

                                                        #დავალება 6 

#ფუნქცია არის მოქმედების შესასრულებელი რამ ფუნქცია თუარ ექნება რაიმეს მოქმედებაც არ შესრულდება ფუნქცია რეალურ ცხოვრებაში რო წარმოვიდგინოთ
#მაგალითად ჩვენ რო არ გვქონდეს ფუნქცია ვერ ვიმოძრავებდით ვერ შევასწულებდით მოქმდებას ყველაფერი რაც მოქმედებს აქვს თავისი ფუნქციონალი
#python ში ფუნქციის გამოყენება ძაან პრაქტიკულია შეგვიძლია შევქმნათ ფუნქცია და გამოვიძახოთ კოდი რამდენჯერაც გვინდა და მივანიჭოთ სხვა და სხვა
#არგუნემტები პარამეტრებს ახლიდან კოდის წერის ნაცვლად.


                                                        #დავალება 7

# array  = [ 6, 3 , 8 , 90 , 54 , 3 , 6 , 8 , 34 , 6 , 8 , 34 , 1 , 457 , 0 ]
# x = array[ 6 : 8 ]
# print(x)

                                                        #დავალება 8

# masive = []
# for i in range(5):
#     text = input("Enter text:")
#     masive.append(text)
#     print(masive)


                                                        #დავალება 9 

# array = ["ana" , "nata" , "elene" , "anano" , "gabro" , "gogia" , "nikusha"]

# array.append("nene")  #ბოლოში ჩამატება
# print(array)

# array.insert( 1  , "andro") #ჩამატება იმ ინდექსზე რომელზეც გვინდა
# print(array)

# array.pop(3)  #ამოღება იმ ელემენტის რომელიც გვინდა ამ შემთხვევაში მესამე ინდექსზე მდგომი მეოთხე ელემენტი
# print(array)

# array.reverse() #შემოტრიალდება ლისტი
# print(array)

# array.remove("ana")  #იმ ელემენტის ამოღება რომელიც არ გვინდა სტრინგით
# print(array)


                                                        #დავალება 10

#შეგვიძლია
# array = [10, 3.14, "Hello", True and False, [1, 2, 3]]
# print(array)