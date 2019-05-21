
import random
import MeCab

def get_file(filename):
    return open(filename, "r").read()

def wakati(text):
    # わかち書き
    tagger = MeCab.Tagger('-Owakati')
    result = tagger.parse(text)
    return result.split()

def make_markov_chain(wordlist):
    # マルコフ連鎖用のテーブルを作成
    markov = {}
    w1 = ""
    w2 = ""
    for word in wordlist:
        if w1 and w2:
            if (w1, w2) not in markov:
                markov[(w1, w2)] = []
            markov[(w1, w2)].append(word)
        w1, w2 = w2, word
    return markov

def generate_text(markov, sentence_num=10, min_length=30):
    # 文章の自動生成
    sentences = []
    sentence = ""
    w1, w2 = random.choice(list(markov.keys()))
    while len(sentences) < sentence_num:
        tmp = random.choice(markov[(w1, w2)])
        sentence += tmp
        if tmp == '。':
            if len(sentence) >= min_length:
                sentences.append(sentence)
            sentence = ""
        w1, w2 = w2, tmp

    return '\n'.join(sentences)

if __name__ == "__main__":
    markov = make_markov_chain(wakati(get_file('input.txt')))
    print(generate_text(markov))
