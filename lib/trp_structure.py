from dataclasses import dataclass
import typing

MAGIC: int = 0xDCA24D00

# https://www.psdevwiki.com/ps3/TROPHY.TRP

@dataclass
class TRPHeader:
    magic: int
    version: int
    file_size: int
    file_count: int
    entry_size: int
    dev_flag: int

    def __post_init__(self):
        try:
            assert self.magic == MAGIC
        except AssertionError:
            print(f"[ERROR] Wrong magic value: {self.magic:X}")
            exit(1)

@dataclass
class TRPEntry:
    name: str
    offset: int
    size: int
