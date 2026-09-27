import collections


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        """Cycle Detection (DFS)

        Un arbore nu poate conține un ciclu.
        Pe măsură ce se adaugă muchii una câte una, prima muchie care formează
        un ciclu este conexiunea redundantă.

        Pentru fiecare muchie nouă (u, v):
        - Se adaugă temporar în graf
        - Se execută o căutare în adâncime (DFS) pentru a verifica dacă
        există un ciclu
        - Dacă în timpul căutării în adâncime se revizitează un nod (fără a veni
        de la părintele său), se formează un ciclu → acea muchie este răspunsul

        v - vertices, e - edges
        T = O(e * (v + e)), S = O(v + e)
        """
        # n = len(edges)
        # adj = [[] for _ in range(n + 1)]

        # def dfs(node, par):
        #     if visit[node]:
        #         return True

        #     visit[node] = True
        #     for nei in adj[node]:
        #         if nei == par:
        #             continue
        #         if dfs(nei, node):
        #             return True
        #     return False

        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        #     visit = [False] * (n + 1)

        #     if dfs(u, -1):
        #         return [u, v]
        # return []



        """DFS (Optimal) 

        În loc să verificăm dacă există un ciclu după fiecare muchie, construim
        întregul graf o singură dată și identificăm nodurile ciclului printr-o
        singură căutare în adâncime (DFS).

        Ideea principală:
        - Într-un graf neorientat format din n muchii între n noduri, există
        exact un singur ciclu.
        - În timpul parcurgerii în adâncime (DFS), dacă ajungem la un nod care
        a fost deja vizitat, tocmai am găsit începutul ciclului.
        - Pe măsură ce recursivitatea „se derulează” înapoi, marcăm fiecare nod
        de pe acea cale de întoarcere ca făcând parte din ciclu, până când
        ajungem înapoi la începutul ciclului.

        După ce avem setul ciclului (toate nodurile care se află pe ciclu):
        - Arta redundantă trebuie să conecteze două noduri ale ciclului.
        - Problema cere muchia care apare ultima în intrare dintre muchiile ciclului,
        așa că scanăm muchiilea începând de la sfârșit și returnăm prima muchie
        (u, v) în care u și v se află amândouă în ciclu.

        v - vertices, e - edges
        T = O(e * (v + e)), S = O(v + e)
        """
        # n = len(edges)
        # adj = [[] for _ in range(n + 1)]
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)

        # visit = [False] * (n + 1)
        # cycle = set()
        # cycle_start = -1

        # def dfs(node, par):
        #     nonlocal cycle_start
        #     if visit[node]:
        #         cycle_start = node
        #         return True

        #     visit[node] = True
        #     for nei in adj[node]:
        #         if nei == par:
        #             continue
        #         if dfs(nei, node):
        #             if cycle_start != -1:
        #                 cycle.add(node)
        #             if node == cycle_start:
        #                 cycle_start = -1
        #             return True
        #     return False

        # dfs(1, -1)

        # for u, v in reversed(edges):
        #     if u in cycle and v in cycle:
        #         return [u, v]

        # return []



        """Topological Sort (Kahn's Algorithm)

        Această metodă se bazează pe ideea de „îndepărtare a frunzelor”
        (denumită adesea „tăiere topologică”). Chiar dacă graficul este
        neorientat, putem totuși elimina în mod repetat nodurile cu gradul 1:
        - Nodurile cu gradul 1 nu pot face parte dintr-un ciclu (un ciclu
        necesită ca fiecare nod să aibă gradul ≥ 2).
        - Așadar, introducem toate nodurile cu gradul 1 într-o coadă și le
        eliminăm.
        - Când eliminăm un nod, gradul vecinului său scade; acel vecin ar
        putea deveni o nouă frunză (grad 1), așa că îl eliminăm la rândul său.
        - După finalizarea acestui proces, singurele noduri rămase cu grad > 0
        sunt exact nodurile ciclului.

        În final, muchia redundantă trebuie să fie o muchie ale cărei ambele
        capete se află încă în ciclu. Deoarece avem nevoie de ultima astfel de
        muchie în ordinea de intrare, scanăm muchiile în sens invers și
         returnăm prima muchie care leagă două noduri rămase ale ciclului.

        v - vertices, e - edges
        T = O(e * (v + e)), S = O(v + e)
        """
        n = len(edges)
        indegree = [0] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        q = collections.deque()
        for i in range(1, n + 1):
            if indegree[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()
            indegree[node] -= 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)

        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v]:
                return [u, v]
        return []



        """Disjoint Set Union

        Folosește metoda „Disjoint Set Union” (Union-Find) pentru a urmări
        componentele conexe în timp ce adaugi muchii una câte una.

        - Inițial, fiecare nod constituie o componentă separată.
        - Când adăugăm o muchie (u, v):
            - Dacă u și v se află deja în aceeași componentă, adăugarea acestei
            muchii creează un ciclu.
            - Această muchie este exact conexiunea redundantă.
        - Dacă se află în componente diferite, le unim fără probleme.

        Deoarece muchiile sunt procesate în ordine, prima muchie care nu poate
        fi inclusă în uniune este răspunsul.

        v - vertices, e - edges
        T = O(v + e alpha(v)), S = O(v)
        """
        # par = [i for i in range(len(edges) + 1)]
        # rank = [1] * (len(edges) + 1)

        # def find(n):
        #     p = par[n]
        #     while p != par[p]:
        #         par[p] = par[par[p]]
        #         p = par[p]
        #     return p

        # def union(n1, n2):
        #     p1, p2 = find(n1), find(n2)

        #     if p1 == p2:
        #         return False
        #     if rank[p1] > rank[p2]:
        #         par[p2] = p1
        #         rank[p1] += rank[p2]
        #     else:
        #         par[p1] = p2
        #         rank[p2] += rank[p1]
        #     return True

        # for n1, n2 in edges:
        #     if not union(n1, n2):
        #         return [n1, n2]
