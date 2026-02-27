def rotate(text: str, key: int) -> str:
    key %= 26
    out = []

    for ch in text:
        if "a" <= ch <= "z":
            base = ord("a")
            out.append(chr((ord(ch) - base + key) % 26 + base))
        elif "A" <= ch <= "Z":
            base = ord("A")
            out.append(chr((ord(ch) - base + key) % 26 + base))
        else:
            out.append(ch)

    return "".join(out)