from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """Hash Map

        Vrem să copiem o listă în care fiecare nod are atât un pointer „next”,
        cât și un pointer „random”. Provocarea constă în faptul că pointerul „random”
        poate indica oriunde — înainte, înapoi sau chiar spre „None”. Așadar, trebuie
        să ne asigurăm că fiecare nod original este copiat exact o singură dată și că
        toți pointerii sunt reconectați corect.

        O soluție simplă in doua treceri:

        Etapa 1: Creăm o copie a fiecărui nod (doar valorile) și stocăm corespondența:
        nod_original → nod_copiat
        Etapa 2: Folosim această corespondență pentru a reconecta pointerii „next” și
        „random” pentru fiecare nod copiat. Astfel, ne asigurăm că toți pointerii sunt
        valizi și că niciun nod nu este duplicat.

        T = O(n), S = O(n)
        """
        # old_to_copy = {None: None}

        # current = head
        # while current:  # in the first iteration, the copies are created
        #     copy = Node(current.val)
        #     old_to_copy[current] = copy
        #     current = current.next

        # current = head
        # while current:
        #     copy = old_to_copy[current]
        #     copy.next = old_to_copy[current.next]
        #     copy.random = old_to_copy[current.random]
        #     current = current.next

        # return old_to_copy[head]



        """Modify Initial List

        Această metodă evită ocuparea de spațiu suplimentar, cum ar fi
        în cazul unui hash map, folosind temporar pointerul „random”
        pentru a stoca nodurile copiate.

        -Pentru fiecare nod original:
        Creăm o copie a acestuia și o stocăm în pointerul „random” al
        nodului original. Pointerul „next” al copiei indică inițial spre
        ceea ce indica pointerul „random” al nodului original.


        -Ulterior:
        Cu toate nodurile copiei create, fixam pointerul random al copiei.
        Adica alegem copia nodului aratat de pointerul random al nodului initial.
        l1.random se gaseste in nextul copiei actuale iar copia acestui random
        in (l2.next).random

        -In final:
        Refacem randomul in lista originala si nextul in copie. 


        Totul se întâmplă folosind doar manipulări de pointeri — fără
        tabele suplimentare, fără hash map.

        T = O(n), S = O(1)
        """
        if head is None:
            return None

        l1 = head
        while l1:
            l2 = Node(l1.val)
            l2.next = l1.random  # save original random
            l1.random = l2  # save the copy (in the freed pointer instead of hash map)
            l1 = l1.next

        new_head = head.random

        l1 = head
        while l1:
            l2 = l1.random
            l2.random = l2.next.random if l2.next else None  # set the random in the copy
            l1 = l1.next

        l1 = head
        while l1 is not None:
            l2 = l1.random
            l1.random = l2.next  # restore original random
            l2.next = l1.next.random if l1.next else None  # set the next in the copy
            l1 = l1.next

        return new_head
