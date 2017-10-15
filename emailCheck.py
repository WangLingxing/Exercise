import re

email_re = re.compile(r'^(<\w+\s+\w+>\s*)?[0-9a-zA-Z\.\-\_]+@[0-9a-zA-Z]+\.[\w]+$')

print email_re.match("someone@gmail.com").group()
print email_re.match("bill.gates@microsoft.com").group()
print email_re.match("<Tom Paris> tom@voyager.org").group()