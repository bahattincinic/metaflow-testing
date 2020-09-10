import os
import sys
import unittest


if os.getcwd() not in sys.path:
    sys.path.insert(0, os.getcwd())


if __name__ == '__main__':
    unittest.main(module='cases', argv=sys.argv[:1])
