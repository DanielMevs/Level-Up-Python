import secrets


def generate_passphrase(num_words, word_list_path='diceware.wordlist.asc'):
    with open(word_list_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]

    words = [secrets.choice(word_list) for i in range(num_words)]
    return ' '.join(words)