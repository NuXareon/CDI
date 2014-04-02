# Copyright (c) 2013 the authors listed at the following URL, and/or
# the authors of referenced articles or incorporated external code:
# http://en.literateprograms.org/Huffman_coding_(Python)?action=history&offset=20081223225116
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Retrieved from: http://en.literateprograms.org/Huffman_coding_(Python)?oldid=15672

import heapq

# --------------------------------
#      MAKE A HUFFMAN TREE
# --------------------------------
def makeHuffTree(symbolTupleList):
    """makeHuffTree
        Given a symbol list with the frequencies of each one, builds a huffman
        tree. The huffman code lies implicit in it, but it's not written in the
        nodes.
        
        Parameters:
            symbolTupleList: A list with all the symbols and their frequencies 
        Return: 
            The huffman tree of the language
    """
    # Builds a list trees. Here we will store all the partial trees that we will 
    # keep merging to build the final one. We'll arrange it as a heap later on. 
    # At the beggining, the list of trees will be the list of one-node trees made 
    # with all code characters and their frequencies.
    trees = symbolTupleList[:]
    
    # Transform the list of tres in a heap ordered by frequencies
    heapq.heapify(trees)
   
    # While we don't have a single tree with all nodes in it, we keep running the algorithm.
    while len(trees) > 1:
            # Invariant: tree[0] -> most frequent of all trees generated so far,
            #            tree[1] -> second most frequent of all trees generated so far
            
            # We set as a right and left child the trees on the top of the heapTree 
            #(the most frequent ones) and delete them from the heap.
            childR, childL = heapq.heappop(trees), heapq.heappop(trees)
            # Build the parent node seting its value as the sum of its child balues. 
            # Left and right child will be the ones we just created
            parent = (childL[0] + childR[0], childL, childR)
            # We add our new tree to the heap
            heapq.heappush(trees, parent)
        
            # Iterative step: We merged two trees into one. 
            # Each iteration we have 1 tree less in the list.
            # If the algorithm finished, we only have one tree stored 
            # in the 0 position of the trees list. 
            # This is the huffman Tree of the code
    return trees[0]


# ---------------------------------------------
#      RPINT A HUFFMAN TREE IN A READABLE WAY
# ---------------------------------------------
   
def printHuffTree(huffTree, prefix = ''):
    """printHuffTree
        Given a huffman tree, prints it in a readable way with the implicit
        associated code. 
        
        Parameters:
            huffTree: A huffman tree with the frequencies as the main value
            prefix: The acumulated prefix of all the words in the tree (normally
                    empty for the first call and only used for recursive calls)
        Return: 
            Print the huffman tree.
    """
    # HuffTree -> The tree we want to print
    # Prefix -> the code we built so far to reach this part of the tree
    
    # Base case: If this is the only node, just print the value 
    # followed by the acumulated code we generated.
    if len(huffTree) == 2:
        print(huffTree[1], prefix)
    
    # Recursive step: Print its left and right children. 
    # As the tree is stored in a recurrent way, to find the beggining 
    # of the next child, we only need to move one position in the list. 
    # We should have in mind that the code associated to the charaters 
    # is not stored in the huffman tree, so we need to generate it while 
    # exploring the tree. That's why we keep adding a 1 or an 0 to an 
    # accumulated value called 'prefix'. The left child will always get a 0 
    # at the end of the acumulated prefix. The right child will always have a 1. 
    #That will keep building the code for each leaf.
    else:
        printHuffTree(huffTree[1], prefix + '0')
        printHuffTree(huffTree[2], prefix + '1')

 
# ---------------------------------------------
#    BUILT A DICTIONARY GIVEN A HUFFMAN TREE 
# ---------------------------------------------   

def huffCode (huffTree, dictionary, prefix = ''):
    """huffCode
        This function builds the code associated to the given huffman tree
        
        Parameters:
            huffTree: The huffman tree
            dictionary: Where the code is stored (key ; code)
            prefix: The acumulated prefix of all the words in the tree (normally
                    empty for the first call and only used for recursive calls)
             
        Return: 
            dictionary gets filled by the code of each word
    """
    if len(huffTree) == 2:
        dictionary[huffTree[1]] = prefix
    else: 
        huffCode(huffTree[1], dictionary, prefix + '0')
        huffCode(huffTree[2], dictionary, prefix + '1')


