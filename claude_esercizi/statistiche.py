"""
Crea una funzione che accetta una lista di numeri
e restituisce un dizionario contenente:
media, mediana, valore minimo, valore massimo e deviazione standard
"""

import statistics
import math

def stat(nums):
    statistiche = {
        "media": sum(nums) / len(nums),
        "mediana": statistics.median(nums),
        "minVal": min(nums),
        "maxVal": max(nums),
        "ds": statistics.stdev(nums)
    }
    return statistiche

print(stat([1, 2, 3, 4, 5, 6]))


#implementazione manuale senza import statistics

def static(nums: list):
    # Calcolo corretto della media
    media = sum(nums) / len(nums)
    
    # Calcolo corretto della mediana
    mediana = statistics.median(nums)
    
    # Calcolo corretto del massimo e minimo
    maxVal = nums[0]
    minVal = nums[0]
    for n in nums[1:]:
        if n > maxVal:
            maxVal = n
        if n < minVal:
            minVal = n
    
    # Calcolo corretto della deviazione standard
    somma_scarti_quadratici = sum((n - media)**2 for n in nums)
    deviazione_std = math.sqrt(somma_scarti_quadratici / (len(nums) - 1))  # Per campione
    
    statistiche = {
        "media": media,
        "mediana": mediana,
        "massimo": maxVal,
        "minimo": minVal,
        "deviazione-std": deviazione_std
    }
    return statistiche

print(static([1, 2, 3, 4, 5, 6]))
