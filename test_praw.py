import praw
import typing

import os
from dotenv import load_dotenv
from test_keywords import most_common_keywords
from test_sentiment import overall_rating, highest_lowest
load_dotenv()

# Returns a subreddit instance with the given name
def get_subreddit(name):
    reddit = praw.Reddit(
        client_id = os.getenv('CLIENT_ID'),
        client_secret = os.getenv('CLIENT_SECRET'),
        user_agent = os.getenv('USER_AGENT')
    )
    return reddit.subreddit(name)

# Filters a list of submissions and only returns those that satisfy condition
def filter_submissions(submissions):
    condition = lambda s : 'waitlist' not in s
    return [s for s in submissions if condition(s.title)]

def get_submissions(search_term, subreddit_name, limit):
    subreddit = get_subreddit(subreddit_name)
    submissions = filter_submissions(subreddit.search(search_term))
    return submissions if not limit else submissions[:limit]

def get_comments(search_term, subreddit_name, submission_limit=None):
    submissions = get_submissions(search_term, subreddit_name, submission_limit)
    comments = []
    for submission in submissions:
        for comment in submission.comments:
            comments.append(comment.body)
    return comments

comments = get_comments('cs70', 'berkeley', 8)
print(comments)
overall_rating(comments, 'cs70')
highest_lowest(comments)