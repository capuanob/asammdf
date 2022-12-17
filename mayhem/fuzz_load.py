#! /usr/bin/env python3
import atheris
import sys
import fuzz_helpers
from struct import error
from asammdf.blocks.utils import MdfException

with atheris.instrument_imports():
    import asammdf

@atheris.instrument_func
def TestOneInput(data):
    if len(data) < 10:
        return -1

    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        with fdp.ConsumeMemoryFile(all_data=True, as_bytes=True) as f:
            f.name = 'fuzz'
            with asammdf.MDF(f) as mdf:
                for i, group in enumerate(mdf.groups):
                    pass
            mdf.scramble('test')
    except (MdfException, error, UnicodeDecodeError) as e:
        return -1
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
