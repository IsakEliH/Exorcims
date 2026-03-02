"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    gen: str = ""
    get_letter = lambda number: "ABCD"[(number % 4) - 1]

    for n in range(1, number + 1):
        gen += get_letter(n)
        yield gen
        gen = ""


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    produced: int = 0

    for n in range(1, number + 1):
        if n == 13:
            continue

        seat_letter = generate_seat_letters(4)
        seat = ""
        for _ in range(4):
            if produced >= number:
                break
            seat: str = str(n) + next(seat_letter)
            yield seat
            produced += 1


def assign_seats(passengers: list[str]):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    assigned: dict[str, str] = {}
    seat_gen = generate_seats(len(passengers))

    for passenger in passengers:
        assigned[passenger] = next(seat_gen)

    return assigned


def generate_codes(seat_numbers: list[str], flight_id: str):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    final = ""

    for seat in seat_numbers:
        final += seat
        final += flight_id

        while len(final) < 12:
            final += "0"

        yield final
        final = ""
