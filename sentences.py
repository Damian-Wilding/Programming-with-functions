import random

def get_determiner(grammatical_number):
    if grammatical_number == 1:
        words = ['the', 'one']
    else:
        words = ['some', 'many']
    word = random.choice(words)
    return word

def get_noun(grammatical_number):
    if grammatical_number == 1:
        words = ['Batman', 'dude', 'toilet', 'bean', 'Jotoro']
    else:
        words = ['roommates', 'monster trucks', 'barnacles', 'pringles', 'penguins', 'phones', 'drunkards']
    word = random.choice(words)
    return word

def get_verb(grammatical_number, tense):
    if tense.lower() == 'past':
        words = ['killed', 'pooped', 'silenced', 'ran', 'flew', 'punched', 'died']
    elif tense.lower() == 'present':
        if grammatical_number == 1:
            words = ['kills', 'passes', 'speaks', 'tilts', 'blows up', 'eats']
        else:
            words = ['kill', 'eat', 'punch', 'fly', 'poop', 'nerd-out', 'grow']
    elif tense.lower() == 'future':
        words = ['will die', 'will speak', 'will watch', 'will commit', 'will try', 'will munch']
    word = random.choice(words)
    return word

def get_preposition():
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    word = random.choice(words)
    return word
        
def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    whole_shabang = f'{preposition} {determiner} {noun}'
    return whole_shabang


def main():
    grammatical_number = 1
    tense = 'past'
    determiner = get_determiner(grammatical_number)
    determiner = determiner.capitalize()
    noun = get_noun(grammatical_number)
    verb = get_verb(grammatical_number, tense)
    prep_phrase = get_prepositional_phrase(grammatical_number)
    print(f'{determiner} {noun} {verb} {prep_phrase}.')

    grammatical_number = 2
    tense = 'past'
    determiner = get_determiner(grammatical_number)
    determiner = determiner.capitalize()
    noun = get_noun(grammatical_number)
    verb = get_verb(grammatical_number, tense)
    prep_phrase = get_prepositional_phrase(grammatical_number)
    print(f'{determiner} {noun} {verb} {prep_phrase}.')
    
    grammatical_number = 1
    tense = 'present'
    determiner = get_determiner(grammatical_number)
    determiner = determiner.capitalize()
    noun = get_noun(grammatical_number)
    verb = get_verb(grammatical_number, tense)
    prep_phrase = get_prepositional_phrase(grammatical_number)
    print(f'{determiner} {noun} {verb} {prep_phrase}.')
    
    grammatical_number = 2
    tense = 'present'
    determiner = get_determiner(grammatical_number)
    determiner = determiner.capitalize()
    noun = get_noun(grammatical_number)
    verb = get_verb(grammatical_number, tense)
    prep_phrase = get_prepositional_phrase(grammatical_number)
    print(f'{determiner} {noun} {verb} {prep_phrase}.')
    
    grammatical_number = 1
    tense = 'future'
    determiner = get_determiner(grammatical_number)
    determiner = determiner.capitalize()
    noun = get_noun(grammatical_number)
    verb = get_verb(grammatical_number, tense)
    prep_phrase = get_prepositional_phrase(grammatical_number)
    print(f'{determiner} {noun} {verb} {prep_phrase}.')
    
    grammatical_number = 2
    tense = 'future'
    determiner = get_determiner(grammatical_number)
    determiner = determiner.capitalize()
    noun = get_noun(grammatical_number)
    verb = get_verb(grammatical_number, tense)
    prep_phrase = get_prepositional_phrase(grammatical_number)
    print(f'{determiner} {noun} {verb} {prep_phrase}.')
    

main()