def shaircrypt(name):
    transtable = (
        (u"a", u"|-) "),
        (u"b", u"|6 "),
        (u"c", u"|_- "),
        (u"d", u"0| "),
        (u"e", u"0_ "),
        (u"f", u"|-- "),
        (u"g", u"0__ "),
        (u"h", u"|)- "),
        (u"i", u"|` "),
        (u"k", u"|( "),
        (u"l", u"|| "),
        (u"m", u"|`|`| "),
        (u"n", u"|-| "),
        (u"o", u"|_-| "),
        (u"p", u"|. "),
        (u"q", u"0.| "),
        (u"r", u"\)( "),
        (u"s", u"(_) "),
        (u"u", u"|_| "),
        (u"v", u"\) "),
        (u"w", u"((( "),
        (u"x", u"(|) "),
        (u"y", u"_\\ "),
        (u"z", u"--- "),
        (u"t", u"|_ "),
        (u"j", u"-|- "),
        (u"A", u"|-)b "),
        (u"B", u"|6b "),
        (u"C", u"|_-b "),
        (u"D", u"0|b "),
        (u"E", u"0_b "),
        (u"F", u"|--b "),
        (u"G", u"0__b "),
        (u"H", u"|)-b "),
        (u"I", u"|`b "),
        (u"K", u"|(b "),
        (u"L", u"||b "),
        (u"M", u"|`|`|b "),
        (u"N", u"|-|b "),
        (u"O", u"|_-|b "),
        (u"P", u"|.b "),
        (u"Q", u"0.|b "),
        (u"R", u"\)(b "),
        (u"S", u"(_)b "),
        (u"U", u"|_|b "),
        (u"V", u"\)b "),
        (u"W", u"(((b "),
        (u"X", u"(|)b "),
        (u"Y", u"_\\b "),
        (u"Z", u"---b "),
        (u"T", u"|_b "),
        (u"J", u"-|-b "),
    )
    for symb_in, symb_out in transtable:
        name = name.replace(symb_in, symb_out)
    return(print(name))

def shairdecrypt(name):
    transtable = (
        (u"|-) ", u"a"),
        (u"|6 ", u"b"),
        (u"|_- ", u"c"),
        (u"0| ", u"d"),
        (u"0_ ", u"e"),
        (u"|-- ", u"f"),
        (u"0__ ", u"g"),
        (u"|)- ", u"h"),
        (u"|` ", u"i"),
        (u"|( ", u"k"),
        (u"|| ", u"l"),
        (u"|`|`| ", u"m"),
        (u"|-| ", u"n"),
        (u"|_-| ", u"o"),
        (u"|. ", u"p"),
        (u"0.| ", u"q"),
        (u"\)( ", u"r"),
        (u"(_) ", u"s"),
        (u"|_| ", u"u"),
        (u"\) ", u"v"),
        (u"((( ", u"w"),
        (u"(|) ", u"x"),
        (u"_\\ ", u"y"),
        (u"--- ", u"z"),
        (u"|_ ", u"t"),
        (u"-|- ", u"j"),
        (u"|-)b ", u"A"),
        (u"|6b ", u"B"),
        (u"|_-b ", u"C"),
        (u"0|b ", u"D"),
        (u"0_b ", u"E"),
        (u"|--b ", u"F"),
        (u"0__b ", u"G"),
        (u"|)-b ", u"H"),
        (u"|`b ", u"I"),
        (u"|(b ", u"K"),
        (u"||b ", u"L"),
        (u"|`|`|b ", u"M"),
        (u"|-|b ", u"N"),
        (u"|_-|b ", u"O"),
        (u"|.b ", u"P"),
        (u"0.|b ", u"Q"),
        (u"\)(b ", u"R"),
        (u"(_)b ", u"S"),
        (u"|_|b ", u"U"),
        (u"\)b ", u"V"),
        (u"(((b ", u"W"),
        (u"(|)b ", u"X"),
        (u"_\\b ", u"Y"),
        (u"---b ", u"Z"),
        (u"|_b ", u"T"),
        (u"-|-b ", u"J"),
        
    )
    for symb_in, symb_out in transtable:
        name = name.replace(symb_in, symb_out)
    return(print(name))
print (" _____ _   _   ___  ___________ ")
print ("/  ___| | | | / _ \|_   _| ___ \ ")
print ("\ `--.| |_| |/ /_\ \ | | | |_/ /")
print (" `--. \  _  ||  _  | | | |    / ")
print ("/\__/ / | | || | | |_| |_| |\ \ ")
print ("\____/\_| |_/\_| |_/\___/\_| \_|")
print ("English Ver. 1.2")
print ("----------------------------------------------")
print ("Oh! I almost forgot. Copy all gaps, or your text wont decrypt. (you cant try add space at the end of the text if it wont decrypt)")
print ("----------------------------------------------")
def choose():
    while True:
        print('(E)ncrypt or (d)ecrypt? Or maybe (q)uit?')
        mode = input().lower()
        if mode in 'd'.split():
            return decrypting()
        if mode in 'e'.split():
            return crypting()
        if mode in 'q'.split():
            return exit()
        else:
            print('no.')
def decrypting():
    name = input("Put your text here to decrypt: ")
    shairdecrypt(name)
    choose()
def crypting():
    name = input("Put your text here to encrypt: ")
    shaircrypt(name)
    choose()
mode = choose()