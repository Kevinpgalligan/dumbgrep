import argparse
import sys
import re
import math

def main():
    parser = argparse.ArgumentParser(description="A replacement for grep.")
    parser.add_argument("pattern", type=str, help="the pattern to search for")
    parser.add_argument("-v", dest="invert",  default=False, action="store_true", help="invert matches")
    parser.add_argument("--max-count", "-m", type=int, default=math.inf, help="max number of matches to print")
    args = parser.parse_args()
    regex = re.compile(args.pattern)
    matches = 0
    for line in sys.stdin:
        match = regex.search(line)
        if args.invert != bool(match):
            matches += 1
            try:
                sys.stdout.write(highlight(match, line))
            except BrokenPipeError:
                # Next process in pipe isn't accepting input
                # anymore, let's stop.
                break
        if matches >= args.max_count:
            break

def highlight(match, line):
    if not match or not sys.stdout.isatty():
        return line
    return (line[:match.start()]
        + "\033[31m" # change to red
        + line[match.start():match.end()]
        + "\033[0m" # reset
        + line[match.end():])

if __name__ == "__main__":
    main()
