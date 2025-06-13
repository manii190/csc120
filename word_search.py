'''
File: pokemon.py
Author: Tezza Reddy
Course: CSC 120, Spring 2025
Purpose: This programming project processes 
Pokémon data and handles queries about it.
'''
def read_pokemon_data(filename):
    '''
    Reads Pokémon data from a CSV file and organizes 
    it by Pokémon type.
    Args:
        filename (str): The name of the file containing 
        Pokémon data.
    Returns:
        dict: A dictionary where keys are Pokémon types 
        and values are lists of Pokémon stats.
    '''
    pokemon_data = {}
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        # Skip comment lines (lines starting with '#')
        if len(line) > 0 and line[0] != "#":
            fields = line.strip().split(",")
            if len(fields) >= 12:
                name = fields[1]
                type1 = fields[2]
                total = int(fields[4])
                hp = int(fields[5])
                attack = int(fields[6])
                defense = int(fields[7])
                special_attack = int(fields[8])
                special_defense = int(fields[9])
                speed = int(fields[10])

                if type1 not in pokemon_data:
                    pokemon_data[type1] = []
                pokemon_data[type1].append({
                    "Total": total,
                    "HP": hp,
                    "Attack": attack,
                    "Defense": defense,
                    "SpecialAttack": special_attack,
                    "SpecialDefense": special_defense,
                    "Speed": speed
                })
    return pokemon_data

def compute_averages(pokemon_data):
    '''
    Computes the average stats for each Pokémon type.
    Args:
        pokemon_data (dict): A dictionary where keys 
        are Pokémon types and values are lists of Pokémon stats.
    Returns:
        dict: A dictionary where keys are Pokémon 
        types and values are dictionaries of average stats.
    '''
    averages = {}
    for poke_type, pokemon_list in pokemon_data.items():
        totals = {
            "Total": 0,
            "HP": 0,
            "Attack": 0,
            "Defense": 0,
            "SpecialAttack": 0,
            "SpecialDefense": 0,
            "Speed": 0
        }
        count = len(pokemon_list)
        for pokemon in pokemon_list:
            for key in totals:
                totals[key] += pokemon[key]
        averages[poke_type] = {key: totals[key] / count for key in totals}
    return averages

def find_max_averages(averages):
    '''
    Finds the Pokémon types with the highest average 
    values for each stat.
    Args:
        averages (dict): A dictionary where keys are Pokémon 
        types and values are dictionaries of average stats.
    Returns:
        dict: A dictionary where keys are stats and values 
        are tuples of (max_value, list of types with max_value).
    '''
    max_averages = {}
    stats = ["Total", "HP", "Attack", "Defense", "SpecialAttack", "SpecialDefense", "Speed"]
    for stat in stats:
        max_value = -1
        max_types = []
        for poke_type, stats_dict in averages.items():
            if stats_dict[stat] > max_value:
                max_value = stats_dict[stat]
                max_types = [poke_type]
            elif stats_dict[stat] == max_value:
                max_types.append(poke_type)
        max_averages[stat] = (max_value, max_types)
    return max_averages

def process_queries(max_averages):
    '''
    Processes user queries and prints the Pokémon types with
    the highest average values for the specified stat.
    Args:
        max_averages (dict): A dictionary where keys are stats 
        and values are tuples of (max_value, list of types with max_value).
    '''
    while True:
        query = input().strip().lower()
        if query == "":
            return  # Stop processing queries
        else:
            # Map user-friendly query names to internal stat names
            query_map = {
                "total": "Total",
                "hp": "HP",
                "attack": "Attack",
                "defense": "Defense",
                "specialattack": "SpecialAttack",
                "specialdefense": "SpecialDefense",
                "speed": "Speed"
            }
            if query in query_map:
                stat = query_map[query]
                if stat in max_averages:
                    max_value, max_types = max_averages[stat]
                    for poke_type in sorted(max_types):
                        # Print the value with full precision
                        print(f"{poke_type}: {max_value}")

def main():
    filename = input().strip()
    pokemon_data = read_pokemon_data(filename)
    averages = compute_averages(pokemon_data)
    max_averages = find_max_averages(averages)
    process_queries(max_averages)

if _name_ == "_main_":
    main()