import os
import streamlit as st
from src.get_text import call_api, parse_text
from src.text_analyze import summarize


CLIENT_ID = os.environ.get('CLIENT_ID')
SECRET_KEY = os.environ.get('SECRET_KEY')
USERNAME = os.environ.get('REDDIT_USERNAME')
PASSWORD = os.environ.get('REDDIT_PASSWORD')


subreddits = [
              'cscareerquestions',
              'askcarsales',
              'golf',
              'askbattlestations',
              'talesfromtechsupport',
              'bestoflegaladvice'
              ]

if __name__ == '__main__':
    subreddit = st.selectbox(
                             label='Choose a subreddit',
                             options=subreddits
                             )
    data = call_api(CLIENT_ID, SECRET_KEY, USERNAME, PASSWORD, subreddit)
    text = parse_text(data)
    st.write(summarize(text))
