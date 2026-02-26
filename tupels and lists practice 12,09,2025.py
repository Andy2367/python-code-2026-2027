'''
12/09/2025
andy cowie
notes tuples and lists practice
'''
# non messy data
text = "hello my name is jeff pleas don't be a person and be like matteo"

parts = text.split(" ")  # splits part at spaces
tuple_text = tuple(parts) # puts parts in to a tuple

print (tuple_text) # prints the tuple


# messy data

text2 = "jhon  ,. 23 / london!!! )jeff + lain = 123456789'10"

clean_text = text2.replace(".", ",").replace("/", ",").replace("(", ",").replace("!!!", ",").replace("+", ",").replace("=", ",").replace("'", ",").replace(" ", "") # replaces all funky symbles with coma
split = clean_text.split(",")
tupled = tuple(split)
print (tupled)