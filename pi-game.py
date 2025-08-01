import random
import decimal


def calculate_pi_with_high_precision(precision):
    decimal.getcontext().prec = precision + 2
    pi = decimal.Decimal(0)
    for k in range(precision + 2):
        pi += (decimal.Decimal(-1) ** k) / (1024 ** k) * (
                    decimal.Decimal(256) / (10 * k + 1) + decimal.Decimal(1) / (10 * k + 9) - decimal.Decimal(64) / (
                        10 * k + 3) - decimal.Decimal(32) / (4 * k + 1) - decimal.Decimal(4) / (
                                10 * k + 5) - decimal.Decimal(4) / (10 * k + 7) - decimal.Decimal(1) / (4 * k + 3))
    return pi * decimal.Decimal(1 / 2 ** 6)


precision = 100
pi_value = calculate_pi_with_high_precision(precision)


def get_random_number():
    return random.randint(1, 100)


def get_pi_decimal(number):
    pi_digits = str(pi_value)[2:]
    if number <= len(pi_digits):
        return int(pi_digits[number - 1])
    else:
        print("Die zufällig generierte Zahl ist zu groß. Die Anzahl der Nachkommastellen von Pi beträgt 38.")
        return None


def play_game():
    while True:
        random_number = get_random_number()
        if random_number is None:
            continue

        user_input = input(
            f"Geben Sie die {random_number}. Nachkommastelle von pi ein (oder 'q' zum Beenden): "
        )

        # Erst auf 'q' prüfen, dann erst in int umwandeln!
        if user_input.lower() == 'q':
            print("Spiel beendet.")
            break

        try:
            user_input = int(user_input)
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein oder 'q' zum Beenden.")
            continue

        correct_digit = get_pi_decimal(random_number)
        if correct_digit is not None:
            if user_input == correct_digit:
                print("Richtig!")
            else:
                print(f"Falsch. Die richtige Antwort war {correct_digit}.")


if __name__ == "__main__":
    play_game()

