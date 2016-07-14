import sys

from bitflying.echo import EchoAPIClient


def main(argv=sys.argv[1:]):
    client = EchoAPIClient()
    print(client.price())

if __name__ == '__main__':
    sys.exit(main())
