# Copyright (c) 2013 by Gilbert Ramirez <gram@alumni.rice.edu>

from dftestlib import dftest

class testTime(dftest.DFTest):
    trace_file = "http.cap"

    def test_eq_1(self):
        dfilter = 'frame.time == "Dec 31, 2002 07:55:31.3"'
        self.assertDFilterCount(dfilter, 1)

    def test_eq_2(self):
        dfilter = 'frame.time == "Jan 31, 2002 07:55:31.3"'
        self.assertDFilterCount(dfilter, 0)

    def test_ne_1(self):
        dfilter = 'frame.time != "Dec 31, 2002 07:55:31.3"'
        self.assertDFilterCount(dfilter, 0)

    def test_ne_2(self):
        dfilter = 'frame.time != "Jan 31, 2002 07:55:31.3"'
        self.assertDFilterCount(dfilter, 1)

    def test_gt_1(self):
        dfilter = 'frame.time > "Dec 31, 2002 07:54:31.3"'
        self.assertDFilterCount(dfilter, 1)

    def test_gt_2(self):
        dfilter = 'frame.time > "Dec 31, 2002 07:55:31.3"'
        self.assertDFilterCount(dfilter, 0)

    def test_gt_3(self):
        dfilter = 'frame.time > "Dec 31, 2002 07:56:31.3"'
        self.assertDFilterCount(dfilter, 0)

    def test_ge_1(self):
        dfilter = 'frame.time >= "Dec 31, 2002 07:54:31.3"'
        self.assertDFilterCount(dfilter, 1)

    def test_ge_2(self):
        dfilter = 'frame.time >= "Dec 31, 2002 07:55:31.3"'
        self.assertDFilterCount(dfilter, 1)

    def test_ge_3(self):
        dfilter = 'frame.time >= "Dec 31, 2002 07:56:31.3"'
        self.assertDFilterCount(dfilter, 0)

    def test_lt_1(self):
        dfilter = 'frame.time < "Dec 31, 2002 07:54:31.3"'
        self.assertDFilterCount(dfilter, 0)

    def test_lt_2(self):
        dfilter = 'frame.time < "Dec 31, 2002 07:55:31.3"'
        self.assertDFilterCount(dfilter, 0)

    def test_lt_3(self):
        dfilter = 'frame.time < "Dec 31, 2002 07:56:31.3"'
        self.assertDFilterCount(dfilter, 1)

    def test_le_1(self):
        dfilter = 'frame.time <= "Dec 31, 2002 07:54:31.3"'
        self.assertDFilterCount(dfilter, 0)

    def test_le_2(self):
        dfilter = 'frame.time <= "Dec 31, 2002 07:55:31.3"'
        self.assertDFilterCount(dfilter, 1)

    def test_le_3(self):
        dfilter = 'frame.time <= "Dec 31, 2002 07:56:31.3"'
        self.assertDFilterCount(dfilter, 1)

