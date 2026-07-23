"""
NexSpace - Entry point.

This file is a thin interface: it imports the nexspace class from
NexCLI.py and starts the CLI. All logic lives in NexCLI.py.
"""

from NexSpace import nexspace


def main():
    Nex = nexspace()
    Nex.start()


if __name__ == "__main__":
    main()
