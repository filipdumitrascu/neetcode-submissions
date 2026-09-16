from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """Hash Set

        Pentru a detecta dacă o listă conține un ciclu, o idee simplă este
        să ținem minte fiecare nod pe care îl vizităm. Pe măsură ce avansăm
        prin listă, dacă ajungem vreodată la un nod pe care l-am mai întâlnit
        înainte, înseamnă că lista se intoarce asupra ei însăși — deci
        există un ciclu.

        Dacă ajungem la capăt (null) fără să repetăm vreun nod,
        atunci nu există niciun ciclu.

        T = O(n), S = O(n)
        """
        # curr = head
        # seen = set()

        # while curr:
        #     if curr in seen:
        #         return True
        #     seen.add(curr)

        #     curr = curr.next

        # return False



        """Fast and Slow Pointers
        
        Folosim doi pointeri care se deplasează prin listă cu viteze diferite:
        - cel lent se deplasează cu câte un pas odată
        - cel rapid se deplasează cu câte două pași odată
        Dacă lista conține un ciclu, pointerul rapid va ajunge, în cele din urmă,
        să „depășească” pointerul lent, ceea ce înseamnă că se vor întâlni la un
        anumit nod din interiorul ciclului.

        Dacă lista nu conține un ciclu, pointerul rapid va ajunge la capăt
        (null) și bucla se oprește.
        Această metodă este eficientă și utilizează un spațiu suplimentar
        constant.

        T = O(n), S = O(1)
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
