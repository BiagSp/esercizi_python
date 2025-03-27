"""
Descrizione: Scrivi una funzione che prenda una lista di numeri interi e restituisca la somma di tutti gli elementi.

"""
from typing import List
import unittest

class Solution():
    def somma(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total += num
        return total
    

class TestSolution(unittest.TestCase):
    def test_somma(self):
        sol = Solution()
        self.assertEqual(sol.somma([1,2,3,4,5]), 15)
        self.assertEqual(sol.somma([]), 0)
        self.assertEqual(sol.somma([0,0,0,0]), 0)


def main():
    sol = Solution()
    lista = [1,2,3,4,5]
    risultato = sol.somma(lista)
    print(f"La somma della lista é: {risultato}")

if __name__ == "__main__":
    unittest.main()