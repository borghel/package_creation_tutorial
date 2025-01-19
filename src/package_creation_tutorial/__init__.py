



# __init__.py
from .string_ops import reverse_string, count_vowels, capitalize_words

__all__ = ["reverse_string", "count_vowels", "capitalize_words", "hello_world"]

def hello_world():
    reversed_text = reverse_string("Bonjour")
    vowel_count = count_vowels("Bonjour")
    capitalized_text = capitalize_words("bonjour tout le monde")
    
    return f"Bonjour depuis le package_creation_tutorial !\n" \
           f"Reversed: {reversed_text}\n" \
           f"Vowel count: {vowel_count}\n" \
           f"Capitalized: {capitalized_text}"
