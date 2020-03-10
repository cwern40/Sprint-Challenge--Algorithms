'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    finish = len(word)
    start = 0
    amount = 0
    if len(word) <= 1:
        return 0
    
    if word[start] + word[start+1] == "th":
        amount += 1

    amount += count_th(word[start+1:finish])
    return amount