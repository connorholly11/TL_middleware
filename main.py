# main.py
import PropTradingProtocol_pb2 as ptp
from auth import get_access_token, get_accounts, get_api_key, authenticate_user, get_accounts
from data_logging import append_position_info_to_csv, append_order_info_to_csv, database_reporter, our_trades_logger, event_logger
from trade_operations import trade_copier, send_orders, send_order_to_tradestation
from TS_API import get_accounts, get_historical_orders, stream_positions_new, stream_bars, get_positions, get_bars
from websocket_client import open_websocket, send_positions_request
from tradestation_to_nt import process_tradestation_orders

access_token = get_access_token()


def main():
  if __name__ == "__main__":
    if access_token:
        # Example usage of the existing functionality
        account_ids = ["11045632","SIM1169695f", "210CHOLL"]  #
        #get_positions(account_ids, access_token)
    else:
        print("Failed to authenticate.")
  
    token, wss_uri = authenticate_user()
    
    if token and wss_uri:
      open_websocket(wss_uri, token)
  
  
main()




