import time

print('''------------------------------------ METRO TICKET BOOKING------------------------------------
      ''')
#TAKING INPUT FROM THE USER
def user_name():
    name=input("Enter your name:")
    return name
user_input_name=user_name()
#VERIFIYING THE USER INPUT VALUE
count=1

def user_verify(user_input_name):
    count=1
    while count<=3:
        print('Entry:',count)
        if user_input_name.isdigit():
            print("Invalid Input Entry: {}! Enter the correct Details ".format(count))
            if count==2:
                print("last attempt!")
            elif count==3:
                print("Too Many Attempts Reached!")
                return False
            user_input_name=user_name()
        else:
            print("You Entry is Matched",user_input_name)
            return True
        count=count+1
    return False    
user_verify(user_input_name)