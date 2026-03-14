
# Binance Futures Testnet Trading Bot

## Overview
This project is a Python command line trading bot developed as part of a Python Developer internship assignment. The application interacts with the Binance Futures Testnet (USDT-M) to place trading orders using a structured and modular Python codebase.

The bot allows users to place MARKET, LIMIT, and STOP-LIMIT orders using a CLI interface. It includes structured logging, input validation using Pydantic, and robust exception handling.

The system is designed to demonstrate clean code architecture, API interaction, and reliable runtime behavior.

---

## Features

### Core Functionality
- Place MARKET orders
- Place LIMIT orders
- Support BUY and SELL
- Command Line Interface (CLI)
- Input validation using Pydantic
- Structured logging
- Custom exception handling

### Bonus Feature
- Support for STOP-LIMIT orders

---


## Requirements

Python version

Python 3.9+

Install dependencies

pip install -r requirements.txt

Main libraries used

python-binance  
pydantic  
python-dotenv

---

## Binance Futures Testnet Setup

1. Open Binance Futures Testnet

https://testnet.binancefuture.com

2. Login using GitHub authentication.

3. Navigate to API Management.

4. Generate API credentials.

5. Create a `.env` file in the project root.

Example `.env` file

BINANCE_API_KEY=your_api_key  
BINANCE_SECRET_KEY=your_secret_key

---

## Running the Trading Bot

General command format

python cli.py --symbol SYMBOL --side SIDE --type ORDER_TYPE --quantity QUANTITY --price PRICE --stop_price STOP_PRICE

Parameters

symbol: Trading pair (example BTCUSDT)  
side: BUY or SELL  
type: MARKET, LIMIT, or STOP_LIMIT  
quantity: Amount of asset to trade  
price: Required for LIMIT and STOP_LIMIT  
stop_price: Trigger price for STOP_LIMIT  

---

## Example Commands

### Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

### Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000

### Stop-Limit Order (Bonus Feature)

python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --quantity 0.01 --price 59000 --stop_price 59200

Explanation

The stop price triggers the order.  
When the stop price is reached, a limit order is placed at the specified price.

Example scenario

Current BTC price = 58500  
stop_price = 59200  
limit_price = 59000

When BTC reaches 59200, a limit buy order at 59000 is created.

---

## Example CLI Output

Order Request
----------------------
Symbol: BTCUSDT
Side: BUY
Order Type: MARKET
Quantity: 0.01

Order Response
----------------------
Order ID: 12345678
Status: FILLED
Executed Quantity: 0.01
Average Price: 59200

---

## Logging

All API requests, responses, and errors are logged.

Log file location

logs/trading_bot.log

Example log entry

2026-03-14 14:12:03 | INFO | Sending order request  
2026-03-14 14:12:04 | INFO | Order response received  
2026-03-14 14:12:04 | ERROR | API error occurred  

---

## Error Handling

The system handles:

- Invalid CLI inputs
- Validation errors
- Binance API failures
- Network errors

Custom exceptions ensure errors are reported clearly without crashing the application.

---

## Assumptions

- The bot connects only to Binance Futures Testnet
- Testnet funds are used for simulated trading
- LIMIT orders require a price
- STOP-LIMIT orders require both price and stop_price

---

## Author

Rajat  
Python Developer Internship Assignment
