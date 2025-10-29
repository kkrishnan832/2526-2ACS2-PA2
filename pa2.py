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
    print(f"play_quiz function called with {file_url}. if ur ready to stop studying, enter 'quit'.")
    my_quiz = open(file_url, 'r')
    line = my_quiz.readline()
    for line in my_quiz:
        answers_list = line.split(',')
        print(f"{answers_list[1]}")
        user_answer = input("answer: ")
        correct = answers_list[0].strip()
        if user_answer == correct:
            print("Good job!")
            score += 1
        elif user_answer == "quit" or "Quit":
            break    
        else:
            print(f"So close! The answer was {correct}") 
            score += 0
    my_quiz.close()    
    return score    


def show_scores(score): 
    print("shows_scores function called")
    print(f"Your score was {score}!")
    with open('scores.txt', 'r') as display_scores:
        for line in display_scores:
            print(line.strip())


def add_scores(score):
    print("add_scores function called with score to add as a parameter")
    username = input("what is your username?")
    leaderboard = open("scores.txt", "a")
    leaderboard.write(f"\n{username}: {score}\n")
    leaderboard.close()

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
    times_quiz_options = ["TIMESTABLES", "TIMES TABLES", "TIMESTABLE", "TIMES TABLE"]
    periodic_quiz_options = ["PERIODIC TABLE", "PERIODICTABLE", "PERIODICTABLES", "PERIODIC TABLES"]
    all_quiz_options = ["TIMESTABLES", "TIMES TABLES", "TIMESTABLE", "TIMES TABLE", "PERIODIC TABLE", "PERIODICTABLE", "PERIODICTABLES", "PERIODIC TABLES"]
    first_choice = ""
    user_score = 0
    game_on = True
    quiz_name = ""

    while game_on:
        print("welcome to the review game")
        
        while first_choice not in e_options: #first runs bc first choice is empty string, then bc not exiting
            for item in initial_choices:
                print(f"- {item}") #print options
            first_choice = input("what would you like to do?\n> ").lower().strip()
            if first_choice in p_options: #playing
                quiz_fn = input("what is the name of your file? options: times_tables or periodic_table.\n> ").lower().strip() 
                while quiz_fn.upper() not in all_quiz_options:
                    print_error() 
                    print("your choices are:")
                    for item in all_quiz_options:
                        print(f"- {item}")
                    quiz_fn = input("what is the name of your file?\n> ") 
                if quiz_fn in times_quiz_options:
                    quiz_name = "times_tables"
                elif quiz_fn in periodic_quiz_options:
                    quiz_name = "periodic_table"       
                quiz_ext = input("is it a .txt or .csv file?\n> ").lower().strip() #ask file name
                while quiz_ext not in file_types:
                    print_error() 
                    print("your choices are:")
                    for item in file_types: #if file type isn't csv or txt, print options and try again
                        print(f"- {item}")
                    quiz_ext = input("is it a .txt or .csv file?\n> ").lower().strip()
                if quiz_ext in [".csv","csv"]: #if csv
                    file_url = (f"{quiz_name}.csv") #either way im gonna make it txt lol
                else:
                    file_url = (f"{quiz_name}.txt") #if txt #fix ts
                print(file_url)
                user_score = play_quiz(file_url) #int score
                add_scores(user_score)
            elif first_choice in h_options: #history
                show_scores(user_score)
            elif first_choice in e_options:#exit
                game_on = False
            else:
                print_error() #error

        print("goodbye!")

main()