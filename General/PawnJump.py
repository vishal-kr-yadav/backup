#pawnJump is function that will take Array as a input
def pawnJump(Array):
    #calculating the length of the Array
    array_length = len(Array)

    #initializing array_Index and toBeReturned
    array_Index = 0
    to_Be_Returned = 0

    #looping till the array_index is less then the size of the Array and arrayIndex must be greater than 0
    while (array_Index < array_length and array_Index >= 0):
        #adding the index position of the array and the element of array at array_Index
        array_Index += Array[array_Index]

        #after each jump of pawn incrementing the to_Be_Returned variable
        to_Be_Returned += 1;

        #checking whether a pawn will ever jump from the aray or not
        if (to_Be_Returned > array_length):
            return -1
            break

    #returning on which jump the pawn will jump out of the array
    return to_Be_Returned;


#initialize the array
Array=[]
length_of_array=raw_input("Enter how many number do you want in an array:")
for i in range (int(length_of_array)):
    Array.append(int(raw_input()))
A=pawnJump(Array)
print'Returned from the pawn_Jump_Function:',A





