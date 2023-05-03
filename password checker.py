import string
print('Welcome to Passcheker\n')

def checker():
    password = input('please enter your password...')
    
    lwr_count = upr_count = dgt_count = spl_count = 0
    for item in password:
        if item in string.ascii_lowercase:
            lwr_count +=1
        elif item in string.ascii_uppercase:
            upr_count+=1
        elif item in string.digits:
            dgt_count+=1
        else:
            spl_count+=1
            
    item_count = [lwr_count , upr_count , dgt_count , spl_count]
    score = 0
    sum = 0
    for i in item_count:
        if i>0 :
            score += 1
        sum += i
            
            
    strengh = ""       
    if sum < 6:
        strengh = 'weak'
    else:
        if score <3:
            strengh = 'weak'
        elif score <4 :
            strengh = 'medium'
        else:
            strengh = 'strong'
            
            
    print(f'\nyour password is {strengh}\n\n')
    
    
while True:
    checker()
    retry = input ('Do you want to retry? y')
    if retry == 'y':
        continue
    else:
        print('\n\nThank You For Choosing Us')
        break
    


