#auth.py

import requests
import os
from config import load_config
import json
from dotenv import load_dotenv

def get_access_token(): #### Tradestation access token
  credentials = load_config()
  url = "https://signin.tradestation.com/oauth/token"
  payload = f'grant_type=refresh_token&client_id={credentials["CLIENT_ID"]}&client_secret={credentials["CLIENT_SECRET"]}&refresh_token={credentials["REFRESH_TOKEN"]}'
  headers = {'Content-Type': 'application/x-www-form-urlencoded'}
  response = requests.post(url, headers=headers, data=payload)
  response_data = response.json()
  if 'access_token' in response_data:
    return response_data['access_token']
  else:
    print("Error obtaining access token:", response_data)


def get_api_key(): #### volumetrica rest api
  return os.environ.get('x_api_key')

load_dotenv()

def authenticate_user(): #### volumetrica trader login
  auth_url = "https://authdxfeed.volumetricatrading.com/api/auth/token"
  david_login = "augulis.david@gmail.com"
  david_password = os.environ.get('DAVID_PASSWORD')
  plt_key = os.environ.get('PLT_KEY')
  headers = {"PltfKey": plt_key}
  payload = {
      "login": david_login,
      "password": david_password,
      "withDetails": True,
      "version": 2,
      "environment": 0,
      "connectOnlyTrading": True
  }

  response = requests.post(auth_url, json=payload, headers=headers)
  if response.status_code == 200:
    auth_response = response.json()
    token = auth_response.get("token")
    wss_uri = response.headers.get("wss")
    print("Login successful. Token:", token)
    print("WebSocket URI:", wss_uri)
    return token, wss_uri
  else:
    print(
        f"Failed to authenticate. Status: {response.status_code}, {response.text}"
    )
    return None, None


def get_accounts(access_token):

  url = "https://sim-api.tradestation.com/v3/brokerage/accounts"

  headers = {"Authorization": f"Bearer {access_token}"}

  response = requests.request("GET", url, headers=headers)

  print(response.text)
