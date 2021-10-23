import praw
import typing

import os
from dotenv import load_dotenv
load_dotenv()

def scrape_class(class_name: str) -> None:
    """
    Given the name of a class, return something...
    """
    reddit = praw.Reddit(
        client_id = os.getenv('CLIENT_ID'),
        client_secret = os.getenv('CLIENT_SECRET'),
        user_agent = os.getenv('USER_AGENT')
    )
