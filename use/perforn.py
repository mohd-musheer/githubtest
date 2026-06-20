from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from test.operations import sum2, sub2

def opr():
    assert sum2(10,2)==12
    assert sum2(-4,-3)==-7
    assert sub2(1,4)==-3
    assert sub2(5,-5)==10
    
    
opr()