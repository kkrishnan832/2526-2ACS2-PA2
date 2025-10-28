'''
Make a flashcard review game that reads through a file
where each line consists of a term and its definition.

An example text file and an example CSV file have been provided to you.

A masterful program includes the ability to create a new file
and load your own terms/definitions into it, before running the quiz on that file.

Save game records to a different file. Log username and high score.
Allow the user the option to view this file by printing it to the console.

You should at minimum edit the helper functions.
You may not necessarily have to edit the main function.
'''

def play_quiz(file_url):
    score = 0
    print(f"play_quiz function called with {file_url}")
    my_quiz = open(file_url, 'r')
    line = my_quiz.readline()
    while line.strip() != ",":
        line = my_quiz.readline()
    print(line)
    user_answer = input("\nAnswer: ")
    if user_answer == "" #what comes after comma/real answer
        print("Good job!")
        score =+ 1
    else
        print("So close! The answer was {line[3]}") #first three lines of file

def show_scores(): #this is what i need help with, how do i store stuff??
    print("shows_scores function called")
    

def add_scores(new_score):
    print("add_scores function called with score to add as a parameter")
    username = input("What is your username?")
    username == "" #store under whatever i'm using in history


def print_error():
    print("*"*50)
    print(" "*22+"error!"+" "*22)
    print(" "*12+"that is not a valid option"+" "*12)
    print(" "*17+"please try again"+" "*17)
    print("*"*50)

def main():
    #initialize variables
    initial_choices = ["play","see history","exit"]
    file_types = [".txt", ".csv", "txt", "csv"]
    p_options = ["play","p","play game"]
    h_options = ["see history", "history", "h", "see", "sh", "s"]
    e_options = ["exit","e","exit game"]
    first_choice = ""
    game_on = True

    while game_on:
        print("welcome to the review game")
        
        while first_choice not in e_options: #first runs bc first choice is empty string, then bc not exiting
            for item in initial_choices:
                print(f"- {item}") #print options
            first_choice = input("what would you like to do?\n> ").lower().strip()
            if first_choice in p_options: #playing
                quiz_fn = input("what is the name of your file?\n> ").lower().strip() 
                quiz_ext = input("is it a .txt or .csv file?\n> ").lower().strip() #ask file name
                while quiz_ext not in file_types:
                    print_error() 
                    print("your choices are:")
                    for item in file_types: #if file type isn't csv or txt, print options and try again
                        print(f"- {item}")
                    quiz_ext = input("is it a .txt or .csv file?\n> ").lower().strip()
                if quiz_ext in [".csv","csv"]: #if csv
                    file_url = quiz_fn+".csv" 
                else:
                    file_url = quiz_fn+".txt" #if txt
                user_score = play_quiz(file_url) #int score
                add_scores(user_score)
            elif first_choice in h_options: #history
                show_scores()
            elif first_choice in e_options:#exit
                game_on = False
            else:
                print_error() #error
        
        print("goodbye!")

main()