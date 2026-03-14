# Binance Futures Testnet Trading Bot

## Overview
This project is a Python command line trading bot developed as part of a Python Developer internship assignment.  
The bot interacts with the **Binance Futures Testnet (USDT-M)** to place trading orders through a CLI interface.

Supported order types:
- MARKET
- LIMIT
- STOP-LIMIT (Bonus Feature)

The project demonstrates:
- Modular project architecture
- CLI interface
- Input validation using Pydantic
- Structured logging
- Custom exception handling
- Interaction with Binance Futures API

---

## Features

### Core Features
- Place **MARKET orders**
- Place **LIMIT orders**
- Support **BUY** and **SELL**
- CLI based interface
- Input validation using **Pydantic**
- Structured **logging**
- Custom **exception handling**

### Bonus Feature
- **STOP-LIMIT order support**

---

## Project Structure

```
TRADING_BOT/

bot/
│
├── components/
│   ├── client.py
│   ├── orders.py
│   └── validators.py
│
├── custom_logging/
│   └── custom_logging.py
│
├── exception/
│   └── custom_exception.py
│
├── __init__.py

notebooks/
└── experiments.ipynb

.env
cli.py
requirements.txt
setup.py
```

---

## Requirements

Python version

```
Python 3.11
```

Install dependencies

```bash
pip install -r requirements.txt
```

Main libraries used

```
python-binance
pydantic
python-dotenv
```

---

# Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/Rajat-Shrma/TradingBot.git
```

Navigate to the project directory

```bash
cd trading-bot
```

---

## 2. Create Virtual Environment (Recommended)

Create virtual environment

```bash
python -m venv venv
```

Activate environment

### Linux / Mac

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Binance Testnet API Keys

Open Binance Futures Testnet

```
https://testnet.binancefuture.com
```

Create API credentials and add them in a `.env` file.

Example:

```bash
API_KEY=your_api_key
SECRET_KEY=your_secret_key
```

---

## Running the Trading Bot

General command format

```bash
python cli.py --symbol SYMBOL --side SIDE --type ORDER_TYPE --quantity QUANTITY --price PRICE --stop_price STOP_PRICE
```

---

## Example Commands

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000
```

### Stop-Limit Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --quantity 0.01 --price 59000 --stop_price 59200
```

---

## Example CLI Output

```
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
```

---

## Logging

All API requests, validation, responses, and errors are logged.

Log file location

```
logs/
```

Example log

```
2026-03-14 13:10:47,757 | INFO | root | Line: 15 | Message: Begins
2026-03-14 13:10:47,757 | INFO | root | Line: 38 | Message: Parameter Validation Completed.
2026-03-14 13:10:48,087 | INFO | root | Line: 47 | Message: Binance Client object Created.
```

---

## Error Handling

The system handles:

- Invalid CLI input
- Validation errors
- Binance API failures
- Network errors

Custom exceptions ensure errors are reported clearly without crashing the application.

---

## Assumptions

- The bot connects only to **Binance Futures Testnet**
- Environment is properly setup with API_KEY and SECRET_KEY
- LIMIT orders require `price`
- STOP-LIMIT orders require both `price` and `stop_price`

---

## Author

Rajat  
