card_number = input("Enter your card number: ")
sum = 0

# Colors
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

if len(card_number) != 16:
    print(f"{RED}Invalid card number ⚠️{RESET}")
    exit()

card_digits = [int(digit) for digit in card_number]

for i in range (16):
    if i%2 == 0:
        double = card_digits[i] * 2
        if double > 9:
            double = (double // 10) + (double % 10)
        card_digits[i] = double
    
    sum += card_digits[i]


if sum % 10 == 0:
    print(f"{GREEN}The credit card is valid{RESET}")
else:
    print(f"{RED}The credit card is invalid{RESET}")