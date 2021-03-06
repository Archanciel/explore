import unittest
import sys
from io import StringIO

from pandas_average_rate_explore import *

class MyTestCase(unittest.TestCase):
    def test_func_computeDataFrameAmounts_SELL_ALL_DEPOSIT_SELL_ALL_YIELD(self):
        stdout = sys.stdout
        capturedStdoutStr = StringIO()
        sys.stdout = capturedStdoutStr

        droppedColLst = [REALIZED_CAP_GAIN_PERCENT,
                         POTENTIAL_CAP_GAIN_PERCENT]

        computeDataFrameAmounts(SELL_ALL_DEPOSIT_SELL_ALL_YIELD, droppedColLst)

        sys.stdout = stdout

        expectedOutputStr = \
'''

SELL_ALL_DEPOSIT_SELL_ALL_YIELD

       CHSB  AT DF RT  AVG RT  AT CUR RT  Y CHSB  Y CUR RATE  REALI CAP G  POT CAP G
0  10000.00   5000.00     0.0        0.0  155.26         0.0          0.0        0.0
1  10000.00  10000.00     0.0        0.0  163.82         0.0          0.0        0.0
2   1000.00   2000.00     0.0        0.0  167.66         0.0          0.0        0.0
3   -500.00   -500.00     0.0        0.0  170.62         0.0          0.0        0.0
4   -500.00  -1000.00     0.0        0.0  162.54         0.0          0.0        0.0
5   1000.00    800.00     0.0        0.0  712.55         0.0          0.0        0.0
6 -22532.55 -27039.06     0.0        0.0    0.10         0.0          0.0        0.0
       CHSB  AT DF RT    AVG RT  AT CUR RT  Y CHSB  Y CUR RATE   REALI CAP G     POT CAP G
0  10000.00   5000.00  0.500000  15000.000  155.26     232.890      0.000000  10232.890000
1  10000.00  10000.00  0.750000  15000.000  163.82     245.730      0.000000  15478.620000
2   1000.00   2000.00  0.809524   1500.000  167.66     251.490      0.000000  15230.110000
3   -500.00   -500.00  0.809524   -750.000  170.62     255.930     95.238095  15140.801905
4   -500.00  -1000.00  0.809524   -750.000  162.54     243.810    595.238095  15039.373810
5   1000.00    800.00  0.809070   1500.000  712.55    1068.825      0.000000  16808.198810
6 -22532.55 -27039.06  0.809070 -33798.825    0.10       0.150  10048.583810      0.000000
'''
        self.maxDiff = None
        self.assertEqual(expectedOutputStr, capturedStdoutStr.getvalue())

    def test_func_computeDataFrameAmounts_SELL_ALL_DEPOSIT_SELL_ALL_MINUS_ONE_YIELD(self):
        stdout = sys.stdout
        capturedStdoutStr = StringIO()
        sys.stdout = capturedStdoutStr

        droppedColLst = [REALIZED_CAP_GAIN_PERCENT,
                         POTENTIAL_CAP_GAIN_PERCENT]

        computeDataFrameAmounts(SELL_ALL_DEPOSIT_SELL_ALL_MINUS_ONE_YIELD, droppedColLst)

        sys.stdout = stdout

        expectedOutputStr = \
