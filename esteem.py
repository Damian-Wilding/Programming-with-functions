def main():
    score = 0
    print('For each question, enter "A" for strongly agree, "a" for agree, "d" for disagree", and "D" for strongly disagree.')
    answer = input('I feel that I am a person of worth, at least on an equal plane with others.')
    score += positive_question(answer)
    answer = input('I feel that I have a number of good qualities.')
    score += positive_question(answer)
    answer = input('All in all, I am inclined to feel that I am a failure.')
    score += negative_question(answer)
    answer = input('I am able to do things as well as most other people.')
    score += positive_question(answer)
    answer = input('I feel I do not have much to be proud of.')
    score += negative_question(answer)
    answer = input('I take a positive attitude toward myself.')
    score += positive_question(answer)
    answer = input('On the whole, I am satisfied with myself.')
    score += positive_question(answer)
    answer = input('I wish I could have more respect for myself.')
    score += negative_question(answer)
    answer = input('I certainly feel useless at times.')
    score += negative_question(answer)
    answer = input('At times I think I am no good at all.')
    score += negative_question(answer)
    print(f'Your score is: {score}')
    if score < 15:
        print('Bruh you good? You may have a problematic low self-esteem issue.')

def positive_question(answer):
    points = 0
    if answer == 'A':
        points = 3
    elif answer == 'a':
        points = 2
    elif answer == 'd':
        points = 1
    elif answer =='D':
        points = 0
    else:
        print("bruh that isn't a valid option")
    return points

def negative_question(answer):
    points = 0
    if answer == 'A':
        points = 0
    elif answer == 'a':
        points = 1
    elif answer == 'd':
        points = 2
    elif answer =='D':
        points = 3
    else:
        print("bruh that isn't a valid option")
    return points
    

main()