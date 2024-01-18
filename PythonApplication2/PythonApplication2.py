# 1
# nimi=input("Mis on sinu nimi?").capitalize()
# print ("Tere,",nimi)
# if nimi=="Juku":
#     print("Lahme kinno")
#     age=int(input("Kui vana sa oled?"))
#     if age<0 or age>100:
#     pilet="valed vanus"
#     elif 0<age<6:
#     pilet="free ticket"
#     elif 6<=age<14:
#     pilet="lapse pilet"
#     elif 14<=age<65:
#     pilet="täispilet"
#     elif age<=100:
#     pilet="sooduspilet"
#     print(pilet) #Ilus ja õige vastus! "Vale vanus" või "On vaja osta..."

# else:
#     print("Ma ootan Jukut")

# 2
# nimi1=str(input("mis on sinu nimi?"))
# nimi2=str(input("ja mis on sinu nimi?"))
# print(nimi1, "ja", nimi2, "te olete naabrid")

# 3
# dlina=int(input("dlina?"))
# shirina=int(input("shirina?"))
# P=dlina+dlina+shirina+shirina
# S=dlina*shirina
# print("p =",P, "s =", S)
# remont=input("nado remont?")
# if remont==(jah):
#     metr=int(input("kui palju maksaks ruutmeetri kohta?"))
#     price=metr*S
#     print("hind=", price)
# else:
#     print("Head aega")

# 4
from random import *
initial_price = uniform(500, 1000) 
print(f"Alghind: {initial_price} евро")
if initial_price > 700:
    discount_percentage = 30
    discount_amount = (discount_percentage / 100) * initial_price
    discounted_price = initial_price - discount_amount
    print("Soodushind: {discounted_price} ")
else:
    print("Hind ilma allahindluseta, kuna alghind ei ületa 700 eurot.")