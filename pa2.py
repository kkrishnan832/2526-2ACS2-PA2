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
    for line in my_quiz:
        if ',' in line: # split the line at the first comma
            answers_list = line.strip().split(',')
            if len(answers_list) > 1:
                print(f"{answers_list[1]}")
                user_answer = input("answer: ")
                if user_answer in answers_list:
                    index = answers_list.index(user_answer)
                    correct_answer = (answers_list[index - 1])
                    if user_answer == correct_answer:
                        print("Good job!")
                        score += 1
                    else:
                        print(f"So close! The answer was {correct_answer}") 
                        score += 0
        else:
            print("Comma found, but nothing after it.")
            break

    my_quiz.close()    
    return score    

def show_scores(): 
    print("shows_scores function called")
    print("Your score was {score}!")

def add_scores(score):
    print("add_scores function called with score to add as a parameter")
    username = input("What is your username?")
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