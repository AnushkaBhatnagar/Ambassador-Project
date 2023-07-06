from flask import Flask, redirect, request, session, url_for
from flask_oauthlib.client import OAuth, OAuthException
from db import access_db


app = Flask(__name__)
app.secret_key = 'development'

oauth = OAuth(app)

azure_ad = oauth.remote_app(
    'azure_ad',
    consumer_key='288235a8-2417-4a52-9ec9-29fa5b4f6b0f',
    consumer_secret='5d3414a1-5d09-4acd-9c54-8119f4afbb6c',
    request_token_params={'scope': 'openid email profile'},
    base_url='https://login.microsoftonline.com/common/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://login.microsoftonline.com/common/oauth2/v2.0/token', 
    authorize_url='https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
)

@app.route('/login')
def login():
    return azure_ad.authorize(callback=url_for('authorized', _external=True))

@app.route('/authorized')
def authorized():
    response = azure_ad.authorized_response()
    if response is None or isinstance(response, OAuthException):
      return 'Access denied: reason=%s error=%s' % (
            response.get('error'), 
            response.get('error_description')
        )
    
    session['access_token'] = response['access_token']
    session['refresh_token'] = response['refresh_token']

    return redirect('/')


@app.route('/protected')
def protected():
    if 'access_token' not in session:
        return 'Unauthorized'
    
    access_token = session['access_token']

    return 'Protected'


@app.route("/")
def hello():
  # s = access_db("SELECT * FROM Persons;")
  # print(s)
  return "Hello World!"

if __name__ == "__main__":
  app.run(debug=True, port=8000)
