pip install requests

import requests

# LinkedIn API credentials
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
REDIRECT_URI = 'https://your-redirect-uri'

# Authorization URL
AUTH_URL = f'https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&state=123456'

# Redirect the user to the authorization URL
print('Please visit the following URL to authorize the application:')
print(AUTH_URL)
auth_code = input('Enter the authorization code: ')

# Access token request URL
TOKEN_URL = 'https://www.linkedin.com/oauth/v2/accessToken'

# Exchange the authorization code for an access token
response = requests.post(TOKEN_URL, params={
    'grant_type': 'authorization_code',
    'code': auth_code,
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'redirect_uri': REDIRECT_URI
})

# Extract the access token from the response
access_token = response.json()['access_token']


# Profile API URL
PROFILE_URL = 'https://api.linkedin.com/v2/me'

# Send API request to retrieve profile information
headers = {
    'Authorization': f'Bearer {access_token}',
    'Connection': 'Keep-Alive'
}
response = requests.get(PROFILE_URL, headers=headers)

# Print the profile data
profile_data = response.json()
print(profile_data)


import json

# Save profile data to
