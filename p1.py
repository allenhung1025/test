if __name__ == "__main__":
    output = []
    for word in input().split(' '):
        output.append(word[::-1])
    string = ' '.join(output)
    print(string)
