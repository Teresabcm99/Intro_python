f_name=input("What is your name?")
surname=input("What is your surname?")
print(surname +" "+ f_name)

fav_number=input("What is your favourite number?")
age= input("How old are you?")
print(int(fav_number) + int(age))

#problema granja

cows=4
chicken=2
pigs=4

Question=input ("How many animals are in the farm?")

print(int(Question[0])*cows)
print(int(Question[8])*pigs)
print(int(Question[16])*chicken)
#*(chicken)=
#*(pigs)=+ int(Question[7])*pigs+ int([Question[16,17])*chicken)


#Problem

total=int(input("how many clases were held?"))
Attendance= int(input("how many classes did you attend?"))

percentage_att=(Attendance/total*100)



if percentage_att<=74:
    print("You failed")
elif percentage_att <=75:
    print("You passed")


#If loops exercises
num1=4
num2=8
num3=5

if num1!=num2!=num3:
    print(num1+num2+num3)
elif num1==num2==num3:
    print(3*(num1+num2+num3))


i= 2
while i <=20:
    print(i+2)