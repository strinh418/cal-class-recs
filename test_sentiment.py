from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sa = SentimentIntensityAnalyzer()

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

def rate_list(lst):
    "Rates everything in a list."
    for q in lst:
        print(f'Quote: {q}')
        rating = sa.polarity_scores(q)['compound']
        print(f'Rating: {rating}')
        print('\n')
    print('\n\n')

def overall_rating(lst, kw):
    "Finds the average rating of everything in the list."
    counter = 0
    rating = 0
    for q in lst:
        rating += sa.polarity_scores(q)['compound']
        counter += 1
    print(f'OVERALL RATING FOR {kw}: {rating/counter}')

def highest_lowest(lst):
    "Prints the highest and lowest items in the list."
    ratings = []
    for q in lst:
        rating = sa.polarity_scores(q)['compound']
        ratings.append((q, rating))
    positive = max(ratings, key=lambda t: t[1])
    negative = min(ratings, key=lambda t: t[1])
    print(f'Most positive comment: {positive[0]}')
    print(f'Rating: {positive[1]}')
    print(f'Most negative comment: {negative[0]}')
    print(f'Rating: {negative[1]}')

# rate_list(reddit_quotes)
# rate_list(rmp_quotes)
highest_lowest(reddit_quotes+rmp_quotes)
overall_rating(reddit_quotes+rmp_quotes, 'CS170')