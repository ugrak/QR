#!/usr/bin/env python3

from PIL import Image
import sys


def from_pixels(pixels_name, out_name, size):
    im = Image.new("RGBA", size)

    with open(pixels_name, "r") as fin:
        tup = []
        data = fin.read().split()
        tmp = []
        for raw in data:
            if raw == '1': out = 0x00
            else: out = 0xff
            tup.append((out, out, out, 255))
            raw = fin.read(1)

        im.putdata(tup)

    im.save(out_name)


def usage():
    print(f"Usage: {sys.argv[0]} <pixels_file> <image_width> <image_height>")
    exit(1)


def main ():
    if len(sys.argv) != 4:
        usage()

    pixels_name = sys.argv[1]

    from_pixels(pixels_name, pixels_name+'.png', (int(sys.argv[2]), int(sys.argv[3])))


if __name__ == "__main__":
    main()

    #TODO: automated crypt/decrypt script
