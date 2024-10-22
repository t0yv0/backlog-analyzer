import os
from joblib import Memory

memory = Memory(os.path.expanduser("~/.banal/memory"), verbose=0)
