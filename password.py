from curses.ascii import isdigit
import random

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#single
def num_choice():
    num_length = (input("Length: "))
    new_pw_num = []

    if num_length.isdigit() == False:
        print("Invalid input...")
        num_choice()
    else:
        for x in range(int(num_length)):
            random_num = random.randint(1,9)
            new_pw_num.append(random_num)

        map_new_pw_num = map(str, new_pw_num) 
        str_pw_num = list(map_new_pw_num)
        num = (''.join(str_pw_num))
        print(num)

def char_choice():
    char_length = (input("Length: "))
    new_pw_char = []

    if char_length.isdigit() == False:
        print("Invalid input...")
        char_choice()
    else:
        for x in range(int(char_length)):
            random_char = random.choice(abc)
            new_pw_char.append(random_char)

        char = (''.join(new_pw_char))
        print(char)

#mixed
def num_choice_mixed():
    num_length = (input("Necessary Numbers: "))
    new_pw_num = []

    if num_length.isdigit() == False:
        return ''
    else:
        for x in range(int(num_length)):
            random_num = random.randint(1,9)
            new_pw_num.append(random_num)
        map_new_pw_num = map(str, new_pw_num) 
        str_pw_num = list(map_new_pw_num)
        num = (''.join(str_pw_num))
        return num

def char_choice_mixed():
    char_length = (input("Necessary Letters: "))
    new_pw_char = []

    if char_length.isdigit() == False:
        return ''
    else:
        for x in range(int(char_length)):
            random_char = random.choice(abc)
            new_pw_char.append(random_char)
        char = (''.join(new_pw_char))
        return char

def cap_char_choice_mixed():
    cap_char_length = (input("Necessary Capitals: "))
    new_pw_cap_char = []

    if cap_char_length.isdigit() == False:
        return ''  
    else:
        for x in range(int(cap_char_length)):
            random_cap_char = random.choice(abc)
            new_pw_cap_char.append(random_cap_char)
        lower_char = (''.join(new_pw_cap_char))
        cap_char = lower_char.upper()
        return cap_char

def sym_choice_mixed():
    sym_length = (input("Necessary Symbols: "))
    new_pw_sym = []
    
    if sym_length.isdigit() == False:
        return ''
    else:
        for x in range(int(sym_length)):
            symbol = ['!', '@', '#', '$', '%', '^', '&', '*']
            random_sym = random.choice(symbol)
            new_pw_sym.append(random_sym)

        sym = ''.join(new_pw_sym)
        return sym

def mixed_alpha():
    unshuffled_pw = num_choice_mixed() + char_choice_mixed() + cap_char_choice_mixed() + sym_choice_mixed()
    shuffled_pw = ''.join(random.sample(unshuffled_pw,len(unshuffled_pw)))
    print(shuffled_pw)
    with open('passwordgeneration.txt', 'a') as password:
        password.write(shuffled_pw)

def sin_alpha(sin_choice):
    if choice == '1':
        num_choice()
    elif choice == '2':
        char_choice()
    else:
        print("Invalid Input")

def menu(choice):
    if choice == '1':
        sin_choice = str(input("""1. Numbers
2. Letters
Selection: """))
        sin_alpha(sin_choice)
    elif choice == '2':
        mixed_alpha()
    else:
        print("Invalid Input")

print("""Password Generator
""")

choice = str(input("""What is your desired generator?

1. Single Alphanumeric
2. Mixed Alphanumeric
Selection: """))
print("""
""")

menu(choice)
