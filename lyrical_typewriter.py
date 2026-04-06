import time
import sys
import os
from colorama import init, Fore, Style

init(autoreset=True)

TITLE  = Fore.CYAN + Style.BRIGHT
VERSE  = Fore.WHITE
CHORUS = Fore.YELLOW

lyrics = [
    ('Tera mera afsana',                                          VERSE, 3.4),
    ('Poora hua na, jaana',                                       VERSE, 3.4),
    ('Pal-pal jeena muhaal',                                      VERSE, 1.3),
    ('mera tere bina',                                            VERSE, 1.1),
    ('Yeh saare nashe bekaar',                                    VERSE, 1.1),
    (' teri aankhon ke siwa',                                     VERSE, 1.0),
    ('Ghar nahi jaata, main bahar, rehta tera intezaar',          VERSE, 1.3),
    ('Mere khwabon mein aa na karke 16 singhaar',                 VERSE, 1.5),
    ('Main ab kyun hosh mein aata nahi?',                         VERSE, 1.3),
    ('Sukoon yeh dil kyun paata nahi?',                           VERSE, 0.4),
    ('Kyun todun khud se jo the waade?',                          VERSE, 0.4),
    ('Ke ab yeh ishq nibhana nahi',                               VERSE, 0.4),
    ('Main modun tumse jo yeh chehra',                            VERSE, 0.4),
    ('Dobara nazar milana nahi',                                  VERSE,0.4 ),
    ('Yeh duniya jaane mera dard',                                VERSE,0.4 ),
    ('Tujhe yeh nazar kyun aata nahi?',                           VERSE,1.2 ),
    ('',                                                          VERSE,0.3 ),
    ('Sohneya, yoon tera sharmana meri jaan na le-le',            CHORUS,1.3),
    ('Kaan ke peechhe zulf chupana, meri jaan, kya kehne!',       CHORUS,1.5),
    ('Zaalima, tauba tera nakhra! Iske waar kya kehne!',          CHORUS,1.5),
    ('Thaam ke baithe dil ko ghayal, kahin haar na baithein',     CHORUS,0.8),
    ('',                                                          VERSE,0.3 ),
    ('Teri nazrein mujhse kya kehti hain,',                       VERSE,0.8 ),
    ('inmein wafa behti hai,',                                    VERSE,1.2 ),
    ('Thodi-thodi si raazi,',                                     VERSE,0.6 ),
    ('thodi si khafa rehti hain',                                 VERSE,1.8 ),
    ('Log hain zaalim bade',                                      VERSE,1.5 ),
    (' inmein jafa dekhi hai',                                    VERSE,1.5 ),
    ('Yeh duniya teri nahi, maine tujh mein haya dekhi hai',      VERSE,1.5 ),
    ('',                                                          VERSE,0.3 ),
    ('Jeena muhaal mera tere bina',                               VERSE,  0.8),
    ('Yeh saare nashe bekaar',                                    VERSE,  0.6),
    (' teri aankhon ke siva',                                     VERSE,  0.4),
    ('Ghar nahi jaata, main bahar',                               VERSE,  1.2),
    ('tera intezaar',                                             VERSE,  0.8),
    ('mere.',                                                     VERSE,  0.6),
    ('khwabon mein aa na karke 16 singhaar',                      VERSE,  1.0),
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_width():
    try:
        return os.get_terminal_size().columns
    except:
        return 80  

def center(text):
    width = get_width()
    
    clean = text.replace(Fore.CYAN, '').replace(Fore.WHITE, '') \
                .replace(Fore.YELLOW, '').replace(Style.BRIGHT, '') \
                .replace(Style.RESET_ALL, '').replace(Style.DIM, '')
    pad = max(0, (width - len(clean)) // 2)
    return ' ' * pad

def typewrite(text, color):
    if text == '':
        print()
        return
    prefix = center(color + text)
    sys.stdout.write(prefix)
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(0.06)
    print(Style.RESET_ALL)

clear()
width = get_width()
print('\n' * (os.get_terminal_size().lines // 2 - 2) if os.name else '\n' * 8)
title_text = "PAL PAL ~ Talwinder"
print(' ' * max(0, (width - len(title_text)) // 2) + TITLE + title_text)
print()
time.sleep(1.2)
clear()
print('\n' * 3)

for text, color, delay in lyrics:
    typewrite(text, color)
    time.sleep(delay)