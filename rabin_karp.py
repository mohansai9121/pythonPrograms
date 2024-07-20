# Rabin Karp String matching algorithm

text = input("Enter the text:")
pattern = input("Enter pattern:")

for i in range(0, len(text)-len(pattern)+1):
    if hash(text[i:i+len(pattern)]) == hash(pattern):
        print(f"{pattern} found at position {i+1} in the text")
