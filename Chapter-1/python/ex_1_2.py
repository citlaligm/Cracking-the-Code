
def isPermutations(word1, word2):
    if len(word1)==0 or len(word2)==0:
        return False
    
    if len(word1) != len(word2):
        return False
    
    encoding = [False]*128
    
    for letter in word1:
        encoding[ord(letter)] = not encoding[ord(letter)]
      
    #print(encoding)
    for letter in word2:
        encoding[ord(letter)] = not encoding[ord(letter)]
      
    #print(encoding)
    return all(encoding)
    
    
    
def test_isPertmutation():
    #Test different lenght of strings
    
    word1, word2 = "abcd",""
    assert isPermutations(word1, word2) == False
    
    #Test upper letter is different to lower case letter
    word1, word2 = "Abc","abc"
    assert isPermutations(word1, word2) == False
    
    #Test empty strings
    word1, word2 = "",""
    assert isPermutations(word1, word2) == False