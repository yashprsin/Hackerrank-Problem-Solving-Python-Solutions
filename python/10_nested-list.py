if __name__ == '__main__':
    python_students = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])
    
    second_postion = sorted(set(s for n,s in python_students))[1]
    print('\n'.join(sorted(n for n,s in python_students if s == second_postion)))