# while True:
#     try:
#         temp = input("Enter temperature: ")
#         temp_in_c = float(temp)
#         break
#     except:
#         print("Please enter a valid number.")
#         continue

# temp_in_f = temp_in_c * 9 / 5 + 32
# print(f'{temp_in_c}°C is {temp_in_f: .2f}°F')

#################################################################

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin
# import ssl, sys

# sys.stdout.reconfigure(encoding="utf-8", errors="replace")
# sys.stdin.reconfigure(encoding="utf-8", errors="replace")

# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input("Enter - ").strip()

# headers = {
#     "User-Agent": "Mozilla/5.0",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     "Accept-Language": "en-US,en;q=0.5",
#     "Accept-Encoding": "identity"  # مهم‌ترین خط برای python.org
# }

# req = urllib.request.Request(url, headers=headers)

# html = urllib.request.urlopen(req, context=ctx, timeout=15).read()

# soup = BeautifulSoup(html, "html.parser")

# links = soup.select("a[href]")
# print("Links found:", len(links))

# for a in links[:30]:
#     print(urljoin(url, a["href"]))

#################################################################

# def reverse(t):
#     rev_text = ''
#     length = len(t)
#     for i in range(length):
#         rev_text = rev_text + t[length - 1 - i]
#     return rev_text

# while True:
#     text = input("Enter a string to reverse: ")
#     if text != '':
#         break
#     else:
#         print("Please enter something...")
#         continue

# print(reverse(text))

####################################################################################################
###################################################################################################

# print('''A strong password must:
# 1. Be at least 8 characters long.
# 2. Have at least one lowercase letter.
# 3. Have at least one uppercase letter.
# 4. Have at least one digit.
# 5. Have at least one special character.
# 6. No spaces.
# ''')

# SPECIALS = {
#     '!', '@', '#', '$', '%', '^', '&', '*',
#     '(', ')', '-', '_', '=', '+', '[', ']',
#     '{', '}', ';', ':', '"', ',', '.', '<',
#     '>', '/', '\\', '?', '|'
# }

# def get_password():
#     while True:
#         pw = input('Enter your password please: ')
#         if pw != '':
#             return pw  # do not strip; we want to detect spaces

# def password_check(pw: str) -> bool:
#     has_len     = len(pw) >= 8
#     has_lower   = any(c.islower() for c in pw)
#     has_upper   = any(c.isupper() for c in pw)
#     has_digit   = any(c.isdigit() for c in pw)
#     has_special = any(c in SPECIALS for c in pw)
#     has_space   = any(c.isspace() for c in pw)

#     ok = True
#     if not has_len:
#         print('It must be at least 8 characters long.')
#         ok = False
#     if not has_lower:
#         print('It must have at least one lowercase letter.')
#         ok = False
#     if not has_upper:
#         print('It must have at least one uppercase letter.')
#         ok = False
#     if not has_digit:
#         print('It must have at least one digit.')
#         ok = False
#     if not has_special:
#         print('It must have at least one special character.')
#         ok = False
#     if has_space:
#         print('It must not have any spaces.')
#         ok = False

#     return ok

# # ask once per loop
# while True:
#     pw = get_password()
#     if password_check(pw):
#         break

# print('Well done! Your password is saved!')

####################################################################################################
####################################################################################################

# import msvcrt
# import string

# SPECIALS = set(string.punctuation)

# def get_password_with_stars(prompt="Enter your password: "):
#     print(prompt, end="", flush=True)
#     pw = ""

#     while True:
#         ch = msvcrt.getwch()

#         # ENTER
#         if ch == "\r":
#             print()
#             break

#         # BACKSPACE
#         elif ch == "\b":
#             if len(pw) > 0:
#                 pw = pw[:-1]
#                 print("\b \b", end="", flush=True)

#         # ARROW KEYS or FUNCTION KEYS (start with '\xe0' or '\x00')
#         elif ch in ["\xe0", "\x00"]:
#             msvcrt.getwch()  # read the next char and ignore
#             continue

#         # ESCAPE KEY
#         elif ch == "\x1b":
#             continue  # ignore ESC

#         # NORMAL CHARACTERS
#         else:
#             pw += ch
#             print("*", end="", flush=True)

#     return pw


# def metrics(pw: str):
#     length = len(pw)
#     has_lower = has_upper = has_digit = has_special = has_space = False

#     for c in pw:
#         if c.islower(): has_lower = True
#         if c.isupper(): has_upper = True
#         if c.isdigit(): has_digit = True
#         if c in SPECIALS: has_special = True
#         if c.isspace(): has_space = True

#     return {
#         "len_ok": length >= 8,
#         "has_lower": has_lower,
#         "has_upper": has_upper,
#         "has_digit": has_digit,
#         "has_special": has_special,
#         "has_space": has_space,
#         "length": length
#     }


# def score_from_metrics(m):
#     score = 0
#     L = m["length"]

#     # Length points
#     if L >= 8:  score += 2
#     if L >= 12: score += 1
#     if L >= 16: score += 1

#     # Variety
#     types = sum([m["has_lower"], m["has_upper"], m["has_digit"], m["has_special"]])
#     score += types

#     # Bonuses
#     if types == 4: score += 2
#     if L >= 20:    score += 1

#     # Penalty
#     if m["has_space"]: score -= 1

#     # Clamp
#     score = max(0, min(10, score))
#     label = "Weak" if score <= 4 else ("Medium" if score <= 7 else "Strong")
#     return score, label


# def password_check_and_score(pw: str):
#     m = metrics(pw)
#     messages = []

#     if not m["len_ok"]:      messages.append("It must be at least 8 characters long.")
#     if not m["has_lower"]:   messages.append("It must have at least one lowercase letter.")
#     if not m["has_upper"]:   messages.append("It must have at least one uppercase letter.")
#     if not m["has_digit"]:   messages.append("It must have at least one digit.")
#     if not m["has_special"]: messages.append("It must have at least one special character.")
#     if m["has_space"]:       messages.append("It must not have any spaces.")

#     score, label = score_from_metrics(m)
#     ok = len(messages) == 0
#     return ok, messages, score, label


# # ------------------ MAIN PROGRAM ------------------

# print("""
# A strong password must:
# 1. Be at least 8 characters long.
# 2. Have at least one lowercase letter.
# 3. Have at least one uppercase letter.
# 4. Have at least one digit.
# 5. Have at least one special character.
# 6. No spaces.
# """)

# while True:
#     pw = get_password_with_stars("Enter your password: ")
#     ok, msgs, score, label = password_check_and_score(pw)

#     # Show problems
#     for msg in msgs:
#         print(msg)

#     # Show strength
#     print(f"Strength: {label} ({score}/10)")
    
#     if ok:
#         print("Well done! Your password is saved!")
#         print(f"Your password is: {pw}")
#         break

############################################################################
############################################################################

# age = int(input('Enter the age to get the price: '))

# if (age <12):
#     price = 8
# elif (age>=12 and age<=64):
#     price = 12
# else:
#     price = 10

# print(f'The ticket price is: ${price}')

############################################################################
############################################################################

import time

for i in range(10, -1, -1):
    if i == 5:
        print("Halfway point reached!")
    else:
        print(i)
    time.sleep(1)

print("Time's Up!")


