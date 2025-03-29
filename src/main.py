from time import time_ns


def string_numerical_represent(word) -> list[int]:
    return [ord(letter) for letter in word]


def load_words() -> list[tuple[list[int], str]]:
    with open("src/allowed_words.txt") as FILE:
        data: list[tuple[list[int], str]] = [(string_numerical_represent(i), i) for i in FILE.read().split("\n") if i]
    return data


# NOTICE: This function is currently unused
def SABCM(string: str) -> int:
    abc: str = "abcdefghijklmnopqrstuvwxyz"
    for char in string:
        abc = abc.replace(char, "1")
    for i in abc:
        if i != "1":
            abc = abc.replace(i, "0")
    return int(abc, 2)


def convert(phrase: str, wordle_output: str) -> tuple[list[int], list[int], list[tuple[int, int]]]:
    cases: list[str] = ["🟥","🟨","🟩"]
    wordle_output = wordle_output.replace("0", cases[0]).replace("1", cases[1]).replace("2", cases[2])
    letters = []
    must = []
    ignore = []
    for i,it in enumerate(wordle_output):
        if it == cases[1]:
            letters.append(phrase[i])
        if it == cases[2]:
            must.append((i, phrase[i]))
        if it == cases[0]: 
            ignore.append(phrase[i])

    return (
        string_numerical_represent(letters),
        string_numerical_represent(ignore),
        [(index, string_numerical_represent(letter)[0]) for index,letter in must]
    )
    





def main() -> None:
    words: list[tuple[list[int], str]] = load_words()
    phrase: str = input("start word? ")
    output: str = input("validity? ")
    letters, ignore, must = convert(phrase, output)
    if len(phrase) != len(output):
        exit()
    log = [(output, phrase)]
    x = time_ns()
    words = [
        (numerical_representation,word) for numerical_representation,word in words
        if (
            not any(map((lambda x: x in ignore), numerical_representation))  # if any characters in ignore are not present
        ) and (
            all(map((lambda x: x in numerical_representation), letters))  # if a character from letters is present somewhere
        ) and (
            # if characters from must are there and are in the correct position
            sum(
                (ai == i and aai == it)
                for (ai, aai), (i, it) in zip(must, enumerate(numerical_representation))
            ) >= len(must)
        )
    ]
    print(*words, sep="\n")
    print(len(words), must, letters, ignore, output, time_ns()-x)


if __name__ == "__main__":
    main()
