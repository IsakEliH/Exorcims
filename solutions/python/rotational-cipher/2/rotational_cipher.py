def rotate(text: str, key: int) -> str:
    key %= 26
    out = []

    for char in text:
        if "a" <= char <= "z":
            base = ord("a")
            out.append(chr((ord(char) - base + key) % 26 + base))
        elif "A" <= char <= "Z":
            base = ord("A")
            out.append(chr((ord(char) - base + key) % 26 + base))
        else:
            out.append(char)

    return "".join(out)