'''

SELL_ALL_DEPOSIT_SELL_ALL_MINUS_ONE_YIELD

       CHSB  AT DF RT  AVG RT  AT CUR RT  Y CHSB  Y CUR RATE  REALI CAP G  POT CAP G
0  10000.00   5000.00     0.0        0.0  155.26         0.0          0.0        0.0
1  10000.00  10000.00     0.0        0.0  163.82         0.0          0.0        0.0
2   1000.00   2000.00     0.0        0.0  167.66         0.0          0.0        0.0
3   -500.00   -500.00     0.0        0.0  170.62         0.0          0.0        0.0
4   -500.00  -1000.00     0.0        0.0  162.54         0.0          0.0        0.0
5   1000.00    800.00     0.0        0.0  712.55         0.0          0.0        0.0
6 -22531.55 -27037.86     0.0        0.0    0.10         0.0          0.0        0.0
       CHSB  AT DF RT    AVG RT  AT CUR RT  Y CHSB  Y CUR RATE   REALI CAP G     POT CAP G
0  10000.00   5000.00  0.500000  15000.000  155.26     232.890      0.000000  10232.890000
1  10000.00  10000.00  0.750000  15000.000  163.82     245.730      0.000000  15478.620000
2   1000.00   2000.00  0.809524   1500.000  167.66     251.490      0.000000  15230.110000
3   -500.00   -500.00  0.809524   -750.000  170.62     255.930     95.238095  15140.801905
4   -500.00  -1000.00  0.809524   -750.000  162.54     243.810    595.238095  15039.373810
5   1000.00    800.00  0.809070   1500.000  712.55    1068.825      0.000000  16808.198810
6 -22531.55 -27037.86  0.809070 -33797.325    0.10       0.150  10047.383810      1.500000
'''
        self.maxDiff = None
        self.assertEqual(expectedOutputStr, capturedStdoutStr.getvalue())

    def test_to_func_computeDataFrameAmounts_SELL_ALL_DEPOSIT_SELL_1000_YIELDS(self):
        stdout = sys.stdout
        capturedStdoutStr = StringIO()
        sys.stdout = capturedStdoutStr

        droppedColLst = [REALIZED_CAP_GAIN_PERCENT,
                         POTENTIAL_CAP_GAIN_PERCENT]

        computeDataFrameAmounts(SELL_ALL_DEPOSIT_SELL_1000_YIELDS, droppedColLst)

        sys.stdout = stdout

        expectedOutputStr = \
'''

SELL_ALL_DEPOSIT_SELL_1000_YIELDS

      CHSB  AT DF RT  AVG RT  AT CUR RT  Y CHSB  Y CUR RATE  REALI CAP G  POT CAP G
0  10000.0    5000.0     0.0        0.0  155.26         0.0          0.0        0.0
1  10000.0   10000.0     0.0        0.0  163.82         0.0          0.0        0.0
2   1000.0    2000.0     0.0        0.0  167.66         0.0          0.0        0.0
3   -500.0    -500.0     0.0        0.0  170.62         0.0          0.0        0.0
4   -500.0   -1000.0     0.0        0.0  162.54         0.0          0.0        0.0
5   1000.0     800.0     0.0        0.0  712.55         0.0          0.0        0.0
6 -22000.0  -26400.0     0.0        0.0    0.10         0.0          0.0        0.0
      CHSB  AT DF RT    AVG RT  AT CUR RT  Y CHSB  Y CUR RATE  REALI CAP G     POT CAP G
0  10000.0    5000.0  0.500000    15000.0  155.26     232.890     0.000000  10232.890000
1  10000.0   10000.0  0.750000    15000.0  163.82     245.730     0.000000  15478.620000
2   1000.0    2000.0  0.809524     1500.0  167.66     251.490     0.000000  15230.110000
3   -500.0    -500.0  0.809524     -750.0  170.62     255.930    95.238095  15140.801905
4   -500.0   -1000.0  0.809524     -750.0  162.54     243.810   595.238095  15039.373810
5   1000.0     800.0  0.809070     1500.0  712.55    1068.825     0.000000  16808.198810
6 -22000.0  -26400.0  0.809070   -33000.0    0.10       0.150  9409.523810    798.825000
'''
        self.maxDiff = None
        self.assertEqual(expectedOutputStr, capturedStdoutStr.getvalue())

    def test_to_func_computeDataFrameAmounts_SELL_ALL_DEPOSIT_SELL_ONLY_ONE_YIELD(self):
        stdout = sys.stdout
        capturedStdoutStr = StringIO()
        sys.stdout = capturedStdoutStr

        droppedColLst = [REALIZED_CAP_GAIN_PERCENT,
                         POTENTIAL_CAP_GAIN_PERCENT]

        computeDataFrameAmounts(SELL_ALL_DEPOSIT_SELL_ONLY_ONE_YIELD, droppedColLst)

        sys.stdout = stdout

        expectedOutputStr = \
