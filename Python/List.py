#hackerrank link - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
if __name__ == '__main__':
    l = []
    N = int(input())
    for i in range(0,N):
        x = input().split() #x = ['remove', 'e']
        if x[0] == 'insert':
            l.insert(int(x[1]),int(x[2]))
        elif x[0] == 'print':
            print(l)
        elif x[0] == 'remove':
            l.remove(int(x[1])) 
        elif x[0] == 'append':
            l.append(int(x[1]))
        elif x[0] == 'sort':
            l.sort()
        elif x[0] == 'pop':
            l.pop()
        elif x[0] == 'reverse':
            l.reverse()