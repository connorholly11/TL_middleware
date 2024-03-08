# TradeStation - NinjaTrader Integration

This project enables the integration between TradeStation and NinjaTrader, allowing orders to be sent from TradeStation to NinjaTrader using custom tags. The code is organized into multiple modules, each serving a specific purpose.

## Modules

### auth.py

The `auth.py` module handles authentication and token retrieval for various services.

- `get_access_token()`: Retrieves the TradeStation access token using the provided credentials.
- `get_api_key()`: Retrieves the Volumetrica REST API key from environment variables.
- `authenticate_user()`: Authenticates the user with Volumetrica Trader using the provided login credentials.
- `get_accounts()`: Retrieves account information from TradeStation using the access token.

### config.py

The `config.py` module provides a function to load the configuration settings from a JSON file.

- `load_config()`: Loads the configuration settings from the `config.json` file.

### data_logging.py

The `data_logging.py` module handles data logging and reporting functionalities.

- `append_position_info_to_csv()`: Appends position information to a CSV file named `position_info.csv`.
- `append_order_info_to_csv()`: Appends order information to a CSV file named `order_info.csv`.
- `database_reporter()`: Generates a report based on the specified CSV file.
- `our_trades_logger()`: Logs trade information to a CSV file named `our_trades.csv`.
- `event_logger()`: Logs event information to a CSV file named `event_logs.csv`.

### main.py

The `main.py` module serves as the entry point of the application.

- `main()`: The main function that orchestrates the authentication, websocket connection, and data retrieval processes.

### PropTradingProtocol_pb2.py

The `PropTradingProtocol_pb2.py` module contains the Protocol Buffer definitions for the Volumetrica trading protocol.

### trade_operations.py

The `trade_operations.py` module handles trade-related operations and order sending.

- `send_orders()`: Sends orders to TradeStation using the provided access token, symbol, quantity, and trade action.
- `trade_copier()`: Copies trades from Volumetrica to TradeStation and NinjaTrader.
- `send_order_to_tradestation()`: Sends an order to TradeStation based on the Volumetrica order details.
- `send_order_to_ninjatrader()`: Sends an order to NinjaTrader based on the Volumetrica order details.

### tradestation_algo_testing.py

The `tradestation_algo_testing.py` module focuses on retrieving algo orders from TradeStation and sending them to NinjaTrader.

- `get_tradestation_orders()`: Retrieves orders from TradeStation using the provided access token and account ID.
- `send_order_to_ninjatrader()`: Sends an order to NinjaTrader by creating an OIF file.
- `process_tradestation_orders()`: Continuously retrieves TradeStation orders, filters algo orders based on the custom tag, and sends them to NinjaTrader.

### trade_operations.py

The `streaming.py` module provides functions for streaming data from TradeStation.

- `get_accounts()`: Retrieves account information from TradeStation using the access token.
- `get_bars()`: Retrieves bar chart data from TradeStation for a specified symbol.
- `stream_positions()`: Streams position data from TradeStation for the specified account IDs.
- `start_streaming_positions()`: Initiates the streaming of position data.
- `stream_positions_with_details()`: Streams position data with additional details.
- `stream_bars()`: Streams bar chart data for a specified symbol.
- `stream_positions_new()`: Streams position data for the specified account IDs.
- `get_positions()`: Retrieves position information for the specified account IDs.
- `get_historical_orders()`: Retrieves historical order information for the specified account IDs.

### websocket_client.py

The `websocket_client.py` module handles websocket communication with Volumetrica Trader.

- `close_websocket_connection()`: Closes the websocket connection.
- `send_ping()`: Sends a ping message to maintain the websocket connection.
- `open_websocket()`: Opens a websocket connection and handles incoming messages.
- `send_positions_request()`: Sends a request for position information over the websocket.

## Setup and Usage

1. Install the required dependencies listed in the `requirements.txt` file.
2. Configure the necessary credentials and settings in the `config.json` file and environment variables.
3. Run the `main.py` script to start the application.
4. The application will authenticate with the required services, establish websocket connections, and begin processing trades and orders.
5. Trades from Volumetrica will be copied to TradeStation and NinjaTrader based on the defined rules and mappings.
6. Algo orders from TradeStation will be filtered based on the custom tag and sent to NinjaTrader using OIF files.
7. The application will log relevant data and events to CSV files for further analysis and reporting.

Note: Make sure to review and update the file paths, credentials, and other configuration settings according to your specific setup and requirements.

## Dependencies

- `requests`: Used for making HTTP requests to various APIs.
- `websocket-client`: Used for establishing websocket connections.
- `protobuf`: Used for parsing and serializing Protocol Buffer messages.
- `pandas`: Used for data manipulation and analysis.
- `python-dotenv`: Used for loading environment variables from a `.env` file.

Please refer to the `requirements.txt` file for the full list of dependencies.

## License

This project is licensed under the [MIT License](LICENSE).
