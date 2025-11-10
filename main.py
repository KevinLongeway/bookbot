from pathlib import Path
from stats import get_num_words

def get_book_text(filepath: str) -> str:
    path = Path(filepath)
    # treat relative paths as relative to this script's directory
    if not path.is_absolute():
        path = Path(__file__).resolve().parent / path
    if not path.exists():
        raise FileNotFoundError(f"Book file not found: {path}")
    return path.read_text(encoding="utf-8")

def main():
    try:
        text = get_book_text("books/frankenstein.txt")
    except Exception as e:
        print(e)
        return
    print(f"Found {get_num_words(text)} total words")

# call main to execute the program
main()