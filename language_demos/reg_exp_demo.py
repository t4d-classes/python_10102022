import re

# content = "as busy as a bee"

# r = re.compile(r"as")

# match the regular expression from the start of the content
# print(r.match(content))

# searches the string for a match
# print(r.search(content))

# returns a list of the matches
# print(r.findall(content))

# returns all matches as match objects
#print(list(r.finditer(content)))

# content = "red|green;blue:yellow"
# r = re.compile(r"\||;|:")
# print(r.split(content))
# print(r.sub(",", content))

# content = "red|green;blue:yellow"
# r = re.compile(r"[];:]")
# print(r.split(content))
# print(r.sub(",", content))

content = """apple
banana
apple
Banana
banana
apple
avocado
"""

# r = re.compile(r"^apple", re.MULTILINE)
# r = re.compile(r"^a[a-z]*", re.MULTILINE)
# r = re.compile(r"[a-z]*a$", re.MULTILINE | re.IGNORECASE)

#print(list(r.finditer(content)))

# content = "<b>content 1</b><span>test</span><b>content 2</b><div>fun</div>"

# r = re.compile(r"<span>(.*)</span>")
# r = re.compile(r"<b>(.*?)</b>")
# r = re.compile(r"<.*?>(.*?)</.*?>")

# for match in r.finditer(content):
#     print(match.groups())


# r = re.compile(r"^Add: ([0-9]*)", re.MULTILINE)

# with open("report.txt") as report_file:
#     report_content = report_file.read()
#     m = r.search(report_content)
#     add_calc_count = m.groups()[0]
#     print(add_calc_count)

content = "Bob Smith"

r = re.compile(r"(?P<first_name>[A-Za-z]*) (?P<last_name>[A-Za-z]*)")

match = r.match(content)

print(match.groupdict())