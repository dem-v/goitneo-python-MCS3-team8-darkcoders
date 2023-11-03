def split_phones(phone_string):
    if phone_string is None or len(phone_string) < 2:
        return []

    splitted = phone_string.split()
    phones = []
    for s in splitted:
        phones.extend(s.split(","))

    phones = [phone.strip() for phone in phones if phone.strip()]

    return phones
