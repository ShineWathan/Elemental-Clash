import pytest
from project import ai_punishment, my_punishment

choices = ["rock", "paper", "scissors"]

def test_player_choice():
    player_choice = "rock"
    assert player_choice in choices

def test_ai_punishment():
    punishment_message, is_matched = ai_punishment()
    assert punishment_message is not None
    assert isinstance(is_matched, bool)

def test_my_punishment():
    my_command = "Write 'I am stupid' 6times"
    assert my_punishment(my_command) == None

if __name__ == "__main__":
    pytest.main()
