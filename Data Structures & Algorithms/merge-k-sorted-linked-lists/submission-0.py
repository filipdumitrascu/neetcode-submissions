from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Brute Force    TLE

        Cea mai simplă metodă de a uni toate listele inlantuite este aceea de a
        ignora structura listelor (ca sunt sortate): de a colecta toate valorile,
        de a le sorta și apoi de a reconstrui o singură listă inlantuita sortată.
        Această metodă nu folosește nicio logică sofisticată de unire — se bazează
        exclusiv pe colectare și sortare. Este ușor de implementat, dar nu este
        eficientă, deoarece sortarea ocupă cea mai mare parte a timpului de execuție.

        T = O(n log n), S = O(n)
        """
        # nodes = []
        # for lst in lists:
        #     while lst:
        #         nodes.append(lst.val)
        #         lst = lst.next
        # nodes.sort()

        # dummy = ListNode()
        # curr = dummy

        # for node in nodes:
        #     curr.next = ListNode(node)
        #     curr = curr.next
        # return dummy.next



        """K Pointers

        Alegem în mod repetat cel mai mic head dintre toate listele și îl adăugăm
        la lista noastră de rezultate.
        La fiecare pas:

        -Analizăm headul al fiecărei liste care nu este goală.
        -Alegem cel cu cea mai mică valoare.
        -Deplasăm pointerul acelei liste mai departe.
        -Adăugăm nodul ales la lista noastră combinată.

        Acest procedeu este similar cu combinarea a k arrayuri sortate prin
        alegerea constantă a celui mai mic element disponibil.

        n - num(nodes), k - num(lists)
        T = O(n * k), S = O(1)
        """
        # res = ListNode(0)
        # cur = res

        # while True:
        #     min_node = -1
        #     for i in range(len(lists)):
        #         if not lists[i]:
        #             continue

        #         if min_node == -1 or lists[min_node].val > lists[i].val:
        #             min_node = i

        #     if min_node == -1:
        #         break

        #     cur.next = lists[min_node]
        #     lists[min_node] = lists[min_node].next
        #     cur = cur.next

        # return res.next



        """Merge Lists One by One

        În loc să îmbinăm toate cele k liste deodată cu k pointeri, le putem îmbina pe rând.
        Mai întâi îmbinăm lista 0 cu lista 1 → obținem o listă sortată.
        Apoi îmbinăm rezultatul cu lista 2.
        Apoi îmbinăm rezultatul cu lista 3.
        Repetăm până când toate listele sunt îmbinate.

        Fiecare operație de îmbinare este identică cu problema standard
        „Imbinarea a două liste inlantuite sortate”:
        -Comparăm capetele.
        -Atașăm cea mai mică.
        -Deplasăm indicatorul listei respective mai departe.
        -Continuăm până când una dintre liste rămâne goală, apoi atașăm
        restul celeilalte liste.

        T = O(n * k), S = O(1)
        """
        # def merge_two_lists(head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        #     dummy = ListNode()
        #     curr = dummy

        #     while head1 and head2:
        #         if head1.val < head2.val:
        #             curr.next = head1
        #             head1 = head1.next
        #         else:
        #             curr.next = head2
        #             head2 = head2.next
        #         curr = curr.next

        #     if head1:
        #         curr.next = head1

        #     if head2:
        #         curr.next = head2

        #     return dummy.next

        # if len(lists) == 0:
        #     return None

        # for i in range(1, len(lists)):
        #     lists[i] = merge_two_lists(lists[i - 1], lists[i])

        # return lists[-1]



        """Divide and Conquer

        În loc să îmbinăm toate cele k liste simultan (cu k pointeri) sau una câte una,
        în ordine, putem folosi o strategie de tip „divide and conquer, similară modului în
        care funcționează merge sort.

        Idee:
        -Împărțim lista de liste inlantuite în două jumătăți.
        -Îmbinăm recursiv jumătatea din stânga într-o singură listă sortată.
        -Îmbinăm recursiv jumătatea din dreapta într-o singură listă sortată.
        -În final, îmbinăm aceste două liste sortate într-o singură listă sortată.

        Prin îmbinarea constantă a perechilor de liste, reducem efortul total
        comparativ cu îmbinarea secvențială a celor k liste.
        Fiecare îmbinare a două liste este liniară în raport cu lungimea lor totală,
        iar numărul de niveluri de îmbinare este de aproximativ log k.

        Acest lucru face ca abordarea să fie atât clară, cât și eficientă.

        T = O(n log k), S = O(k)
        """
        def merge_two_lists(head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            curr = dummy

            while head1 and head2:
                if head1.val < head2.val:
                    curr.next = head1
                    head1 = head1.next
                else:
                    curr.next = head2
                    head2 = head2.next
                curr = curr.next

            if head1:
                curr.next = head1

            if head2:
                curr.next = head2

            return dummy.next

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_lists.append(merge_two_lists(l1, l2))
            lists = merged_lists
        return lists[0]
