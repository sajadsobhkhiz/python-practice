'''
hours = input("Enter hours:")
h = float(hours)
rate = input("Enter the rate:")
r = float(rate)

if h > 40:
    e = h - 40  # extra hours
    gross = (40 * r) + (e * r * 1.5)
else:
    gross = h * r
    
print(gross)
'''


'''
try:
    score = input("Enter score (between 0.0 and 1.0):")
    s = float(score)
except:
    print("Please enter the number between 0.0 and 1.0")
    exit()
    
if s > 1 or s < 0:
    print("the number is out of range!")
elif s >= 0.9:
    print("A") 
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")  
elif s >= 0.6:
    print("D")
else:
    print("F")
'''


'''
def computepay(h, r):
    if h > 40:
        e = h - 40  # extra hours
        gross = (40 * r) + (e * r * 1.5)
    else:
        gross = h * r
    return gross

hours = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    hours = float(hours)
    rate = float(rate)
except:
    print("please enter numbers!")
    exit()
        
p = computepay(hours, rate)
print("Pay", p)
'''

'''
while True:
    line = input("Enter something: ")
    if(line == 'done'):
        break
    print(line)

print("Done!")
'''

'''
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        num=int(num)
    except:
        print("Invalid input")
        continue

    if largest != None:
        if num > largest:
            largest = num
    else:
        largest = num 

    if smallest != None:
        if num < smallest:
            smallest = num
    else:
        smallest = num

print("Maximum is ", largest)
print("Minimum is", smallest)
'''

'''
text = "X-DSPAM-Confidence:    0.8475"
for letter in text:
    try:
        is_digit = int(letter)
        pos = text.find(letter)
        break
    except:
        continue


num_found = float(text[pos:])
print(num_found)
'''

'''
fexist = False
fhand = ""
while(not fexist):
    try:
        fname = input('Enter the file name: ')
        fhand = open(fname)
        fexist = True
    except:
        print('the file is not exist!')

for line in fhand:
    line = line.upper().rstrip()
    print(line)
'''

'''
fexist = False
fhand = ""
count = 0
total = 0
while(not fexist):
    try:
        fname = input('Enter the file name: ')
        fhand = open(fname)
        fexist = True
    except:
        print('the file is not exist!')

for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        for letter in line:
            try:
                is_digit = int(letter)
                pos = line.find(letter)
                break
            except:
                continue
        num_found = float(line[pos:])
        total = total + num_found

print("Average spam confidence:", total/count)
'''


'''
Open the file romeo.txt and read it line by line. For each line,
split the line into a list of words using the split() method. 
The program should build a list of words. For each word on each 
line check to see if the word is already in the list and 
if not append it to the list. When the program completes, 
sort and print the resulting words in python sort() order as shown in the desired output.
'''
# words = list()
# fexist = False
# fhand = ""
# while(not fexist):
#     try:
#         fname = input('Enter the file name: ')
#         fhand = open(fname)
#         fexist = True
#     except:
#         print('the file is not exist!')

# for line in fhand:
#     word_temp=line.split()
#     for word in word_temp:
#         if(word not in words):
#             words.append(word)

# words.sort()         
# print(words)


'''
Open the file mbox-short.txt and read it line by line. 
When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out 
the second word in the line (i.e. the entire address of the person 
who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. 
Also look at the last line of the sample output to see how to print the count.
'''
# count = 0
# words = list()
# fhand = open('mbox-short.txt')
# for lines in fhand:
#     if lines.startswith("From "):
#         count = count + 1
#         words = lines.split()
#         print(words[1])

# print("There were", count, "lines in the file with From as the first word")

'''
Write a program to read through the mbox-short.txt and figure out 
who has sent the greatest number of mail messages. The program looks for
'From ' lines and takes the second word of those lines as the person who
sent the mail. The program creates a Python dictionary that maps the 
sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using 
a maximum loop to find the most prolific committer.
'''
# counts = dict()

# fhand = open('mbox-short.txt')

# for line in fhand:
#     if line.startswith("From "):
#         words = line.split()
#         email = words[1]
#         counts[email] = counts.get(email, 0) + 1

# maximum = None
# max_sender = None

# for key, value in counts.items():
#     if maximum is None or value > maximum:
#         maximum = value
#         max_sender = key

# print(max_sender, maximum)

'''
Write a program to read through the mbox-short.txt and figure out 
the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time
and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out 
the counts, sorted by hour as shown below.
'''

