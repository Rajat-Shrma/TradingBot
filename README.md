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
Python 3.9+
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
git clone https://github.com/your-username/trading-bot.git
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
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
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

All API requests, responses, and errors are logged.

Log file location

```
logs/trading_bot.log
```

Example log

```
2026-03-14 14:12:03 | INFO | Sending order request
2026-03-14 14:12:04 | INFO | Order response received
2026-03-14 14:12:04 | ERROR | API error occurred
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
- Testnet funds are used for simulated trading
- LIMIT orders require `price`
- STOP-LIMIT orders require both `price` and `stop_price`

---

## Author

Rajat  
Python Developer Internship Assignment
