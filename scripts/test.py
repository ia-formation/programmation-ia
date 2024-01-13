import traceback
import sys


def mefun(x):
    return len[x]

s = "test"
try:
    mefun(10)
except Exception as e:
    data = traceback.extract_tb(sys.exc_info()[2])
    print(data[-1][-1])
