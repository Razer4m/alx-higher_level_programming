#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    num_arguments = len(arguments)

    if num_arguments == 0:
        print("0 arguments.")
    else:
        print(num_arguments, end=" ")
        print("argument" if num_arguments == 1 else "arguments", end=":\n")

        for i, arg in enumerate(arguments, start=1):
            print(f"{i}: {arg}")
