def comparison(_phrase_1, _phrase_2):
    if len(phrase_1) > len(phrase_2):
        print("Phrase_1 is longer than phrase_2")
    elif len(phrase_1) < len(phrase_2):
        print("Phrase_2 is longer than phrase_1")
    else:
        print("Phrases are the same length")
    return _phrase_1, _phrase_2


if __name__ == '__main__':
    print("Enter phrase_1: ")
    phrase_1 = str(input())
    print("Enter phrase_2: ")
    phrase_2 = str(input())
    comparison(phrase_1, phrase_2)


