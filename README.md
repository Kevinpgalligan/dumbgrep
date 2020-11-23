## dumbgrep
A Python implementation of grep, which can be used as a template for CLI tools.

Accompanying article: [Recreating grep in Python](https://kevingal.com/blog/cli-tools.html) (working title).

Usage:

```
$ dumbgrep existence </tmp/war-and-peace.txt
in this part of the house and did not even know of the existence of
even wish to know of his existence but would now have been offended
[...]
$ dumbgrep -h
usage: __init__.py [-h] [-v] [--max-count MAX_COUNT] pattern

A replacement for grep.

positional arguments:
  pattern               the pattern to search for

optional arguments:
  -h, --help            show this help message and exit
  -v                    invert matches
  --max-count MAX_COUNT, -m MAX_COUNT
                        max number of matches to print
```

### Installation
Why would you want to do that, you mad, silly person?

Anyway, if you really want to, clone the repository and run `python3 setup.py install`. You can then run dumbgrep from the CLI.
