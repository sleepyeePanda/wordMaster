from random import shuffle
words = {'English': 'Korean', 'apple': '사과', 'banana': '바나나', 'cat': '고양이', 'dragon': '용'}

def wordGenerator(words):
    keys = list(words.keys())
    shuffle(keys)
    for eng in keys:
        yield eng
g = wordGenerator(words)
for i in range(5):
    print(next(g))