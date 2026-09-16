from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Brute Force

        Stocăm toate nodurile într-un array, astfel încât să putem accesa
        direct nodul situat la n poziții de la capăt. Odată ce știm ce nod trebuie
        șters, nu trebuie decât să ajustăm pointerul „next” al nodului anterior.

        T = O(n), S = O(n)
        """
        # nodes = []
        # curr = head
        # while curr:
        #     nodes.append(curr)
        #     curr = curr.next

        # remove_index = len(nodes) - n
        # if remove_index == 0:
        #     return head.next

        # nodes[remove_index - 1].next = nodes[remove_index].next
        # return head



        """Iteration, two pass

        Pentru a evita o rezolvare prin spatiu aditional, putem face doua treceri
        pentru a elimina nodul. Mai întâi numărăm câte noduri sunt în listă.
        Odată ce știm lungimea totală, nodul care trebuie șters se află la
        poziția total_len - n de la început. Efectuăm o a doua trecere pentru a ajunge
        la nodul situat imediat înaintea acestuia și îl omitem.

        T = O(n), S = O(1)
        """
        # total_len = 0
        # curr = head
        # while curr:
        #     total_len += 1
        #     curr = curr.next

        # remove_index = total_len - n
        # if remove_index == 0:
        #     return head.next

        # curr = head
        # for i in range(total_len - 1):
        #     if (i + 1) == remove_index:
        #         curr.next = curr.next.next
        #         break
        #     curr = curr.next
        # return head



        """Two Pointers

        O solutie si mai eficienta care realizeaza stergerea in spatiu constant si
        doar cu o singura trecere o reprezinta o tehnica smart cu 2 pointeri.
        
        Folosește doi pointeri astfel încât distanța dintre ele să fie exact n.
        Mai întâi, deplasează pointerul din dreapta cu n pași înainte.
        Apoi, deplasează ambii pointeri simultan.
        Când pointerul din dreapta ajunge la capăt, pointerul din stânga se
        va afla chiar înaintea nodului pe care trebuie să-l eliminăm.
        Astfel se evită o trecere separată pentru numărarea lungimii, în timp ce
        lista este parcursă în timp O(N).
        Avantajul principal este că distanța de n noduri ne indică unde trebuie
        să ștergem, fără a stoca noduri sau a calcula mai întâi lungimea.
        Folosim un dummy node pentru a nimeri poninterul left fix inaintea nodului
        n de la coada.

        T = O(n), S = O(1)
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next
    
        left.next = left.next.next
        return dummy.next
