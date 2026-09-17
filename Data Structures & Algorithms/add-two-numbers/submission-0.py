from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Recursive

        Adunăm cele două liste exact așa cum adunăm două numere pe hârtie.

        Fiecare nod conține o cifră, iar deoarece listele sunt stocate în
        ordine inversă, capul listei conține poziția unităților — ceea ce
        simplifică adunarea.
        
        La fiecare pas:

        -Se ia o cifră din l1 (sau 0 dacă lista s-a terminat)
        -Preluăm o cifră din l2 (sau 0 dacă s-a terminat)
        -Le adunăm cu carryul primit
        -Creăm un nod nou pentru cifra curentă (suma % 10)
        -Transmitem noul carry (suma // 10) mai departe folosind recursivitatea

        Recursivitatea procesează în mod natural cifrele de la stânga la
        dreapta și se oprește numai când:

        -ambele liste sunt procesate complet și
        -nu mai rămâne niciun carry.

        T = O(m + n), S = O(m + n)
        """
        # def add(l1: Optional[ListNode], l2: Optional[ListNode], carry: int) -> Optional[ListNode]:
        #     if not l1 and not l2 and carry == 0:
        #         return None

        #     value_l1 = l1.val if l1 else 0
        #     value_l2 = l2.val if l2 else 0

        #     carry, val = divmod(value_l1 + value_l2 + carry, 10)

        #     next_node = add(
        #         l1.next if l1 else None,
        #         l2.next if l2 else None,
        #         carry,
        #     )

        #     return ListNode(val, next_node)

        # return add(l1, l2, 0)



        """Iterative

        Simulăm adunarea obișnuită la fel cum o facem pe hârtie
        — cifră cu cifră. Listele stochează numerele în ordine inversă,
        astfel încât primele noduri reprezintă poziția cifrei 1.
        
        Acest lucru face ca adunarea să fie simplă:
        -Adunăm cele două cifre.
        -Adunăm carryul din pasul anterior.
        -Salvăm cifra rezultată (suma % 10) într-un nod nou.
        -Actualizează carryul (suma // 10).
        -Deplasează ambii indicatori mai departe.
        
        Continuăm până când ambele liste sunt finalizate ȘI nu mai
        rămâne niciun carry. Un nod duumy ne ajută să construim și să
        returnăm cu ușurință lista finală.

        T = O(m + n), S = O(1)
        """
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            value_l1 = l1.val if l1 else 0
            value_l2 = l2.val if l2 else 0

            # new digit
            val = value_l1 + value_l2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            # update ptrs
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
