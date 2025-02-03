total_fees = calculate_total_fees(bid_amount)
if total_fees is not None:
    print(f"Total fees for a standard vehicle with bid {bid_amount}: ${total_fees:.2f}")
else:
    print(f"Unable to calculate total fees for a standard vehicle with bid {bid_amount}")