# ---------------------------------------------
#     ENCODES A MESSAGE GIVEN A DICTIONARY
# --------------------------------------------- 
  

def huffCoding (message, dictionary):
    """huffCode
        This function builds the coded string associated to the given
        character string
        
        Parameters:
            message: The string that needs to be coded
            dictionary: The coding dictionary. 
                        (original character -> coded character)
             
        Return: 
            result: The string with the coded message. An error message if the
                  input can't be coded using the dictionary.
    """
    # Message: The string we want to encode
    # Dictionary: Contains the code associated to each character we can have in the message
    codedMessage = ''
    for c in message:
        # Invariant: result = encoded message from message[0] to message[i]
        if c in dictionary:
            codedMessage += dictionary[c]
        else :
            return 'Error: The message contains symbols allowed by the dictionary'
    return codedMessage

# ---------------------------------------------
#     DECODES A MESSAGE GIVEN A DICTIONARY
# ---------------------------------------------   

def huffDecoding (message, dictionary):
    """huffCode
        This function decodes a given coded message into the original one
        
        Parameters:
            message: The string that needs to be decoded
            dictionary: The coding dictionary. 
                        (original character -> coded character)
            ¡
             
        Return: 
            result: The string with the decoded message
    """
    # Message: The string we want to decode
    # Dictionary: Contains the code associated to each character we can have in the message
    result = ''
    currentToken = ''
    
    # Built a reverse version of the encoding dictionary
    inverseDictionary = {v:k for k, v in dictionary.items()}
    
    # For each character of the code, check if there's a character to decode into
    for i in message:
        currentToken += i
        if currentToken in inverseDictionary:
            # If our token is represented by a character, 
            # add it to the result and restart the acumulated token
            result += inverseDictionary[currentToken]
            currentToken = ''
    
    # If there's still a token to check but no more message, 
    # means that the message could not be decoded properly
    if currentToken != '':
        result ='It was not possible to decode your message. Check the code is valid'
    
    return result
    
# ------------------------------------------------------
#   CALCULATES THE AVERAGE LENGTH OF A HUFFMAN CODE
# ------------------------------------------------------   

def huffLength (symbolList):
    """huffCode
        Calculates the average word length of a given huffman code ponderated
        using the appereance frequency
        
        Parameters:
            symbolList: The list of symbols and their probability
            
             
        Return: 
            length: the average length
    """
    
    # Get the code for each character
    dictionary = dict()
    huffCode (makeHuffTree(symbolList), dictionary)
    
    length = 0
    # For each symbol, add the ponderated length to the average
    for c in symbolList:
        length += len(dictionary[c[1]]) * c[0]
    return length

# --------------------------------------------------------
#   CALCULATES THE VARIANCE OF LENGTH OF A HUFFMAN CODE
# --------------------------------------------------------   

def huffVariance (symbolList):
    """huffVariance
        Calculates the variance word length of a given huffman code ponderated
        using the appereance frequency
        
        Parameters:
            symbolList: The list of symbols and their probability
            
             
        Return: 
            length: the average length
    """
        
    # Get the average length
    averageLength = huffLength(symbolList)
    variance = 0
    
    # Get the code for each character
    dictionary = dict()
    huffCode (makeHuffTree(symbolList), dictionary)
    
    for c in symbolList:
         variance +=  c[0] * (len(dictionary[c[1]])-averageLength)**2 
    return variance    
      
exampleData = [
  (0.124167  , 'e'),
  (0.0969225 , 't'),
  (0.0820011 , 'a'),
  (0.0768052 , 'i'),
  (0.0764055 , 'n'),
  (0.0714095 , 'o'),
  (0.0706768 , 's'),
  (0.0668132 , 'r'),
  (0.0448308 , 'l'),
  (0.0363709 , 'd'),
  (0.0350386 , 'h'),
  (0.0344391 , 'c'),
  (0.028777  , 'u'),
  (0.0281775 , 'm'),
  (0.0235145 , 'f'),
  (0.0203171 , 'p'),
  (0.0189182 , 'y'),
  (0.0181188 , 'g'),
  (0.0135225 , 'w'),
  (0.0124567 , 'v'),
  (0.0106581 , 'b'),
  (0.00393019, 'k'),
  (0.00219824, 'x'),
  (0.0019984 , 'j'),
  (0.0009325 , 'q'),
  (0.000599  , 'z')
]

