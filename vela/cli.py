import argparse
from vela.core import clone_repository


def main():
    parser = argparse.ArgumentParser(description="Vela - Coding Assistant")
    parser.add_argument('-r', '--repo', type=str, help='Clone GitHub repository')

    args = parser.parse_args()

    if args.repo:
        clone_repository(args.repo)


if __name__ == "__main__":
    main()