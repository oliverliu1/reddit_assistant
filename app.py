import os
from src.get_text import call_api, parse_text
from src.text_analyze import summarize


CLIENT_ID = os.environ.get('CLIENT_ID')
SECRET_KEY = os.environ.get('SECRET_KEY')
USERNAME = os.environ.get('REDDIT_USERNAME')
PASSWORD = os.environ.get('REDDIT_PASSWORD')


if __name__ == '__main__':
    data = call_api(CLIENT_ID, SECRET_KEY, USERNAME, PASSWORD)
    text = parse_text(data)
    print(summarize(text))
