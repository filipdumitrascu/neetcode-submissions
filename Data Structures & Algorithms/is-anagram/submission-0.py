class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Sorting

        Daca 2 stringuri sunt anagrame, acestea au aceleasi caractere cu
        aceeasi frecventa. Sortand ambele stringuri, si pozitia caracterelor
        devine identica. Astfel, stringurile sunt egale.

        T  = O(n log n), S = O(n)
        """
        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)



        """Array (for ASCII characters)

        Mai bine decat sortarea, putem sa numaram de cate ori apar ce caractere
        in string. Din moment ce problema garanteaza literele mici ale afabetului
        engelz, un array de size fix, lungime 26 e suficient. Declaram un singur
        array unde crestem valoarea de pe pozitia  ord(i) - ord('a')
        pentru litera 'i' daca litera apara in stringul s si o scadem daca apare
        in t.  Daca la final toate cele 26 de caractere au valoarea egala cu 0
        inseamna ca in cele 2 stringuri numarul de aparitii ale feicarui caracter
        este acelasi ==> sunt anagrame.

        T = O(n), S = O(26) = O(1)
        """
        # if len(s) != len(t):
        #     return False

        # char_freq: list[int] = [0] * 26
        # for i in range(len(s)):
        #     char_freq[ord(s[i]) - ord('a')] += 1
        #     char_freq[ord(t[i]) - ord('a')] -= 1
        
        # return all(freq == 0 for freq in char_freq)



        """Hash Map (for Unicode characters)

        Rezolvarea este similara cu anterioarea doar ca in cazul in care lucram
        cu caractere unicode, (nu e harcodat 26), trebuie folosit un hash map.

        T = O(n), S = O(u) = O(1)
        """
        if len(s) != len(t):
            return False

        char_freq: dict[str, int] = {}
        for i in range(len(s)):
            char_freq[s[i]] = char_freq.get(s[i], 0) + 1
            char_freq[t[i]] = char_freq.get(t[i], 0) - 1

        return all(freq == 0 for freq in char_freq.values())
