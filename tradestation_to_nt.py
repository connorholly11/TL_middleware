#2nd option instead of this would be to make a 2nd login on tradestation (~$70/month) and have the algo orders come from that login.

import time
import requests
from auth import get_access_token

print('ts to nt')
def get_tradestation_orders(access_token, account_id):
    url = f"https://api.tradestation.com/v3/brokerage/accounts/{account_id}/orders"
    headers = {"Authorization": f"Bearer {access_token}"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises a HTTPError for bad responses
        return response.json()["Orders"]
    except requests.exceptions.HTTPError as e:
        print(f"Failed to retrieve TradeStation orders. Error: {e}")
        return []

def send_order_to_ninjatrader(order):
    # Example conversion mapping, adjust based on actual requirements
    symbol_conversion = {
        "TradeStationSymbolFormat": "NinjaTraderSymbolFormat"  # Placeholder, replace with actual mappings
    }
    trade_action_conversion = {
        "Buy": "BUY",
        "Sell": "SELL"
    }
    
    symbol = symbol_conversion.get(order["Symbol"], order["Symbol"])  # Fallback to original symbol if not found
    quantity = order["Quantity"]
    trade_action = trade_action_conversion.get(order["TradeAction"], order["TradeAction"])  # Fallback to original action if not found

    NT_order = f"PLACE;Sim101;{symbol};{trade_action};{quantity};MARKET;;;DAY;;;;"

    timestamp_ns = int(time.time() * 1e9)
    file_name = f"oif{timestamp_ns}.txt"
    file_path = rf"C:\Users\connor holly\Documents\NinjaTrader 8\incoming\{file_name}"

    try:
        with open(file_path, 'w') as file:
            file.write(NT_order)
        print(f"Order saved into {file_name} successfully.")
        print("This order came from tradestation_to_nt.py")
    except Exception as e:
        print(f"Failed to save order to file. Error: {e}")

def process_tradestation_orders():
    access_token = get_access_token()
    account_id = "SIM1169695f"
    while True:
        orders = get_tradestation_orders(access_token, account_id)
        for order in orders:
            send_order_to_ninjatrader(order)
        time.sleep(5)  # Wait for 5 seconds before checking for new orders again

if __name__ == "__main__":
    process_tradestation_orders()
