from random import choice
from main import speak, get_command  # Do not do this


def play():
    print('Playing rock-paper-scissors...')
    speak('let\'s play rock paper scissors')
    while True:
        player = get_player_input()
        if player == '':
            continue

        ai = choice(['r', 'p', 's'])
        match ai:
            case 'r':
                speak('I choose rock')
            case 'p':
                speak('I choose paper')
            case 's':
                speak('I choose scissor')

        check_winner(player, ai)

        speak('do you want to play again?')
        play_again = get_command().lower()
        if 'yes' in play_again or 'sure' in play_again:
            continue

        speak('okay')
        break


def get_player_input():
    speak('Choose your weapon?')
    print('Rock, Paper, scissor')
    player_input = get_command()
    print(f'> {player_input}')

    if 'rock' in player_input.lower():
        speak('you choose rock')
        return 'r'
    elif 'paper' in player_input.lower():
        speak('you choose paper')
        return 'p'
    elif 'scissor' in player_input.lower():
        speak('you choose scissor')
        return 's'
    else:
        speak('Please say your weapon again')
        return ''


def check_winner(player, ai):
    if player == ai:
        print('Result: Tie')
        speak('tie!')
    elif ai == 'r' and player == 's':
        print('Result: Lose')
        speak('Rock beats scissors, I win!')
    elif ai == 's' and player == 'p':
        print('Result: Lose')
        speak('Scissors beats paper! I win!')
    elif ai == 'p' and player == 'r':
        print('Result: Lose')
        speak('Paper beats rock, I win!')
    else:
        print('Result: Win')
        speak('You win!\n')


if __name__ == '__main__':
    play()
