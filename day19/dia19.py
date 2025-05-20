def palindrome_test(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(palindrome_test('level'))
print(palindrome_test('radar'))
print(palindrome_test('ame a ema'))
print(palindrome_test('love'))