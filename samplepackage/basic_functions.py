def make_me_happy():
    return "Today is Saturday!"


def make_me_feel_bad():
    return "Tomorrow is Monday... :("


# Duplicated lines
def make_me_feel_very_bad():
    return "Tomorrow is Monday... :("


def day_evaluator(day):
    if day in ["Monday", "Tuesday"]:
        return 2
    elif day in ["Wednesday", "Thursday"]:
        return 6
    elif day == "Friday":
        return 8
    elif day == "Saturday":
        return 10
    elif day == "Sunday":
        return 7
    else:
        raise ValueError(f"{day} is not a possible value")
