def calculate_redemption(tokens, days_held):
    if days_held < 7:
        rate = 0.70
        tier = "Instant"
    elif days_held < 30:
        rate = 0.85
        tier = "Weekly"
    else:
        rate = 1.00
        tier = "Monthly"

    payout = tokens * rate
    return payout, rate, tier


def main():
    print("=== Token Redemption Simulator ===")

    try:
        tokens = float(input("Enter number of tokens: "))
        days = int(input("Enter days held: "))

        payout, rate, tier = calculate_redemption(tokens, days)

        print("\n--- Result ---")
        print(f"Redemption Tier: {tier}")
        print(f"Rate Applied: {rate * 100}%")
        print(f"Final Payout: ${payout}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
