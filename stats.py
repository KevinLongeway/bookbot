def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)

def character_frequency(text: str) -> dict:
    frequency = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            frequency[char] = frequency.get(char, 0) + 1
    return frequency

def sort_on(item: dict) -> list:
    return item["num"]

def sorted_list(text: str) -> list:
    freq = character_frequency(text)
    freq_list = [{"char": char, "num": count}
                 for char, count in freq.items()]
    freq_list.sort(key=sort_on, reverse=True)
    return freq_list