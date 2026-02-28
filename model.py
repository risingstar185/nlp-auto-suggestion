import textdistance
import re
from collections import Counter

# ===== Load Text File =====
with open(r"C:\Users\Admin\Downloads\autocorrect book.txt", "r", encoding="utf-8") as f:
    text = f.read()

# ===== Preprocessing =====
data = text.lower()
words = re.findall(r'\w+', data)

# ===== Word Frequency =====
word_freq = Counter(words)

# ===== Probability Calculation =====
total_freq = sum(word_freq.values())
probs = {word: word_freq[word] / total_freq for word in word_freq.keys()}


# ===== Autocorrect Function =====
def autocorrect(word, top_n=5):
    word = word.lower()

    # If word exists
    if word in probs:
        return [(word, 1.0, probs[word])]

    similarities = []

    for vocab_word in word_freq.keys():
        similarity = 1 - textdistance.Jaccard().distance(word, vocab_word)

        similarities.append(
            (vocab_word, similarity, probs[vocab_word])
        )

    # Sort by similarity first, then probability
    similarities = sorted(
        similarities,
        key=lambda x: (x[1], x[2]),
        reverse=True
    )

    return similarities[:top_n]
