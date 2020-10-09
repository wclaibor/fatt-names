from random import *
global letter_count 
letter_count = 0
class letter():
    # Each letter has a lowercase character, an uppercase character, and
    # identifiers as vowel or consonant.
    def __init__(self, lowerchar, upperchar, is_vowel, is_consonant):
        global letter_count
        self.upperchar = upperchar
        self.lowerchar = lowerchar
        self.is_vowel = is_vowel
        self.is_consonant = is_consonant
        self.num = letter_count
        letter_count += 1

# Define the alphabet.
global alphabet
alphabet = [letter('a','A',True,False),
            letter('b','B',False,True),
            letter('c','C',False,True),
            letter('d','D',False,True),
            letter('e','E',True,False),
            letter('f','F',False,True),
            letter('g','G',False,True),
            letter('h','H',False,True),
            letter('i','I',True,False),
            letter('j','J',False,True),
            letter('k','K',False,True),
            letter('l','L',False,True),
            letter('m','M',False,True),
            letter('n','N',False,True),
            letter('o','O',True,False),
            letter('p','P',False,True),
            letter('q','Q',False,True),
            letter('r','R',False,True),
            letter('s','S',False,True),
            letter('t','T',False,True),
            letter('u','U',True,False),
            letter('v','V',False,True),
            letter('w','W',False,True),
            letter('x','X',False,True),
            letter('y','Y',True,True),
            letter('z','Z',False,True)
            ]

# Define probability matrix.
# prob[i][j] = probability that letter j comes after letter i
global prob
prob = []
for i in range(0,len(alphabet)):
    prob.append([])
    for j in range(0,len(alphabet)):
        prob[i].append(1)

prob[23][23] = 0 # No xx.
prob[12][3] = 0.1 # Rare md.
prob[16][17] = 0 # No qr.
prob[23][16] = 0 # No xq.
prob[23][12] = 0 # No xm.
prob[12][23] = 0 # No mx.
prob[23][7] = 0 # No xh.
prob[21][11] = 0 # No vl.

# Normalize the probability matrix.
for i in range(0,len(alphabet)):
    total = 0
    for j in range(0,len(alphabet)):
        total += prob[i][j]
    for j in range(0,len(alphabet)):
        prob[i][j] /= total

def rand_int(x1,x2):
    # Generate a random integer number between x1 and x2.
    r = int( int(x1) + random()*(int(x2)-int(x1)) )
    return r

def make_name():
    # Determine name length.
    lmin = 3 # Minimum length.
    lmax = 10 # Maximum length.
    name_length = rand_int(lmin,lmax)
    
    # Initialize string.
    my_name = ""
    
    prev_vowel = False # Was the previous letter a vowel?
    prev_consonant = False # Was the previous letter a consonant?
    prev2_vowel = False # Were the previous 2 letters vowels?
    prev2_consonant = False # Were the previous 2 letters consonants?
    prev_num = 0
    # Generate letters for name.
    for i in range(0,name_length):
        if (i == 0):
            a = alphabet[rand_int(0,25)]
            my_name = my_name + a.upperchar
        else:
            a = get_letter(prev_num,prev2_vowel,prev2_consonant)
            my_name = my_name + a.lowerchar
        prev2_vowel = (a.is_vowel and prev_vowel)
        prev2_consonant = (a.is_consonant and prev_consonant)
        prev_vowel = a.is_vowel
        prev_consonant = a.is_consonant
        prev_num = a.num
    return my_name
        
        
def get_letter(prev_num,need_consonant,need_vowel):
    global alphabet
    # Generate a random letter.
    done = False
    while (not done):
#        a = alphabet[rand_int(0,25)]
        a = pick_letter(prev_num)
        if ((need_consonant and a.is_vowel) or (need_vowel and a.is_consonant)):
            done = False
        else:
            done = True
    return a

def pick_letter(i):
    global prob
    r = random()
    total = 0
    for j in range(0,len(alphabet)):
        total += prob[i][j]
        if( r <= total or j == len(alphabet) ):
            return alphabet[j]
    print("problem!")
    return alphabet(25)
        
name1 = make_name()
print(name1)
