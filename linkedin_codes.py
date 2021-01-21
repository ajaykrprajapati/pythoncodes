import math
import time
import re
import pickle
import sched

def get_digit_reverse():
    input_digit = input("enter digit to be reveresed:")
    input_digit = int(input_digit)
    reminder=""
    while(input_digit>0):
        reminder = reminder+ str(input_digit%10)
        input_digit = input_digit//10
    print("reminder:", reminder)

def get_prime_factor():
    start_time = time.time()
    input_digit = input("put number whose prime factor you want to find:")
    input_digit = int(input_digit)

    while(input_digit%2 == 0):
        print("2")
        input_digit = input_digit/2
        print(input_digit)

    for i in range(3, int(math.sqrt(input_digit))+1,2):
        while input_digit%i == 0:
            print(i)
            input_digit=input_digit//2

    if input_digit > 2:
        print(input_digit)
    print("--- %s seconds ---" % (time.time() - start_time))

def is_palindrome():
    start_time = time.time()
    input_digit = input("put number whose prime factor you want to find:")
    # ignore spaces and special char
    x = re.findall(r'[a-z]+', input_digit.lower())
    print("x:", x)
    forward = ''.join(re.findall(r'[a-z]+', input_digit.lower()))
    print("forward: ", forward)
    backward = forward[::-1]
    print(forward+":"+backward)
    if forward == backward:
        print("Its palindrome")
    else:
        print("No its palindrome")
    print("--- %s seconds ---" % (time.time() - start_time))

def get_sorted_string():
    start_time = time.time()
    str = input("put number whose prime factor you want to find:")
    str_list = str.split(" ")
    str_list = [ w.lower() + w for w in str_list]
    str_list.sort()
    str = [w[len(w)//2:] for w in str_list]
    print(str)
    print("--- %s seconds ---" % (time.time() - start_time))

def get_search_list_items(search_list, item):
    indices = list()
    for i in range(len(search_list)):
        if search_list[i] == item:
            indices.append([i])
        elif isinstance(search_list[i], list):
            for index in get_search_list_items(search_list[i], item):
                indices.append([i]+index)
    return indices

def save_dict():
    dict = {'k':'v'}
    with open('dict_file.pickle','wb') as file:
        pickle.dump(dict, file)
        # file.write(dict)
    with open('dict_file.pickle', 'rb') as file:
        print(pickle.load(file))
        # print(file.read())

# def count_unique_word():
    





#menu
def menu():
    print("\n\nselect from following:")

    print("1. get_digit_reverse")
    print("2. get_prime_factor")
    print("3. is_palindrome")
    print("4. Sort_a_string")
    print("5. search an item from list")
    print("6. save dict into file(pickeling used for serializing and deserializing)")
    val = int(input("Enter your value: "))
    if val == 1:
        get_digit_reverse()
    elif val == 2:
        get_prime_factor()
    elif val == 3:
        is_palindrome()
    elif val == 4:
        get_sorted_string()
    elif val == 5:
        search_list = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
        print("search_list: ", search_list)
        print("item to be searched: 2")
        item = 2
        print(get_search_list_items(search_list, item))
    elif val == 6:
        save_dict()

    else:
        print("invalid input")
    menu()

menu()






























