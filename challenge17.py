import re

text = "the ghost that says boo hounts the loo"

match = re.findall(".oo", text, re.IGNORECASE)
print(match)
