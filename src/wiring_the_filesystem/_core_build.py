from pathlib import Path

from cffi import FFI

ffi = FFI()
ffi.cdef(
    """
    char* compute(int argv, char *argv[]);
    """
)


ffi.set_source(
    "wiring_the_filesystem._core",
    Path(__file__).parent.joinpath("_core.c").read_text(),
)

if __name__ == "__main__":
    ffi.compile()
