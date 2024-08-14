import numpy as np
a = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
print(repr(a))
print(repr(a[0, :]))  # 첫번째 행, 모든열
print(repr(a[:, 1]))  # 전체 행, 열 인덱스
print(repr(a[1, 1:]))  # 두번째 행, 두번째 열부터 끝열
print(repr(a[:2, :2])) # 첫번째두번째 행, 첫번째두번째 열