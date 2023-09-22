import typing

ENTRY_NAME_MAX_LENGTH: int = 32

class TRPParser:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.pointer: int = 0

    def read_uint32(self) -> int:
        data = int.from_bytes(self.raw_data[self.pointer:self.pointer+4], 'big', signed=False)
        self.pointer += 4
        return data
    
    def read_uint64(self) -> int:
        data = int.from_bytes(self.raw_data[self.pointer:self.pointer+8], 'big', signed=False)
        self.pointer += 8
        return data

    def skip(self, offset: int) -> None:
        self.pointer += offset

    def read_entry_name(self) -> str:
        name = self.raw_data[self.pointer:self.pointer+ENTRY_NAME_MAX_LENGTH].decode('ascii')
        name = name.rstrip('\0')
        self.pointer += ENTRY_NAME_MAX_LENGTH
        return name

    def read_entry(self, offset: int, size: int) -> bytes:
        return self.raw_data[offset:offset+size]