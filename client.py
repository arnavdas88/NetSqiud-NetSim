import argparse
from Core.Telnet import Telnet

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='quantum node telnet client')
    parser.add_argument('--host', default=None)
    parser.add_argument('--port', default=None)
    args = parser.parse_args()

    if args.port is None:
        raise Exception("--port is a necessary switch.")
        exit()

    t = None

    if args.host is not None:
        t = Telnet(args.host, args.port)
    else:
        t = Telnet(port = args.port)

    t.client()
