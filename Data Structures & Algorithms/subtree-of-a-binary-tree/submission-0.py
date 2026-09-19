from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """Recursvie DFS

        Pentru a verifica dacă un arbore este un subarbore al altuia, facem
        două lucruri:
        -Parcurgem fiecare nod al arborelui principal (rădăcina) folosind DFS.
        -La fiecare nod, verificăm dacă subarborele care începe de aici este
        exact același cu subRoot.

        Așadar, pentru fiecare nod din arborele mare:
        -Dacă valoarea sa se potrivește cu rădăcina lui subRoot, comparăm ambii
        subarbori în întregime.
        -Dacă sunt identici, subRoot este un subarbore.
        -În caz contrar, continuăm căutarea pe copiii din stânga și din dreapta.

        Funcția auxiliară is_same_tree verifică pur și simplu dacă două arbori
        se potrivesc exact, nod cu nod.

        m - num of nodes root
        n - num of nodes subRoot
        T = O(m * n), S = O(m + n)
        """
        # def is_same_tree(first: Optional[TreeNode], second: Optional[TreeNode]) -> bool:
        #     if not first and not second:
        #         return True

        #     if not first or not second:
        #         return False

        #     if first.val != second.val:
        #         return False

        #     return is_same_tree(first.left, second.left) and is_same_tree(first.right, second.right)

        # if not subRoot:
        #     return True

        # if not root:
        #     return False

        # if is_same_tree(root, subRoot):
        #     return True

        # return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



        """Serialization and Pattern Matching using
        KMP (Knuth-Morris-Pratt)
        
        
        
        T = O(m + n), S = O(m + n)
        """
        # def serialize_tree(node: Optional[TreeNode]) -> str:
        #     if not node:
        #         return "#"
        #     return f"${node.val}" + serialize_tree(node.left) + serialize_tree(node.right)

        # def build_lps(pattern: str) -> list[int]:
        #     """
        #     LPS = Longest Proper Prefix which is also Suffix.

        #     lps[i] = length of the longest proper prefix of pattern[:i + 1]
        #              which is also a suffix of pattern[:i + 1].
        #     """
        #     lps = [0] * len(pattern)

        #     prefix_length = 0
        #     index = 1

        #     while index < len(pattern):
        #         if pattern[index] == pattern[prefix_length]:
        #             prefix_length += 1
        #             lps[index] = prefix_length
        #             index += 1

        #         elif prefix_length > 0:
        #             prefix_length = lps[prefix_length - 1]

        #         else:
        #             lps[index] = 0
        #             index += 1

        #     return lps

        # def contains_pattern(text: str, pattern: str) -> bool:
        #     if not pattern:
        #         return True

        #     lps = build_lps(pattern)

        #     text_index = 0
        #     pattern_index = 0

        #     while text_index < len(text):
        #         if text[text_index] == pattern[pattern_index]:
        #             text_index += 1
        #             pattern_index += 1

        #             if pattern_index == len(pattern):
        #                 return True

        #         elif pattern_index > 0:
        #             pattern_index = lps[pattern_index - 1]

        #         else:
        #             text_index += 1

        #     return False

        # serialized_root = serialize_tree(root)
        # serialized_subtree = serialize_tree(subRoot)

        # return contains_pattern(serialized_root, serialized_subtree)



        """Serialization and Pattern Matching using
        Z function
        
        În loc să comparăm direct arborii, putem mai întâi transforma fiecare
        arbore într-un șir de caractere și apoi să verificăm pur și simplu dacă
        un șir este conținut în celălalt.

        1.Serializăm atât S_root, cât și S_sub în șiruri de caractere folosind
        aceeași metodă de traversare (de exemplu, preordered).
        2.În timpul serializării, trebuie să includem marcatori pentru copiii nul
        (cum ar fi #) și separatori (cum ar fi $), astfel încât formele diferite
        să nu pară accidental identice în șirul de caractere.
        3.Odată ce avem:
        -S_root = serializarea arborelui principal
        -S_sub = serializarea subarborelui

        problema devine:
        „Este S_sub un subșir al lui S_root?”

        Pentru a verifica acest lucru în mod eficient, putem folosi un algoritm
        de potrivire a tiparelor cu timp liniar (cum ar fi funcția Z sau KMP)
        în loc de o căutare naivă a subșirurilor.

        T = O(m + n), S = O(m + n)
        """
        def serialize_tree(node: Optional[TreeNode]) -> str:
            if not node:
                return "#"
            return f"${node.val}" + serialize_tree(node.left) + serialize_tree(node.right)

        def build_z_array(text: str) -> list[int]:
            z_array = [0] * len(text)

            left = 0
            right = 0

            for index in range(1, len(text)):
                if index <= right:
                    z_array[index] = min(
                        right - index + 1,
                        z_array[index - left]
                    )

                while (
                    index + z_array[index] < len(text)
                    and text[z_array[index]]
                    == text[index + z_array[index]]
                ):
                    z_array[index] += 1

                if index + z_array[index] - 1 > right:
                    left = index
                    right = index + z_array[index] - 1

            return z_array

        serialized_root = serialize_tree(root)
        serialized_subtree = serialize_tree(subRoot)

        separator = "|"
        combined_text = serialized_subtree + separator + serialized_root

        z_array = build_z_array(combined_text)
        pattern_length = len(serialized_subtree)

        for index in range(pattern_length + 1, len(combined_text)):
            if z_array[index] == pattern_length:
                return True

        return False
