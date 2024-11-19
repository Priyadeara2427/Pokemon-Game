# Pokémon Battle Game 🐾⚔️
Welcome to the Pokémon Battle Game! 🕹️ Test your strategy and luck as you battle it out with a computer opponent in this exciting game. Choose the number of rounds, decide who picks the Pokémon, and let the battles begin!

# 🌟 Features
* 🎮 Customizable Rounds: Select the number of rounds to play.
* 🤖 Dynamic Pokémon Selection: Decide if the player or computer picks Pokémon for battles.
* ⚡ Battle Mechanics: Pokémon stats determine the winner of each round.
* 📊 Score Tracking: Scores are updated after each round.
* 🏆 Winner Announcement: The final winner is declared after all rounds.

# 🚀 How It Works

## 1. Setup the Game:
* Input the number of rounds you want to play.
* Choose whether the player or the computer will select Pokémon.

## 2. Battle Phase:
* Pokémon are selected based on your preference.
* Stats like attack, defense, and speed are compared to decide the round's winner.

## 3. Results:
* Scores are tracked after each round.
* At the end of the game, the final winner is announced based on total victories.


# 🛠️ Technologies Used
* Programming Language: Python 🐍
* Libraries:
  * random (for Pokémon selection and battle mechanics)
  * JSON (to store Pokémon stats, if applicable)

# 🎮 How to Run
1. **Clone the Repository**: 
   ```shell
   git clone https://github.com/Priyadeara2427/Pokemon-game.git
   cd Pokemon-game


2. **Run the game:**:
   ```shell
   python src/pokemon_game.py

# 🔮 Future Enhancements
* 🎨 Add a GUI for a more immersive experience.
* 🌍 Include multiplayer functionality.
* 🧠 Add AI to make computer selections smarter.
* 🐉 Introduce more Pokémon and unique abilities.

# Pokémon API Integration
This project uses the PokeAPI to fetch data about Pokémon, including names, stats, abilities, and more.

## How to Access the API
* Base API URL
** All data is accessed through the PokeAPI base URL:
   ```shell
    https://pokeapi.co/api/v2/
   
* Fetching Pokémon List:
1. Retrieve a paginated list of Pokémon:
    ```shell
   GET https://pokeapi.co/api/v2/pokemon?offset={offset}&limit={limit}
   
2. Replace {offset} to skip a number of entries.
  
3. Replace {limit} to set the number of results per request.
Example:
Copy code
   ```shell
    GET https://pokeapi.co/api/v2/pokemon?offset=0&limit=20

* Detailed Pokémon Data
Get detailed information about a specific Pokémon by ID or name:
   ```shell
  GET https://pokeapi.co/api/v2/pokemon/{id or name}

Example:
1. By ID:
    ```shell
    https://pokeapi.co/api/v2/pokemon/1 (Bulbasaur)
2. By Name:
    ```shell
    https://pokeapi.co/api/v2/pokemon/pikachu
    
3. Other Endpoints
* Pokémon Species:
   ```shell
    https://pokeapi.co/api/v2/pokemon-species/{id or name}
* Abilities: 
   ```shell
     https://pokeapi.co/api/v2/ability/{id or name}

* Types: https:
    ```shell
      //pokeapi.co/api/v2/type/{id or name}
      
### Documentation
For detailed information, visit the PokeAPI Documentation

### 🤝 Contributing
We welcome contributions! 

**🎉 Enjoy the game and become the ultimate Pokémon trainer! 🎉**

# Contributors
* Priya Verma


