#data_logging.py
import csv
from datetime import datetime
import os
import pandas as pd
from trade_operations import trade_copier





def append_position_info_to_csv(position_infos):
  csv_file_name = "position_info.csv"
  headers = [
      "Time", "ContractId", "OpenPrice", "DailyBought", "DailySold", "DailyPl",
      "HasOpenPl", "DailyCommissions", "SnapType", "AccNumber", "FeedSymbol"
  ]

  file_exists = os.path.isfile(csv_file_name)
  with open(csv_file_name, 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    if not file_exists:
      writer.writeheader()

    for position_info in position_infos:
      row = {
          "Time": datetime.now(),
          "ContractId": position_info.ContractId,
          "OpenPrice": position_info.OpenPrice,
          "DailyBought": position_info.DailyBought,
          "DailySold": position_info.DailySold,
          "DailyPl": position_info.DailyPl,
          "HasOpenPl": position_info.HasOpenPl,
          "DailyCommissions": position_info.DailyCommissions,
          "SnapType": position_info.SnapType,
          "AccNumber": position_info.AccNumber,
          "FeedSymbol": position_info.FeedSymbol
      }
      writer.writerow(row)


def append_order_info_to_csv(balance_infos, order_infos):
  csv_file_name = "order_info.csv"
  headers = [
      "Time", "Balance", "AccNumber", "MarginUsed", "StopDrawdownOverall",
      "StopDrawdownIntraday", "ProfitTarget", "ContractId", "OrgServerId",
      "OrgClientId", "SeqServerId", "SeqClientId", "FilledQty", "AvgPrice",
      "SnapType", "FeedSymbol", "OcoLinkedGroupId", "OcoParentOrderId"
  ]

  file_exists = os.path.isfile(csv_file_name)
  with open(csv_file_name, 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    if not file_exists:
      writer.writeheader()

    for balance_info, order_info in zip(balance_infos, order_infos):
      row = {
          "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
          "Balance": balance_info.Balance,
          "AccNumber": balance_info.AccNumber,
          "MarginUsed": balance_info.MarginUsed,
          "StopDrawdownOverall": balance_info.StopDrawdownOverall,
          "StopDrawdownIntraday": balance_info.StopDrawdownIntraday,
          "ProfitTarget": balance_info.ProfitTarget,
          "ContractId": order_info.ContractId,
          "OrgServerId": order_info.OrgServerId,
          "OrgClientId": order_info.OrgClientId,
          "SeqServerId": order_info.SeqServerId,
          "SeqClientId": order_info.SeqClientId,
          "FilledQty": order_info.FilledQty,
          "AvgPrice": order_info.AvgPrice,
          "SnapType": order_info.SnapType,
          "FeedSymbol": order_info.FeedSymbol,
          "OcoLinkedGroupId": order_info.OcoLinkedGroupId,
          "OcoParentOrderId": order_info.OcoParentOrderId
      }
      writer.writerow(row)
      trade_copier(row)

      
      our_trades_logger(row)

def database_reporter(csv_file_name):
  # Read the CSV file
  df = pd.read_csv(csv_file_name)
  if csv_file_name == "our_trades.csv":
    # Separate into longs and shorts
    longs = df[df['Quantity'] > 0]
    shorts = df[df['Quantity'] < 0]

    # Calculate the sum of quantities and the count for each symbol
    summary = df.groupby('Symbol').agg(Contracts=('Quantity', 'sum'),
                                       Trades=('Symbol',
                                               'count')).reset_index()

    # Calculate average price for longs and shorts separately
    longs_price = longs.groupby('Symbol')['AveragePrice'].mean()
    shorts_price = shorts.groupby('Symbol')['AveragePrice'].mean()

    # Join the summaries with the average prices
    summary = summary.join(longs_price, on='Symbol', rsuffix='_Longs')
    summary = summary.join(shorts_price, on='Symbol', rsuffix='_Shorts')

    # Print or return the summary
    print(summary.to_string())

  else:
    print("write function for the report")


def our_trades_logger(row):
  csv_file_name = "our_trades.csv"
  headers = [
      "OrderTime", "OriginalAction", "FlippedAction", "Symbol", "Quantity",
      "AveragePrice"]

  order_time = row["Time"]  
  original_action = '1' if row[
      'FilledQty'] > 0 else '2'  ### 1 = long, 2 = short
  flipped_action = '2' if original_action == '1' else '1'
  symbol = row['FeedSymbol']
  avg_price = row['AvgPrice']
  quantity = abs(row['FilledQty'])
  
  file_exists = os.path.isfile(csv_file_name)
  with open(csv_file_name, 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    if not file_exists:
      writer.writeheader()

    row = {
        "OrderTime": order_time,
        "OriginalAction": original_action,
        "FlippedAction": flipped_action,
        "Symbol": symbol,
        "Quantity": quantity,
        "AveragePrice": avg_price
    }

    writer.writerow(row)
  database_reporter(csv_file_name)




def event_logger(ws_name, message):
  csv_file_name = "event_logs.csv"
  headers = ["Time","Ws_name", "Message" ]

  file_exists = os.path.isfile(csv_file_name)
  with open(csv_file_name, 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    if not file_exists:
      writer.writeheader()

    row = {
          "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
          "Ws_name": ws_name,
          "Message": message}
    writer.writerow(row)


