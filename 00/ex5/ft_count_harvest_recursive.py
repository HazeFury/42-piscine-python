def print_days(current: int, days: int) -> None:
    if current > days:
        print("Harvest time!")
        return
    else:
        print(f"Day {current}")
        print_days(current + 1, days)


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    print_days(1, days)
