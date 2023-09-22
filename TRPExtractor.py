from argparse import ArgumentParser
import os

from lib.trp import TRP
from lib.trp_parser import TRPParser

if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument(metavar="TROPHY.TRP", dest="trp", help="input file")
    arg_parser.add_argument("-o", default="TROPHY_DATA", help="output folder", dest="out", metavar="TROPHY_DATA")
    args = arg_parser.parse_args()

    with open(args.trp, 'rb') as trp:
        trp_bin = trp.read()

    trp = TRP(TRPParser(trp_bin))

    if not os.path.exists(args.out):
         os.mkdir(args.out)

    os.chdir(args.out)

    total_size: int = 0

    for entry in trp.entries:
        print(f"[INFO] Extracting {entry.name}...")
        buffer = trp.parser.read_entry(entry.offset, entry.size)
        with open(entry.name, 'wb') as fd:
            fd.write(buffer)
        total_size += entry.size

    print(f"[INFO] Extracted {total_size / 1_000_000 :0.2f} MB successfully.")