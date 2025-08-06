# Not running it but import it into python, like a module
def break_words(stuff):
    """ This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """ Sort the words. """
    return sorted(words)

def print_first_word(words):
    ''' Prints the first word after opoping it off. '''
    word = words.pop(0)
    print(word)
def print_last_word(words):
    ''' Prints the last word after opoping it off. '''
    word = words.pop(-1)
    print(word)
    
def sort_sentence(sentence):
    '''Take in the full sentence and return the sorted words.'''
    words = break_words(sentence)
    return sort_words(words)
    
def print_first_and_last(sentence):
    ''' Print the first and last words of the sentence.'''
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    ''' Sort the sentence and then Print the first and last words.'''
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

    