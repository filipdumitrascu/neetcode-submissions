import collections


class Solution:
    def canFinish(self, num_courses: int, prerequisites: list[list[int]]) -> bool:
        """DFS - Cycle Detection

        Fiecare curs reprezintă un nod, iar fiecare condiție prealabilă
        reprezintă o muchie orientată. Poți finaliza toate cursurile numai dacă
        nu există niciun ciclu în acest graf orientat.

        Un ciclu înseamnă:
        - Cursul A necesită cursul B
        - Cursul B necesită cursul C
        - Cursul C necesită cursul A
        Deci rămâi blocat pentru totdeauna.

        Folosim DFS cu detectarea ciclurilor:
        - În timpul efectuării DFS, ține evidența cursurilor din calea de
        recursivitate curentă.
        - Dacă vizităm un curs care se află deja în calea curentă → s-a găsit
        un ciclu.
        - Dacă un curs nu mai are cerințe preliminare, este în regulă.

        v - courses, e - prerequisites
        T = O(v + e), S = O(v + e)
        """
        # Map each course to its prerequisites
        crs_to_pre = {i: [] for i in range(num_courses)}
        for crs, pre in prerequisites:
            crs_to_pre[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False
            if crs_to_pre[crs] == []:
                return True

            visiting.add(crs)
            for pre in crs_to_pre[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            crs_to_pre[crs] = []
            return True

        for c in range(num_courses):
            if not dfs(c):
                return False
        return True



        """Top Sort (Kahn's Algo)

        Tratează fiecare curs ca pe un nod și fiecare condiție prealabilă ca pe
        o muchie orientată. Dacă un curs nu are condiții prealabile, acesta
        poate fi urmat imediat.

        Algoritmul lui Kahn selectează în mod repetat cursurile care nu au
        nicio condiție prealabilă. Când terminăm un curs, eliminăm efectul de
        dependență al acestuia asupra celorlalte cursuri.

        Dacă toate cursurile pot fi urmate în acest mod - nu există ciclu,
        returnează true
        Dacă unele cursuri nu sunt urmate niciodată - există un ciclu,
        returnează false

        v - courses, e - prerequisites
        T = O(v + e), S = O(v + e)
        """
        in_degree = [0] * num_courses
        adj = [[] for _ in range(num_courses)]

        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            in_degree[prerequisite[0]] += 1

        queue = collections.deque()
        for i in range(num_courses):
            if in_degree[i] == 0:
                queue.append(i)

        nodes_visited = 0
        while queue:
            node = queue.popleft()
            nodes_visited += 1

            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return nodes_visited == num_courses
