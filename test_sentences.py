import random
from sentences import get_determiner, get_noun, get_verb, get_prepostion, get_prepostional_phrase
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["the", "one"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        word = get_determiner(1)
        # Verify that the word returned from get_determiner is
        # one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    single_nouns = ['Batman', 'dude', 'toilet', 'bean', 'Jotoro']
    for _ in range(12):
        word = get_noun(1)
        assert word in single_nouns
    plural_nouns = ['roommates', 'monster trucks', 'barnacles', 'pringles', 'penguins', 'phones', 'drunkards']
    for _ in range(12):
        word = get_noun(2)
        assert word in plural_nouns

def test_get_verb():
    future_verbs = ['will die', 'will speak', 'will watch', 'will commit', 'will try', 'will munch']
    past_verbs = ['killed', 'pooped', 'silenced', 'ran', 'flew', 'punched', 'died']
    present_singular_verbs = ['kills', 'passes', 'speaks', 'tilts', 'blows up', 'eats']
    present_plural_verbs = ['kill', 'eat', 'punch', 'fly', 'poop', 'nerd-out', 'grow']
    for _ in range(20):
        word = get_verb(1, 'future')
        assert word in future_verbs
    for _ in range(20):
        word = get_verb(2, 'future')
        assert word in future_verbs
    for _ in range(20):
        word = get_verb(1, 'past')
        assert word in past_verbs
    for _ in range(20):
        word = get_verb(2, 'past')
        assert word in past_verbs
    for _ in range(20):
        word = get_verb(1, 'present')
        assert word in present_singular_verbs
    for _ in range(20):
        word = get_verb(2, 'present')
        assert word in present_plural_verbs





def main():
    test_get_determiner()
    test_get_noun()
    test_get_verb()

if 'test_sentences.py' == "__main__":
    main()

pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])