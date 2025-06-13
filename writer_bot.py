"""
venna mani abhiram reddy 
css- 120
project:writer_bot
Generates random text using Markov chain analysis from a source text.
    """
SEED = 8
NONWORD = " "
import random
random.seed(SEED)

class MarkovChain:
    """Manages the Markov chain table and text generation."""
    def __init__(self):
        self.table = {}

    def build_table(self, words, prefix_size):
        """Builds the Markov chain table from the word list."""
        prefix = []
        for i in range(prefix_size):
            prefix.append(NONWORD)
        # Process each word to build the table
        for word in words:
            prefix_tuple = tuple(prefix)
            if prefix_tuple in self.table:
                self.table[prefix_tuple].append(word)
            else:
                self.table[prefix_tuple] = [word]
            # Update prefix: shift left and add new word
            for i in range(prefix_size - 1):
                prefix[i] = prefix[i + 1]
            prefix[prefix_size - 1] = word
        prefix_tuple = tuple(prefix)
        if prefix_tuple in self.table:
            self.table[prefix_tuple].append(NONWORD)
        else:
            self.table[prefix_tuple] = [NONWORD]

    def generate_text(self, words, prefix_size, num_words):
        """Generates random text based on the Markov chain table."""
        """PAPPAMAETRS: The `generate_text` method takes `self`
        , the class instance for the Markov chain's table; `words`,
          a string list for initial text; 
          `prefix_size`, an integer for context word count
          and `num_words`, an integer for total output words.
        ARRGRS: Arguments include `words`, 
        like `;`prefix_size`, like `2` for bigrams; 
        and `num_words`, like `10` for output length.
        RETURN: Returns a string list starting with `prefix_size`
          words from `words`, then random words from the table up 
          to `num_words`, like `["the", "cat", "in", "hat"]`."""
        generated = []
        # Start with the first prefix_size words from the input text
        for i in range(prefix_size):
            if i < len(words):
                generated.append(words[i])
            else:
                generated.append(NONWORD)
        prefix = []
        for i in range(prefix_size):
            prefix.append(generated[i])
        count = len(generated)
        while count < num_words:
            prefix_tuple = tuple(prefix)
            if prefix_tuple not in self.table or \
                len(self.table[prefix_tuple]) == 0:
                break
            suffixes = self.table[prefix_tuple]
            if len(suffixes) == 1:
                next_word = suffixes[0]
            else:
                index = random.randint(0, len(suffixes) - 1)
                next_word = suffixes[index]
            generated.append(next_word)
            count = count + 1
            # Update prefix
            for i in range(prefix_size - 1):
                prefix[i] = prefix[i + 1]
            prefix[prefix_size - 1] = next_word
        return generated

def main():
    filename = input()
    prefix_size = int(input())
    num_words = int(input())
    file = open(filename, 'r')
    words = []
    line = file.readline()
    while line:
        line_words = line.strip().split()
        for word in line_words:
            words.append(word)
        line = file.readline()
    file.close()
    markov = MarkovChain()
    markov.build_table(words, prefix_size)
    generated_text = markov.generate_text(words, prefix_size, num_words)
    # Print output: 10 words per line
    for i in range(len(generated_text)):
        if i % 10 == 0 and i > 0:
            print()
        if i > 0:
            print(" ", end="")
        print(generated_text[i], end="")
    print()
main()