import sys

def read_file_from_stdin():
    print("Reading file content from stdin...")
    content = sys.stdin.read()
    print("File Content:")
    print(content)

if __name__ == "__main__":
    read_file_from_stdin()
