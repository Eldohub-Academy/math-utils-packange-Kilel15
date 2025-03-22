# Description: This script runs all tests in the `tests` directory.
import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover("tests")

    runner = unittest.TextTestRunner()
    runner.run(suite)
