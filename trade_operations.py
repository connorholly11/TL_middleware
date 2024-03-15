import requests
from auth import get_access_token
import time
import getpass
import os

username = getpass.getuser()
access_token = get_access_token()
username = getpass.getuser()

def send_orders(access_token, symbol, quantity, trade_action):
    url = "https://sim-api.tradestation.com/v3/orderexecution/orders"

    payload = {
        "AccountID": "SIM1169695f",
        "Symbol": symbol,
        "Quantity": str(quantity),
        "OrderType": "Market",
        "TradeAction": trade_action,
        "TimeInForce": {"Duration": "DAY"},
        "Route": "Intelligent"
    }

    print(payload)

    headers = {
        "content-type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)

def trade_copier(row):
    print('Entering trade_copier function')
    original_action = '1' if row['FilledQty'] > 0 else '2'  # 1 = long, 2 = short
    flipped_action = '2' if original_action == '1' else '1'
    symbol = row['FeedSymbol']
    price = row['AvgPrice']
    quantity = abs(row['FilledQty'])


    converted_symbol_nt = symbol
    converted_symbol_ts = symbol.replace('/', '')
    converted_symbol_ts = symbol.replace(':XCME', '')

    trade_action = "BUY" if original_action == "1" else "SELL"  # should be fading like this

    # Generate the OIF order string
    NT_order = f"PLACE;Sim101;{converted_symbol_nt};{trade_action};{quantity};MARKET;;;DAY;;;;"

    # Generate a filename with the current timestamp in nanoseconds
    timestamp_ns = int(time.time() * 1e9)
    file_name = f"oif{timestamp_ns}.txt"

    # Define the file path including the dynamic file name
    file_path = rf"C:\Users\{username}\Documents\NinjaTrader 8\incoming\{file_name}"

    # Save the NT_order string into the dynamically named file
    with open(file_path, 'w') as file:
        file.write(NT_order)

    print(f"Order saved into {file_name} successfully.")
    print("This order came from trade_copier (Volumetrica)")

    send_orders(access_token, converted_symbol_ts, quantity, trade_action)
    print(f"FIX Message: 8=FIX.4.2|35=D|55={symbol}|54={flipped_action}|40=2|44={price}|38={quantity}")


def send_order_to_tradestation(access_token, volumetrica_order):
    # Step 1: Parse Volumetrica Order
    symbol = volumetrica_order.get("Symbol")
    quantity = volumetrica_order.get("Quantity")
    volumetrica_order_type = volumetrica_order.get("OrderType")
    volumetrica_trade_action = volumetrica_order.get("TradeAction")

    # Step 2: Convert Volumetrica Order to TradeStation Format
    order_type = "Market" if volumetrica_order_type == "VolumetricaMarket" else "Limit"
    trade_action = "Buy" if volumetrica_trade_action == "VolumetricaBuy" else "Sell"

    # Construct the payload for TradeStation API
    payload = {
        "AccountID": "SIM1169695f",  # TradeStation account ID
        "Symbol": symbol,
        "Quantity": quantity,
        "OrderType": order_type,
        "TradeAction": trade_action,
        "TimeInForce": {"Duration": "DAY"},
        "Route": "Intelligent"
    }

    # Step 3: Send Order to TradeStation
    url = "https://sim-api.tradestation.com/v3/orderexecution/orders"
    headers = {
        "content-type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    # Send the POST request to TradeStation
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print("Order sent successfully to TradeStation.")
    else:
        print(f"Failed to send order. Status Code: {response.status_code}, Response: {response.text}")

def send_order_to_ninjatrader(volumetrica_order):
    # Commenting out this line to prevent sending Volumetrica orders to NinjaTrader
    send_order_to_ninjatrader(volumetrica_order)
    pass