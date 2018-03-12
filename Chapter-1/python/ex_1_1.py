def isUnique(word):
    encoding = [False]*128
    if len(word) == 0:
        return True
    
    for letter in word:
        if encoding[ord(letter)]:
            return False
        else:
            encoding[ord(letter)] = True
            
    return True
            
            
def test_isUnique():
    assert isUnique("") == True           #Test the empty string 
    assert isUnique("Hello") == False     #Test a non-unique characters string
    assert isUnique("Helo") == True       #Test a string with all unique characters
    assert isUnique("hello") == False     #Test a non-unique characters string with all 
    assert isUnique("7elo") == True       #Test a number as a string in a unique string
    assert isUnique("7e lo") == True      #Test spaces
    assert isUnique("7e  lo") == False    #Test double space
     
