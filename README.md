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


Initializing an empty anagram_groups dictionary that will store anagram groups. The key will be a sorted string of letters and the value will be a list of words that are anagrams.

Iterate through each word in the list of words.

For each word, the letters are sorted and then combined into one string using the join(sorted(word)) method. This way you get a sorted sequence of letters in a given word.

Check if the sorted string of letters (sorted_word) already exists in the anagram_groups dictionary.

a. If it does not exist, we add a new key to the dictionary, where the key is a sorted string of letters and the value is a list containing only the current word.

b. If the key exists, we add the current word to the list of values ​​​​assigned to this key. This ensures that all words that are anagrams are in the same list.

Finally, the function returns a list of lists, where each sublist contains words that are anagrams.

As a result, by calling the function group_anagrams(["tsar", "rat", "tar", "star", "tars", "cheese"]), we will get a list of anagram groups as shown in the example.