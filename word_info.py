def get_position(sentence: str, position: int) -> str:
    """
    Returns information about a specific word in a sentence.
    
    Parameters:
        sentence (str): The input sentence containing multiple words.
        position (int): The position (1-based) of the word to analyze.
    
    Returns:
        str: A formatted message showing the word and its letter count.
    """
    words = sentence.split()
    if position < 1 or position > len(words):
        return "Invalid word position."
    word = words[position - 1]
    return f"Word {position} is '{word}' and it has {len(word)} letters."


def count_term_occurrences(sentence: str, term: str) -> str:
    """
    Counts how many times a specific term or letter appears in a sentence,
    ignoring capitalization.
    
    Parameters:
        sentence (str): The sentence to analyze.
        term (str): The term or letter to search for.
    
    Returns:
        str: A formatted message showing how many times the term appears.
    """
    # Convert both sentence and term to lowercase for case-insensitive search
    count = sentence.lower().count(term.lower())
    return f"The term '{term}' appears {count} times in your sentence."


def count_word_occurrences(sentence: str, word: str) -> str:
    """
    Counts how many times a whole word appears in a sentence,
    ignoring capitalization.
    
    Parameters:
        sentence (str): The sentence to analyze.
        word (str): The word to count.
    
    Returns:
        str: A formatted message showing how many times the word appears.
    """
    words = sentence.lower().split()
    count = words.count(word.lower())
    return f"The word '{word}' appears {count} times in your sentence."


def show_total_words(sentence: str) -> str:
    """
    Returns the total number of words in the sentence.
    
    Parameters:
        sentence (str): The sentence to analyze.
    
    Returns:
        str: A formatted message showing the total number of words.
    """
    count = len(sentence.split())
    return f"Your sentence contains {count} words."


def show_last_two_words(sentence: str) -> str:
    """
    Returns the last two words in the sentence.
    Parameters: sentence (str): The sentence to analyze.
    Returns: 
        str: A formatted message with the last two words.
    """
    words = sentence.split()
    if len(words) < 2:
        return "Your sentence has fewer than two words."
    return f"The last two words are '{words[-2]}' and '{words[-1]}'."


def main() -> None:
    """
    Provides a menu-based interface for analyzing a sentence.
    The user enters a sentence, then chooses from several analysis options:
        1. Find the position of a word in the sentence
        2. Count how many times a term or letter appears
        3. Show total number of words in the sentence
        4. Show the last two words in the sentence
        5. Quit
    """
    sentence = input("Enter a sentence: ")

    while True:
        print("\nChoose an option:")
        print("1 - Find the position of a word in the sentence")
        print("2 - Count how many times a term or letter appears")
        print("3 - Show total number of words in the sentence")
        print("4 - Show the last two words in the sentence")
        print("5 - Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            position = int(input("Enter a word position: "))
            print(get_position(sentence, position))

        elif choice == "2":
            term = input("Enter the term or letter to search for: ")
            print(count_term_occurrences(sentence, term))

        elif choice == "3":
            print(show_total_words(sentence))

        elif choice == "4":
            print(show_last_two_words(sentence))

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# Run the program
main()
