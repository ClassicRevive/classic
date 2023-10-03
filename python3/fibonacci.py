

''' Check if the inputted number is part of fibonacci sequence '''

num = int(input())

fib = [0, 1]

if num == 0:  # edge case
    print('yes')
else:
    i = 1
    newfib = 0
    while newfib < num:  # keep adding newfibs until we reach or exceed the number we're searching for
        newfib = fib[i] + fib[i - 1]
        fib.append(newfib)

        i += 1

    # if the last number in the list = num, then num is in fibonacci sequence
    if fib[-1] == num:
        print('yes')
    else:
        print('no')
