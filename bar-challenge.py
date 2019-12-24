# If you can read this code, tell your bartender the
# Secret word of the day for a free drink on us.

your_drink = input("your drink: ")

def reverse(s):
    char_list = list(s)
    reversed_char_list = char_list[::-1]
    reversed_string = ''.join(reversed_char_list)
    
    return reversed_string

bartender = {
    "str1": "ers",
    "str2": reverse("rap"),
    "str3": "amet",
    "request": lambda preference : 
        print(preference + '.Secret word:' + 
            bartender['str2'] + bartender['str3'] + bartender['str1'])
}

bartender['request'](your_drink)