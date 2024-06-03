def count_alphabets(word):
    alphabet_count = [0] * 26

    for char in word:
        index = ord(char) - ord('a')
        alphabet_count[index] += 1
        
    print(" ".join(map(str, alphabet_count)))
    
word = input().strip()
count_alphabets(word)