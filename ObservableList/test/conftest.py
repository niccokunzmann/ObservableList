"""Configure the test environment."""

import sys
import os

HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(HERE, "..", ".."))

if sys.version_info[0] == 2:
    import mock
    sys.modules["unittest.mock"] = mock
