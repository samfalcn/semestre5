def encrypt(txt, op):
    codes = []
    estring =[]
    for i in txt:
        code = (ord(i)+op)
        codes.append(code)
    for l in codes:
        fst = chr(l)
        estring.append(fst)
    s= ''.join(estring)
    print(s)
    return codes

def decrypt(codes, op):
    fstring = []
    dcode = []
    for j in codes:
        k = j - op
        dcode.append(k)
    for l in dcode:
        fst = chr(l)
        fstring.append(fst)
    z= ''.join(fstring)       
    return z

text = str(input("Add text: "))
op = int(input("Code: "))
codes= encrypt(text, op)
final_text = decrypt(codes, op)
print(final_text)
