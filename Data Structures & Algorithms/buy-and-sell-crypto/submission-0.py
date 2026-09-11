class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """Brute Force

        Un approach straight forward verifica fiecare pereche buy-sell. Pentru
        fiecare zi, pretindem ca cumparam stockul si luam toate ziele urmatoare
        ca potential moment de vanzare. Salvam cel mai mare profit.

        T = O(n^2), S = O(1)
        """
        # for i in range(len(prices) - 1):
        #     for j in range(i + 1, len(prices)):
        #         max_profit = max(max_profit, prices[j] - prices[j])
        # return max_profit



        """Sliding Window

        Vrem sa cumparam la un pret mic si sa vindem la un pret mai mare care
        vine dupa el. Folosind 2 pointeri, putem sa tinem aceasta evidenta eficient:
        - left e ziua de cumparat (cautam cel mai mic pret)
        - right e ziua de vandut (cautam cel mai mare pret)

        Daca pretul la right e mai mare ca cel la left, putem face profit asa ca
        updatam profitul maxim. Daca pretul la right e mai mic, left ia valoarea
        lui right pentru ca mereu un pret de cumparare mai ieftin e mai bun.
        Mutand pointerii asa, scanam lista o data si mereu pastram oportunitatea
        de cumparare cea mai buna.

        T = O(n), S = O(1)
        """
        left = 0
        max_profit = 0

        for right in range(1, len(prices)):
            # profitable?
            if prices[left] < prices[right]:
                max_profit = max(max_profit, prices[right] - prices[left])
            # if not, there was found a better buy day
            else:
                left = right

        return max_profit
