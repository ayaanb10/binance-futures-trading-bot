# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading bot developed for Binance Futures Testnet (USDT-M). The application allows users to place MARKET and LIMIT orders through a command-line interface while following a structured and reusable architecture.

The bot includes input validation, logging, exception handling, and a dedicated Binance client layer to ensure maintainability, reliability, and scalability.

---

## Features

### Core Features

* Place MARKET orders on Binance Futures Testnet
* Place LIMIT orders on Binance Futures Testnet
* Support for both BUY and SELL order sides
* Command-line interface using argparse
* Input validation for order parameters
* Structured project architecture
* API request and response logging
* Exception handling for invalid inputs and API errors

### Bonus Feature Implemented

**Enhanced CLI User Experience**

* Helpful command descriptions using argparse help messages
* Automatic normalization of user inputs (BUY/SELL, MARKET/LIMIT)
* User-friendly validation feedback
* Clear order summaries before execution
* Success and error messages displayed in a readable format

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading.log
│
├── cli.py
├── README.md
├── requirements.txt
├── .gitignore
└── .env
```

---

## Technologies Used

* Python 3.x
* python-binance
* python-dotenv
* argparse
* logging

---

## Prerequisites

* Python 3.x
* Binance Futures Testnet Account
* Binance Futures Testnet API Key and Secret

Testnet URL:

```text
https://testnet.binancefuture.com
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd trading_bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Credentials

Create a `.env` file in the project root directory:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

## Usage

### Place a MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

### View CLI Help

```bash
python cli.py --help
```

---

## Example Output

```text
ORDER SUMMARY

Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

SUCCESS

Order ID: 14496597315
Status: NEW
Executed Qty: 0.0000
```

---

## Logging

All API requests, responses, and errors are logged to:

```text
logs/trading.log
```

The log file contains:

* Order request details
* Binance API responses
* Validation errors
* Runtime exceptions

Logs from both MARKET and LIMIT order executions are included.

---

## Error Handling

The application handles:

* Invalid order side values
* Invalid order types
* Invalid quantities
* Missing LIMIT order price
* Binance API exceptions
* Runtime and network-related errors

---

## Assumptions

* Binance Futures Testnet account is active.
* Valid API credentials are stored in `.env`.
* User provides a valid trading symbol supported by Binance Futures Testnet.
* LIMIT orders require a valid price value.

---

## Evaluation Criteria Coverage

| Requirement             | Status |
| ----------------------- | ------ |
| MARKET Orders           | ✅      |
| LIMIT Orders            | ✅      |
| BUY & SELL Support      | ✅      |
| CLI Input Handling      | ✅      |
| Input Validation        | ✅      |
| Logging                 | ✅      |
| Error Handling          | ✅      |
| Structured Architecture | ✅      |
| README Documentation    | ✅      |
| requirements.txt        | ✅      |
| Bonus: Enhanced CLI UX  | ✅      |

---

## Author

Ayaan Banatwalla
