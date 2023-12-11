if __name__ == '__main__':
    N = int(input())
    List = [];
    for i in range(N):
        qurey = input().split();
        if qurey[0] == 'insert':
            List.insert(int(qurey[1]), int(qurey[2]))
        elif qurey[0] == 'remove':
            List.remove(int(qurey[1]))
        elif qurey[0] == 'append':
            List.append(int(qurey[1]))
        elif qurey[0] == 'print':
            print(List)
        elif qurey[0] == 'sort':
            List.sort();
        elif qurey[0] == 'pop':
            List.pop();
        elif qurey[0] == 'reverse':
            List.reverse();
