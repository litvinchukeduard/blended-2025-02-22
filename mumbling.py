'''
This time no story, no theory. The examples below show you how to write function accum:
Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.
'''

def accum(string_argument: str) -> str:
    result_list = []
    for symbol in string_argument:
        str_index = string_argument.index(symbol)
        final_part = symbol * (str_index + 1)
        # result_str += final_part.capitalize() + '-'
        result_list.append(final_part.capitalize())
    # return result_str[:-1]
    return '-'.join(result_list)

# print(accum("abcd"))
# print(accum("RqaEzty"))
# print(accum("cwAt"))

my_list = ["a", "b", "c"] # a,b,c 
# print(' hello '.join(my_list))
my_list.join("-")
# print("abcd"[:-1])
