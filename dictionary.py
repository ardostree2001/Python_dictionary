import time
global word
global mean
global line

str = "\n\n------English Dictionary------\n\n 1. Add \n 2. Search \n 3. Delete \n 4. View \n 0. Exit\n\n\nEnter your choice: "



dict = {"Hell":"Place Where Deamons Live","Heaven":"Place Where Gods Live"}

# Input Statement
def ip():

    case = int(input(str))

    #Selection of function
    if case==1:
        add()

    elif case==2:
        search()

    elif case==3:
        delete()

    elif case==4:
        view()

    elif case==0:
        exit()

    else:
        print("Enter Correct Input")
        ip()


#Function Definition
def search():
    word= input("\n\nEnter the word:  ")
    if word in dict:
        print("{} - {}\n\n".format(word,dict[word]))
        time.sleep(5)
    else:
        print("\n\n\nThe word doesn't exist in dictionary")
        time.sleep(5)
    return ip()


def add():
    word= input("\n\nEnter the word:  ")

    if word in dict:
        print("\n\n\nThis Word Already Exist In Dictionary\n\n")
        time.sleep(5)
    
    else:  
        mean= input("\n\nEnter the meaning:  ")
        dict[word] = mean
        print("\n\n\nWord Added Successfully")
        time.sleep(5)
    return ip()

def delete():
    word= input("\n\nEnter the word:  ")

    if word in dict:
        del dict[word]
        print("\n\n\nThe word is removed from the dictionary")
        time.sleep(5)
    
    else:
        print("\n\n\nThe word doesn't exist in the dictionary")
        time.sleep(5)
    return ip()    

def view():
    for word in dict:
       print("{} - {}\n".format(word,dict[word]))
    time.sleep(5)
    return ip()    
ip()