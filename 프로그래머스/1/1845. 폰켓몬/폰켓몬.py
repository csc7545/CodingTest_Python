def solution(nums):
    unique_pokemons = len(set(nums))
    
    return min(unique_pokemons, len(nums) // 2)
