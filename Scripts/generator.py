import json
import itertools
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def get_tags(list_items):
    tags = []
    for a, b in itertools.combinations(list_items, 2):
        tags.append(a + b)
    return tags


def get_has_tags(content):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(content)
    word_tokens = [word.lower() for word in word_tokens if word.isalpha()]
    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    word_dict = {}
    for word in filtered_sentence:
        lowercase_word = word.lower()
        if lowercase_word in word_dict.keys():
            word_dict[lowercase_word] += 1
        else:
            word_dict[lowercase_word] = 1

    list_of_words = sorted(word_dict.items(), reverse=True, key=lambda x: x[1])
    temp = []
    counter = 1
    for elem in list_of_words:
        if counter < 5:
            temp.append(elem[0].lower())
            counter = counter + 1
    return get_tags(temp)


def get_all_has_tags(description):
    return json.dumps({
        'tags': get_has_tags(description)
    })


if __name__ == '__main__':
    print("main")
