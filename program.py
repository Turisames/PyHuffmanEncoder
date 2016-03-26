
'''
This is a program that reads a text file and creates a
Huffman encoding based on that text.

This means:
The program looks, which characters are most frequent
and associates it with the least amount of bits to
represent it. The rarest character takes the
highest number of bits to represent.
'''

def take_file_name():
    return input("What is the name of the file you want to have read? ")
#
def create_dict( Name="" ):

    if Name == "":
        Name = take_file_name()

    filu = open( Name, encoding='utf-8' )

    chars = {}

    for line in filu:

        for sign in line:

            if sign not in chars:
                chars[ sign ] = 1
            else:
                chars[ sign ] += 1

    filu.close()

    return chars
#
def chars_in_order( charDict = {} ):

    charList = sorted( charDict , key=(lambda avain : charDict[ avain ] ), reverse=True)

    i = 0
    vektor = []

    for element in charList:
        if element == "\n":
            a = "\"{}\" has ".format("linebreak") + str( charDict[ element ] ) + " instances."
            vektor.append( a )
        else:
            a = "\"{}\" has ".format(element) + str(charDict[ element ] ) + " instances."
            vektor.append( a )
        a = "\tValue to represent it is {}.".format( i )
        vektor.append( a )
        i += 1
    a = "This document has {} distinct characters.".format( i + 1 )
    vektor.append( a )

    return vektor
#
def print_vektor( vektor = [] ):
    for line in vektor:
        print( line )
#
def main():

    charsDict = create_dict(  )

    vektor = chars_in_order( charsDict )

    print_vektor( vektor )

#
main()