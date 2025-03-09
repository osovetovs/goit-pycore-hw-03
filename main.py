from helpers.date_helper import get_days_from_today, get_upcoming_birthdays
from helpers.lottery_helper import get_lottery_numbers
from helpers.pnum_helper import normalize_phone_number

if __name__ == "__main__":
    print(get_days_from_today(date="2025-10-09"))
    print(get_lottery_numbers(min_num=1, max_num=49, quantity=6))
    print(normalize_phone_number(phone_number="    +38(050)123-32-34"))
    print(normalize_phone_number(phone_number="    38(096)123-45-67"))

    users = [
        {"name": "Albert Einstein", "birthday": "1879.03.14"}, #Friday
        {"name": "Paul Pogba", "birthday": "1993.03.15"}, # Saturday
        {"name": "Alexandra Daddario", "birthday": "1986.03.16"},  # Sunday
        {"name": "Jane Smith", "birthday": "1990.01.27"},  # past
        {"name": "John Doe", "birthday": "1990.06.27"}  # future
    ]
    print(get_upcoming_birthdays(users=users))