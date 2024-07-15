words = ["necessary", "kidnapped", "religions", "renovated", "fanatical", "ignorance", "flavoring"]

for i in range(len(words)-1):
    word1 = words[i]
    word2 = words[i+1]
    
    common_chars = set(word1) & set(word2)
    
    if common_chars:
        print(f"Words '{word1}' and '{word2}' have common characters: {', '.join(common_chars)}")