from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """Array

        Pentru a reordona lista legată după modelul:
        L0 → Ln → L1 → L(n-1) → L2 → ...

        O abordare simplă constă în stocarea tuturor nodurilor într-un
        array. Odată stocate, putem accesa cu ușurință nodurile atât
        de la început, cât și de la sfârșit, folosind doi pointeri.
        Prin legarea alternativă a nodurilor din față (indexul i)
        și din spate (indexul j), putem rearanja lista în ordinea dorită.

        T = O(n), S = O(n)
        """
        # if not head:
        #     return

        # nodes = []
        # cur = head
        # while cur:
        #     nodes.append(cur)
        #     cur = cur.next

        # i = 0
        # j = len(nodes) - 1
        # while i < j:
        #     nodes[i].next = nodes[j]
        #     i += 1
        #     if i >= j:
        #         break
        #     nodes[j].next = nodes[i]
        #     j -= 1

        # nodes[i].next = None



        """Rverse and Merge

        Pentru a reordona lista după modelul
        L1 → Ln → L2 → Ln-1 → L3 → Ln-2 → ...,
        putem împărți problema în trei pași simpli:

        1. Găsim mijlocul listei folosind pointerii
        „slow” și „fast”. Astfel, lista se împarte în
        două jumătăți.

        2. Inversăm a doua jumătate a listei.
        Astfel, este ușor să îmbinăm nodurile din față
        și din spate alternativ.

        3. Îmbinăm cele două jumătăți unul câte unul:
        Luăm un nod din prima jumătate (first), apoi unul
        din a doua jumătate inversată (second) și repetăm.

        Această metodă este clară, intuitivă și utilizează
        doar O(1) spațiu suplimentar.

        T = O(n), S = O(1)
        """
        # 1. Find half
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse
        second = slow.next
        slow.next = None  # split
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # 3. Merge
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
