import re
def find_secret_message(paragraph):
    paragraph = paragraph.lower()
    paragraph = re.sub("[^A-Za-z0-9]", " ", paragraph).replace("  ", " ")
    res,seen = [],{}
    for word in paragraph.split():
        seen[word] = seen.get(word, 0) + 1
        if seen[word] == 2:
            res.append(word)
    print(" ".join(res))


find_secret_message("have. cat sky! kills. eats Have Cat, ALWAYS message: message. sun saves. never pippi the cat, Code! kills! eats! T-Rex. Good always: have")
