import random
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
special_characters=['!','@','#','$','%','^','&','*','(',')','+']
alpha = int(input("Enter number of alphabets you want in your pw: "))
num = int(input("Enter number of numbers in your pw: "))
special_character = int(input("Enter number of speacial characters in your pw: "))
pw_list=[]
for alphabet in range(alpha):
    pw_list+=random.choice(alphabets)
for number in range(num):
    pw_list+=random.choice(numbers)
for speacial in range(special_character):
    pw_list+=random.choice(special_characters)
random.shuffle(pw_list)
Strong_PW=""
for char in pw_list:
    Strong_PW+=char
print("Your PW is: ", Strong_PW)