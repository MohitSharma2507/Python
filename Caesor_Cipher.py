words = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
is_play = True


def encryption(str1,list):
    for i in list:
        if i is ' ':
            str1 += " "
        else:
            index = words.index(i) 
            new_index = index+shift 
                
            if new_index < 0:
                new_index = ((new_index+26) % 26)
            else:
                new_index =(new_index % 26)
                if words[new_index] is 'c':
                    str1+=" "
                else:    
                    str1 += words[new_index]

    print(f"Here is the encrypted result :{str1}")   

def decryption(str1,list):
       for i in list:
                if i is ' ':
                    str1 += " "
                else:
                    index = words.index(i) 
                    new_index = index - shift 
                
                    if new_index < 0:
                        new_index = ((new_index+26) % 26)
                    else:
                        new_index =(new_index % 26)
                    if words[new_index] is 'c':
                            str1+=" "
                    else:    
                        str1 += words[new_index]  

       print(f"Here is the descrypted result : {str1}")  
      
while is_play:
    str1 = " "
    list=[]
    user_type=input("Type 'encrypt' for encryption, type 'decrypt' for decryption: ")
    user_mess=input("Type your message: ")
    shift=int(input("Type the shift number: "))

    for i in user_mess:
     list.append(i)  

    if user_type == 'encrypt':
           encryption(str1,list)

    elif user_type == 'decrypt':
           decryption(str1,list)

    play=input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
    if play == 'no':
        is_play=False
 