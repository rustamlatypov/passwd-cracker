# going through the .txt file
def get_wordlist(s):
    W = set()
    with open(s, encoding='latin-1') as f:
        for line in f:
            W.add(line.strip())
    return W