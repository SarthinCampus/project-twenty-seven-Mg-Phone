import re

text = input()

# Match dates like 05/07/2025 or 31-12-2024
pattern = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'

dates = re.findall(pattern, text)

for date in dates:
    print(date)
