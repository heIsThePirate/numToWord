# PROGRAM TO CONVERT A GIVEN NUMBER INTO WORDS IN INDIAN SYSTEM.

# Some defined key-value pairs.
mydict = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

# The divisor for place value is chosen from this dict.
startAt = {1:1, 2:10, 3:100, 4:1000, 5:1000, 6:100000, 7:100000, 8:10000000, 9:10000000}

# Defines the corresponding place value strings.
placeValues = {0:'', 1:'', 10:'', 100:'hundred', 1000:'thousand', 100000:'lakh', 10000000:'crore'}

# Multiplication factor for 2-digit nums.
multFactor = {1:1, 10:10}

def indianSystem(number):
    length = len(str(number));
    answer = ''
    if number == 0:
        answer += mydict[number]
    else:
        while number:
            # Conditional statement separating 2-digit nums from more than 2-digit nums.
            if length > 2:
                value = number // startAt[length]
                valueLen = len(str(value))
                tempString = ''
                while value:
                    # For values < 21 the strings are already pre-defined in mydict.
                    if value > 20:
                        newValue = value // startAt[valueLen]
                        newValue = newValue * multFactor[startAt[valueLen]]
                        tempString = tempString + mydict[newValue] + ' '
                        value = value % startAt[valueLen]
                        valueLen = len(str(value))
                    else:
                        tempString += mydict[value] + ' '
                        value = 0
                # Concatenating the tempString to the answer string and adding the placeValue string.
                answer = answer + tempString + placeValues[startAt[length]] + ' '
                number = number % startAt[length]
                length = len(str(number))
            
            # else clause for <= 2-digit nums.
            else:
                tempString = ''
                while number:
                    valueLen = len(str(number))
                    # For values < 21 the strings are already pre-defined in mydict.
                    if number > 20:
                        value = number // startAt[valueLen]
                        value = value * multFactor[startAt[valueLen]]
                        tempString = tempString + mydict[value] + ' '
                        number = number % startAt[valueLen]
                    else:
                        tempString += mydict[number]
                        number = 0
                answer = answer + tempString
    # return the answer string having the given number converted to indian system.    
    return answer