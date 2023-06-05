import logging

logger = logging.getLogger("MAIN")


def validate_and_execute(days, unit):
    try:
        if days.isdigit():
            result = days_to_units(int(days), unit)
            print(result)
    except ValueError:
        logger.error("Error occurred!")
        print("Invalid input!")


def days_to_units(days, unit):
    if unit == "hours":
        return f"{days} are {days * 24} {unit}."
    elif unit == "minutes":
        return f"{days} are {days * 24 * 60} {unit}."
    elif unit == "seconds":
        return f"{days} are {days * 24 * 60 * 60} {unit}."
    else:
        return "Not a conversion value"


input_message = "Enter a number of days and conversion units! Enter 'exit' to close.\n"
