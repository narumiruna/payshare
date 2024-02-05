from sharepay import Currency
from sharepay import SharePay


def main() -> None:
    p = SharePay(name="Sendai", currency=Currency.JPY, alias={"yoan": "john"})

    p.add_payment(amount=300, currency="JPY", payer="narumi", members=["narumi", "dogiko", "ben"])
    p.add_payment(amount=600, currency="JPY", payer="dogiko", members=["dogiko", "ben", "john"])
    p.add_payment(amount=900, currency="JPY", payer="ben", members=["john", "yoan"])

    p.settle_up()


if __name__ == "__main__":
    main()
