#!/usr/bin/env python3
import argparse
from .api import crawl


def parse_arguments():
    """ Parse and return command-line arguments.
    :return: An argparse namespace object containing the command-line
    argument values.
    :rtype: argparse.Namespace

    """

    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--domains', nargs='+',
                        help='one or more allowed domains', required=True)

    parser.add_argument('-s', '--start_urls', nargs='+',
                        help='one or more start urls', required=True)

    parser.add_argument('-o', '--outpath', help='directory path for output.',
                        default='./output')

    parser.add_argument('-e', '--extensions', nargs='*',
                        help='one or more document extensions (e.g., ".pdf")')

    parser.add_argument('-t', '--times', nargs='?',
                        help='one or two timestamps in YYYYmmddHHMMSS format')

    args = parser.parse_args()

    return args


if __name__ == "__main__":

    args = parse_arguments()

    if args.extensions is None:
        args.extensions = ['.pdf', '.doc', '.docx']

    if len(args.times) == 1:
        args.times = args.times[0]
    elif len(args.times) > 2:
        raise argparse.ArgumentError("Too many timestamp values")

    crawl(args.domains, args.start_urls,
          args.outpath, args.extensions, args.times)

