# streaming.py

import requests
import json
import socketio  # Import the socketio instance
from data_logging import append_position_info_to_csv, append_order_info_to_csv, event_logger

def get_accounts(access_token):
    url = "https://api.tradestation.com/v3/brokerage/accounts"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_bars(access_token, symbol, barsback, lastdate):
    url = f"https://api.tradestation.com/v3/marketdata/barcharts/{symbol}?barsback={barsback}&lastdate={lastdate}"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    return response.json()


def stream_positions(access_token, account_ids, changes=False):
    # Construct the URL for streaming positions, including the 'changes' query parameter if needed.
    url = f"https://api.tradestation.com/v3/brokerage/stream/accounts/{account_ids}/positions"
    if changes:
        url += "?changes=true"

    headers = {"Authorization": f"Bearer {access_token}"}

    # Make a GET request with streaming enabled to continuously receive data.
    with requests.get(url, headers=headers, stream=True) as response:
        # Ensure the response status code is OK (200) before proceeding.
        if response.status_code == 200:
            # Iterate over each line in the streaming response.
            for line in response.iter_lines():
                # Ensure line is not empty.
                if line:
                    # Decode line (byte format) to string and print.
                    print(line.decode('utf-8'))
        else:
            # Print error status code if streaming was unsuccessful.
            print(f"Error streaming positions: {response.status_code}")

def start_streaming_positions(access_token, account_ids, changes=False):
    # Invoke the streaming functionality with the provided parameters.
    stream_positions(access_token, account_ids, changes)


# Existing code remains unchanged...

def stream_positions_with_details(access_token, account_ids, changes=False):
    # Convert list of account IDs to a comma-separated string if necessary
    account_ids_str = ','.join(account_ids) if isinstance(account_ids, list) else account_ids

    # Construct the streaming URL, append 'changes' query if specified
    url = f"https://api.tradestation.com/v3/brokerage/stream/accounts/{account_ids_str}/positions"
    if changes:
        url += "?changes=true"

    headers = {"Authorization": f"Bearer {access_token}"}

    # Make a GET request with streaming enabled
    with requests.get(url, headers=headers, stream=True) as response:
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    try:
                        # Parse the line as JSON and print details
                        json_data = json.loads(line)
                        print("#" * 80)
                        if "PositionID" in json_data:
                            print(f"Position ID: {json_data['PositionID']}, Symbol: {json_data['Symbol']}, Quantity: {json_data['Quantity']}")
                        else:
                            # Print any other JSON data received for inspection
                            print(json_data)
                        print("#" * 80)
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON: {e}")
        else:
            print(f"Error streaming positions: {response.status_code}")


def stream_bars(access_token, symbol = "MSFT"):


  url = f"https://api.tradestation.com/v3/marketdata/stream/barcharts/{symbol}"

  headers = {"Authorization": f"Bearer {access_token}"}

  response = requests.request("GET", url, headers=headers, stream=True)

  for line in response.iter_lines():
      if line:
          print(line)


def stream_positions_new(account_IDs, access_token, sio):  # Accept socketio instance as a parameter
    account_IDs_str = ",".join(account_IDs)
    
    url = f"https://sim-api.tradestation.com/v3/brokerage/stream/accounts/SIM1169695f/positions"
    print(url)
    headers = {"Authorization": f"Bearer {access_token}"}
    
    response = requests.request("GET", url, headers=headers, stream=True)
    
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            try:
                message = json.loads(decoded_line)
                # Concatenate key-value pairs into a single string
                message_str = ", ".join(f"{key}:{value}" for key, value in message.items())
                print(message_str)  # Print the concatenated message string for logging
                event_logger("Tradestation WS", message_str)
                sio.emit('update_data', {'message': message_str})  # Emit the single string
            except json.JSONDecodeError:
                print("Error decoding JSON")
                sio.emit('update_data', {'message': f'Error decoding JSON'})  # Emit the cleaned message

            except KeyError as e:
                print(f"Key error: {e}")
                sio.emit('update_data', {'message': f'Key error: {e}'})  # Emit the cleaned message



def get_positions(account_IDs, access_token):
  account_IDs_str = ",".join(account_IDs)

  # Assuming account_IDs is either a single ID or a list of IDs joined by commas already
  url = f"https://sim-api.tradestation.com/v3/brokerage/accounts/{account_IDs_str}/positions"
  
  headers = {"Authorization": f"Bearer {access_token}"}
  
  response = requests.request("GET", url, headers=headers)
  
  print(response.text)

def get_historical_orders(account_IDs, access_token):
  account_IDs_str = ",".join(account_IDs)

  url = f"https://api.tradestation.com/v3/brokerage/accounts/210A6482/historicalorders"
  print(url)
  querystring = {"since":"2024-01-03"}
  
  headers = {"Authorization": f"Bearer {access_token}"}
  
  response = requests.request("GET", url, headers=headers, params=querystring)

  # Assuming the response is in JSON format
  response_data = response.json()



  # Print the Orders content
  print("Response:", response_data)

  # Check if Orders is present and not empty
  if response_data.get('Orders'):
      print("Orders:")
      for order in response_data['Orders']:
          # Assuming each order is a dictionary, print each key-value pair
          for key, value in order.items():
              print(f"  {key}: {value}")
          print()  # Print a newline for readability between orders
  else:
      print("No orders found.")