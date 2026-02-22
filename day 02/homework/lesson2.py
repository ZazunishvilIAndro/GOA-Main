#level 2 დავალება 2)
# Debugging — არის კოდის გამართვის პროცესი, როდესაც პროგრამისტი პოულობს და 
# ასწორებს შეცდომებს, რომ პროგრამამ სწორად იმუშაოს.


#დავალება 3 და ასევე 4 ერთად)
float= 6.1
int = 9
print (int+float)
print (int-float)
print (int*float)
print (int/float)


#დავალება 5)
age = "25"
print (age + 5)
# რიცხვით მნიშვნელობას არ ჩირდება პრჭყალები თორე რიცხვითი მნიშვნელობა ანუ 
# integer გადაკეთდება string-ად და integers ვერ დავუმათებთ strings

#სწორია:
age = 25
print (age + 5)


#დავალება 6)
name = "ანდრო"
lastname = "ზაზუნიშვილი"
age = 16
height = 1.80
country = "საქართველო"
print ("მე მქვია" " " + name + " " + lastname + " " "ვარ"" "+ str(age) + " " + "წლის" + " " + "ჩემი ქვეყანაა" + " " + country +" " "და ვარ"" " + str(height) + " " + "სიმაღლეში")


#დავალება 7)
total = 100
print(total)
#მოცემული კოდი გამოიტანს 100ს. ცვლადი შევქმენით მივანიჭეთ მნიშვნელობა და printis საშვალებით გამოვა ეკრანზე 100


#დავალება 8)
total = 120
people = 4
print(total/people)
#თითოეული ადამიანი იხდის 30ს


#დავალება 9)
price = 80
discount = 0.5
final_price = (price-(price*discount))
print(final_price)
#საბოლოო ფასია 40


#დავალება 10)
num = 6
if num % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")