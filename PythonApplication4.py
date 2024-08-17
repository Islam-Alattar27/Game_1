
import random as r

def play_game():
    w = r.choice(["Rock", "Paper", "Scissors"])
    e = int(input("\nWelcome to the game (Rock - Paper - Scissors)\n\nPlease choose a number:\n1- Rock\n2- Paper\n3- Scissors\n"))
    
    while e==1 or 2 or 3:
        if e == 1:
            if w == "Scissors":
                print("You win!")
                break
            elif w == "Paper":
                print("You lose!")
                break
            else:
                print("It's a draw!")
                break
        elif e == 2:
            if w == "Scissors":
                print("You lose!")
                break
            elif w == "Paper":
                print("It's a draw!")
                break
            else:
                print("You win!")
                break
        elif e == 3:
            if w == "Scissors":
                print("It's a draw!")
                break
            elif w == "Paper":
                print("You win!")
                break
            else:
                print("You lose!")
                break
        else:
            print("Please choose a number 1, 2, or 3")
           
            

def main():
    while True:
        choice = int(input("\nChoose an option:\n1- Play the game\n2- Exit the program\n"))
        
        if choice == 1:
            play_game()
        elif choice == 2:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")

main()
print("im islam")