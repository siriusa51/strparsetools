from strparsetools import string2timedelta, datasize2float

value = string2timedelta("1w2days1h1Minutes1s")
print(value)

# ------------------------------------------------

value = datasize2float("1G2Mb3k4")
print(value)