'''

SELL_ALL_DEPOSIT_SELL_ONLY_ONE_YIELD

      CHSB  AT DF RT  AVG RT  AT CUR RT  Y CHSB  Y CUR RATE  REALI CAP G  POT CAP G
0  10000.0    5000.0     0.0        0.0  155.26         0.0          0.0        0.0
1  10000.0   10000.0     0.0        0.0  163.82         0.0          0.0        0.0
2   1000.0    2000.0     0.0        0.0  167.66         0.0          0.0        0.0
3   -500.0    -500.0     0.0        0.0  170.62         0.0          0.0        0.0
4   -500.0   -1000.0     0.0        0.0  162.54         0.0          0.0        0.0
5   1000.0     800.0     0.0        0.0  712.55         0.0          0.0        0.0
6 -21001.0  -25201.2     0.0        0.0    0.10         0.0          0.0        0.0
      CHSB  AT DF RT    AVG RT  AT CUR RT  Y CHSB  Y CUR RATE  REALI CAP G     POT CAP G
0  10000.0    5000.0  0.500000    15000.0  155.26     232.890     0.000000  10232.890000
1  10000.0   10000.0  0.750000    15000.0  163.82     245.730     0.000000  15478.620000
2   1000.0    2000.0  0.809524     1500.0  167.66     251.490     0.000000  15230.110000
3   -500.0    -500.0  0.809524     -750.0  170.62     255.930    95.238095  15140.801905
4   -500.0   -1000.0  0.809524     -750.0  162.54     243.810   595.238095  15039.373810
5   1000.0     800.0  0.809070     1500.0  712.55    1068.825     0.000000  16808.198810
6 -21001.0  -25201.2  0.809070   -31501.5    0.10       0.150  8210.723810   2297.325000
'''
        self.maxDiff = None
        self.assertEqual(expectedOutputStr, capturedStdoutStr.getvalue())

    def test_to_func_computeDataFrameAmounts_SELL_ALL_DEPOSIT_SELL_NO_YIELD(self):
        stdout = sys.stdout
        capturedStdoutStr = StringIO()
        sys.stdout = capturedStdoutStr

        droppedColLst = [REALIZED_CAP_GAIN_PERCENT,
                         POTENTIAL_CAP_GAIN_PERCENT]

        computeDataFrameAmounts(SELL_ALL_DEPOSIT_SELL_NO_YIELD, droppedColLst)

        sys.stdout = stdout

        expectedOutputStr = \
'''

SELL_ALL_DEPOSIT_SELL_NO_YIELD

      CHSB  AT DF RT  AVG RT  AT CUR RT  Y CHSB  Y CUR RATE  REALI CAP G  POT CAP G
0  10000.0    5000.0     0.0        0.0  155.26         0.0          0.0        0.0
1  10000.0   10000.0     0.0        0.0  163.82         0.0          0.0        0.0
2   1000.0    2000.0     0.0        0.0  167.66         0.0          0.0        0.0
3   -500.0    -500.0     0.0        0.0  170.62         0.0          0.0        0.0
4   -500.0   -1000.0     0.0        0.0  162.54         0.0          0.0        0.0
5   1000.0     800.0     0.0        0.0  712.55         0.0          0.0        0.0
6 -21000.0  -25200.0     0.0        0.0    0.10         0.0          0.0        0.0
      CHSB  AT DF RT    AVG RT  AT CUR RT  Y CHSB  Y CUR RATE  REALI CAP G     POT CAP G
0  10000.0    5000.0  0.500000    15000.0  155.26     232.890     0.000000  10232.890000
1  10000.0   10000.0  0.750000    15000.0  163.82     245.730     0.000000  15478.620000
2   1000.0    2000.0  0.809524     1500.0  167.66     251.490     0.000000  15230.110000
3   -500.0    -500.0  0.809524     -750.0  170.62     255.930    95.238095  15140.801905
4   -500.0   -1000.0  0.809524     -750.0  162.54     243.810   595.238095  15039.373810
5   1000.0     800.0  0.809070     1500.0  712.55    1068.825     0.000000  16808.198810
6 -21000.0  -25200.0  0.809070   -31500.0    0.10       0.150  8209.523810   2298.825000
'''
        self.maxDiff = None
        self.assertEqual(expectedOutputStr, capturedStdoutStr.getvalue())


if __name__ == '__main__':
    unittest.main()
