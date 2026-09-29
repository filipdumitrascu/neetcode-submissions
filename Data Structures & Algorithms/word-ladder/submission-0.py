import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        """BFS

        Această problemă poate fi modelată ca găsirea celui mai scurt drum
        într-un graf neponderat, în care fiecare cuvânt reprezintă un nod,
        iar muchiile leagă cuvintele care diferă cu exact un caracter.
        Precalculăm lista de adiacență comparând toate perechile de cuvinte.
        Algoritmul BFS găsește în mod natural cel mai scurt drum, deoarece
        explorează toate nodurile aflate la distanța k înainte de orice nod
        aflat la distanța k+1.

        n - words, m - len(word)
        T = O(n^2 * m), S = (n^2)
        """
        # if (endWord not in wordList) or (beginWord == endWord):
        #     return 0

        # n, m = len(wordList), len(wordList[0])
        # adj = [[] for _ in range(n)]
        # mp = {}
        # for i in range(n):
        #     mp[wordList[i]] = i

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         cnt = 0
        #         for k in range(m):
        #             if wordList[i][k] != wordList[j][k]:
        #                 cnt += 1
        #         if cnt == 1:
        #             adj[i].append(j)
        #             adj[j].append(i)

        # q, res = collections.deque(), 1
        # visit = set()
        # for i in range(m):
        #     for c in range(97, 123):
        #         if chr(c) == beginWord[i]:
        #             continue
        #         word = beginWord[:i] + chr(c) + beginWord[i + 1:]
        #         if word in mp and mp[word] not in visit:
        #             q.append(mp[word])
        #             visit.add(mp[word])

        # while q:
        #     res += 1
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if wordList[node] == endWord:
        #             return res
        #         for nei in adj[node]:
        #             if nei not in visit:
        #                 visit.add(nei)
        #                 q.append(nei)

        # return 0



        """BFS II

        În loc să calculăm în avans întregul graf de adiacență, putem genera
        vecini pe parcurs. Pentru fiecare cuvânt, încercăm să înlocuim fiecare
        caracter cu toate cele 26 de litere. Dacă cuvântul rezultat există în
        setul nostru de cuvinte, acesta este un vecin valid. Această abordare
        sacrifică timpul de calcul în avans în favoarea generării unui număr
        potențial mai mare de vecini în timpul algoritmului BFS.

        n - words, m - len(word)
        T = O(m^2 * n), S = O(m^2 * n)
        """
        # if (endWord not in wordList) or (beginWord == endWord):
        #     return 0

        # words, res = set(wordList), 0
        # q = collections.deque([beginWord])
        # while q:
        #     res += 1
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         if node == endWord:
        #             return res
        #         for i in range(len(node)):
        #             for c in range(97, 123):
        #                 if chr(c) == node[i]:
        #                     continue
        #                 nei = node[:i] + chr(c) + node[i + 1:]
        #                 if nei in words:
        #                     q.append(nei)
        #                     words.remove(nei)
        # return 0



        """BFS III

        Putem folosi modele cu caractere joker pentru a grupa în mod eficient
        cuvintele aflate la o distanță de un caracter una de alta. Pentru
        fiecare cuvânt, se creează modele prin înlocuirea fiecărui caracter
        cu un caracter joker. Cuvintele care au același model sunt vecine.
        Această precalculare permite căutarea vecinilor în timp O(1) în timpul
        BFS, deoarece trebuie doar să verificăm grupurile de modele.

        n - words, m - len(word)
        T = O(m^2 * n), S = O(m^2 * n)
        """
        # if endWord not in wordList:
        #     return 0

        # nei = collections.defaultdict(list)
        # wordList.append(beginWord)
        # for word in wordList:
        #     for j in range(len(word)):
        #         pattern = word[:j] + "*" + word[j + 1 :]
        #         nei[pattern].append(word)

        # visit = set([beginWord])
        # q = collections.deque([beginWord])
        # res = 1
        # while q:
        #     for i in range(len(q)):
        #         word = q.popleft()
        #         if word == endWord:
        #             return res
        #         for j in range(len(word)):
        #             pattern = word[:j] + "*" + word[j + 1 :]
        #             for neiWord in nei[pattern]:
        #                 if neiWord not in visit:
        #                     visit.add(neiWord)
        #                     q.append(neiWord)
        #     res += 1
        # return 0



        """Meet In The Middle (BFS)

        Algoritmul BFS standard explorează un număr exponențial mai mare de
        noduri pe măsură ce distanța crește. Prin rularea simultană a două
        căutări BFS pornind de la beginWord și endWord, ne putem întâlni la
        mijloc, reducând efectiv la jumătate adâncimea de căutare și diminuând
        considerabil spațiul de căutare. La fiecare pas, extindem frontiera mai
        mică pentru a echilibra sarcina de lucru.

        n - words, m - len(word)
        T = O(m^2 * n), S = O(m^2 * n)
        """
        if endWord not in wordList or beginWord == endWord:
            return 0
        
        m = len(wordList[0])
        wordSet = set(wordList)
        
        qb, qe = collections.deque([beginWord]), collections.deque([endWord])
        fromBegin, fromEnd = {beginWord: 1}, {endWord: 1}

        while qb and qe:
            if len(qb) > len(qe):
                qb, qe = qe, qb
                fromBegin, fromEnd = fromEnd, fromBegin
            for _ in range(len(qb)):
                word = qb.popleft()
                steps = fromBegin[word]
                for i in range(m):
                    for c in range(97, 123):
                        if chr(c) == word[i]:
                            continue
                        nei = word[:i] + chr(c) + word[i + 1:]
                        if nei not in wordSet:
                            continue
                        if nei in fromEnd:
                            return steps + fromEnd[nei]
                        if nei not in fromBegin:
                            fromBegin[nei] = steps + 1
                            qb.append(nei)
        return 0
