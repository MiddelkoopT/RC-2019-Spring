#!/usr/bin/python3

import matplotlib.pyplot as plt
import pandas
import numpy

ts = pandas.Series(numpy.random.randn(1000),
                   pandas.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()

