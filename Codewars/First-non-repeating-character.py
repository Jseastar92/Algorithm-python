#First code

def first_non_repeating_letter(string):
    s = ''.join(string[i] for i in range(len(string)) \
    if not string[i].lower() in string[i+1::].lower()\
    and not string[i].lower() in string[0:i].lower() )

    if s :
        return s[0]
    else :
        return ''

#print(first_non_repeating_letter('moonmen'))
