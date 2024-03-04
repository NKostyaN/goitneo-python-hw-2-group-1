def strip_phone_number(phone: str, digits=10) -> str:
    phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    if len(phone) > digits:
        phone = phone[-digits : len(phone)]
    return phone


if __name__ == "__main__":
    print(strip_phone_number("    +38(050)123-32-34", 6))
    print(strip_phone_number("     0503451234"))
    print(strip_phone_number("(050)8889900"))
    print(strip_phone_number("380-50-111-22-22"))
    print(strip_phone_number("38 050 111 22 11   "))
