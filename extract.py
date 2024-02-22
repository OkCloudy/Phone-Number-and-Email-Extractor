import pyperclip, re

phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo1 = phone_regex.search("")
print(mo1.group)

text = pyperclip.paste()
print(text)