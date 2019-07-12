import urllib.request, urllib.parse, urllib.error
import oauth
import hidden

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

def augment(url, parameters):
    secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer(secrets['1zoYhdI1K5euxocBjzOS1IXvb'],secrets['0dGLKU2xOlswdpul96jG9uCi6Rh04PGyVpmEnpC6Mrt1g7AWSU'])
    token = oauth.OAuthToken(secrets['40464395-y76NWQwcNrphnaqAgKfcjs6Yjpxqdp6di2psBTEXz'], secrets['JidOgQiZ7cvMhRjEKi44V8scwa4KXi9AbGYKxWod53IV2'])

    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer,
                    token=token, http_method='GET', http_url=url,
                    parameters=parameters)
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(),
                               consumer, token)
    return oauth_request.to_url()


def test_me():
    print('* Calling Twitter...')
    url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
                  {'screen_name': 'drchuck', 'count': '2'})
    print(url)
    connection = urllib.request.urlopen(url)
    data = connection.read()
    print(data)

    print('=================================')
    headers = dict(connection.getheaders())
    print(headers)