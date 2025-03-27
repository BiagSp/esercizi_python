"""
Descrizione: Data una lista di numeri interi, trova la lunghezza della sottosequenza crescente più lunga.

"""

import unittest
from typing import List

class Solutio:
    def sottosequeza(self,nums:List[int]) -> int:
        underS = []
        for i in nums:
            for j in nums:
                if j < i:
                    underS.append(j)
            j += 1
        i += 1


nums = [1,5,4,2,5,67,8,3]


def lis(arr):
    if not arr:
        return 0
    n = len(arr)
    dp = [1] * n    
    for i in range(1,n):
        for j in range(0,i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

