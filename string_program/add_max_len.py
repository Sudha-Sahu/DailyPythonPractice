# create a function which take 2 argument 1. Sentence 2. k, return all the words which have a length greater thank k
def filter_len(sentence, k):
    out_string = ''
    for word in sentence.split(' '):
        if len(word) >= k:
            out_string += word + ' '
    return out_string


if __name__ == "__main__":
    string_ = "Hello Everyone, How are you?"
    _str = filter_len(string_, 5)
    print(_str)

