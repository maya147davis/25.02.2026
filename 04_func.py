import random
import time

def get_user_choice() -> str:
    """
    get choice from user until got a valid choice
    :return:  str - 'rock', 'paper', 'scissors'
    """
    pass

def get_random_computer_choice() -> str:
    """
    random 1 options from 'rock', 'paper', 'scissors'
    :return:  str - 'rock', 'paper', 'scissors'
    """
    pass

def print_user_choice_icon_and_delay(choice, how_long_sleep) -> None:
    """
    print the user choice + icon and sleep 2-3
    :param choice:  str - 'rock', 'paper', 'scissors'
    :param how_long_sleep:  how long sleep in seconds
    :return: None
    """
    pass

def print_computer_choice_icon(choice) -> None:
    """
    print computer choice + icon
    :param choice:  str - 'rock', 'paper', 'scissors'
    :return:
    """
    pass

def get_game_result(user_choice, computer_choice) -> str:
    """

    :param user_choice:  str - 'rock', 'paper', 'scissors'
    :param computer_choice: str - 'rock', 'paper', 'scissors'
    :return: str winner - 'user', 'draw', 'computer'
    """
    pass

def print_result_and_icon(get_result) -> None:
    """
    👋 💥🤝✅
    Print result with icon
    :param get_result: str winner - 'user', 'draw', 'computer'
    :return: None
    """
    pass

# Icons for each choice
ICONS = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️",
}

print("🎮 Rock–Paper–Scissors")

user_choice = get_user_choice()
print_user_choice_icon_and_delay(user_choice)
computer_choice = get_random_computer_choice()
print_computer_choice_icon(computer_choice)
get_result = get_game_result(user_choice, computer_choice)
print_result_and_icon(get_result)

