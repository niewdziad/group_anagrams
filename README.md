# group_anagrams
anagram management :)

Inicjalizacja pustego słownika anagram_groups, który będzie przechowywał grupy anagramów. Kluczem będzie posortowany ciąg liter, a wartością będzie lista słów, które są anagramami.

Iteracja przez każde słowo w liście words.

Dla każdego słowa, litery są sortowane, a następnie połączone w jeden ciąg znaków za pomocą metody join(sorted(word)). W ten sposób uzyskuje się posortowany ciąg liter w danym słowie.

Sprawdzenie, czy posortowany ciąg liter (sorted_word) istnieje już w słowniku anagram_groups.

a. Jeśli nie istnieje, dodajemy nowy klucz do słownika, gdzie klucz to posortowany ciąg liter, a wartość to lista zawierająca tylko aktualne słowo.

b. Jeśli klucz istnieje, dodajemy aktualne słowo do listy wartości przypisanej do tego klucza. Dzięki temu wszystkie słowa, które są anagramami, znajdują się w tej samej liście.

Na koniec funkcja zwraca listę list, gdzie każda podlista zawiera słowa, które są anagramami.

W rezultacie, wywołując funkcję group_anagrams(["tsar", "rat", "tar", "star", "tars", "cheese"]), otrzymamy listę grup anagramów, jak pokazano w przykładzie.