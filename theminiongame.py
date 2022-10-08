def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    kevins_score = 0
    stuarts_score = 0
    
    word_len = len(string)

   
    for letter in range(word_len):
        if string[letter] in vowels:
            kevins_score += word_len - letter
        else:
            stuarts_score += word_len - letter
    
    if (kevins_score > stuarts_score):
        print("Kevin", kevins_score)
        
    elif(stuarts_score > kevins_score): 
        print("Stuart", stuarts_score)
    
    else:
        print("Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)