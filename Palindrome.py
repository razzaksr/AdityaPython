# hey="Razak Mohamed"
# print(hey)
# print(hey[::])
# print(hey[:])
# print(hey[::-1])

def findPalindrome(users):
    if users == users[::-1]:
        return "Palindrome"
    else:
        return "Not a palindrome"

status=findPalindrome("DAD")
print(status)