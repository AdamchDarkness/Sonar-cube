def average(nums):
    # Mauvaise pratique : pas de vérification d’entrée
    total = 0
    for n in nums:
        total += n
    return total / len(nums)

def duplicate_function(nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)
