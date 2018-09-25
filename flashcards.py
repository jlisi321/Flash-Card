import os
import time

def print_menu():
    folder_contents = os.listdir("/Users/joelisi/Documents/PROGRAMMING/flash_cards/sets")
    for folder_file in folder_contents:
        #find what number file we are on
        file_number = int(folder_file[0:2])
        file_number = "(" + str(file_number) + ")"


        set_name = folder_file[2:-4]
        set_name = set_name.replace("_", " ")
        set_name = file_number + set_name
        print(set_name)

    print("Message: Make sure to input a number within the range or the program will produce an error and shut down.")
    time.sleep(2)
    set_choice = int(input("Enter the corresponding number with your set choice:"))



    if(isinstance(set_choice, int) == True):
        return set_choice, folder_contents[set_choice - 1]


#run a continous loop until user quits
while(True):
    #def print_menu(all flash card sets), this function returns a choice for a set
    set_choice, set_file = print_menu()
    score = 0
    number_of_questions = 0

    open_file = open("/Users/joelisi/Documents/PROGRAMMING/flash_cards/sets/" + set_file)
    file_lines = open_file.readlines()
    print("Directions: Enter vocab relating to the definition")
    for line in file_lines:
        if(line == ""):
            break

        comma = line.find(",")
        question  = line[0:comma] + ":"
        answer = line[comma + 1:]
        user_answer = str(input(question))
        user_answer = user_answer.strip()
        answer = answer.strip()
        user_answer = user_answer.upper()

        if(user_answer == answer):
            print("You got it right!")
            score = score + 1
        elif(user_answer != answer):
            print("You got it wrong, the answer is " + answer)

        number_of_questions = number_of_questions + 1
        score_display = "Score:" + str(score) + "/" + str(number_of_questions)
        print(score_display)


    print("Score:" + str(score) + "/" + str(len(file_lines)))
    open_file.close()
    break

    #read the flashcard text file lines

    #print out the line to the command prompt, set the second half of the line
    #to the answer.

    #ask for an input from the user for the answer

    #check if user input is equal to answer, if it is tell them good job and add
    #one to the score. If they get it wrong then don't add a point and tell them
    #the correct answer
