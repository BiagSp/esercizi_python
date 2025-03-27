"""
Descrizione: Scrivi una funzione che determini se una data stringa è un palindromo 
(si legge allo stesso modo da sinistra a destra e da destra a sinistra). 
Ignora spazi e punteggiatura, e considera le lettere senza distinzione 
tra maiuscole e minuscole.

"""
import unittest
import string


class Solution:
    def palindrome(self, stri: str) -> bool:
        stri = stri.lower()
        stri = ''.join(c for c in stri if c.isalnum())
        start = 0
        end = len(stri) - 1
        while start < end:
            if stri[start] != stri[end]:
                return False
            start += 1
            end -= 1
        return True
    
class TestSolution(unittest.TestCase):
    def test_palindrome(self):
        sol = Solution()
        self.assertEqual(sol.palindrome("tenet"), True)
        self.assertEqual(sol.palindrome("palindroma"), False)

if __name__ == "__main__":
    unittest.main()