import sys
from pathlib import Path
from stats import get_num_words, character_frequency, sorted_list
count_characters = character_frequency

def get_book_text(filepath: str) -> str:
    path = Path(filepath)
    # treat relative paths as relative to this script's directory
    if not path.is_absolute():
        path = Path(__file__).resolve().parent / path
    if not path.exists():
        raise FileNotFoundError(f"Book file not found: {path}")
    return path.read_text(encoding="utf-8")

def main():
    if sys.argv[1:] == []:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    try:
        text = get_book_text(book_path)
    except Exception as e:
        print(e)
        return
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    for item in sorted_list(text):
        print(f"{item['char']}: {item['num']}")
    print("============= END =============")

# call main to execute the program
main()