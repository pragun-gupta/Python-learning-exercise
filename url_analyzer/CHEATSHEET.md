# Python Cheatsheet

## Terminal commands
- cd: Opens the directory file
- python --version: Shows the version of python installed
- python filename .py: Runs a file. The terminal has to be in the file's folder, so check the prompt. Ex: python hello.py
- cd folder / cd .. : Move into a folder, or up one level. dir lists the files in the current folder.
- >>> prompt : Means we are inside the python script. Type exit() to get back to the normal terminal
- cls: clears the terminal screen (Windows)

## Input and output
- input("text"): asks the user to type something and gives it back as a string.
- print(x): shows a value. 

## Strings
- len(s): number of characters
- f-string: Puts values inside text with curly braces. print(f"Length: {len(url)}")
- s.isdigit(): True if the character is a digit
- s.startswith('https'): True if the string begins with that text
- input('URL: '): returns what the user typed.
- len(): counts characters in a string.
- strip(): So it doesn't count spaces

## The in operator
- x in text: True if x appears inside the text, otherwise False. Ex: '@' in url
- print any expression: print() accepts anything that works out to a value, so we can print a True/False check directly. Ex: print("Contains @:", '@' in url)

## Loopa and Conditions
- for ch in url: goes through a string one character at a time.
- if condition: runs the indented lines only when the condition is True.
- Loop variable replaces input(): for url in urls: gives me one URL per pass, so the checks use url and the input() line goes away. Ex: for url in urls:
- Nested loop: A loop inside a loop. The outer one picks a URL, the inner one goes through that URL's characters. Ex: for ch in url:

## Counting pattern
- Start count = 0 before the loop, test with if inside, add 1 when it matches, print after the loop. count += 1
# Counting with count
- s.count(text): Returns how many times the text appears in the string. No loop needed. Ex: url.count('.') [It counts dots in the path and query too, not just the domain.]

## startswith and https
- s.startswith(text): True if the string begins with that text, otherwise False.Ex: url.startswith('https')
- Case sensitive: startswith treats HTTPS and https as different. Use .lower() first if I need to ignore case. Ex: url.lower().startswith('https')
- NOTE: https is not proof of safety, Many phishing sites use https, so missing https is only a weak signal. The model will weigh many features together.

## Lists and dictionaries
- List of URLs: A list holds many items in square brackets, separated by commas. Ex: urls = ["https://a.co", "http://b.com"]

## Files
- (add)

## Git and .gitignore
- git status: see what changed
- git add .: stage everything
- git commit -m "msg": save a snapshot
- git push: send it to GitHub
- .gitignore: Lists files Git should skip: secrets, generated data, cache folders.
.env, *.db, features.csv, __pycache__/

## Mistakes I made 

- I stored True/False in my counter and it overwrote the tally. Use a separate counter and an if.
- Printing inside versus after the loop changes how many times it runs.
- A terminal command runs in the folder shown in the prompt, so python file.py fails if the file is in another folder.
- Typing python then >>> means I’m inside Python, and exit() gets me out.
- if vs elif: elif only runs when the earlier branches did not. Independent questions need separate ifs, or none at all.