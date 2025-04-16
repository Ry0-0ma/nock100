def reverse_sentence(sentence: str) -> str:
    reverse = sentence[::-1]
    return reverse


if __name__ == "__main__":
    reverse = reverse_sentence('stressed')
    print(reverse)