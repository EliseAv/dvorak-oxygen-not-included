#!/bin/env python3

import pathlib

def main():
    converter = dict(zip(
        "-=qwertyuiop[]asdfghjkl;'zxcvbnm,./",
        "[]',.pyfgcrl/=aoeuidhtns-;qjkxbmwvz"))
    here = pathlib.Path(__file__).resolve().parent
    in_path = here / 'oni-qwerty.txt'
    out_path = here / 'oni-dvorak.txt'
    with in_path.open() as in_file, out_path.open('w') as out_file:
        for line in in_file:
            first = line[0]
            first = converter.get(first, first)
            out_file.write(first + line[1:])

if __name__ == '__main__':
    main()
