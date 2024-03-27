from typing import TextIO

try:
    x = 5
    y = -12

    if y < 0:
        raise ValueError("Divisor has to be a positive number")

    print(x / y)

except (ZeroDivisionError, ValueError) as e:
    print(f"{type(e).__name__}: {e}")

except Exception as e:
    print(f"{type(e).__name__}: {e}")

else:
    print("No errors encountered - prints only when no errors")

finally:
    print("finally block will be executed doesn't matter if error or no")

print("Continue...")
print()

# task
try:
    daily_salary = int(input("Daily pay? "))
    num_of_days = int(input("How many days did you work? "))

except Exception as e:
    print(f"{type(e).__name__}: {e}")

else:
    print(f"Your pay will be: ${daily_salary * num_of_days}")
