#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    print("{}".format(sum(int(arg) for arg in arguments)))
