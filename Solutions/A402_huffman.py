## A402_huffman. See the Copyright (c) 2013 notice of the authors at the end
#  Modified by sxd on 7.4.2014

# We will use the module heapq
from heapq import heapify, heappop, heappush

# Make a Huffman tree taking a list L with the pairs (p,a),
# where a is a source symbol, p probability (see EN_ in A402.py).
def make_huffman_tree(L):
    trees = L[:]
    heapify(trees)
    while len(trees) > 1:
        wR, wL = heappop(trees), heappop(trees)
        w = (wL[0] + wR[0], wL, wR)
        heappush(trees, w)
    return trees[0]

mht = make_huffman_tree

## Build a Huffman encoding table  

# If T is a Huffman tree, next function fills the global table
# named HE, initially empty, with the Huffman encoding
def make_huffman_encoding(T, HE, prefix = ''):
    if len(T) == 2:
        HE[T[1]] = prefix
    else: 
        make_huffman_encoding(T[1], HE, prefix + '0')
        make_huffman_encoding(T[2], HE, prefix + '1')

# Alternative definition, which does not require external HE
def MHE(T, prefix = ''):
    if len(T) == 2: return {T[1]:prefix}
    else: 
        B0 = MHE(T[1], prefix + '0')
        B1 = MHE(T[2], prefix + '1')
        B0.update(B1)
    return B0
    
mhe=make_huffman_encoding

## Extras: Huffman coding and decoding

# Error messages
error_huffman_coding = \
  'huffman_coding: the message contains symbols not known to the HE'
error_huffman_decoding = \
  'huffman_decoding: the decoding could not proceed further'

# Takes a message M and a Huffman enconding table HE
# and outputs the corresponding binary encoding
def huffman_coding (M, HE):
    X = ''
    for c in M:
        if c in HE: X += HE[c]
        else: return error_huffman_coding
    return X

# Takes a binary string X and a Huffman encoding table HE
# and returns the decoded message M, or an error message
# if it cannot be decoded
def huffman_decoding(X, HE):
    l = max(len(HE[a]) for a in HE)
    M = ''  # for the decoded message  
    x = ''  # current binary segment 
    D = {c:a for (a,c) in HE.items()} # Decoding table
    for b in X:
        x += b
        if len(x) > l: break
        if x in D:
            M += D[x]
            x = ''
    if x != '':
        print(error_huffman_decoding)
        print("--the segment", x, 'is not decodable')
        print("Decoded message so far:")
        return M
    else: return M
    


'''
Copyright (c) 2013 the authors listed at the following URL, and/or
the authors of referenced articles or incorporated external code:
http://en.literateprograms.org/Huffman_coding_(Python)?action=history&offset=20081223225116

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Retrieved from: http://en.literateprograms.org/Huffman_coding_(Python)?oldid=15672
'''