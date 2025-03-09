from datetime import datetime, timedelta


def get_days_from_today(date: str) -> int:
    """
    Function to calculate days number from today based on provided value
    :param date: date in string format of YYYY-MM-DD
    :return: Integer value of calculated days
    """
    try:
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        return (given_date - today).days
    except ValueError:
        raise ValueError("Invalid date format. Use 'YYYY-MM-DD'")


def get_upcoming_birthdays(users: list) -> list:
    """
    Function to get upcoming birthdays within the next 7 days
    :param users: List of dictionaries with name and birthday keys
    :return: List of dictionaries with name and congratulation_date keys
    """
    today = datetime.today().date()
    upcoming_birthdays = []
    one_week = timedelta(days=7)

    for user in users:
        birthday = datetime.strptime(
            user["birthday"], "%Y.%m.%d"
        ).date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        if today <= birthday_this_year <= today + one_week:
            if birthday_this_year.weekday() in [5, 6]:
                birthday_this_year += timedelta(
                    days=(7 - birthday_this_year.weekday()))

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime('%Y.%m.%d')
            })

    return upcoming_birthdays