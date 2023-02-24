from typing import List, Any

import praw
import pandas as pd
import self as self
from praw.models import MoreComments

# Read-only instance


reddit_read_only = praw.Reddit(client_id="###########",  # your client id
                               client_secret="####################",  # your client secret
                               user_agent="#########")  # your user agent

# Authorized instance
reddit_authorized = praw.Reddit(client_id="UKF10WKArJCs5i1taIfQmQ",  # your client id
                                client_secret="uJMx1rcreYlBDtcsZm-GEAngxN2BBw",  # your client secret
                                user_agent="#######",  # your user agent
                                username="#########",  # your reddit username
                                password="#########")  # your reddit password

subreddit = reddit_read_only.subreddit("###############") # subredit name

for post in subreddit.hot(limit=100):
    print(post.title)
    print()

posts = subreddit.top(time_filter="year")
# Scraping the top posts of the current month

posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }

for post in posts:
    # Title of each post

    posts_dict["Title"].append(post.title)

    # Text inside a post

    posts_dict["Post Text"].append(post.selftext)

    # Unique ID of each post

    posts_dict["ID"].append(post.id)

    # The score of a post

    posts_dict["Score"].append(post.score)

    # Total number of comments inside the post

    posts_dict["Total Comments"].append(post.num_comments)

    # URL of each post
    posts_dict["Post URL"].append(post.url)

# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
top_posts
top_posts.to_csv("Top Posts.csv", index=True)


# URL of the post
url = " ################################################"

# Creating a submission object
submission = reddit_read_only.submission(url=url)

post_comments = {"Comments": [], "Score": []}

for comment in submission.comments:
    post_comments["Score"].append(comment.score)
    if type(comment) == MoreComments:
        continue
        # the ID of the comment

    post_comments["Comments"].append(comment.body)

# creating a dataframe
comments_df = pd.DataFrame(post_comments)
comments_df
comments_df.to_csv("Top Comments.csv", index=True)
