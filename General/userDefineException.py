class Error(Exception):
    pass


class valueTooLarge(Error):
    pass


class valueTooSmall(Error):
    pass


def main():
    number = 10
    try:
        input_number = int(input("Enter a number:"))

        if input_number > number:
            raise valueTooLarge

        if input_number < number:
            raise valueTooSmall

        else:
            print("perfect")

    except valueTooLarge:
        print("Value is too large")

    except valueTooSmall:
        print("Value is too small")

    finally:
        print("Exception Creation over")


if __name__ == "__main__":
    main()
