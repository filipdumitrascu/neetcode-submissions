class Solution:
    """ First Idea

    Stocam toate lungimile separate prin virgula si pe urma un alt simbol
    si stringurile in sine

    encode: len1,len2,len3#str1str2str3

    m - sum(len(strs)), n - num(strs)
    T = O(m + n), S = O(m + n)
    """



    """Second Idea (Optimal)

    Putem sa atasam lungimea fiecarui string de acesta.

    encode: len1#str1len2#str2len3#str3

    Diezul e un delimitator bun intre lungime si string iar prin lungime stim
    exact cate caractere sa citim in string (indiferent daca are stringul diez
    sau cifre in el)

    La decode citim pana la diez stiind ca accestea sunt cifre din lungime.
    Convertim in int si citim atatea caractere pentru a obtine stringul.
    E mai eficient ca approachul anterior pentru ca evita construirea unor
    memorii auxiliare pentru lungimi si continut.

    m - sum(len(strs)), n - num(strs)
    T = O(m + n), S = O(m + n)
    """
    def encode(self, strs: list[str]) -> str:
        parts = []
        for s in strs:
            parts.append(str(len(s)))
            parts.append("#")
            parts.append(s)

        return ''.join(parts)

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i: j])
            result.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
