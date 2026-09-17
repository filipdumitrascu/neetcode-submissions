class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    """Hash Map + Doubly Linked List

    Ne dorim ca toate operațiile să aibă complexitate O(1), respectând în
    același timp regulile LRU (Least Recently Used).

    Pentru a realiza acest lucru, combinăm:
    - un Hash Map -> care mapeaza cheia la pointerul nodului. Astfel, stim
    mereu in memorie unde este nodul (acem pointerul) si evitam parcuregera
    intregii liste
    - Listă dublu inlantuita -> mutăm rapid nodurile în poziția celui mai
    recent utilizat și eliminăm nodul cel mai puțin recent utilizat de la
    celălalt capăt în O(1).

    Păstrăm:
    -Nodul cel mai recent utilizat aproape de partea dreaptă.
    -Nodul cel mai puțin recent utilizat aproape de partea stângă.
    
    De fiecare dată când:
    -Obținem o cheie: 
      -mutăm nodul respectiv spre dreapta (cel mai recent utilizat).
    -Introducem o cheie:
     -Dacă există: 
      -actualizăm valoarea și îl mutăm spre dreapta.
     -Dacă este nou:
      -Dacă s-a atins capacitatea maximă: eliminăm nodul real situat
      cel mai la stânga (LRU).
      -Insertăm noul nod în partea dreaptă.

    Nodurile dummy din stânga și din dreapta simplifică logica
    de inserare/eliminare.

    get/put: T = O(1)
    space: S = O(n)
    """
    def __init__(self, capacity: int):
        self.len = 0
        self.cap = capacity
        self.cache = {}  # key -> node (for pointer locations, not for key-val store)

        # left = Least Recently Used, right = Most Recently Used
        # The boundaries are not elements. They are dummy nodes
        self.left_boundary = Node(0, 0)
        self.right_boundary = Node(0, 0)

        self.left_boundary.next = self.right_boundary
        self.right_boundary.prev = self.left_boundary

    def _insert(self, node: Node):
        """Insert node at right because it is the MRU"""
        node.next = self.right_boundary
        node.prev = self.right_boundary.prev

        self.right_boundary.prev.next = node
        self.right_boundary.prev = node

    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
            self.cache[key] = Node(key, value)
            self._insert(self.cache[key])
            return

        self.len += 1
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        # Remove from the list and the hashmap the LRU
        if self.len > self.cap:
            lru = self.left_boundary.next
            self._remove(lru)
            del self.cache[lru.key]
            self.len -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
