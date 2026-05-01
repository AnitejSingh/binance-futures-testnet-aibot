import argparse
from bot.client import BinanceClient
from bot.orders import OrderService
from bot.validators import validate_input
from bot.logging_config import setup_logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

        client = BinanceClient().get_client()
        order_service = OrderService(client)

        print("\n=== Order Summary ===")
        print(vars(args))

        response = order_service.place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n=== Order Response ===")
        print(response)

        print("\n✅ Order placed successfully!")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
