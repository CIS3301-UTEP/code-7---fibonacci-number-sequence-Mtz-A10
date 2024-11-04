def get_fibonacci_number(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    
    return get_fibonacci_number (position-2) \
            +get_fibonacci_number(position-1)


def get_fibonacci_number_sequence(number):
    if number == 0:
        return[0]
    elif number == 1:
        return [0,1]
    
    previous_x = 0
    previous_y = 1

    number_sequence = [0,1]
    
    for i in range(2, number+1):
        current = previous_x + previous_y
        previous_x = previous_y
        previous_y = current

        number_sequence.append(current)

    return number_sequence


if __name__ == "__main__":
    position = 3
    result = get_fibonacci_number(position)
    print(f"Fibonacci({position}) = {result}")

    number = 6
    result = get_fibonacci_number_sequence(number)
    print(f"Fibonacci sequence ({number}) = {result}")