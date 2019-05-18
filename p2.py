if __name__ == "__main__":
    integer = int(input())
    tc = 0
    for i in range(1, integer + 1):
        if i % 15 == 0:
            tc += 1
        elif i % 3 == 0:
            pass
        elif i % 5 == 0:
            pass
        else:
            tc += 1
    print(tc)            