# fhand = open('mbox-short.txt')
# hours = list()
# for line in fhand:
#     if line.startswith("From "):
#         hours.append(line.split()[5].split(":")[0])   

# counts  = dict()
# for h in hours:
#     counts[h] = counts.get(h,0) + 1

# for k, v in sorted(counts.items()):
#     print(k,v)


# ChatGPT Solution
# fhand = open('mbox-short.txt')

# counts = dict()

# for line in fhand:
#     if line.startswith("From "):
#         time = line.split()[5]
#         hour = time.split(":")[0]
#         counts[hour] = counts.get(hour, 0) + 1

# for k, v in sorted(counts.items()):
#     print(k, v)


# import re

# lst = list()
# hand = open('regex_sum_2326219.txt')

# for line in hand:
#     nums = re.findall(r'[0-9]+', line)
#     if nums:             # This means: if list is not empty
#         lst.extend(nums) # append all found numbers to your list
# total = 0
# count = 0
# for num in lst:
#     count = count + 1
#     total = total + int(num)

# print(f'There are {count} values with a sum = {total}')


##################################################################
##################################################################

# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())

# mysock.close()

##################################################################
##################################################################

# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())

# mysock.close()

##################################################################
##################################################################

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# or pip install beautifulsoup4 to ensure you have the latest version
# and unzip it in the same directory as this file

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl # defauts to certicate verification and most secure protocol (now TLS)

# # Ignore SSL/TLS certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

##################################################################
##################################################################

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl 


# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter URL: ')
# count = input('Enter Count: ')
# position = input('Enter Position: ')
# print('Retrieving: ', url)

# for i in range(int(count)):
#     html = urllib.request.urlopen(url, context=ctx).read()
#     soup = BeautifulSoup(html, 'html.parser')
#     tags = soup('a')
#     pos = 0
#     for tag in tags:
#         pos = pos + 1
#         if pos == int(position) :
#             url = tag.get('href', None)
#             print('Retrieving: ', url)
#             break
#     continue
    
##################################################################
############################ChatGPT Solution######################
# import urllib.request
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input("Enter URL: ")
# count = int(input("Enter Count: "))
# position = int(input("Enter Position: "))

# print("Retrieving:", url)

# for i in range(count):
#     # Read HTML
#     html = urllib.request.urlopen(url, context=ctx).read()
#     soup = BeautifulSoup(html, "html.parser")

#     # Get all anchor tags
#     tags = soup.find_all("a")

#     # Find the link at the given position
#     url = tags[position - 1].get("href")   # position starts at 1, list starts at 0
#     print("Retrieving:", url)
##################################################################
##################################################################


# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl # defauts to certicate verification and most secure protocol (now TLS)

# # Ignore SSL/TLS certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')

# # Retrieve all of the anchor tags
# tags = soup('span')
# total = 0
# count = 0
# for tag in tags:
#    count = count + 1
#    total = total + int(tag.contents[0])

# print ('Count ', count)
# print ('Sum ', total)

##################################################################
##################################################################

# import urllib.request
# import xml.etree.ElementTree as ET

# url = input('Enter location: ')
# if len(url) < 1 : 
#     url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

# print('Retrieving', url)
# uh = urllib.request.urlopen(url)
# data = uh.read()
# print('Retrieved',len(data),'characters')
# tree = ET.fromstring(data)

# counts = tree.findall('.//count')
# nums = list()

# for result in counts:
#     # Debug print the data :)
#     nums.append(int(result.text))

# print('Count:', len(counts))
# print('Sum:', sum(nums))

##################################################################
##################################################################

# import json

# data = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Brent"
#   }
# ]'''

# info = json.loads(data)
# print('User count:', len(info))

# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])

##################################################################
##################################################################

# import urllib.request
# import json

# url = input('Enter location: ')
# if len(url) < 1 : 
#     url = 'https://py4e-data.dr-chuck.net/comments_42.json'

# print('Retrieving', url)
# uh = urllib.request.urlopen(url)
# data = uh.read()
# print('Retrieved',len(data),'characters')

# info = json.loads(data)
# comments = info['comments']

# total = 0
# for item in comments:
#     total = total + item['count']

# print('Count:', len(comments))
# print('Sum:',total)

##################################################################
##################################################################

import urllib.request, urllib.parse
import json, ssl

# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break

    plus_code = js['features'][0]['properties']['plus_code']
    print('Plus code', plus_code)
    
##################################################################
##################################################################
