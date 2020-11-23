from random import randint
import copy

story = (
        "One day I and my {} friend decided to go to the {} game in {}." +
        "We really wanted to see the {} play the {}." +
        "So, we {} are {} down to the {} and bought some ()'s." +
        "We got into the game and it was lot of fun." +
        "We are same {} {} and drank some {} {}." +
        "We had a great time and we will go again."
)

word_dict = {
    'adjective': ['greedy', 'harsh', 'abrasive', 'tasty'],
    'city name': ['Dhaka', 'Chicago', ' Canada', 'NYC'],
    'noun': ['Hasnat', 'Osman', 'Khaled', 'Raj'],
    'action': ['Play', 'Game', 'Run'],
    'sports noun': ['Cricket', 'Football', 'Handball'],
    'place': ['park', 'desert', 'forest', 'store']

}


def get_word(type, local_dict):
    words = local_dict[type]
    cnt = len(words) - 1
    index = randint(0, cnt)
    return local_dict[type].pop(index)


def create_story():
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('adjective', local_dict),
        get_word('sports noun', local_dict),
        get_word('city name', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('action', local_dict),
        get_word('noun', local_dict),
        get_word('place', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict),
    )


print("Story 1: ")
print(create_story())
