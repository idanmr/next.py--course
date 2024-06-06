import functools
#1
with open('names.txt', 'r') as f:
    print(max(f.readlines(), key=len))
    #or
    print(sorted([line.strip() for line in f], key=len)[-1:])


#2
with open('names.txt', 'r') as f:
    print(sum(len(word) for word in f.read().split()))

#3
with open('names.txt', 'r') as f:
    lines = [line.strip() for line in f]
    min_len = min(len(line) for line in lines)
    print('\n'.join(line for line in lines if len(line) == min_len))

#4
with open('names.txt', 'r') as f:
    with open('name_length.txt', 'w') as output_file:
        output_file.write('\n'.join(map(str, map(len, f.read().split()))))
#with open('name_length.txt', 'r') as file:
    #print(file.read())

#5

name_length = int(input("Enter name length: "))
with open('names.txt', 'r') as f:
    print('\n'.join(line for line in [line.strip() for line in f] if len(line) == name_length))
