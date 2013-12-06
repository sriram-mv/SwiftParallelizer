import sys
import os

def xauth():
    with open('swift_xauth.conf','r') as swift_open:
        xauth = swift_open.read()
    return xauth

def main():
    xauth()

if __name__ == '__main__':
    main()