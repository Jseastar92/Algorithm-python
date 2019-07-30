#Second Code
def first_non_repeating_letter(string):
    string_l = string.lower()

    for i in range(len(string_l)):
        if string_l.count(string_l[i]) == 1:
            return string_l[i]
        else : return ""


first_non_repeating_letter('a')
