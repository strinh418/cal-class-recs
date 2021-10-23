import nltk
from nltk.corpus import stopwords
import string
from collections import Counter


sw = stopwords.words('english')
other_words = ['professor', 'computer', 'science', 'berkeley', 'hes', 'im',]
sw.extend(other_words)


def most_common_keywords(lst, k=10):
    c = Counter()
    for p in lst:
        p = p.lower() # lowercase the words
        p = p.translate(str.maketrans('', '', string.punctuation))
        p = p.split()
        for w in p:
            if w not in sw:
                c[w] += 1
    common = c.most_common(k)
    for t in common:
        print(t)
    return common

reddit_quotes = [
    'I had such low expectations and I still managed to fail my expectations.',
    "big facts, 170 was decently cool (coming from someone who really enjoyed 70... I thought I'd like 170 more than I actually did... it got a little too abstract for my liking near the end but the coding final project is definitely super fun)",
    "I can tell you right now that if you hate theory and proofs then you'll hate CS170 and it will feel like a slog. ",
    "This class is the worst fucking thing I've ever seen. The amount of mismanagement amongst staff is unheard of and completely unacceptable, especially for a class of its size. ",
    "It wasn’t as bad as last time I feel",
    "I'm worried because it was a less brutal than the first one but I'm pretty sure I didn't do as well on it so I'm gonna be on the really low end of the curve :/"
]

rmp_quotes = [
    "DeNero is hilarious and a great professor. Lectures and expectations are super clear",
    " His lectures are very clear, the exams are straightforward, and he gives the best curves.",
    " Super annoying. I'm not bitter reviewing because of a bad gradeI did well in the class, I just hated every second of it.",
    "This guy very clearly cares about teaching his students, and he's a very good lecturer. However, he's a genius, and he has an extremely hard time understanding when students don't \"get\" what he's saying."
]

phrases = reddit_quotes + rmp_quotes

most_common_keywords(phrases)