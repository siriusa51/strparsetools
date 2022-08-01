from strparsetools import string2timedelta, datasize2float, camel, recamel

value = string2timedelta("1w2days1h1Minutes1s")
print(value)

# ------------------------------------------------

value = datasize2float("1G2Mb3k4")
print(value)

# ------------------------------------------------

value = camel("parse-tools")
print(value)

# ------------------------------------------------

value = recamel("parseTools")
print(value)
