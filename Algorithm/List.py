my_str = "this is a test"
str_element = my_str.split()
print(str_element)
rev_element = []
for element in str_element:
    rev_element.append(element[::-1])
    print(rev_element)
    new_str = "".join(rev_element)
    print(new_str)


