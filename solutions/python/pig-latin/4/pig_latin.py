def translate(text: str) -> str:
    """
    Translate each word from a text to Pig Latin

    :param text: A string of words
    :type text: str
    :return: A string of translated words
    :rtype: str
    """
    split_text: list[str] = text.split()

    vowel: str = "aeiou"

    def find_first_vowel(word: str, y_flag: bool) -> int:
        """
        Return the index of the first vowel
        Vowel is defined: "aeiou"

        :param word: Word string
        :type word: str
        :param y_flag: Include 'y' in search of index
        :type y_flag: bool
        :return: Index of first vowel found, else 0
        :rtype: int
        """
        for index, char in enumerate(word):
            if y_flag and char == "y":
                return index
            if char in vowel:
                return index
        return 0

    def move_consonants(word: str, y_flag: bool = False) -> str:
        index = find_first_vowel(word, y_flag)
        return word[index:] + word[:index]

    def qu_check(word: str) -> str:
        if word[-1] == "q" and word[0] == "u":
            return word[1:] + "u"
        return word

    def followed_by(word: str, follower: str, one: bool) -> bool:
        next_letter = find_first_vowel(word, one)

        if one:
            return word[next_letter] == follower
        return word[next_letter - 1] == follower[0] and word[next_letter] == follower[1]

    def rule1(word: str) -> bool:
        return word.startswith("yt") or word.startswith("xr") or word[0] in vowel

    def rule2(word: str) -> bool:
        if find_first_vowel(word, False) == 0:
            return False
        if rule3(word):
            return False
        return True

    def rule3(word: str) -> bool:
        return followed_by(word, "qu", False)

    def rule4(word: str) -> bool:
        return followed_by(word, "y", True)

    def run(split_text: list[str]) -> str:
        ADD_END: str = "ay"

        final_string: list[str] = []

        for word in split_text:
            if rule1(word):
                final_string.append(word + ADD_END)

            elif rule2(word):
                new_word = move_consonants(word)
                final_string.append(new_word + ADD_END)

            elif rule3(word):
                new_word = move_consonants(word)
                qu_word = qu_check(new_word)
                final_string.append(qu_word + ADD_END)

            elif rule4(word):
                new_word = move_consonants(word, True)
                final_string.append(new_word + ADD_END)

        return " ".join(final_string)

    return run(split_text)
