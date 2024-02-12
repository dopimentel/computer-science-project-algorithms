def validate_tuple(tup):
    return (
        isinstance(tup, tuple)
        and len(tup) == 2
        and isinstance(tup[0], int)
        and isinstance(tup[1], int)
    )


def study_schedule(permanence_period, target_time=None):
    if target_time is None:
        return None
    count = 0
    for period in permanence_period:
        if not validate_tuple(period):
            return None

        if target_time in range(period[0], period[1] + 1):
            count += 1
    return count


if __name__ == "__main__":
    print(
        study_schedule(
            [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5), (6, 7)], 5
        )
    )
    print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 1))
    print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5)], 3))
    print(study_schedule([(1, 1), (2, 2), (3, 3), (4, 4)], 1))
    print(study_schedule([(1, 2), (1, 3), (2, 3)], 2))
    print(
        study_schedule(
            [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5), (6, 7)], None
        )
    )
    print(
        study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], None)
    )
    print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5)], None))
    print(study_schedule([(1, 1), (2, 2), (3, 3), (4, 4)], None))
    print(study_schedule([(1, 2), (1, 3), (2, 3)], None))
    print(
        study_schedule(
            [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5), (6, 7)], 5
        )
    )
    print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 1))
    print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5)], 3))
