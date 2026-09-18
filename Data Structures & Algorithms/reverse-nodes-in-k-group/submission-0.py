from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Recursive

        Pentru a inversa nodurile în grupuri de k, verificăm mai întâi dacă segmentul
        curent conține cel puțin k noduri.
        -Dacă sunt mai puține de k, lăsăm nodurile așa cum sunt.
        -Dacă avem k noduri, atunci:
         -Inversăm recursiv restul listei, începând cu nodul care urmează după
          aceste k noduri.
         -Apoi inversăm grupul curent de k noduri.
         -Atașăm grupul inversat la restul deja procesat.

        Aceasta oferă o abordare clară de sus în jos:
        rezolvăm mai întâi restul listei, apoi corectăm grupul curent.
        
        T = O(n), S = O(n / k)
        """
        # group_end = head
        # group_size = 0

        # # Check if there are at least k nodes
        # while group_end and group_size < k:
        #     group_end = group_end.next
        #     group_size += 1

        # # Not enough nodes to form a complete group
        # if group_size == k:
        #     next_group_start = self.recursive(group_end, k)

        #     # Reverse current group
        #     reversed_group_head = next_group_start  # prev
        #     curr = head

        #     while group_size > 0:
        #         temp = curr.next
        #         curr.next = reversed_group_head
        #         reversed_group_head = curr
        #         curr = temp
        #         group_size -= 1

        #     head = reversed_group_head

        # return head



        """Iterative
        
        Inversăm lista câte un grup de dimensiunea k, folosind pointeri,
        fără recursivitate.

        Idei cheie:
        -Folosim un nod fictiv înaintea headului listei pentru a simplifica
        cazurile limită.
        -La fiecare pas:
         1. Găsim al k-lea nod pornind de la nodul anterior al grupului curent.
            Dacă nu mai sunt k noduri rămase, ne oprim (lăsăm restul așa cum este).
         2. Inversăm nodurile din acest segment de dimensiunea k.
         3. Reconectăm segmentul inversat înapoi în listă.
         4. Trecem la următorul grup.
    
        Prin repetarea acestui proces, inversăm fiecare grup complet de k
        noduri, păstrând restul listei intact.

        T = O(n), S = O(1)
        """
        def get_group_end(curr: Optional[ListNode], k: int) -> Optional[ListNode]:
            """Return the kth node starting from curr."""
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        dummy = ListNode(0, head)
        prev_group_end = dummy

        while True:
            curr_group_end = get_group_end(prev_group_end, k)
            if not curr_group_end:
                break

            next_group_start = curr_group_end.next

            # Reverse current group
            prev = next_group_start  # to not lose group connections (update below)
            curr = prev_group_end.next

            while curr != next_group_start:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect previous group to reversed group (update here)
            temp = prev_group_end.next
            prev_group_end.next = curr_group_end
            prev_group_end = temp

        return dummy.next
