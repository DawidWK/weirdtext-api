import re
from encoder import can_encode


def decode_sentence(sentence, orginal_words):
    """
    Decode only if the sentence has a magic separator at the beginning and at the end.

    Args:
        sentence (string): sentence, can contains special characters.
        orginal_words (string): orgnial_words in alphabetical order separated with space bar

    Returns:
        string: decoded sentence
    """
    SEPARATOR = "\n—weird—\n"
    words_span = []
    output = []

    if sentence[0:9] != SEPARATOR or sentence[-9:] != SEPARATOR:
        raise ValueError("'sentence' is not encoded with weirdtext encoder")

    sentence = sentence[len(SEPARATOR):-len(SEPARATOR)]

    output_sentence = list(sentence)

    tokenize_re = re.compile(r'(\w+)', re.U)
    processed_sentence = tokenize_re.findall(sentence)  # list of all words without special characters and without magic separator

    for word in processed_sentence:
        word_list = list(word)
        word_part = word_list[1 : len(word_list) - 1]
        if len(word_list) > 3 and can_encode(word_part):
            output.append(decode_word(word, orginal_words))
        else:
            output.append(word)

    for match in tokenize_re.finditer(sentence):  # gets span of words excluded special character
        words_span.append(match.span())

    for i, word_span in enumerate(words_span):
        output_sentence[word_span[0]:word_span[1]] = output[i]

    return "".join(output_sentence)


def decode_word(word, orginal_words):
    """
    Decode word only if available in orginal_words list,
    With binary search algorithm lookup for a word with the same first character,
    after that pointers move back to the first word with the same first character
    then it checks if the word can be made with the same characters

    Args:
        word (string): sentence, can contains special characters.
        orginal_words (string): orgnial_words in alphabetical order separated with space bar

    Returns:
        string: decoded sentence
    """
    words_list = orginal_words.split(" ")
    is_same_word = True
    left = 0
    right = len(words_list) - 1
    tmp_hash = {}
    while (left <= right):
        mid = (left + right) // 2
        if (words_list[mid][0].lower() == word[0].lower()):  # word with same starting character
            left = mid  # only for naming convenience switch pointer
            while left >= 0 and words_list[left][0].lower() == word[0].lower() :  # move pointer to first word with same starting character
                left = left - 1
            left += 1  # move pointer back to position where is first word with same starting character
            while left < len(words_list) and words_list[left][0].lower() == word[0].lower():  # iterate through all words with same starting character
                if (len(words_list[left]) == len(word)):  # check if words are the same lenght
                    if (words_list[left][-1].lower() == word[-1].lower()):  # check if words last char is the same
                        for char in words_list[left]:  # save the number of each letter in orginal word
                            if char in tmp_hash:
                                tmp_hash[char] += 1
                            else:
                                tmp_hash[char] = 1
                        for char in word:
                            if char in tmp_hash and tmp_hash[char] != 0:  # compare the number of letters in encoded word and orginal
                                tmp_hash[char] -= 1
                            else:
                                is_same_word = False
                                break
                        if is_same_word:
                            return words_list[left]
                left += 1
            raise ValueError("word is not in orginal word list")

        elif (words_list[mid][0].lower() < word[0].lower()):
            left = mid + 1
        else:
            right = mid - 1

    raise ValueError("word is not in orginal word list")


if __name__ == "__main__":
    input = "\n—weird—\nTihs is a lnog loonog tset setncene,\nwtih smoe big (biiiiig) wdros!\n—weird—\n"
    orginal_words = "long looong sentence some test This with words"
    word = "tsdet"

    print(decode_sentence(input, orginal_words))
