i=1
while i <= 10:
    line = '$' * (2 * i - 1)
    print(line.center(10))

    user_input = input("Press Space to continue, any other key to stop: ")

    if user_input == ' ':
        i = i + 1
    else:
        break 

#output
 #  $     
#Press Space to continue, any other key to stop:  
#  $$$    
#Press Space to continue, any other key to stop:  
# $$$$$   
#Press Space to continue, any other key to stop: b