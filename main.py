import tweepy

CONSUMER_KEY = 'OUlITy1hWl9xMXMwNWlDNGVyWmw6MTpjaQ'
CONSUMER_SECRET = 'dwY2lOYLrrZnLQ6zqMHX-d6QoZPq6rCAYXx9C8DS_b70MMLdn8'
ACCESS_KEY = '1524089119697211392-ZSlDBhrWNgBKqQWDpiqYuScTY5DDVp'
ACCESS_SECRET = 'CkObLuwfTqfJ6smVhPNRdvfJLCUJC5e69Yv04ieUVlJEf'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()
type(mentions)

mentions[0].__dict__.keys()
