import argparse
import csv


###################################### Functions Definitions ######################################

#in-params String
#out-param Dictionary
def freqCount(str):
    freqDict = {}

    for c in str:
        try:
            freqDict[c] += 1
        except:
            freqDict[c] = 1

    if len(freqDict) % 2 == 0:
        freqDict[''] = 0
    
    return freqDict

#in-params Dictionary
#out-param List<Array[int, Array]>
def dicToList(freqDict): 
    unorderedList = [[freq, [char, ""]] for char, freq in freqDict.items()]
        
    sortedList = sorted(unorderedList, key=lambda x: x[0], reverse=True)
    #print(sortedList) #Debug print
    return sortedList


#in-params Array[int, Array] , List<Array[int, Array]>
#out-param List<Array[int, Array]>   
def putQ(item ,list):
    priority = item[0]
    index = 0
    end = 0
    while index < len(list) and end == 0:
        if priority >= list[index][0]:
            list.insert(index, item)
            end = 1 #after put no need for extra loop, break with flag
        index += 1
    if end == 0: #if we didn't find any smaller values, our value is, so put it in the end
        list.insert(index, item)
    
#in-params List<Array[int, Array]> 
#out-param List<Array[int, Array...]> (starting list but with only one element containing all others)
def huffmanEncode(symbNfreqList):
    freqNArrays = symbNfreqList
    while len(freqNArrays) > 1:

        #get 3 elements with lowest frequencies
        lo = freqNArrays.pop()
        mi = freqNArrays.pop()
        hi = freqNArrays.pop()
        
        #put corresponding huffman trit in String of Array
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in mi[1:]:
            pair[1] = '1' + pair[1]
        for pair in hi[1:]:
            pair[1] = '2' + pair[1]

        #print([lo[0] + mi[0] + hi[0]] + lo[1:] + mi[1:] + hi[1:]) #Debug print
        
        #put back an element of combined frequencies and arrays of those poped
        putQ([lo[0] + mi[0] + hi[0]] + lo[1:] + mi[1:] + hi[1:], freqNArrays)

    return freqNArrays

#in-params Dictionary, String
#out-param String 
def huffmanDecode (dictionary, text):
    res = ""

    #given huffman has unique code for each character
    while text: 
        for k in dictionary:            #run through dictionary 
            if text.startswith(k):      #to find character for first trit code of text
                res += dictionary[k]
                text = text[len(k):]
    return res

#in-params String
#out-param String 
def dnaEncode (huffStr):
    dnaStr = ''
    prevbase = 'A' #assume previous base for first was 'A'

    #create the given DNA encode table in a dictionary of tuples
    dnaDict = {}
    dnaDict['A'] = ('C','G','T')
    dnaDict['C'] = ('G','T','A')
    dnaDict['G'] = ('T','A','C')
    dnaDict['T'] = ('A','C','G')
    

    for trit in huffStr:
        currBase = dnaDict[prevbase][int(trit)]
        dnaStr += currBase
        prevbase = currBase

    #print(dnaStr) #Debug print
    return dnaStr    
        
    
#in-params String
#out-param String     
def dnaDecode (dnaStr):
    huffStr = ''
    prevbase = 'A' #assume previous base for first was 'A'

    #create the given DNA decode table in a dictionary of tuples
    dnaDict = {}
    dnaDict['A'] = (' ','0','1','2')
    dnaDict['C'] = ('2',' ','0','1')
    dnaDict['G'] = ('1','2',' ','0')
    dnaDict['T'] = ('0','1','2',' ')

    for base in dnaStr:
        huffStr += str(dnaDict[prevbase][dnaToNumber(base)])
        prevbase = base    
        
    #print(huffStr) #Debug print
    return huffStr    
    
#in-params String
#out-param int
# -- only used by 'dnaDecode' function to get int representation of DNA base
def dnaToNumber(base):
    dnaDict = {}
    dnaDict['A'] = 0
    dnaDict['C'] = 1
    dnaDict['G'] = 2
    dnaDict['T'] = 3
    
    return dnaDict[base]
    

    
######################################## Main Program Flow #########################################


#define arguments
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--decrypt", action="store_true", help="include -d to decrypt")
parser.add_argument("input", help="Input file name")
parser.add_argument("output", help="Output file name for result of input file")
parser.add_argument("huffman", help="Output file name for huffman code")
args = parser.parse_args()

#csv default configuration
csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)

#Decoding
if args.decrypt:
    print("DNA Decoding requested")
    print("... ")
    #get dna text
    input = open(args.input)
    contents = input.read() #file to string
    #print(contents) #Debug print
    input.close()

    #read given csv 
    with open(args.huffman) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=['char','code'])
        #and transform to dictionary
        dict = { line['code']: line['char'] for line in reader } 
        #print(dict) #Debug print
    
    huffCode = dnaDecode (contents)
    #print(huffCode) #Debug print
    decText = huffmanDecode (dict,huffCode)    
    #print(decText) #Debug print

    #write original file
    output = open(args.output, 'w')
    output.write(decText)
    output.close()
    print("DNA Decoding completed")

#Encoding
else:
    print("DNA Encoding requested")
    print("... ")

    #get original text
    input = open(args.input)
    contents = input.read() #file to string
    #print(contents) #Debug print
    input.close()
    

    symbNfreqDict = freqCount(contents) #create dictionary of char, frequecy
    #print(symbNfreqDict) #Debug print
    symbNfreqList = dicToList(symbNfreqDict)
    #print(symbNfreqList) #Debug print

    huff = huffmanEncode(symbNfreqList)

    huffarray = huff[0][1:] #get array excluding frequecy
    #print(huffarray) #Debug print

    #write csv representation of huffman array
    with open(args.huffman, 'w', newline='') as csvfile:
        huffwriter = csv.writer(csvfile)
        for x in huffarray : huffwriter.writerow (x) 
    
    #create dictionary of 2D array
    huffDict = dict(( huffarray[i][0], huffarray[i][1]) for i in range(len(huffarray)))
    #print(huffDict) #Debug print

    #encode original string to huffman
    huffStr = ""
    for ch in contents:
        huffStr += str(huffDict.get(ch))
      
    #print(huffStr) #Debug print 
    
    #encode huffman to DNA and write it
    output = open(args.output, 'w')
    output.write(dnaEncode(huffStr))
    output.close()

    print("DNA Encoding completed")
    