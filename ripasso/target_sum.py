"""
Descrizione: Data una lista di numeri interi e un numero target, scrivi una funzione che trovi due numeri nella lista la cui somma
 sia uguale al target. La funzione dovrebbe restituire gli indici di questi due numeri. 
Puoi assumere che ci sia esattamente una soluzione, e non puoi usare lo stesso elemento due volte.

"""

import unittest
from typing import List

class Solution:
    def target_sum(self, nums: List[int], target:int) -> bool:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        # Secondo l'assunzione, il problema garantisce che ci sia sempre una soluzione,
        # quindi questo return non dovrebbe mai essere raggiunto.
        return []
    
class TestSolution(unittest.TestCase):
    def test_target_sum(self):
        sol = Solution()
        self.assertEqual(sol.target_sum([2,2,1,3],4),[0,1])
        self.assertEqual(sol.target_sum([3,2,4],6),[1,2])

if __name__ == "__main__":
    unittest.main()