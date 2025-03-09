import re


def normalize_phone_number(phone_number: str) -> str:
    """
    Function to normalize phone numbers to a standard format
    :param phone_number: Raw phone number as a string
    :return: Normalized phone number with country code
    """
    digits = re.sub(r'[^\d+]', '', phone_number).strip()
    if digits.startswith('380'):
        return '+' + digits
    elif digits.startswith('+'):
        return digits
    else:
        return '+38' + digits