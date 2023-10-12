# lambda function examples 

def reverse(s):
    # ::-1 is used to print string in reverse order
    return s[::-1]
reverse("Hello CS")

animals = ["cat", "dog", "hedghog", "rabbit"]

#iterator = map (reverse, animals)

iterator = map(lambda s: s[::-1], animals)

print(list(iterator))