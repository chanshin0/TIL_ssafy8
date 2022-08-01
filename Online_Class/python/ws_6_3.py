vowels = ['a','e','i','o','u']
def count_vowels(strings):
    count = 0
    for str in strings:
        if str in vowels:
            count += 1
    return count

print(count_vowels('apple')) #=> 2
print(count_vowels('banana')) #=> 3