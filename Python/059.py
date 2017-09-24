encrypted = map(int,open('p059_cipher.txt').read().split(','))



def is_eng(ch):
    if 65 <= ch <= 90:
        return True
    elif 97 <= ch <= 122:
        return True
    else:
        return False


def decrypt():
    max_key = []
    max_good = 0
    for a in range(97, 123):
        for b in range(97, 123):
            for c in range(97, 123):
                good = 0
                key = [a, b, c]
                for x in xrange(len(encrypted)):
                    char = encrypted[x] ^ key[x%3]
                    if is_eng(char):
                        good += 1 
                if good > max_good:
                    max_good = good
                    max_key = key

    return max_key

                
                
suma = 0
text = ""
key = decrypt()
for x in xrange(len(encrypted)):
    char = encrypted[x] ^ key[x%3]
    suma += char
    text += chr(char)

print text
print suma