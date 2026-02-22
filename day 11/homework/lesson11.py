                                                       #დავალება 6
def array_plus_array(arr1,arr2):
    return sum(arr1 + arr2)


def area_or_perimeter(l , w):
    if l == w:
        return l * w
    else:
        return (l + w) +  (l + w)


def better_than_average(x, y):
    average = sum(x) / len(x)
    return y > average


def hello(name = ""):
    if not name:
        return "Hello, World!"
    else:
        return f"Hello, {name.capitalize()}!"
    

def vowel_indices(word):
    vowels = "aeiouyAEIOUY"
    result = []
    for i in range(len(word)):
        if word[i]  in vowels :
            result.append(i + 1)
    return result










