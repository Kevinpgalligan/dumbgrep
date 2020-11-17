import argparse
import sys
import re

def main():
    parser = argparse.ArgumentParser(description="A replacement for grep.")
    parser.add_argument("pattern", type=str, help="the pattern to search for")
    args = parser.parse_args()
    regex = re.compile(args.pattern)
    for line in sys.stdin:
        if regex.search(line):
            sys.stdout.write(line)

if __name__ == "__main__":
    main()
