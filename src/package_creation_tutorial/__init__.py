

# Importation des fonctions ou classes nécessaires depuis les modules du package
from .string_ops import reverse_string, count_vowels, capitalize_words

# Une fonction d'exemple pour démonstration
def hello():
    return "Bonjour depuis le package_creation_tutorial !"

# Liste des éléments accessibles directement lorsque ce package est importé
__all__ = [
    "reverse_string",
    "count_vowels",
    "capitalize_words",
    "hello",
]
