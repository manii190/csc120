def primary_stress_position(phoneme_list):
    index = 0
    while index < len(phoneme_list):
        if phoneme_list[index][-1] == '1': 
            return index
        index += 1
    return None