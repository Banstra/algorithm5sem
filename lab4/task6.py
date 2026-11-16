def reverse_words(text: str) -> str:
    words = text.split()

    def reverse_from(index: int) -> list[str]:
        if index < 0:
            return []
        return [words[index]] + reverse_from(index - 1)

    return " ".join(reverse_from(len(words) - 1))

if __name__ == "__main__":
    input_text = input("Введите текст: ")
    reversed_text = reverse_words(input_text)
    print(f"Текст с обратным порядком слов: {reversed_text}")
