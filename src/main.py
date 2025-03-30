from time import time_ns


def string_numerical_represent(word) -> list[int]:
    return [ord(letter) for letter in word]


def load_words() -> list[tuple[list[int], str]]:
    with open("src/allowed_words.txt") as FILE:
        data: list[tuple[list[int], str]] = [(string_numerical_represent(i), i) for i in FILE.read().split("\n") if i]
    return data


def wordlify(word: str, wordle_output: str) -> str:
    cases: list[str] = ["🟥","🟨","🟩"]
    length: int = len(word) + 4
    wordle_output: str = ''.join(map((lambda x: cases[int(x)]), list(wordle_output)))
    return rf"""
        /{"="*length}\/{"="*(length + 5)}\
        |{word.center(length)}||{wordle_output.center(length)}|
        \{"="*length}/\{"="*(length + 5)}/
    """


def convert(phrase: str, wordle_output: str) -> tuple[list[int], list[int], list[tuple[int, int]]]:
    letters, must, ignore = [], [], []
    for i,it in enumerate(wordle_output):
        match it:
            case "1":
                letters.append(phrase[i])
            case "2":
                must.append((i, phrase[i]))
            case "0": 
                ignore.append(phrase[i])

    return (
        string_numerical_represent(letters),
        string_numerical_represent(ignore),
        [(index, string_numerical_represent(letter)[0]) for index,letter in must]
    )


# The filter function
def word_filter(numerical_representation: list[int], ignore: list[int], letters: list[int], must: list[tuple[int, int]]) -> bool:
    # Check if no character in `ignore` is in the word
    if any(ch in ignore for ch in numerical_representation):
        return False
    # Check if all required letters are present somewhere in the word
    if not all(letter in numerical_representation for letter in letters):
        return False
    # Check if `must` characters are in the correct positions
    if not all(numerical_representation[ai] == aai for ai, aai in must):
        return False
    return True

 
def main() -> None:
    words: list[tuple[list[int], str]] = load_words()
    phrase: str = input("start word? ")
    output: str = input("validity? ")
    letters, ignore, must = convert(phrase, output)
    
    if len(phrase) != len(output):
        exit()  # Make sure the string length and the wordle output have the same length
    start_time: int = time_ns()

    # Apply filtering to words
    filtered_words: list[tuple[list[int], str]] = [
        (numerical_representation, word) for numerical_representation, word in words if word_filter(
            numerical_representation,
            ignore, letters, must
        )
    ]

    print(len(filtered_words),"words |", f"{time_ns() - start_time}ns")
    print(*[i[1] for i in filtered_words], sep="\n")
    print(wordlify(phrase, output))


if __name__ == "__main__":
    main()

