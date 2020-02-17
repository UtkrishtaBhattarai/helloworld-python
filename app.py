# python code runs line by line

print("Hello world")
print("0---")
print("|||")
print('*' * 10)

# defning variable in python
numberfirst = 1
numbersecond = 2
print(numberfirst * numbersecond)

# types of variable in python
# is_true=True
# price=990.9

##on some hospital scenario
# name="John"
# age=20
# is_new=False

# name1=input("What is your name? ")
# print("Hi"+" "+ name1)

# asking person name and color and print like utkrishta likes black
# name2=input("What is your name ? ")
# color=input("What is your favourite color? ")
# print("My name is "+ name2+" "+ "and my favourite color is"+" "+ color+".")

# parsing into string
# lets calculate the age

# displayage=input("What is your birth year?: ")
# calculateage=2020-int(displayage)
# print(calculateage)

# print(type(displayage))# used to print the variable type

##get weight in gram and show it in kilo
# gram_weight =int(input("Please enter your weight in gram: "))
# print((gram_weight/1000))

# defining quotes by someone

print('Someone said "Where do you live"')

# email for someone

print(''' 
Hi john, 
i am utrkishta bhattarai
who are you ?
Best regards
''')

# indexing strings in python
index = "What is my name"
print(index[0])  # getting first aplhabet of the index variable
print(index[-1])  # getting last alphabet of the index
print(index[0:3])  # getting multiple alphabets starting from index 0 to index 3 excluding 3
print(index[0:])  # getting all from index 0

# formatted string
fname = "John"
lname = "Smith"
msg = f'{fname} [{lname}] is a coder'
print(msg)

course = 'Python for Beginners'
print(len(course))  ##counting the number of input

print(course.upper());  ##uppercase conversion
print(course.find('o'));  # finding
print(course.replace('for', 'For'))

# if python is in course
# boolen expression

print('Python' in course)  ##retuns boolean value

##int and float

print(10+3)
print(10%3)

x=10
x=x+3
print(x)

x+=3 #works same as x=x+3

y=10+3*2
print(y)

z=2.9 ##rounding values
print(round(z))

a=-2.9
print(abs(a))



#conditional statements
price_house=1000000
has_good=False

if has_good:
    downpayment=0.1*price_house
else:
     downpayment=(0.2*price_house)
print(f"Down payment for the house is {downpayment}")

has_high_income=True
has_good_credit =True

if has_high_income and has_good_credit:
    print("Eligible for loan")


##assignment

temperature=31
if temperature>30:
    print("It is a hot day")
elif temperature<10:
    print("It is a cold day")
else:
    print("It is neither hot nor cold")


##assignment 2

name=input("please enter your name? ")

if len(name)<3:
    print("The name must be three characters long")
elif len(name)>50:
    print("The name must not be greater than 50 characters")
else:
    print("Name looks good")

#while loop in python

i=1
while i<=5:
    print(i)
    i=i+1
print("Done")


##building a guessing game

secret_number=9
guess_times=0
guess_limit=3
while guess_times<guess_limit:
    guess=int(input("Guess: "))
    guess_times+=1
    if guess==secret_number:
        print("You have won")
        break
else:
    print("Sorry you have failed")

###car simulation game
print("Welcome to our simulation game")
command=""
started=False
stopped=False
while True:
    command=input("> ").lower()
    if command=="start":
        if started:
            print("Car is already started")
        else:
            started=True
            print("car started")
    elif command=="stop":
        if stopped:
            print("Car is already at stop")
        else:
            print("Car stopped")
    elif command=="help":
        print(''' 
start-to start the car 
stop-to stop the car
quit-to quit
        ''')
    elif command=="quit":
        break
    else:
        print("I cant understand your command")






