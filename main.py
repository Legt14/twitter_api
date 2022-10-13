from models import BaseTweets, Tweets, TweetDetail, Interactions, InteractionsDetail

from fastapi import FastAPI, Body, Path, status

app = FastAPI()


@app.get(
    path='/',
    status_code=status.HTTP_200_OK,
    tags=['Tweets'],
    summary= 'Tweet')
def root(
    tweets: Tweets,
    reactions: Interactions):

    result = tweets.dict
    result.update(reactions)

    return result


@app.post(
    path='/post',
    status_code=status.HTTP_201_CREATED,
    tags=['Tweets'],
    summary='Create post')
def create_tweets(
    tweet: BaseTweets = Body(...)):

    return {'tweet': tweet}


@app.get(
    path='/tweets/{tweet_id}',
    status_code=status.HTTP_202_ACCEPTED,
    tags=['Tweets'],
    summary='Detail tweet'
    )
def tweet_detail(
    tweet: TweetDetail,
    reaction_detail: InteractionsDetail,
    tweet_id: int=Path(..., gt=0)):

    result = tweet.dict
    result.update(reaction_detail)

    return {tweet_id:result}


@app.delete(
    path='/')
def delete_tweet():
    return

