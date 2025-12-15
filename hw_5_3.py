from string import punctuation

text = input("Please enter a text: ").title()

for mark in punctuation:
    text = text.replace(mark, "")
text = text.replace(" ", "")
text = text[:140]
hashtag = f"#{text}"
print(hashtag)