def group_anagrams(words):
    anagram_groups = {}  # Słownik przechowujący grupy anagramów, gdzie klucz to posortowany ciąg liter, a wartość to lista słów

    for word in words:
        sorted_word = ''.join(sorted(word))  # Posortowanie liter w słowie i połączenie ich w jeden ciąg znaków
        if sorted_word not in anagram_groups:
            anagram_groups[sorted_word] = [word]  # Jeśli klucz nie istnieje, utwórz nową grupę anagramów z tym słowem
        else:
            anagram_groups[sorted_word].append(word)  # Jeśli klucz istnieje, dodaj słowo do istniejącej grupy anagramów

    return list(anagram_groups.values())  # Zwróć listę list słów, które są anagramami

# Przykładowe dane wejściowe
list_ = ["tsar", "rat", "tar", "star", "tars", "cheese"]
print(group_anagrams(list_))  # [["tsar", "star", "tars"], ["rat", "tar"], ["cheese"]]
