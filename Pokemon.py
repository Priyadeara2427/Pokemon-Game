import random
import sys
import requests

my_pokemon_score = 0
opp_pokemon_score = 0
stats = ['height', 'weight', 'id', 'HP-effort', 'High-Power', 'base_experience', 'Attack']


def opp_stat():
    ''' Allows the opponent to select a random
    stat.
    returns:
        string:random stat generated by the opponent.'''

    opp_stat_choice = random.choice(stats)
    print(f'\n Opponent has chosen {opp_stat_choice} as stat value')
    return opp_stat_choice


def decide_player_or_opp_stat():
    '''  Decides if player or opponent should select the stat.
        based on the input calls player stat() or opp stat()
        selection function.
        If the given input is not valid, allows the player
        to provide the correct input.
        Returns:
            string:returns stat chosen by either
                player or opponent.'''

    player_or_opponent = input("Do you want Player to enter stat or the Opponent (computer)?")

    if player_or_opponent == "Player":
        stat = player_stat_fun()
        return stat

    elif player_or_opponent == "Opponent":
        stat = opp_stat()
        return stat

    else:
        print("Entered wrong input! Please enter either 'Player' or 'Opponent' : ")
        decide_player_or_opp_stat()


def player_stat_fun():
    '''Asks the user to input the stat from the list provided
    if the stat is in the list 'stats',it
        Returns:
            string: returns the stat chosen by the player
    if not:
            it will say incorrect stat and again let the user enter the
            stat by calling the same function'''

    player_stat = input("Enter the stat you want to choose from height, weight, base_experience, High-Power, HP-effort, Attack ")

    if player_stat in stats:
        return player_stat
    else:
        print("Incorrect stat.")
        player_stat = player_stat_fun()
        return player_stat


def pokemon_list():
    '''Prints a list of pokemon names using
       the url given  in the fn'''

    url = f'https://pokeapi.co/api/v2/pokemon-form/'
    response = requests.get(url)
    data = response.json()
    list_pokemons = []
    print("\n--- Pokemon names ---")
    for item in data["results"]:
        list_pokemons.append(item["name"])

    random.shuffle(list_pokemons)
    print(list_pokemons)


def random_pokemon():
    '''Generates a random id and fetches the name of the pokemon
       corresponding to the id generated
       Returns:
           string: Returns pokemon name.'''

    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    sel_num_pok = response.json()
    return sel_num_pok['name']


def pokemon_details(pokemon_name):
    '''Fetches all details about the given pokemon.
        Parameter:
          pokemon_name(string):
             name of the pokemon whose details have
             to be fetched.
          Returns:
              dict:returns a dictionary containing stat info like
              pokemon's id,name,height,weight,base experience,HP-effort...'''
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'
    response = requests.get(url)
    try:
        pokemon = response.json()

        return {
            'name': pokemon['name'],
            'id': pokemon['id'],
            'height': pokemon['height'],
            'weight': pokemon['weight'],
            'base_experience': pokemon['base_experience'],
            'High-Power': pokemon['stats'][0]['base_stat'],
            'HP-effort': pokemon['stats'][0]['effort'],
            'Attack': pokemon['stats'][1]['base_stat']
        }

    except requests.exceptions.HTTPError as err:
        print("HTTP Error")
        # print(err.args[0])
        sys.exit(err)


def play_pokemon(num_of_rounds, my_pokemon_score, opp_pokemon_score):
    '''-Displays a list of pokemon to the player and allows to enter
    the player choice of pokemon.
       -compares the random pokemon generated by the opponent
        with the pokemon chosen by the player with their respective
        stat info and decides the winner for every round.
        counts the score and displays the highest score of
        the players in a csv spreadsheet.
            Parameter:
            - num_of_rounds(int):
               Specifies the total number of rounds in the game.
            - my_pokemon_score(int):
              initial score of the player i.e,0
            -opp_pokemon_score(int)
             initial score of the opponent i.e,0'''
    for each_round in range(num_of_rounds):
        print("Round", each_round + 1)
        stat = decide_player_or_opp_stat()
        pokemon_list()

        my_pokemon = input("\n Enter my Pokemon name from the above list: ")
        my_pokemon_info = pokemon_details(my_pokemon)
        opponent_pokemon = random_pokemon()
        print('The opponent chose: {}'.format(opponent_pokemon))
        opp_pokemon_info = pokemon_details(opponent_pokemon)
        player_stats = my_pokemon_info[stat]
        opponent_stats = opp_pokemon_info[stat]

        # <........comparing stat...........>

        if player_stats > opponent_stats:
            my_pokemon_score = my_pokemon_score + 1
            print(f"player wins")
        elif opponent_stats > player_stats:
            opp_pokemon_score = opp_pokemon_score + 1
            print(f"opponent wins")
        else:
            print('draw')
    # <.................final result................>
    if my_pokemon_score > opp_pokemon_score:
        print("*" * 30)
        print(f"Final Result\n My Pokemon won the game")
    elif opp_pokemon_score > my_pokemon_score:
        print("*" * 30)
        print(f"Final Result\n Opponent Pokemon won the game")
    else:
        print("*" * 30)
        print("\nFinal Result\n The game is a draw")

    # <...........storing in a csv spreadsheet......>
    import csv
    field_names = ['name', 'score']
    data = [
        {'name': 'player', 'score': my_pokemon_score},
        {'name': 'computer', 'score': opp_pokemon_score},
    ]
    with open('result.csv', 'w+') as csv_file:
        result = csv.DictWriter(csv_file, fieldnames=field_names)
        result.writeheader()
        result.writerows(data)


# <..............Main ....................>
if __name__ == "__main__":
    try:
        num_of_rounds = int(input("Enter the number of rounds: "))
        play_pokemon(num_of_rounds, my_pokemon_score, opp_pokemon_score)


    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid number.")
