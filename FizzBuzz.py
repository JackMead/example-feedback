#FizzBuzz by M.Horsler 4/10/23. Utilise Lists to allow manipulation and concatenation to provide desired result.
#Print to Screen function
def Screen(text):
    print (text)

#Define variables
Loop = 1
result_list=[]

while Loop<256:
 #Ensure Bong overrides all by processing first:
    if Loop % 11 == 0:
        result_list.append('Bong')
    else:
        if Loop % 3 == 0:
            result_list.append('Fizz')

        if Loop % 13 == 0:
            result_list.append('Fezz')

# Buzz processed after Fizz to create desired order.
        if Loop %3==0 and Loop%5==0:
            result_list.append('Buzz')

        elif Loop % 5 == 0:
            result_list.append('Buzz')
        
        if Loop % 7 == 0:
            result_list.append('Bang')

# Reverse list for nultiples of 17:
        if Loop % 17 == 0:
            result_list.reverse()

# If list is empty, add index number as a string:
        if not result_list:
            result_list.append(str(Loop))
        
# Insert Fezz to index 0 of string when multiples of 11 & 13 apply:
    if Loop %11==0 and Loop%13==0:
        result_list.insert(0,'Fezz')

# Remove bracket indentations for display:
    result_list = ''.join(result_list)
# Call Screen function to display resulting list:
    Screen (result_list)
# Reset list, and loop until complete.
    result_list=[]
    Loop = Loop + 1