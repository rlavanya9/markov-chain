"""Generate Markov text from text files."""

from random import choice, randint


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()

    return contents
  
print(open_and_read_file("green-eggs.txt"))

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    
    # your code goes here
    

    # text = open_and_read_file("green-eggs.txt")
    words = text_string.split()
    
    for word in (range(len(words)-2)): 
        digram_tuple  = (words[word], words[word + 1])
        if digram_tuple in chains:
            # chains.get(digram_tuple, [])
            chains[digram_tuple].append(words[word +2])
        else:
            chains[digram_tuple] = [words[word +2]]
    return chains    


def make_text(chains):
    """Return text from chains."""
   

    words = []
    keys_list = []

    # your code goes here
    # random_idx1 = randint(range(len(keys_list)))
    # original_key = keys_list[random_idx]
    # random_idx2 = randint(range(len(original_value)))
    # new_key = (original_key[1], keys_list[random_idx2])

    for keys in chains.keys():
        keys_list.append(keys)
    
    original_key = choice(keys_list)  # original_key = choice(list(chains)) 
    words.append(original_key[0])
    words.append(original_key[1])  
    while original_key in chains:
        original_value = chains[original_key]
        random_word = choice(original_value)
        words.append(random_word)
        # new_key = (original_key[1], random_word)
        original_key = (original_key[1], random_word)

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

print(chains)

# Produce random text
random_text = make_text(chains)

print(random_text)
