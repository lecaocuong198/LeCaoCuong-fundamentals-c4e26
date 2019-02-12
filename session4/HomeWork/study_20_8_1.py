letter_count = {}

n = input("Enter the letter? ")

for letter in n :
    letter_count[letter] = letter_count.get(letter,0)+1

letter_items = list(letter_count.items())
letter_items.sort()
print(letter_items)