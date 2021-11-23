import random
import re


def encode_sentence(sentence):
    """
    Encode the sentence, and returns tuple with encoded_sentence and orginal_words.

    Args:
        sentence (string): sentence, can contains special characters.

    Returns:
        tuple: [string]encoded sentence and [string]orginal words list, 
        orgnial_words are sorted in alphabetic order separated with spacebar 
    """
    SEPARATOR = "\n—weird—\n"
    output_sentence = list(sentence)
    words_span = []
    encoded_words = []
    sorted_orginal_words = []

    tokenize_re = re.compile(r'(\w+)', re.U)
    processed_sentence = tokenize_re.findall(sentence)  # list of all words without special characters

    for match in tokenize_re.finditer(sentence):  # gets span of words excluded special character
        words_span.append(match.span())

    for word in processed_sentence:
        encoded_output = encode_word(word)
        encoded_words.append(encoded_output[0])
        if encoded_output[1] is not None:
            sorted_orginal_words.append(encoded_output[1])

    for i, word_span in enumerate(words_span):
        output_sentence[word_span[0]:word_span[1]] = encoded_words[i]

    output_sentence = "".join(output_sentence)
    sorted_orginal_words.sort(key=lambda v: v.upper())  # sort and ignore upper/lower case
    sorted_orginal_words = " ".join(sorted_orginal_words)

    return ((SEPARATOR + output_sentence + SEPARATOR, sorted_orginal_words))


def encode_word(word):
    """
    Encode the word, and returns a tuple with encoded_word and orginal_word.

    Args:
        word (string): word without special characters.

    Returns:
        tuple: encoded word and orginal word, if orgninal and encoded word is 
        the same returns only encoded word and None value
    """
    word_list = list(word)
    if len(word_list) <= 3:
        return (word, None)

    word_part = word_list[1 : len(word_list) - 1]

    if not can_encode(word_part):
        return (word, None)

    while True:
        random.shuffle(word_part)
        encoded_word = (
            f"{word_list[0]}{''.join(word_part)}{word_list[len(word_list ) - 1]}"
        )
        if encoded_word != word:
            break

    return (encoded_word, word)


def can_encode(word_part):
    """
    Check if the middle part of the word can be randomized

    Args:
        word_part (list): List of words character without first and last letter.

    Returns:
        Bool: True for success, False otherwise.
    """
    for i in range(1, len(word_part)):
        if word_part[0] != word_part[i]:
            return True
    return False


if __name__ == "__main__":
    input = "This is a long looong test sentence,\nwith some big (biiiiig) words!"
    print(encode_sentence(input))
