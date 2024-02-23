import pyperclip, re

text = pyperclip.paste()

phone_regex = re.compile(r'''(
                         (?:\d{3}|\(\d{3}\))
                         -\d{3}
                         -\d{4}
                         )''', re.VERBOSE)

email_regex = re.compile(r'''[\w_]+ # matching user part of email
                         @[a-z]+     # matching domain
                         \.com      # matching .com
                         (?=\s)     # positive lookahead for the space
                         ''', re.VERBOSE)

phone_matches = phone_regex.findall(text)

email_matches = email_regex.findall(text)

copy_text = []
copy_text.append("Phone Matches:")

if len(phone_matches) == 0:
    copy_text.append("No phone matches")

for phone_match in phone_matches:
    copy_text.append(phone_match)

copy_text.append("Email Matches:")

if len(email_matches) == 0:
    copy_text.append("No email matches")

for email_match in email_matches:
    copy_text.append(email_match)


pyperclip.copy("\n".join(copy_text))


"""
ju22mp@gmail.com
helllo my email (30)1-401-4506 is 1natwon@yahoo.com what if jdump@gmail.com
hello my number is ju_mp@gmail.com kjh 301-401-4506 alhdsfljkls dfl 
poop@bing.com
(201)-401-4506
"""
