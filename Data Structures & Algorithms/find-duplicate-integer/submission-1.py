class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """Brute force    TLE

        Approachul straightforward este de a lua toate perechiile de
        2 elemente si de a cauta care pereche are elementele identice.
        Astfel, comparand fiecare cu fiecare element, se gaseste cel
        duplicat dar extrem de ineficient si fara a folosi rangeul 1,n

        T = O(n^2), S = O(1)
        """
        # len_nums = len(nums)

        # for i in range(len_nums - 1):
        #     for j in range(i + 1, len_nums):
        #         if nums[i] == nums[j]:
        #             return nums[i]

        # return -1


        
        """Sorting

        Dacă sortăm arrayul, toate numerele duplicate vor apărea unul
        lângă altul. Așadar, după sortare, trebuie doar să parcurgem arrayul
        o singură dată și să verificăm dacă există două elemente consecutive egale.
        Prima pereche egală pe care o găsim este duplicatul.

        T = O(n log m), S = O(n)
        """
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return nums[i]

        # return -1



        """Hash Set

        Putem detecta duplicatele ținând minte numerele pe care le-am
        întâlnit deja. Pe măsură ce parcurgem arrayul, fiecare număr nou
        este verificat:

        Dacă nu se află în mulțime, îl adăugăm.
        Dacă se află deja în mulțime, acel număr trebuie să fie duplicatul.
        O mulțime permite căutarea într-un timp constant, așa că această
        abordare este simplă și eficientă.

        T = O(n), S = O(n)
        """
        # seen = set()

        # for num in nums:
        #     if num in seen:
        #         return num
        #     seen.add(num)

        # return -1



        """Binary Search

        Această metodă utilizează căutarea binară pe intervalul de valori,
        nu pe arrayul în sine. Dacă toate numerele de la 1 la mid au apărut
        cel mult o dată, atunci numărul numerelor <= mid ar trebui să fie <= mid.
        
        Dar dacă numărul este mai mare decât mid, înseamnă că duplicatul trebuie
        să se afle în intervalul [1, mid], deoarece prea multe numere se încadrează
        în acel interval.

        Așadar, repetăm următorii pași:
        -Numărăm câte valori sunt <= mid.
        -Reducem spațiul de căutare în funcție de faptul dacă acest număr este „prea mare”.
        -În cele din urmă, low == high, iar acea valoare este duplicatul.

        T = O(n log n), S = O(1)
        """
        # len_nums = len(nums)
        # low = 1
        # high = len_nums - 1

        # while low <= high:
        #     mid = low + (high - low) // 2
        #     count_appearances = sum(1 for num in nums if num <= mid)

        #     if count_appearances <= mid:
        #         low = mid + 1
        #     else:
        #         high = mid + 1

        # return low



        """Bit Manipulation

        Fiecare număr de la 1 la n-1 ar trebui să apară exact o singură dată,
        dar în array, un număr apare de două ori.

        Așadar, pentru fiecare poziție de bit, comparăm:
        -De câte ori este setat acest bit printre toate numerele din matrice.
        -De câte ori ar trebui să fie setat acest bit printre numerele de la 1 la n-1.
        -Dacă un bit apare de mai multe ori în matrice decât era de așteptat,
        acel bit trebuie să aparțină numărului duplicat.

        Prin combinarea tuturor acestor biți, reconstituim numărul duplicat.

        T = O(32 n) = O(n), S = O(1)
        """
        # duplicate = 0
        # for bit_position in range(32):  # int has 32 bits
        #     # The number of values in nums that have the current bit set to 1.
        #     nums_bit_count = 0

        #     # The number of values in the expected sequence 1..n
        #     # that have the current bit set to 1.
        #     expected_bit_count = 0

        #     # We construct a mask for the bit we are checking.
        #     # Example:
        #     # bit_position = 0 -> 0001
        #     # bit_position = 1 -> 0010
        #     # bit_position = 2 -> 0100
        #     bit_mask = 1 << bit_position

        #     # We count how many times the current bit appears in the number.
        #     for num in nums:
        #         if num & bit_mask:
        #             nums_bit_count += 1

        #     # We count how many times
        #     # the current bit should appear in the normal values 1..n.
        #     for num in range(1, len(nums)):
        #         if num & bit_mask:
        #             expected_bit_count += 1

        #     # If the bit appears more often in the number than in
        #     # the normal sequence, it means that this bit belongs to
        #     # the duplicate number.
        #     if nums_bit_count > expected_bit_count:
        #         duplicate |= bit_mask

        # return duplicate



        """Negative Marking

        For example, if the input array is [1,3,3,2], then for 1, flip the number
        at index 1, making the array [1,-3,3,2]. Next, for -3 flip the number at
        index 3, making the array [1,-3,3,-2]. Finally, when we reach the
        second 3, we'll notice that nums[3] is already negative, indicating that
        3 has been seen before and hence is the duplicate number.

        T = O(n), S = O(1)
        """
        # for num in nums:
        #     curr = abs(num)
        #     if nums[curr] < 0:
        #         duplicate = curr
        #         break

        #     nums[curr] = -nums[curr]

        # # Restore numbers
        # for num in nums:
        #     num = abs(num)
        
        # return duplicate



        """Fast and slow Pointers

        Tratează arrayul ca pe o listă linked, în care fiecare index indică
        spre următorul index, determinat de valoarea sa. Deoarece un număr este
        duplicat, doi indici vor indica spre același element, creând un ciclu — exact
        ca o listă linked cu o buclă.

        Folosind tehnica „fast and slow pointers” a lui Floyd:
        -Pointerul lent se deplasează cu câte un pas pe rând.
        -Pointerul rapid se deplasează cu câte două pași odată.
        Dacă există un ciclu, cei doi pointeri se vor întâlni în cele din urmă.

        Odată ce se întâlnesc, pornim un nou pointer de la început:

        -Deplasați ambii pointeri cu câte un pas odată.
        -Punctul în care se întâlnesc din nou este numărul duplicat
        (punctul de intrare al ciclului).

        T = O(n), S = O(1)
        """
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break

        return slow