exampleData2= [ 
    (0.0651738, 'a'),
    (0.0124248, 'b'),
    (0.0217339, 'c'),
    (0.0349835, 'd'),
    (0.1041442, 'e'),
    (0.0197881, 'f'),
    (0.0158610, 'g'),
    (0.0492888, 'h'),
    (0.0558094, 'i'),
    (0.0009033, 'j'),
    (0.0050529, 'k'),
    (0.0331490, 'l'),
    (0.0202124, 'm'),
    (0.0564513, 'n'),
    (0.0596302, 'o'),
    (0.0137645, 'p'),
    (0.0008606, 'q'),
    (0.0497563, 'r'),
    (0.0515760, 's'),
    (0.0729357, 't'),
    (0.0225134, 'u'),
    (0.0082903, 'v'),
    (0.0171272, 'w'),
    (0.0013692, 'x'),
    (0.0145984, 'y'),
    (0.0007836, 'z'),
    (0.1918182, ' ')
]

# if __name__ == '__main__':
#     
#     
#     print ('----------------------')
#     print ('    DIC13 L 10 04     ') 
#     print ('----------------------', end='\n \n')
#     
#     # We built the huffman tree of the example data
#     print ('We are going to build a Huffman tree with the monogram English frequencies', end='\n \n')
#     huffTree = makeHuffTree(exampleData)
#     
#     # We print the raw form of the huffTree
#     print ('This is the internal representation of the Huffman tree. As we can see, it is stored in a recurrent way where each node is represented as the frequency of the node and its right and left children', end='\n \n')
#     print (huffTree)
#     print ()
#     
#     # We print the huffman tree
#     print ('This is the readable version of the Huffman tree with the codes associated to each character', end='\n \n')
#     printHuffTree(huffTree)
#     print ()
#     
#     # We generate the dictionary
#     print ('Now, we generate a dictionary that store the coding language we generated with the huffman algorithm', end='\n \n')
#     codingDictionary = dict()
#     huffCode(huffTree, codingDictionary)
#     
#     # We print the dictionary to make sure it's properly built
#     print (codingDictionary, end='\n \n')
#     
#     # We try to encode a message
#     print ('Now, we can start encoding messages using this dictionary. Insert a message that you cant to encode (no capitals, no space, no simbols):', end='\n \n')
#     message = input()
#     print ()
#     print ('This is the encoding of your message:')
#     print (huffCoding(message, codingDictionary), end= '\n \n')
#     
#     # We try to decode a message
#     print ('Now, we can start decoding messages using this dictionary. Insert a code that you cant to decode into a message:', end='\n \n')
#     message = input()
#     print ()
#     print ('This is the decoded of version of your input:')
#     print (huffDecoding(message, codingDictionary), end= '\n \n')
#     
#     # Repeat the process with white space
#     print ('Now, we repeat the process with the white space character', end='\n \n')
# 
#     huffTree = makeHuffTree(exampleData2)
#     codingDictionary = dict()
#     huffCode(huffTree, codingDictionary)
#     
#     # We try to encode a message
#     print ('Insert a message that you cant to encode (no capitals, no simbols):', end='\n \n')
#     message = input()
#     print ()
#     print ('This is the encoding of your message:')
#     print (huffCoding(message, codingDictionary), end= '\n \n')
#     
#     # We try to decode a message
#     print ('Insert a code that you cant to decode into a message:', end='\n \n')
#     message = input()
#     print ()
#     print ('This is the decoded of version of your input:')
#     print (huffDecoding(message, codingDictionary), end= '\n \n')
#     
#     # We get the average length of the huffman code
#     print ('This is the average length of the huffman code of the example:')
#     print (huffLength(exampleData), end= '\n \n')
#     
#     # We get the variance of the huffman code
#     print ('This is the variance of the huffman code of the example:')
#     print (huffVariance(exampleData), end= '\n \n')