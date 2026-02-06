import os
import sys

# Ensure project root (one level above tests/) is on sys.path so tests
# can import project modules like `skills` and `trend_fetcher`.
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
