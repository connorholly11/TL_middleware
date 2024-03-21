# main.py
import PropTradingProtocol_pb2 as ptp
from auth import get_access_token, get_accounts, get_api_key, authenticate_user, get_accounts
from data_logging import append_position_info_to_csv, append_order_info_to_csv, database_reporter, our_trades_logger, event_logger
from trade_operations import trade_copier, send_orders, send_order_to_tradestation
from TS_API import get_accounts, get_historical_orders, stream_positions_new, stream_bars, get_positions, get_bars
from websocket_client import open_websocket, send_positions_request
from tradestation_to_nt import process_tradestation_orders


########### FLASK APP START

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import logging
import threading

access_token = get_access_token()
app = Flask(__name__)
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
        #socketio.start_background_task(stream_positions_new, ["placeholder"], access_token, socketio)
        
        # Starting Volumetrica WebSocket as a background task
        socketio.start_background_task(open_websocket, wss_uri, token, socketio)

if __name__ == "__main__":
    socketio.start_background_task(start_websocket_connections)
    socketio.run(app, debug=True, use_reloader=False)