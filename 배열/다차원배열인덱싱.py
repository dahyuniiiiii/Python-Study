import numpy as np
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(repr(a))
print(repr(a[:, [True, False, False, True]]))
print(repr(a[[2, 0, 1], :]))