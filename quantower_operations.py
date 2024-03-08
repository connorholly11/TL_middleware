#currently not being used
#quantower_operations.py
import requests

def trade_copier_quantower(row):
    print('Entering trade_copier_quantower function')
    original_action = '1' if row['FilledQty'] > 0 else '2'  # 1 = long, 2 = short
    symbol = row['FeedSymbol']
    price = row['AvgPrice']
    quantity = abs(row['FilledQty'])

    print('Preparing order data for Quantower')

    # Prepare the order data for Quantower
    order_data = {
        "symbol": symbol,
        "quantity": quantity,
        "price": price,
        "side": "buy" if original_action == "1" else "sell"
    }

    print(f"Sending order to Quantower: {order_data}")

    # Send the order data to the Quantower endpoint
    quantower_url = "http://localhost:8000/orders"  # Replace with the actual Quantower endpoint URL
    try:
        print('Sending POST request to Quantower endpoint')
        response = requests.post(quantower_url, json=order_data, timeout=5)  # Set a timeout of 5 seconds
        print(f"Response from Quantower: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending order to Quantower: {e}")

def send_order_to_quantower(volumetrica_order):
    # Step 1: Parse Volumetrica Order
    symbol = volumetrica_order.get("Symbol")
    quantity = volumetrica_order.get("Quantity")
    volumetrica_order_type = volumetrica_order.get("OrderType")
    volumetrica_trade_action = volumetrica_order.get("TradeAction")

    # Step 2: Format the order data according to Quantower's requirements
    quantower_order = {
        "Symbol": symbol,
        "Quantity": quantity,
        "OrderType": volumetrica_order_type,
        "TradeAction": volumetrica_trade_action
    }

    # Step 3: Send the order to Quantower using the appropriate API method
    # Replace 'quantower_api_url' with the actual Quantower API endpoint URL
    response = requests.post('quantower_api_url', json=quantower_order)  # Placeholder URL

    if response.status_code == 200:
        print("Order sent successfully to Quantower.")
    else:
        print(f"Failed to send order to Quantower. Status Code: {response.status_code}, Response: {response.text}")
