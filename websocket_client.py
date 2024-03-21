import PropTradingProtocol_pb2 as ptp
import websocket
import threading
import time
from auth import authenticate_user
from data_logging import append_position_info_to_csv, append_order_info_to_csv, event_logger
import json



reconnection_attempts = 0
def volumetrica_position_reporter(positions_data, sio):
    # Ensure positions_data is treated correctly as a list of dictionaries
    aggregated_reports = []  # Will hold all formatted position reports
    
    for position_data in positions_data:
        report_fields = [
            'AccNumber', 'FeedSymbol', 'OpenQuantity', 'OpenPrice',
            'OpenPl', 'DailyPl', 'DailyCommissions'
        ]

        # Extract the relevant fields from each position data dictionary
        report_data = {field: position_data.get(field, None) for field in report_fields}
        aggregated_reports.append(report_data)
    
    # Convert the list of aggregated reports to a JSON string for transmission
    report_str = json.dumps(aggregated_reports)
    print(f"REPORT DATA: {report_str}")  # For logging

    # Emit the processed position reports to the client as a single package
    sio.emit('volumetrica-update_positions', {'data': report_str})





def close_websocket_connection(ws):
  ws.close()
  
def send_ping(ws):
  ping_msg = ptp.ClientRequestMsg()
  ping_msg.Ping.Connected = True
  ws.send(ping_msg.SerializeToString(), websocket.ABNF.OPCODE_BINARY)
  threading.Timer(5, send_ping, args=[ws]).start()


def protobuf_to_dict(pb):
    from google.protobuf.json_format import MessageToDict
    return MessageToDict(pb, preserving_proto_field_name=True)

def open_websocket(wss_uri, token, socketio):
    def on_message(ws, message):
        try:
            response_msg = ptp.ServerResponseMsg()
            response_msg.ParseFromString(message)
            print(f"{response_msg}")
            socketio.emit('update_volumetrica_data', {'message': f'{response_msg}'})  # Emit the cleaned message

            message_dict = protobuf_to_dict(response_msg)  # Convert protobuf message to a dictionary
            if 'PositionInfo' in message_dict:
              volumetrica_position_reporter(message_dict['PositionInfo'], socketio)

            # Initialize an empty list to hold our formatted message components
            formatted_messages = []

            # Iterate over each key-value pair in the message dictionary
            for key, value in message_dict.items():
                if isinstance(value, dict):
                    # For nested dictionaries, you could either convert them to a string
                    # or further iterate over their contents. Here, we convert to string for simplicity.
                    formatted_value = json.dumps(value)
                else:
                    formatted_value = str(value)
                
                formatted_messages.append(f"{key}: {formatted_value}")
            # Join all formatted message components with a comma
            clean_message = ", ".join(formatted_messages)

            print(clean_message)  # Print the cleaned message
            event_logger("Volumetrica WS", str(clean_message))
            socketio.emit('update_volumetrica_data', {'message': clean_message})  # Emit the cleaned message


            if len(response_msg.OrderInfo) == 1:
              append_order_info_to_csv(response_msg.BalanceInfo,
                                      response_msg.OrderInfo)
            elif len(response_msg.PositionInfo) == 1:
              append_position_info_to_csv(response_msg.PositionInfo)

        except Exception as e:
            print(f"Error processing message: {e}")
            event_logger("Volumetrica WS", f"Error processing message: {str(e)}")
            socketio.emit('update_volumetrica_data', {'message': f'Error processing message: {str(e)}'})

    
    def on_error(ws, error):
        print("Error: ", error)
        event_logger("Volumetrica WS", f"Error: {str(error)}")
        socketio.emit('update_volumetrica_data', {'message': f'Error: {str(error)}'})

    def on_close(ws, close_status_code, close_msg):
      if reconnection_attempts < 1000:
        print("### closed ###")
        event_logger("Volumetrica WS", f"closeded status code: {close_status_code}: {close_msg}")
        socketio.emit('update_volumetrica_data', {'message': f'closeded status code: {close_status_code}: {close_msg}'})

        time.sleep(4)
                
        print(f"Volumetrica WS Reconnecting... Try #{reconnection_attempts}")

        event_logger("Volumetrica WS", f"Reconnecting... Try #{reconnection_attempts}")
        socketio.emit('update_volumetrica_data', {'message': f'Reconnecting... Try #{reconnection_attempts}'})

        token, wss_uri = authenticate_user()
        if token and wss_uri:
          open_websocket(wss_uri, token)
        reconnection_attempts +=1
      else:
        print(f"Volumetrica WS Reconnection attempt failed too many times, giving up.")
        socketio.emit('update_volumetrica_data', {'message': f'Reconnection attempt failed too many times, giving up.'})
        event_logger("Volumetrica WS", f"Reconnection attempt failed too many times, giving up.")



    def on_open(ws):
      login_request_msg = ptp.ClientRequestMsg()
      login_request_msg.LoginReq.Token = token
      login_binary_message = login_request_msg.SerializeToString()
      ws.send(login_binary_message, websocket.ABNF.OPCODE_BINARY)
      print("Connection opened")
      send_ping(ws)
      event_logger("Volumetrica WS", f"Connection Opened")
      socketio.emit('update_volumetrica_data', {'message': 'Connection Opened'})
      request_msg = ptp.ClientRequestMsg()
      request_msg.InfoReq.AccountListFilterStatus = -1
      request_msg.InfoReq.Modes.append(1)
      request_msg.InfoReq.Modes.append(3)
      request_msg.InfoReq.RequestId = 5
      ws.send(request_msg.SerializeToString(), websocket.ABNF.OPCODE_BINARY)

    try:
      ws = websocket.WebSocketApp(wss_uri,
                                  on_open=on_open,
                                  on_message=on_message,
                                  on_error=on_error,
                                  on_close=on_close)
      print("running")
      ws.run_forever()
    except:
      return print("Authentication failure.")

















##### outdated
def send_positions_request():
  token, wss_uri = authenticate_user()
  def on_message(ws_pos, message):
    try:
      response_msg = ptp.ServerResponseMsg()
      response_msg.ParseFromString(message)
      print(f"POS_WS-{response_msg}-POS_WS")
      if len(response_msg.PositionInfo) == 1:
        append_position_info_to_csv(response_msg.PositionInfo)
        close_websocket_connection(ws_pos)
      socketio.emit('ts-update_data', {'data': 'Your processed message here'})
    except Exception as e:
      print(f"Error processing message: {e}")


  def on_error(ws_pos, error):
    print("Error POS : ", error)
    event_logger("position_ws", error)

  def on_close(ws_pos, close_status_code, close_msg):
    print("### closed POS ###")
    event_logger("position_ws", "closed")

  def on_open(ws_pos):
    login_request_msg = ptp.ClientRequestMsg()
    login_request_msg.LoginReq.Token = token
    login_binary_message = login_request_msg.SerializeToString()
    ws_pos.send(login_binary_message, websocket.ABNF.OPCODE_BINARY)
    print("Connection opened - POS")
    send_ping(ws_pos)
    request_msg = ptp.ClientRequestMsg()
    request_msg.InfoReq.Mode = 3
    request_msg.InfoReq.RequestId = 9
    ws_pos.send(request_msg.SerializeToString(), websocket.ABNF.OPCODE_BINARY)
    #threading.Timer(10, send_positions_request, args=[]).start()


  try:
    ws_pos = websocket.WebSocketApp(wss_uri,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws_pos.run_forever()

  except Exception as e:
    print("Authentication POS WEBSOCKET failure:", e)
    return

