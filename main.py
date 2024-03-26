# main.py
import PropTradingProtocol_pb2 as ptp
from auth import get_access_token, get_accounts, get_api_key, authenticate_user, get_accounts
from data_logging import append_position_info_to_csv, append_order_info_to_csv, database_reporter, our_trades_logger, event_logger
from trade_operations import trade_copier, send_orders, send_order_to_tradestation
from TS_API import get_accounts, get_historical_orders, stream_positions_new, stream_bars, get_positions, get_bars
from websocket_client import open_websocket
from tradestation_to_nt import process_tradestation_orders
import shared
########### FLASK APP START

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import logging
import threading
from flask import Flask, request, jsonify

app = Flask(__name__)



@app.route('/get_checked_accounts')
def get_checked_accounts():
    from shared import accs_to_copy
    return jsonify({'checkedAccounts': accs_to_copy})


@app.route('/update_checked_accounts', methods=['POST'])
def update_checked_accounts():
    data = request.json
    checked_accounts = data.get('checkedAccounts', [])
    
    # Prepare the Python list as a string
    accounts_str = ', '.join([str(acc) for acc in checked_accounts])
    new_content = f'accs_to_copy = [{accounts_str}]\n'

    # Rewrite the file with the updated list
    with open('shared.py', 'w') as file:
        file.write(new_content)

    return jsonify({'status': 'success', 'message': 'File updated'})





access_token = get_access_token()
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')  # Make sure you have an 'index.html' in your templates directory

@socketio.on('connect')
def test_connect():
    print("Client connected")

@socketio.on('disconnect')
def test_disconnect():
    print("Client disconnected")

def start_websocket_connections():
    token, wss_uri = authenticate_user()  # Ensure this function returns the necessary token and URI
    
    if token and wss_uri:
        # Starting TradeStation WebSocket as a background task
        socketio.start_background_task(stream_positions_new, ["placeholder"], access_token, socketio)
        
        # Starting Volumetrica WebSocket as a background task
        socketio.start_background_task(open_websocket, wss_uri, token, socketio)

if __name__ == "__main__":
    socketio.start_background_task(start_websocket_connections)
    socketio.run(app, debug=True, use_reloader=False)