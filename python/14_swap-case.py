def swap_case(s):
    s1 = s.swapcase()
    return s1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)