import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    
    # Pad the string to maximum length.
    origlen = len(s)
    s = s + (1000 - origlen) * 'a'

    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))

    if len(s) > 1000:
        raise ValueError
    
    for c in s:
        if ord(c) > 127:
            raise ValueError
        if c.isalpha():
            if c.islower():
                c=c.upper()
            elif c.isupper():
                c=c.lower()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
          crypted+=digitmapping[c]
        else:
            raise ValueError
             
    # Remove padding
    crypted = crypted[:origlen]
    return crypted

def decode(s):
    return encode(s)

