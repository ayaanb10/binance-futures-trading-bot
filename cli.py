import argparse

from bot.orders import (
    place_market_order,
    place_limit_order
)

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)

from bot.logging_config import logger

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:

    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)

    logger.info(f"Order Request: {vars(args)}")

    print("\nORDER SUMMARY")
    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")

    if args.type == "MARKET":

        response = place_market_order(
            args.symbol,
            args.side,
            args.quantity
        )

    else:

        if args.price is None:
            raise ValueError(
                "Price required for LIMIT order"
            )

        response = place_limit_order(
            args.symbol,
            args.side,
            args.quantity,
            args.price
        )

    logger.info(f"Response: {response}")

    print("\nSUCCESS")
    print("Order ID:", response["orderId"])
    print("Status:", response["status"])
    print("Executed Qty:", response["executedQty"])

except Exception as e:

    logger.error(str(e))

    print("\nFAILED")
    print(e)