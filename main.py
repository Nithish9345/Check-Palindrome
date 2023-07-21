def panlindrome_recursion(s, start, end):

    if start > end:
        return True

    if s[start] != s[end] :
        return False

    return panlindrome_recursion(s, start = start+1, end = end-1)

s = input()
print(panlindrome_recursion(s, 0, len(s)-1))