lookup = {
    255: 1,
    0: 0,
    15: -2
}

from PIL import Image
import sys, os
if sys.argv[1] == "h" or sys.argv[1] == "help":
    print("USE python3 LevelGen.py <path to file>")
    quit()
im = Image.open(sys.argv[1])
px = im.load()
out = [0,[]]
for col in range(im.size[0]):
    for row in range(im.size[1]):
        out[1].append(lookup[px[row, col][0]])
    out[1].append(-1)
out[0] = len(out[1])
out = str(out)
out = out.replace('[', '{')
out = out.replace(']', '}')
print(out)