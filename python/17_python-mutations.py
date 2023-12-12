def mutate_string(string, position, character):
    ls_s = list(string)
    res = ls_s.pop(position)
    ls_s.insert(position,character)
    li = ''.join(ls_s)
    return li

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)