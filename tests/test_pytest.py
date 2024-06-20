# Sanity checks

def test_always_passes():
    assert True

import numpy
def test_import_numpy():
    import numpy as np
    a = [1, 2, 3]
    an = np.array(a)
    return True

# def test_always_fails():
#     assert False