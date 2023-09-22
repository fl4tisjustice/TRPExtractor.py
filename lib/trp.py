from dataclasses import dataclass
import typing

from lib.trp_structure import TRPHeader, TRPEntry
from lib.trp_parser import TRPParser

class TRP:
    def __init__(self, parser: TRPParser):
        self.parser = parser
        self.header: TRPHeader = TRPHeader(
            self.parser.read_uint32(),
            self.parser.read_uint32(),
            self.parser.read_uint64(),
            self.parser.read_uint32(),
            self.parser.read_uint32(),
            self.parser.read_uint32(),
        )
        self.parser.skip(36)

        self.entries: list[TRPEntry] = []
        
        for _ in range(self.header.file_count):
            self.entries.append(TRPEntry(
                self.parser.read_entry_name(),
                self.parser.read_uint64(),
                self.parser.read_uint64()
            ))
            self.parser.skip(self.header.entry_size - 48)
        