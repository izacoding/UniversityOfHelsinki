Eat = int(input("how many time a week do you eat at the student cafeteria?"))
price_for_lunch = float(input("The price of a typical student lunch?"))
groceries_in_a_week = float(input("How much money do you spend on groceries in a week?"))
daily_spend = Eat * price_for_lunch / 7
weekly_spend = groceries_in_a_week / 7
daily = daily_spend + weekly_spend
weekly = daily * 7
print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")
