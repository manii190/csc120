def read_pronunciation_dict(filename):
    """
    loads a file containing a pronunciation
    dictionary and stores it in a dictionary.

    Parameters:
    filename (str): The filename of the
    pronunciation dictionary file.

    Returns: dict: A dictionary that associates
    each word with a list of phonemes and maps words to their pronunciations.
    """
    pron_dict = {}
    file = open(filename, 'r')
    # Iterate over each line in the file
    for line in file:
        line = line.strip()
        space_index = line.find(' ')
        if space_index != -1:
            word = line[:space_index].upper()
            pron = line[space_index + 1:].split()
            # Extract the pronunciation phonemes and split by space
        else:
            word = line.upper()
            pron = []
        # Add the pronunciation to the dictionary (create list if word is new)
        if word in pron_dict:
            pron_dict[word].append(pron)
        else:
            pron_dict[word] = [pron]
    file.close()
    return pron_dict
def extract_rhyme_patterns(pronunciations):
    """ selects rhyming schemes from the provided pronunciation list.
    Parameters:
    pronunciations (list): A collection of phoneme lists,
    each of which reflects a word's pronunciation.
    Returns: list: A collection of tuples, each of which includes the
    phoneme that comes before it as well as
    the phoneme that comes after the stressed vowel.
    """
    patterns = []
    for phonemes in pronunciations:
        i = 0
        while i < len(phonemes):
            # Search for the stressed vowel (phoneme with '1')
            if phonemes[i][-1] == '1':
                break 
            # Stop once we find the primary stress
            i += 1
        if i < len(phonemes):
            prev = phonemes[i - 1]
            # Append the preceding phoneme
            patterns.append((prev, phonemes[i:]))
    return patterns
def find_rhyming_words(dict, target, patterns):
    """ function looks for words that rhyme with the specified word.
    Parameters:
    The pronunciation dictionary that links words with
    their corresponding pronunciations is called dict (dict).
    The word whose rhymes need to be
    discovered is the target (str).
    patterns (list): The rhyme schemes gleaned
    from the pronunciations of the target word.
    Returns: list: A collection of words,
    including duplicates,
    that rhyme with the target word.
    """
    rhymes = []
    for word, prons in dict.items():
        # Iterate through all words and pronunciations in the dictionary
        if word != target:
            for phonemes in prons:
                # Check each pronunciation of other words
                i = 0
                while i < len(phonemes):  
                    # Search for the stressed vowel (phoneme with '1')
                    if phonemes[i][-1] == '1':
                        break
                    i += 1
                if i < len(phonemes):
                    rhyme_part = phonemes[i:]
                    if i > 0:
                        prev = phonemes[i - 1]
                    else:
                        prev = None
                        # Compare this rhyme part with the target's patterns
                    for t_prev, t_rhyme in patterns:
                        if rhyme_part == t_rhyme:
                            if prev != t_prev:
                                rhymes.append(word)
    return rhymes
def print_rhyming_words(rhyming_words):
    """
    Prints the list of rhyming words, one per line.

    Parameters:
        rhyming_words (list): A list of rhyming words to print.
    """
    i = 0
    # Initialize index for rhyming words
    while i < len(rhyming_words):
        # Iterate over all rhyming words
        print(rhyming_words[i])
        # Print the word
        i += 1
def main():
    dict = read_pronunciation_dict(input().strip())
    word = input().strip().upper()
    patterns = extract_rhyme_patterns(dict[word])
    rhyming_words = find_rhyming_words(dict, word, patterns)
    sorted_rhymes = sorted(rhyming_words)
    print_rhyming_words(sorted_rhymes)
main()