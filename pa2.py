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
    print(f"ok, studying with {file_url}. if ur ready to stop studying, enter 'quit'.")
    my_quiz = open(file_url, 'r')
    line = my_quiz.readline()
    for line in my_quiz:
        answers_list = line.split(',') #creating list of terms and answers
        print(f"{answers_list[1].lower().strip()}") #print question
        user_answer = input("answer: ").lower()
        correct = answers_list[0].lower().strip() #check if correct
        if user_answer == correct:
            print("Good job!")
            score += 1 #add to score
        elif user_answer.upper() == "QUIT":
            break    #quit studying
        else:
            print(f"So close! The answer was {correct}.") 
            score += 0 #bad studying
    my_quiz.close()    
    return score    


def show_scores(score): 
    print(f"your score was {score}!")
    with open('scores.txt', 'r') as display_scores:
        for line in display_scores:
            print(line.strip())

def add_scores(score, quiz_name):
    print(f"your score was {score}!")
    username = input("what is your username? ")
    date = input("what is the date? ")
    leaderboard = open("scores.txt", "a")
    leaderboard.write(f"\n{quiz_name}, {date} - {username}: {score}\n")
    leaderboard.close()

def create_quiz(custom_quizzes_list):
    quiz_name = input("what would u like to call ur quiz?\n> ")
    new_file = (f"{quiz_name}.txt")
    print("when making ur quiz, pls structure it with the answer first, then a comma, then the question, before entering to the next line for the next term. u will have a max of 10 terms. ex: 'To talk',Hablar.")
    with open(f'{new_file}', 'w') as file:
        for i in range(10):
            entry = input(f"Term {i + 1} (Answer,Question): ")
            file.write(entry + "\n")
    custom_quizzes_list.append(quiz_name)
    print(f"new quiz '{quiz_name}' has been created.")
    return custom_quizzes_list

def print_error():
    print("*"*50)
    print(" "*22+"error!"+" "*22)
    print(" "*12+"that is not a valid option"+" "*12)
    print(" "*17+"please try again"+" "*17)
    print("*"*50)

def main():
    #initialize variables
    initial_choices = ["play","see history","exit","create new quiz"]
    file_types = [".txt", ".csv", "txt", "csv"]
    p_options = ["play","p","play game"]
    h_options = ["see history", "history", "h", "see", "sh", "s"]
    e_options = ["exit","e","exit game"]
    c_options = ["c", "create new quiz", "create new", "new quiz", "create", "new"]
    times_quiz_options = ["TIMESTABLES", "TIMES TABLES", "TIMESTABLE", "TIMES TABLE", "TIMES_TABLE", "TIMES_TABLES"]
    periodic_quiz_options = ["PERIODIC TABLE", "PERIODICTABLE", "PERIODICTABLES", "PERIODIC TABLES", "PERIODIC_TABLE", "PERIODIC_TABLES"]
    first_choice = ""
    user_score = 0
    game_on = True
    quiz_name = ""
    custom_quizzes_list = []


    while game_on:
        print("welcome to the review game")
        
        while first_choice not in e_options: #first runs bc first choice is empty string, then bc not exiting
            for item in initial_choices:
                print(f"- {item}") #print options
            first_choice = input("what would you like to do?\n> ").lower().strip()
            if first_choice in p_options: #playing    
                print(f"what is the name of your file? premade options: times_tables and periodic_table; your custom options: {custom_quizzes_list}")
                quiz_fn = input("> ").lower().strip()
                if quiz_fn.upper() in times_quiz_options:
                    quiz_name = "times_tables"
                elif quiz_fn.upper() in periodic_quiz_options:
                    quiz_name = "periodic_table" 
                elif quiz_fn.lower() in custom_quizzes_list:
                    quiz_name = quiz_fn
                while quiz_fn.upper() not in times_quiz_options and quiz_fn.upper() not in periodic_quiz_options and quiz_fn.lower() not in custom_quizzes_list:
                    print_error()  
                    print(f"what is the name of your file? premade options: times_tables and periodic_table; your custom options: {custom_quizzes_list}")
                    quiz_fn = input("> ").lower().strip() 
                quiz_ext = input("is it a .txt or .csv file?\n> ").lower().strip() #ask file name
                while quiz_ext not in file_types:
                    print_error() 
                    print("your choices are:")
                    for item in file_types: #if file type isn't csv or txt, print options and try again
                        print(f"- {item}")
                    quiz_ext = input("is it a .txt or .csv file?\n> ").lower().strip()
                if quiz_ext in [".csv","csv"]: #if csv
                    file_url = (f"{quiz_name}.txt") #either way im gonna make it txt lol
                else:
                    file_url = (f"{quiz_name}.txt") #if txt
                user_score = play_quiz(file_url) #int score
                add_scores(user_score, quiz_name)
            elif first_choice in h_options: #history
                show_scores(user_score) 
            elif first_choice in c_options:  
                create_quiz(custom_quizzes_list) #calling the create quiuz function
            elif first_choice in e_options:#exit
                game_on = False  
            else:
                print_error() #error

        print("thanks for studying w us!")

main()