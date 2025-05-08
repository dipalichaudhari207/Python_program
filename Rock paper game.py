import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def play_round():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid input. Choose rock, paper, or scissors: ").lower()
    
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}, computer chose {computer_choice}.")

    result = determine_winner(user_choice, computer_choice)
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")
    
    return result

def main():
    user_score = 0
    computer_score = 0

    while True:
        result = play_round()
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")
        
        play_again = input("Play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
