from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Recursive

        Inversarea unei liste prin recursivitate se realizeaza gandindu-ne in
        termeni de „inversam restul, apoi corectam pointerul nodului curent”.
        Cand ajungem recursiv la sfarsitul listei, acel ultim nod devine noul cap al
        listei. Pe masura ce recursivitatea se deruleaza, fiecare nod indica inapoi
        catre cel care l-a apelat. In final, setam pointerul „next” al capului initial
        la null pentru a finaliza inversarea. Aceasta abordare utilizeaza stiva de
        apeluri pentru a inversa in mod natural directia pointerilor.

        T = O(n), S = O(n)
        """
        # if not head:
        #     return None

        # new_head = head

        # # 1 -> 2 -> 3 -> ...
        # if head.next:  # 2
        #     new_head = self.reverseList(head.next)  # ... -> 3 -> 2
        #     head.next.next = head  # 2 -> 1
        # head.next = None  # 1 -> None

        # return new_head



        """Iterative

        Inversarea iterativă a unei liste constă în schimbarea direcției pointerilor
        pas cu pas. Parcurgem lista de la stânga la dreapta și, pentru fiecare nod, 
        redirecționăm pointerul său „next” astfel încât să indice spre nodul din spatele său.

        Pentru a evita pierderea accesului la restul listei, păstrăm trei pointeri:

        curr → nodul curent pe care îl procesăm
        prev → nodul care ar trebui să urmeze după curr odată ce lista este inversată
        temp → nodul următor inițial (astfel încât să nu rupem lanțul)

        Prin mutarea acestor pointeri înainte la fiecare pas, inversăm treptat întreaga listă.
        Când curr devine nul, lista este complet inversată, iar prev indică noul cap al listei.

        T = O(n), S = O(1)
        """
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
