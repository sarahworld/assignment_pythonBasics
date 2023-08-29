def words(word_list, must_start_with):
    """
    This function prints single word in a new line.
    """

    if(isinstance(word_list,str)):
        for word in word_list.split():
            for val in must_start_with:
                if(word[0] == val.lower() or word[0] == val.upper()):
                    print(word.upper()) 
# 
    elif(isinstance(word_list,list)):
        for word in word_list:
            for val in must_start_with:
                if(word[0] == val.lower() or word[0] == val.upper()):
                    print(word.upper()) 
# 


#words("Hi how are you?", ["h", "y"]);
words(["hello", "hey", "goodbye", "yo", "yes"], ["h", "y"]);
