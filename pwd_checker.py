hasLenMin = False
length = 0
hasUppercase = False
hasLowercase = False
hasNumber = False
hasSpecial = False
strength = ""

print(strength[0:1])
print(strength[1:2])
print(strength[2:])

password = input("Enter a password: ")
hasLength_line = ""
if len(password) >= 8 and len(password) != 0:
    hasLenMin = True
    length = len(password)
    strength = "Low"
    hasLength_line = 'Strength: {}'.format('Yes')
elif len(password) >= 13:
    strength = "Medium"
elif len(password) >= 16:
    strength = "High"
else:
    hasLenMin = False
    hasLength_line = 'Strength: {}'.format('No')


strength_line = f'Strength: {strength}'

if any(c.isupper() for c in password) == True:
    hasUppercase = True
    hasLowercase = True
    uc_line = 'Uppercase: {}'.format('Yes')
else:
    hasLowercase = True
    lc_line = 'Lowercase: {}'.format('Yes')

if any(c.isdigit() for c in password) == True:
    hasNumber = True
    num_line = 'Numbers: {}'.format('Yes')

if any(not c.isalnum() for c in password) == True:
    hasSpecial = True
    spec_line = 'Special CHaracters: {}'.format('Yes')

print(uc_line)
print(num_line)
print(spec_line)
print(strength_line)
