import collections


class Solution:
    def findOrder(self, num_courses: int, prerequisites: list[list[int]]) -> list[int]:
        """Cycle Detection (DFS)

        Fiecare curs reprezintă un nod, iar fiecare cerință prealabilă
        reprezintă o muchie orientată.
        Dorim o ordine a cursurilor astfel încât toate cerințele prealabile
        ale unui curs să fie îndeplinite înaintea acestuia.

        Folosind DFS, vom:
        - Identifica ciclurile (care fac imposibilă finalizarea tuturor
        cursurilor)
        - Adăuga un curs la rezultat după ce toate cerințele sale prealabile
        au fost procesate (acest lucru oferă în mod natural o ordine topologică
        validă)

        v - courses, e - prerequisites
        T = O(v + e), S = O(v + e)
        """
        # prereq = {c: [] for c in range(num_courses)}
        # for crs, pre in prerequisites:
        #     prereq[crs].append(pre)

        # output = []
        # visit, cycle = set(), set()

        # def dfs(crs):
        #     if crs in cycle:
        #         return False
        #     if crs in visit:
        #         return True

        #     cycle.add(crs)
        #     for pre in prereq[crs]:
        #         if dfs(pre) == False:
        #             return False

        #     cycle.remove(crs)
        #     visit.add(crs)

        #     output.append(crs)
        #     return True

        # for c in range(num_courses):
        #     if dfs(c) == False:
        #         return []

        # return output



        """Topological Sort (Kahn's Algorithm)

        Tratează fiecare curs ca pe un nod și fiecare cerință prealabilă ca pe
        o muchie orientată.
        Un curs poate fi urmat numai după ce toate cerințele preliminare ale
        acestuia au fost îndeplinite.

        Algoritmul lui Kahn funcționează astfel:
        - Se aleg întotdeauna cursurile care nu mai au cerințe preliminare
        restante (gradul de intrare = 0)
        - Se elimină aceste cursuri din graf
        - Se deblochează treptat alte cursuri

        Dacă la final unele cursuri rămân blocate, înseamnă că există un ciclu,
        deci nu este posibilă nicio ordine validă.

        v - courses, e - prerequisites
        T = O(v + e), S = O(v + e)
        """
        # indegree = [0] * num_courses
        # adj = [[] for _ in range(num_courses)]
        # for src, dst in prerequisites:
        #     indegree[dst] += 1
        #     adj[src].append(dst)

        # q = collections.deque()
        # for n in range(num_courses):
        #     if indegree[n] == 0:
        #         q.append(n)

        # finish, output = 0, []
        # while q:
        #     node = q.popleft()
        #     output.append(node)
        #     finish += 1
        #     for nei in adj[node]:
        #         indegree[nei] -= 1
        #         if indegree[nei] == 0:
        #             q.append(nei)

        # if finish != num_courses:
        #     return []
        # return output[::-1]



        """Topological Sort (DFS)

        Dorim o ordonare a cursurilor astfel încât fiecare curs să apară după
        cursurile care constituie premise ale acestuia.
        Această abordare combină sortarea topologică cu o traversare de tip DFS.

        Ideea este următoarea:
        - Începem cu cursurile care nu au premise (in_degree = 0)
        - Odată ce alegem un curs, îl „eliminăm” prin reducerea in_degree al
        cursurilor care depind de el
        - Când in_degree al unui curs dependent devine 0, acesta poate fi ales
        în siguranță, așa că continuăm DFS pornind de la el

        Dacă putem vizita toate cursurile în acest fel, există o ordine validă.
        Dacă nu, există un ciclu, ceea ce face imposibilă obținerea unei astfel
        de ordini.

        v - courses, e - prerequisites
        T = O(v + e), S = O(v + e)
        """
        adj = [[] for _ in range(num_courses)]
        indegree = [0] * num_courses
        for nxt, pre in prerequisites:
            indegree[nxt] += 1
            adj[pre].append(nxt)

        output = []

        def dfs(node):
            output.append(node)
            indegree[node] -= 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    dfs(nei)

        for i in range(num_courses):
            if indegree[i] == 0:
                dfs(i)

        return output if len(output) == num_courses else []
