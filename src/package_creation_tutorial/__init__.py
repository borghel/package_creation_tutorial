


# __init__.py

# Importation des fonctions depuis string_ops
from .string_ops import reverse_string, count_vowels, capitalize_words

# Fonction d'exemple pour les tests ou d'autres usages
def hello_world():
    return "Bonjour depuis le package_creation_tutorial !"

# Utilisation des fonctions importées
def example_usage():
    print(reverse_string("Hello"))  # Utilisation de reverse_string
    print(count_vowels("Hello"))    # Utilisation de count_vowels
    print(capitalize_words("hello world"))  # Utilisation de capitalize_words
