def largest_product(series: str, size: int) -> int:

    if size > len(series):
        raise ValueError("span must not exceed string length")

    if size < 0:
        raise ValueError("span must not be negative")

    for num in series:
        if not num.isdigit():
            raise ValueError("digits input must only contain digits")

    if size == 0:
        return 0

    amount_of_spans: int = len(series) + 1 - size

    sums: list[int] = []

    start_span: int = 0
    stop_span: int = start_span + size

    for _ in range(amount_of_spans):
        span: str = series[start_span:stop_span]

        add_num: int = 1
        for str_num in span:
            num = int(str_num)

            add_num *= num
        sums.append(add_num)

        start_span += 1
        stop_span += 1

    return max(sums)
