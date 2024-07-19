# Knuth Morris Pratt string matching algorithm

def check_to_skip(txt, pat):
    matched = 1
    for i in range(1, len(pat)):
        if txt[i] == pat[i]:
            matched += 1
        else:
            break
    return matched


def kmp(txt, pat):
    t = 0
    skip = 0
    while t < len(txt)-len(pat)+1:
        if txt[t] == pat[0]:
            skip = check_to_skip(txt[t:t + len(pat)], pat)
        if skip == len(pat):
            print(f'{pat} found at {t+1} position in text')
            skip = 0
        if skip > 0:
            t += skip
        else:
            t += 1


text = input("Enter the text:")
pattern = input("Enter the pattern to search in the text:")
kmp(text, pattern)
