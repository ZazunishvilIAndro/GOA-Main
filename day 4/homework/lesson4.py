# #ლოგიკური ოპერატორები გამოიყენება ლოგიკური გამოთვლებისთვის, ანუ მაშინ, როცა გვინდა ორი ან მეტი პირობა ერთმანეთს შევადაროთ.
# #ისინი აბრუნებენ მნიშვნელობას True ან False
# #მაგალითად:
# print(15>14)
# print(15>14 and 15<14)
# print(15>14 or 15<14)

# print(True and True or False or True and True and False)
# True and True = True
# True and True = True
# True and False = False
#რადგან პირველი and ოპერატორი სრულდება ეს მოცემული სამი პასუხი ანუ (True;True;False) ჩავსვათ იმის მაგივრად საიდანაც ეს პასუხები მივიღეთ (ზემოთ 3 მაგითის მიხედვით)

# #(True or False or True) ეს არის უკვე ჩასმული მოქმედება 
# True or False = True #ჩავსვათ True or False ის მაგივრად True რადგან True or False უდრის True ს
# #დაგვრჩა (True or True)
# True or True = True


#დავალება 3
# name = input("შემოიტანე შენი სახელი:")
# age = int(input("შემოიტანე შენი ასაკი:"))
# if name == "jonh" and age == 25:
#    print(True)
# else:
#    print(False)


# #დავალება 4
# num = int(input("შემოიტანე მთელი რიცხვი:"))
# num_1 = int(input("შემოიტანე მთელი რიცხვი:"))
# num_2 = int(input("შემოიტანე მთელი რიცხვი:"))

# sum = (num + num_1 + num_2)

# avarage = sum / 3

# print(avarage)


#დავალება 5
#sequensingsequencing არის თანმიმდევრობა ყველაფერი მიდის თანმიმდევრობით selection არის როდესაც საშვალება გაქ რაიმე არჩივნის გაკეთებისთვის
#  iteration არის როდესაც გარკვეული რამ მეორდება რამდენიმეჯერ ან უსასრულოდ
# ჯერ ამზადებ კართოფილს

# შემდეგ ამატებ სუნელებს

# ბოლოს აცხობ ღუმელში

# თუ კარგი ამინდია გახვალ მოკლე მკლავიანით

# თუ ცუდი ამინდია გახვალ გრძელ მკლავიანით


# ცდილობ მაგალითად პაროლის შეყვანას ერთხელ ცდილობ არ გამოდის ორჯერ არა სამჯერ არა იქამდე სანამ სწორ პაროლს არ ჩაწერ


#დავალება 6
#for ციკლი გამოიყენება კოლექციის ან რაიმე დიაპაზონის ელემენტებზე იტერაციისთვის.3 არგუმენტისგან შედგება (start; stop; step)


#დავალება 7
#for loop მუშაობს კოლექციებზე ან range()-ზე while loop კიდე პირობაზე. for loopში წინასწარ გვაქ განსაზღვრული რაოდენობის ინტერაცია while loopში კიდე განუსაზღვრელი სანამ პირობა დაკმაყოფილებულია.
#while loop არის ისეთი მოქმედება, რომელიც მეორდება მანამდე, სანამ რაღაც პირობა მართალია.


#დავალება 8 
# num = int(input("შემოიტანე რაიმე რიცხვი:")) 
# factorial = 1
# while num > 0:
#     factorial *= num 
#     num -= 1 
# print(factorial)


#დავალება 9 
# score = int(input("შემოიტანე ქულა:"))
# if score >= 90:
#      print("A")
# elif score >= 80:
#      print("B")
# elif score >= 70:
#      print("C")
# else:
#      print("F")


#დავალება 10 
# num = int(input("შემოიტანე რაიმე მთელი რიცხვი:"))
# num_1 = int(input("შემოიტანე რაიმე მთელი რიცხვი:"))
# num_2 = int(input("შემოიტანე რაიმე მთელი რიცხვი:"))
# if num > num_1 and num > num_2:
#     print(num)
# elif num_1 > num and num_1 > num_2:
#     print(num_1)
# else:
#     print(num_2)


#დავალება 11
# for i in range(10+1):
#     print(i)


#დავალება 12

# total_sum = 0

# for i in range(1,20+1):
#     total_sum += i
#     print(total_sum)


#დავალება 13
#name = "andro"
#for i in name:
#   print(i)
