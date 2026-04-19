import time
import sys
import os
import pygame
from colorama import init, Fore, Style

init(autoreset=True)

# ===== AUDIO INIT (FIXED) =====
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

SONG_FILE = "palpal.mp3"

# ===== COLORS =====
TITLE  = Fore.MAGENTA + Style.BRIGHT
VERSE  = Fore.WHITE
CHORUS = Fore.YELLOW + Style.BRIGHT
UI     = Fore.CYAN

# ===== FULL LYRICS (YOUR ORIGINAL) =====
lyrics = [
    ('Tera mera afsana', VERSE, 3.4),
    ('Poora hua na, jaana', VERSE, 3.5),
    ('Pal-pal jeena muhaal', VERSE, 1.4),
    ('mera tere bina', VERSE, 1.3),
    ('Yeh saare nashe bekaar', VERSE, 1.3),
    ('teri aankhon ke siwa', VERSE, 1.0),
    ('Ghar nahi jaata, main bahar, rehta tera intezaar', VERSE, 1.8),
    ('Mere khwabon mein aa na karke 16 singhaar', VERSE, 1.6),
    ('Main ab kyun hosh mein aata nahi?', VERSE, 1.3),
    ('Sukoon yeh dil kyun paata nahi?', VERSE, 0.4),
    ('Kyun todun khud se jo the waade?', VERSE, 0.4),
    ('Ke ab yeh ishq nibhana nahi', VERSE, 0.4), 
    ('Main modun tumse jo yeh chehra', VERSE, 0.6),
    ('Dobara nazar milana nahi', VERSE, 0.6),
    ('Yeh duniya jaane mera dard', VERSE, 0.6),
    ('Tujhe yeh nazar kyun aata nahi?', VERSE, 1.3),

    ('', VERSE, 0.2),

    ('Sohneya, yoon tera sharmana meri jaan na le-le', CHORUS, 1.8),
    ('Kaan ke peechhe zulf chupana, meri jaan, kya kehne!', CHORUS, 1.8),
    ('Zaalima, tauba tera nakhra! Iske waar kya kehne!', CHORUS, 1.6),
    ('Thaam ke baithe dil ko ghayal, kahin haar na baithein', CHORUS, 1.3),

    ('', VERSE, 0.3),

    ('Teri nazrein mujhse kya kehti hain,', VERSE, 0.8),
    ('inmein wafa behti hai,', VERSE, 1.2),
    ('Thodi-thodi si raazi,', VERSE, 0.6),
    ('thodi si khafa rehti hain', VERSE, 1.8),
    ('Log hain zaalim bade', VERSE, 1.5),
    ('inmein jafa dekhi hai', VERSE, 1.5),
    ('Yeh duniya teri nahi, maine tujh mein haya dekhi hai', VERSE, 1.5),

    ('', VERSE, 0.3),

    ('Jeena muhaal mera tere bina', VERSE, 0.9),
    ('Yeh saare nashe bekaar', VERSE, 0.7),
    ('teri aankhon ke siva', VERSE, 0.6),
    ('Ghar nahi jaata, main bahar', VERSE, 1.3),
    ('tera intezaar', VERSE, 0.9),
    ('mere...', VERSE, 0.7),
    ('khwabon mein aa na karke 16 singhaar', VERSE, 2.1),


    ('',VERSE,0.3),

    ('Tera-mera afsana',VERSE,1.4),
    ('Poora hua na, jaana',VERSE,0.8),
    ('Hovan band kamre vich kalla',VERSE,0.9),
    ('Fir vi disda ae parshawan',VERSE,0.7),
    ('Saare puchhde ne mainu',VERSE,0.8),
    ('Kyun main gallan nahi karda',VERSE,1),
    ('Kinne sohne ne chehre aithey',VERSE,1),
    ('Dil kyun nahi eh bharda?',VERSE,0.9),
]

# ===== UTIL =====
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_width():
    try:
        return os.get_terminal_size().columns
    except:
        return 80

def center(text):
    width = get_width()
    return ' ' * max(0, (width - len(text)) // 2)



# ===== PLAY SONG =====
def play_song():
    try:
        path = os.path.abspath(SONG_FILE)
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()
    except Exception as e:
        print("ERROR:", e)


# ===== TITLE =====

def animate_title(text):
    clear()
    width = get_width()

    # Center vertically
    try:
        lines = os.get_terminal_size().lines
        print('\n' * (lines // 2 - 2))
    except:
        print('\n' * 8)

    prefix = ' ' * max(0, (width - len(text)) // 2)

    # Simple typing effect
    sys.stdout.write(prefix)
    for char in text:
        sys.stdout.write(TITLE + char)
        sys.stdout.flush()
        time.sleep(0.08)

    print(Style.RESET_ALL)

    # Hold on screen (8 seconds total including typing)
    remaining_time = max(0, 8 - len(text) * 0.08)
    time.sleep(remaining_time)

    clear()
    print('\n' * 3)
# ===== PLAYER UI =====
def show_ui():
    clear()
    width = get_width()

    print(UI + "=" * width)
    print(center("🎧 NOW PLAYING"))
    print(center("Pal Pal ~ Talwiinder"))
    print(UI + "=" * width)
    print()

# ===== TYPEWRITER =====
def typewrite(text, color):
    if text == '':
        print()
        return

    prefix = center(text)
    sys.stdout.write(prefix)

    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(0.04)

    print(Style.RESET_ALL)


# ===== MAIN =====




play_song()  # 🎧 start song FIRST

# small buffer so music actually begins before animation
time.sleep(0.3)

animate_title("Pal Pal ~ Talwinder")  # 🎬 runs WITH music

show_ui()

# slight adjustment so lyrics sync better
time.sleep(0.5)


for text, color, delay in lyrics:
    typewrite(text, color)
    time.sleep(delay + 0.4)  # ⬅️ added 0.3 sec to every line
while pygame.mixer.music.get_busy():
    time.sleep(1)