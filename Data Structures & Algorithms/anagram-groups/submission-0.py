import collections


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """Sorting

        Anagramele devin identice cand caracterele lor sunt sortate.
        De exemplu, "eat", "tea", si "ate" toate devin "aet" dupa sortare.
        Folosind forma sortata a fiecarui string ca cheie intr-un hashmap,
        putem grupa toate anagramele impreuna.

        m = num of strings, n = len of longest string
        T = O(m * n log n), S = O(m * n)
        """
        # groups = collections.defaultdict(list)

        # for s in strs:
        #     sorted_s = ''.join(sorted(s))
        #     groups[sorted_s].append(s)

        # return list(groups.values())



        """Hash Map

        In loc sa sortam fiecare string, il reprezentam  ca frecventa
        caracterelor lui. Un array fix de 26 de caractere pentru alfabetul englez
        (in statement sunt doar aceste caractere) calculeaza de cate ori fiecare
        caracter apare in stringul curent. Se transforma in tuplul pentru a fi
        immutable si folosit ca cheie in dictionar. Astfel, grupa stringurile
        care au acelasi count de caractere, ele fiind anagrame

        m = num of strings, n = len of longest string
        T = O(m * n), S = O(m * n)
        """
        groups = collections.defaultdict(list)

        for s in strs:
            char_freq: list[int] = [0] * 26
            for char in s:
                char_freq[ord(char) - ord('a')] += 1
            groups[tuple(char_freq)].append(s)

        return list(groups.values())
