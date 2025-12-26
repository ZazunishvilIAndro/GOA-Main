                                      #დავალება 2 


# password = 12345678

# attempt = 0
# while attempt < 3:
#     user_password = int(input("enter password:"))
#     attempt+=1
#     if user_password == password:
#         print("correct")
#         break
#     else:
#         print("incorrect")
#         if attempt == 3:
#           print("You have reached the maximum number of attempts")



                                      #დავალება 3

#print(True and False and 5 > 9 and 90 * 30 > 1089 or False and 'Nino' != '' or False or True and 56 * 2 > 90)
#ეს კოდი გამოიტანს trues რადგან ბოლოში რჩება true or false რომელიც არის true 



                                      #დავალება 4

#მასივი არის ელემენტებისგან შემდგარი ერთობლიობა რაზეც ზემოქმედება შესაძლებელია, ასევე შეგიძლია მასში ნებისმიერი ტიპის შენახვა
#მაგალითი:
# array = ["nika", 'mary', 1, 2 ,3, 4, "me"]
# x = array[-4]
# array[-4] = 8
# print(array)


                                       #დავალება 5

# family_names = ["tiko", "vaso", "sandro", "demetre", "nana", "andro"]
# for i in family_names:
#     print(i)


                     
                                       #დავალება 6 

# array = [ 1, 2, 3, 6, 87, 234, 7547, 11, 32, 65, 456, 23,]
# total = sum(array)
# print(total)



                                       #დავალება 7 

#indexing არის ის რითიც შეგიძლია წვდომა მოიპოვო
#მასივზე ამოიღო მასივიდან რაიმე ელემენტი, ჩასვა, ჩაანაცვლო და ასე შემდეგ
#string ზე შესაძლებელია Indexing გამოყენება მაგრამ არ შეგიძლია  string ში არსებულ
#სიტყვაზე იმოქმედო ისე როგორც მასივზე string ზე შეგიძლია indexing ის საშვალებით 
#ეკრანზე გამოიტანე  შენთვის სასურველ index ზე მდგომი ელემენტი, ასო.



                                       #დავალება 8

#indexing იმიტომ არის კარგი პრაქტიკა რომ წვდომა გაქვს მაგალითად მასივზე
#შეგიძლია მართივად დაითვალო რამდენი ელემენტია შენს მასივში,
#და შეგიძლია კიდე სხვა კარგი მოქმედებებიც (ჩანაცვლება, ამოღება, გამოტანა ეკრანზე)


                                       #დავალება 9

# array = ["ggg", "hhh", "aaa", "ppp", "ttt"]
# x = array[2]
# array[0] = "giorgi"
# array[1] = "nika"
# array[2] = "anano"
# array[3] = "elene"
# array[4] = "salome"
# print(array)

# array_1 = ["ggg", "hhh", "aaa", "ppp", "ttt"]
# array_1.append("naira")
# print(array_1)

# array_2 = ["ggg", "hhh", "aaa", "ppp", "ttt"]
# array_2.reverse()
# print(array_2)

# array_3 = ["ggg", "hhh", "aaa", "ppp", "ttt"]
# array_3.extend("mary")
# print(array_3)

# array_4 = ["ggg", "hhh", "aaa", "ppp", "ttt"]
# array_4.remove("ggg")
# print(array_4)

                                         #დავალება 10

# fruits = ["apple", "ananas", "mandarini", "msxali", "banana"]
# x = fruits[::2]
# print(x)

                                          #დავალება 11

fruits = ["apple", "banana", "cherry"]
array_4 = ["ggg", "hhh", "aaa", "ppp", "ttt"]
for i in fruits, array_4:
    print(i)