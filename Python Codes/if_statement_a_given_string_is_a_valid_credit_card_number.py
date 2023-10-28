def is_valid_credit_card(card_number):
    card_number = card_number.replace(" ", "").replace("-", "")

    if not card_number.isdigit():
        return False
    
    if not (13 <= len(card_number) <= 19):
        return False
    
    reversed_card_number = card_number[::-1]
    
    total = 0
    double_next = False

    for digit in reversed_card_number:
        digit = int(digit)
        if double_next:
            digit *= 2
            if digit > 9:
                digit -= 9
            double_next = False
        else:
            double_next = True
        total += digit

    if total % 10 == 0:
        return True
    else:
        return False
    
card_number = input("Enter a credit card number: ")
if is_valid_credit_card(card_number):
    print("Valid credit card number.")
else:
    print("Invalid credit card number.")