'''
File: pokemon.py
name:mani abhiram reddy
Course: CSC 120, Spring 2025
Purpose: This programming project processes
Pokémon data and handles queries about it.
'''
def read_file_and_store_data(filename):
    """
    The function obtains Pokémon information 
    from CSV files through a dictionary structure. 
    categorized by Pokémon type.

    Args:
        The function needs the file name string called
        filename to read Pokémon data from the CSV file.

    Returns:
        The method returns a dictionary structure 
        whose keys represent 
        Pokémon types and each type contains an 
        associated dictionary structure
        The dictionary keys represent Pokémon names while
        the values consist of dictionaries 
        which hold Pokémon statistical information.
    """
    file = open(filename, "r")
    pokemon_data = {}

    for line in file:
        line = line.strip()
        if line and line[0] != "#":
            values = line.split(",")
            if len(values) >= 12:  
                # Ensure the line has enough columns
                name = values[1]
                type1 = values[2] 
                stats = {
                    "Total": int(values[4]),
                    "HP": int(values[5]),  
                    "Attack": int(values[6]),  
                    "Defense": int(values[7]),
                    "SpecialAttack": int(values[8]),
                    "SpecialDefense": int(values[9]),
                    "Speed": int(values[10]) 
                }

                if type1 not in pokemon_data:
                    pokemon_data[type1] = {}
                pokemon_data[type1][name] = stats  
                # Use a nested dictionary

    file.close()
    return pokemon_data


def compute_average_stats(pokemon_data):
    """
    Computes the average stats for each Pokémon type.

    Args:
        The pokemon_data (dict) contains 
        Pokémon types as keys which 
        point to dictionaries that include 
        Pokémon names as keys 
        and their stats as dictionary values.
        The keys within the dictionary represent
        Pokémon names and each Pokémon name contains 
        another dictionary with their 
        respective statistical information.

    Returns:
        A data structure is defined that 
        contains Pokémon types
        as keys which link to inner dictionaries that 
        show Pokémon names alongside 
        their statistic details. 
        The function calculates average statistics
        from the Total, HP, Attack and 
        Defense plus SpecialAttack, SpecialDefense, Speed measurements.
    """
    average_stats = {}

    for poke_type, pokemons in pokemon_data.items():
        count = len(pokemons)
        total_sum = 0
        hp_sum = 0
        attack_sum = 0
        defense_sum = 0
        sp_attack_sum = 0
        sp_defense_sum = 0
        speed_sum = 0

        for stats in pokemons.values():
            total_sum += stats["Total"]
            hp_sum += stats["HP"]
            attack_sum += stats["Attack"]
            defense_sum += stats["Defense"]
            sp_attack_sum += stats["SpecialAttack"]
            sp_defense_sum += stats["SpecialDefense"]
            speed_sum += stats["Speed"]

        average_stats[poke_type] = {
            "Total": total_sum / count,
            "HP": hp_sum / count,
            "Attack": attack_sum / count,
            "Defense": defense_sum / count,
            "SpecialAttack": sp_attack_sum / count,
            "SpecialDefense": sp_defense_sum / count,
            "Speed": speed_sum / count
        }

    return average_stats


def process_and_find_max_averages(averages):
    """
    The function locates Pokémon types 
    that demonstrate the maximum statistical
    averages across all stats.
    The function handles user query 
    inputs for displaying Pokémon 
    types which achieve the highest levels 
    by statistical analysis. 
    average values for the specified stat.

    Args:
        The values in averages (dict)
    appear as keys of Pokémon types while each value 
    contains dictionaries of stat average metrics 
    (Total, HP, Attack, Defense, SpecialAttack, SpecialDefense, Speed). 
    The dictionary contains average statistics for 
    Total, HP, Attack, Defense, SpecialAttack, SpecialDefense, Speed.
    
    Returns:
        The system uses this module to display the result
        output after user query processing.
    """
    stats = ["Total", "HP", "Attack", "Defense",
            "SpecialAttack", "SpecialDefense", "Speed"]
    
    # Initialize the dictionary to store max averages
    max_averages = {}
    stat_index = 0
    while stat_index < len(stats):
        stat = stats[stat_index]
        max_value = -1  
        max_types = [] 

        # Use a for loop to iterate through Pokémon types
        for poke_type in averages:
            current_value = averages[poke_type][stat]
            if current_value > max_value:
                max_value = current_value
                max_types = [poke_type]
            elif current_value == max_value:
                max_types.append(poke_type)

        # Store the result for the current stat
        max_averages[stat] = (max_value, max_types)

        stat_index += 1  # Move to the next stat
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

    # Process queries repeatedly until an empty line is entered
    done = False  # Flag to control the loop
    while not done:
        query = input().strip().lower()
        if query == "":
            done = True
        elif query in query_map:
            stat = query_map[query]
            if stat in max_averages:
                max_value, max_types = max_averages[stat]
                for poke_type in sorted(max_types):
                    # Print the value using string concatenation
                    print(poke_type + ": " + str(max_value))
def main():
    """
    The main function runs the developed program. 
    The application reads Pokémon data points from the file to
    perform calculations for average statistics. 
    User queries lead to process queries for obtaining highest 
    average values for each stat through this function.

    Args:
        None

    Returns:
        None
    """
    filename = input().strip()
    pokemon_data = read_file_and_store_data(filename)
    averages = compute_average_stats(pokemon_data)
    process_and_find_max_averages(averages)
main()