def split_and_join(line):
    # write your code here
    space = ' '
    replace = '-'
    ls = line.strip()
    res = ls.replace(space, replace)
    return res

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)