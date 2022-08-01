# STR-PARSE-TOOLS

This is a set of string parsing tools for python.

The following parsing elements are currently supported:

- String of timedelta to timedelta
- String of bytes size to float
- Variable names are converted between camel and pythonic

## Install

```bash
pip install strparsetools
```

## Example

### String to timedelta

```python
from strparsetools import string2timedelta

string2timedelta("1w2days1h1Minutes1s")
> timedelta(days=9, hours=1, minutes=1, seconds=1)

# ------------------------------------------------

```

### String of bytes size to float

```python
from strparsetools import datasize2float

datasize2float("1G2Mb3k4")
> float(1075842052.0)
```

### Variable names are converted between camel and pythonic

```python
from strparsetools import camel, recamel

camel("parse_tools")
> "parseTools"

recamel("parseTools")
> "parse_tools"
```

