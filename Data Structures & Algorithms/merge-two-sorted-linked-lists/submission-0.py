from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """Recursive

        Fuzionarea recursivă a două liste sortate se realizează alegând întotdeauna
        headul din cele două liste care are valoarea mai mică.
        Headul mai mic trebuie să apară primul în lista rezultată din fuziune.
        Așadar:

        Alegem nodul cu valoarea mai mică.
        Fuzionăm recursiv restul listelor.
        Atașăm rezultatul la nodul ales.

        T = O(m + n), S = O(m + n)
        """
        # if list1 is None:
        #     return list2
        
        # if list2 is None:
        #     return list1
        
        # if list1.val <= list2.val:
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        #     return list1
        
        # list2.next = self.mergeTwoLists(list1, list2.next)
        # return list2



        """Iterative

        Pentru a uni două liste sortate în mod iterativ, construim lista
        rezultată pas cu pas. Păstrăm un pointer node către capătul curent
        al listei unite și, la fiecare pas, alegem headul mai mic dintre
        list1 și list2.

        Deoarece listele sunt deja sortate, headul mai mic trebuie să ocupe
        următoarea poziție în lista unită. Atașăm acel nod, mutăm pointerul mai
        departe și continuăm până când una dintre liste rămâne goală.
        În final, atașăm nodurile rămase din lista care nu este goală.

        Utilizarea unui nod fictiv simplifică și clarifică gestionarea capului
        listei combinate. (fara edge caseuri la inceput daca folosim un dummy node)

        T = O(m + n), S = O(1)
        """
        dummy = ListNode()
        node = dummy

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        
        node.next = list1 or list2

        return dummy.next
