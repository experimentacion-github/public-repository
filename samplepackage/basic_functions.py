def make_me_happy():
    return "Today is Saturday!"


def make_me_feel_bad():
    return "Tomorrow is Monday... :("


# Duplicated lines
def make_me_feel_very_bad():
    return "Tomorrow is Monday... :("


def high_complexity():
    i = 0
    for i in range(5):
        for j in range(5):
            for m in range(5):
                for p in range(5):
                    for q in range(5):
                        i += 1
    if i > 3:
        if j > 3:
            if m > 3:
                for p in range(5):
                    for p in range(5):
                        for p in range(5):
                            if q > 3:
                                i = 0

    if i > 3:
        if j > 3:
            if m > 3:
                for p in range(5):
                    for p in range(5):
                        for p in range(5):
                            if q > 3:
                                i = 0

    if i > 3:
        if j > 3:
            if m > 3:
                for p in range(5):
                    for p in range(5):
                        for p in range(5):
                            if q > 3:
                                i = 0

    if i > 3:
        if j > 3:
            if m > 3:
                for p in range(5):
                    for p in range(5):
                        for p in range(5):
                            if q > 3:
                                i = 0

    if i > 3:
        if j > 3:
            if m > 3:
                for p in range(5):
                    for p in range(5):
                        for p in range(5):
                            if q > 3:
                                i = 0

    if i > 3:
        if j > 3:
            if m > 3:
                for p in range(5):
                    for p in range(5):
                        for p in range(5):
                            if q > 3:
                                i = 0

    return True


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
