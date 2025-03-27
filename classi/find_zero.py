"""
Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, 
return the number with the largest value.

Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.

"""

"""class Solution(object):
    def findClosestNumber(self, nume):
        closest_num = nume[0]
        closest = nume[0]
        for num in range(1,len(nume)):
            if abs(nume[num]) < abs(closest[num]):
                closest = nume[num]
            elif abs(nume[num]) == abs(closest[num]) and nume[num] > closest[num]:
                closest = nume[num]
        return closest
"""


def closest_num():
    # Legge la stringa di input, la divide in parti e converte ogni parte in intero
    nums = list(map(int, input("Inserisci una serie di numeri separati da spazio: ").split()))
    
    # Se la lista è vuota, restituisce None (oppure puoi gestire l'errore come preferisci)
    if not nums:
        return None
    
    # Inizializza il numero più vicino a zero con il primo elemento della lista
    closest = nums[0]
    
    # Itera attraverso tutti i numeri della lista
    for num in nums:
        # Confronta il valore assoluto: se quello di num è minore di quello di closest,
        # oppure se sono uguali ma num è maggiore (per dare la precedenza a numeri positivi),
        # allora aggiorna il valore di closest.
        if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
            closest = num
            
    return closest

print(closest_num())



