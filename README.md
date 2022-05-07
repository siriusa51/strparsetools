# STR-PARSE-TOOLS

This is a set of string parsing tools for python.



The following parsing elements are currently supported:

- String of timedelta to timedelta
- String of data size to float

## Install

```bash
pip install strparsetools
```

## Example

```python
from strparsetools import string2timedelta, datasize2float

value = string2timedelta("1w2days1h1Minutes1s")
print(value)

> timedelta(days=9, hours=1, minutes=1, seconds=1)

# ------------------------------------------------

value = datasize2float("1G2Mb3k4")
print(value)

> float(1075842052.0)
```

