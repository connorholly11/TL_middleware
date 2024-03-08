import PropTradingProtocol_pb2 as ptp
import websocket
import threading
import time
from auth import authenticate_user
from data_logging import append_position_info_to_csv, append_order_info_to_csv, event_logger


def close_websocket_connection(ws):
  ws.close()
  
def send_ping(ws):
  ping_msg = ptp.ClientRequestMsg()
  ping_msg.Ping.Connected = True
  ws.send(ping_msg.SerializeToString(), websocket.ABNF.OPCODE_BINARY)
  threading.Timer(45, send_ping, args=[ws]).start()


def open_websocket(wss_uri, token):
    def on_message(ws, message):
      try:
        response_msg = ptp.ServerResponseMsg()
        response_msg.ParseFromString(message)
        print(response_msg)
        if len(response_msg.OrderInfo) == 1:
          append_order_info_to_csv(response_msg.BalanceInfo,
                                   response_msg.OrderInfo)
        elif len(response_msg.PositionInfo) == 1:
          append_position_info_to_csv(response_msg.PositionInfo)

      except Exception as e:
        print(f"Error processing message: {e}")

    def on_error(ws, error):
      print("Error: ", error)
      event_logger("main_ws", error)

    def on_close(ws, close_status_code, close_msg):
      i = 10
      if i != 0:
        print("### closed ###")
        event_logger("main_ws", "closed")
        time.sleep(3)
        token, wss_uri = authenticate_user()
        if token and wss_uri:
          open_websocket(wss_uri, token)
        i -=1


    def on_open(ws):
      login_request_msg = ptp.ClientRequestMsg()
      login_request_msg.LoginReq.Token = token
      login_binary_message = login_request_msg.SerializeToString()
      ws.send(login_binary_message, websocket.ABNF.OPCODE_BINARY)
      print("Connection opened")
      send_ping(ws)
      send_positions_request()
    
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
    except Exception as e:
      print(f"Error processing POS message: {e}")

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

