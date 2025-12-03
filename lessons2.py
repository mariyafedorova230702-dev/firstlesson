# #1
# ocenka = int(input('vvedy svou ocenku ot 0 do 100: '))

# if 90 <= ocenka <= 100:
#     print('ocenka A')
# elif 80 <= ocenka <= 89:
#     print('ocenka B')
# elif 70 <= ocenka <= 79:
#     print('ocenka C')
# elif 60 <= ocenka <= 69:
#     print('ocenka D')
# elif 0 <= ocenka <= 59:
#     print('ocenka F')            
# else:
#     print("ne pravilno")

# #2
# age = int(input(' vvedite svoy vozrast: '))    

# if age <= 13:
#     print('vy rebenok')
# elif age <= 17:
#     print ('vy podrostok')  
# elif age <= 64:
#     print (' vy vzrosly')
# else:
#     print(' vy nam ne podhodite')  

# #3

# num = int(input(' vvedy chislo: '))  

# if num % 2 ==0:
#     print('chetnoe')
# else:
#     print ('nechet')


# #4
# password_gues = input('inter password: ')
# login_gues = input('inter login: ')
# if password_gues == "1234" and login_gues == "admin":
#     print ('thank you')       
# else:
#     print ('ne pravelno')   


# #5

# time = int(input('napishi vremya ot 0 do 23: '))

# if 0 <= time <= 11:
#     print ('morning')
# elif 12<= time <= 17:
#     print('day')
# elif   18<= time <= 23:
#     print ('night') 
# else:
#     print ('ne pravilno')   


# #6

# temperartur = int(input('napishi temteraturu: '))

# if  temperartur < 0:
#     print ('very cold')
# elif 0 <= temperartur <= 15:
#     print('litl cold')
# elif   16<= time <= 25:
#     print ('nornal') 
# else:
#     print ('hot')



# #7

# spid = int(input('vvedi skorost vozhdenia: '))

# if 0 <= spid <= 60:
#     print ('vse v norne')
# elif 60< spid <= 80:
#     print('preduprizhdenie!!!')
 
# else:
#     print ('shtraf 500 tg')




# #8   

# age_credit = int(input('vvedi vozrast: '))
# dohod = int(input('vvedi svoy dohod: '))

# if age_credit <= 21 and dohod <= 50000:
#     print('super')

# else:
#     print("vy nam ne podhodite")    



# #9

# sum_pay = int(input('vvedi sumu pokupki: '))

# if sum_pay < 1000:
#     print(sum_pay)
# elif sum_pay >= 1000 and sum_pay < 5000:
#     print(sum_pay * (100 - 5) / 100)
# elif sum_pay >= 5000 and sum_pay < 10000:
#     print(sum_pay * (100 - 10) / 100)
# else:
#     print(sum_pay * (100 - 15) / 100)



# age_work = int(input("vvedite vozrast: "))
# stazh = float(input("VVedite stazh v godah:"))


# if age_work >=25 and stazh >= 3:
#     print ("vy mozhete rabotat menager")
# elif age_work >=25 and stazh < 3:
#     print ("Vam nuzhen staz 3 goda( ")
# elif age_work < 25 and stazh >= 3:
#     print ("Vam nuzho but starshe")
# else: 
#     print ("vy nam ne podhodute( ")   