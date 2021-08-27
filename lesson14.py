# requests
# функции сортировки

import requests
import re

def sort_by_quote_len(quote_dict):
    quote = quote_dict["quoteText"]
    return len(quote.split())

def sort_by_quote_link_digits(quote_dict):
    quote_link = quote_dict["quoteLink"]
    pattern = r"[0-9]+"
    digits = re.findall(pattern, quote_link)
    return len("".join(digits))

def get_raw_quote(index):
    params = {"method": "getQuote", "format": "json", "key": index}
    r = requests.get('http://api.forismatic.com/api/1.0/', params=params)
    return r.json()

quotes = []
for index in range(5):
    data = get_raw_quote(index)
    quotes.append(data)

print(quotes)
sort_quotes = sorted(quotes, key=sort_by_quote_link_digits)
print(sort_quotes)


# my_list = [3, 2, 5, 10, -9]
# my_list.sort(reverse=True)
# print(my_list)

# def key_sort(item):
#     return len(str(item))
#
# my_list = ["Q", "qw", "ASDF", "asd", 123, "!@#&*(("]
# new_list = sorted(my_list, key=key_sort)
# print(new_list)