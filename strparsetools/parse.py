import re
from datetime import timedelta
from typing import Union, Optional


__timedelta_pattern__ = re.compile((
    r'((?P<weeks>\d+)w(eeks?)?)?'
    r'((?P<days>\d+)d(ays?)?)?'
    r'((?P<hours>\d+)h(ours?)?)?'
    r'((?P<minutes>\d+)m(inutes?)?)?'
    r'((?P<seconds>\d+)s(econds?)?)?'
    r'((?P<milliseconds>\d+)(ms|milliseconds?))?'
    r'((?P<microseconds>\d+)(us|microseconds?))?'
), re.IGNORECASE)


def string2timedelta(string: Union[str, int, timedelta]) -> Optional[timedelta]:
    """
    Converts a string formatted duration to timedelta.
    Must be entered in order, the order is:
        w[eeks], d[ays], h[ours], m[inutes], [s]econds, [ms|milliseconds], [us|microseconds]

    ps. Case insensitive

    1 = 1s = timedelta(seconds=1)
    1weeks = 1w = timedelta(weeks=1)
    1days = 1d = timedelta(days=1)
    1hours = 1h = timedlta(hours=1)
    1m2s = timedelta(minutes=1, seconds=2)
    ...

    :param string: string to be parsed
    :return: timedelta if match else None
    """
    if isinstance(string, timedelta):
        return string

    if isinstance(string, int):
        return timedelta(seconds=string)

    if string.isdigit():
        string = f"{string}s"

    match = __timedelta_pattern__.fullmatch(string)
    if match:
        parts = {k: int(v) for k, v in match.groupdict().items() if v}
        return timedelta(**parts)

    return None


__unit_pattern__ = re.compile((
    r'((?P<peta>(\d+)(\.\d+)?)pb?)?'
    r'((?P<tera>(\d+)(\.\d+)?)tb?)?'
    r'((?P<giga>(\d+)(\.\d+)?)gb?)?'
    r'((?P<mega>(\d+)(\.\d+)?)mb?)?'
    r'((?P<kilo>(\d+)(\.\d+)?)kb?)?'
    r'((?P<byte>(\d+)(\.\d+)?)(bytes)?)?'
), re.IGNORECASE)

__unit_size__ = {
    "peta": 1024 ** 5,
    "tera": 1024 ** 4,
    "giga": 1024 ** 3,
    "mega": 1024 ** 2,
    "kilo": 1024,
    "byte": 1,
}


def datasize2float(string: Union[int, str]) -> Optional[float]:
    """
    Converts a string formatted datasize to float.
    Must be entered in order, the order is:
        p[b], t[b], g[b], m[b], k[b], [bytes]

    ps. Case insensitive

    1p = 1024 ^ 5 bytes
    1t1.1g = 1TB1.1GB = 1 * 1024 ^ 4 + 1.1 * 1024 ^ 3 bytes
    ...

    :param string: string to be parsed
    :return: float if match else None
    """
    if isinstance(string, int):
        return string

    match = __unit_pattern__.fullmatch(string)
    if match:
        return sum([float(v) * __unit_size__[k] for k, v in match.groupdict().items() if v])

    return None
