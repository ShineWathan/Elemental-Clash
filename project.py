"""
project's title - Elemental Clash
name            - Shine Wathan
GitHub          - ShineWathan
edX usernames   - Rivan_23
country         - Myanmar
Recording data  - 1-Mar-2024
"""

import re
import random
#import pygame

choices = ["rock", "paper", "scissors"]

regex_text = r"'(\w.+)'"
regex_num = r"\d{1,2}"
count = 0
num_times = 0

#not working on CS50
# def play_winning_sound():
#     pygame.mixer.music.init()
#     pygame.mixer.music.load('winning_sound_eff.ogg')
#     pygame.mixer.music.play()

# def play_losing_sound():
#     pygame.mixer.pre_init()
#     pygame.mixer.init()
#     pygame.mixer.music.load('losing_sound_eff.ogg')
#     pygame.mixer.music.play()


def ai_punishment():
    global count, num_times
    ai_command = ["Write 'I am noob' 3times", "Write 'I am stupid' 6times", "Write 'I cannot play this game' 9times", "Write 'I am loser' 12times"]
    ai_command_choice = random.choice(ai_command)
    print(ai_command_choice)
    rgx = re.search(regex_text, ai_command_choice)
    if rgx:
        match = re.search(regex_num, ai_command_choice)
        num_times = int(match.group())
        for i in range(num_times):
            my_type = input().strip()
            count += 1
            my_type_matched = my_type == rgx.group(1)
            message = command_num_of_times(my_type_matched, num_times, count)
            print(message)
            if not my_type_matched:
                print("Don't you understand my command? Hmmm...")
            if count >= num_times:
                break
        return message, my_type_matched

def command_num_of_times(my_type_matched, num_times, count):
    remaining_count = num_times - count
    if my_type_matched:
        if remaining_count > 0:
            return f"You have already typed {num_times - remaining_count} times. You only have {remaining_count} left."
        else:
            return "You have reached the limit."


def my_punishment():
    my_command = input("Command the AI (Eg. Write '' 3times.): ")
    rgx = re.search(regex_text, my_command)
    if rgx:
        match = re.search(regex_num, my_command)
        num_times = int(match.group())
        for i in range(num_times):
            print(rgx.group(1))
def main():
    global count
    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        while player_choice not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        computer_choice = random.choice(choices)
        print("Computer chooses:", computer_choice)

        if player_choice == computer_choice:
            print("It's a draw!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "paper" and computer_choice == "rock") or \
            (player_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            # play_winning_sound()
            my_punishment()
        else:
            print("Computer wins!")
            # play_losing_sound()
            ai_punishment()

        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower().strip()
            if play_again == "yes":
                print("Ok let's play again!")
                count = 0
                break
            elif play_again == "no":
                print("Thanks for playing!")
                #pygame.quit()
                exit()
            else:
                print("Just answer yes or no")


if __name__ == "__main__":
    main()
