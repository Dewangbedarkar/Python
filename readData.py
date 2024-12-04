# import sys
#
# # Read all input from stdin
# input_data = sys.stdin.read()
#
# # Print the content (write to stdout)
# sys.stdout.write(input_data)


import sys


lines_to_write = []
for line in sys.stdin:
    if line.strip().upper() == "STOP":
        break
    lines_to_write.append(line)


sys.stdout.write("".join(lines_to_write))