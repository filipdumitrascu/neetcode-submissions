class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.children = {}


class PrefixTree:
    """Trie

    Un arbore de prefixe (Trie) este o structură de date de tip arbore
    concepută pentru operații rapide asupra șirurilor de caractere.

    Fiecare nod reprezintă un caracter, iar căile care pornesc de la rădăcină
    reprezintă cuvinte.

    -Prefixele comune sunt partajate, ceea ce economisește spațiu.
    -Fiecare nod are 26 de noduri fiice (pentru literele a-z), indexate direct
    folosind pozițiile caracterelor.
    -Un indicator boolean "end_of_word" ne indică dacă un cuvânt complet se
    termină la acel nod.

    De ce este util Trie:
    -Căutarea cuvintelor și a prefixelor are complexitate O(lungimea cuvântului),
    independent de numărul de cuvinte existente.
    -Ideal pentru probleme care implică căutări în dicționar, completare
    automată și verificări de prefixe.

    n - len(word), t - num(trie nodes)
    insert/search/startsWith: T = O(n),
    S = O(t)
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
