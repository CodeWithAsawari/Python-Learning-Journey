NUMPY Functions
1.import numpy as np
2. a = np.array([10, 20, 30, 40])
Ans:[10, 20, 30, 40]
b = np.array([[1,2,3],[4,5,6]])
Ans:[[1 2 3]
[4 5 6]]
3. np.asarray(a)
Ans: array([10, 20, 30, 40])
np.copy(a)
Ans: array([10, 20, 30, 40])
4.
np.zeros((3,3))
Ans: array([[0., 0., 0.],
[0., 0., 0.],
[0., 0., 0.]])
np.ones((2,4))
Ans: array([[1., 1., 1., 1.],
[1., 1., 1., 1.]])
np.empty((2,2))
Ans: array([[2.21353023e-307, 1.75600414e-307],
[1.34609567e-285,             nan]])
5. np.eye(3)
Ans: array([[1., 0., 0.],
[0., 1., 0.],
[0., 0., 1.]])
np.identity(3)
Ans: array([[1., 0., 0.],
[0., 1., 0.],
[0., 0., 1.]])
np.diag([1,2,3])
Ans: array([[1, 0, 0],
[0, 2, 0],
[0, 0, 3]])
6. np.arange(1, 10, 2)
Ans: array([1, 3, 5, 7, 9])
np.linspace(1, 10, 5)
Ans: array([ 1.  ,  3.25,  5.5 ,  7.75, 10.  ])
np.logspace(1, 3, 3)
Ans. array([  10.,  100., 1000.])
RANDOM FUNCTIONS (WITH EXAMPLES)
1. np.random.rand(3,3)
Ans:  array([[0.79649766, 0.96553889, 0.61855298],
[0.31858671, 0.21239574, 0.16447353],
[0.60365648, 0.48378964, 0.34381447]])
np.random.randn(3)
Ans: array([ 0.1043994 ,  0.82613524, -0.79708137])
np.random.randint(1, 100, 5)
Ans: array([39, 81, 14, 70,  9])
np.random.uniform(10, 20, 5)
Ans: array([19.6472757 , 10.50442707, 16.49241649, 18.49984797,
16.4463382 ])
np.random.normal(50, 10, 5)
Ans: array([44.01063346, 67.14289209, 43.96731533, 51.21958176,
59.94161139])
2. arr = np.array([1,2,3,4,5])
Ans: [1 2 3 4 5]
np.random.shuffle(arr)
Ans: [3 1 5 2 4]
np.random.choice(arr, 3)
Ans: array([3, 1, 5])
ARRAY ATTRIBUTES
arr = np.array([[1,2,3],[4,5,6]])
Ans: [[1 2 3]
[4 5 6]]
arr.ndim
Ans: 2
arr.shape
Ans: (2, 3)
arr.size
Ans: 6
arr.dtype
Ans: dtype(‘int32’)
arr.itemsize
Ans: 4
arr.nbytes
Ans: 24
arr.T
Ans: array([[1, 4],
[2, 5],
[3, 6]])
RESHAPING & STRUCTURE
1. a = np.array([1,2,3,4,5,6])
Ans: [1 2 3 4 5 6]
a.reshape(2,3)
Ans: array([[1, 2, 3],
[4, 5, 6]])
np.reshape(a, (3,2))
Ans: array([[1, 2],
[3, 4],
[5, 6]])
np.ravel(a)
Ans: array([1, 2, 3, 4, 5, 6])
a.flatten()
Ans: array([1, 2, 3, 4, 5, 6])
b. np.expand_dims(a, axis=1)
Ans:  array([[1],
[2],
[3],
[4],
[5],
[6]])
np.squeeze(np.array([[[5]]]))
Ans: array(5)
x = np.array([1,2])
y = np.array([3,4])
[1 2]
[3 4]
np.hstack((x,y))
array([1, 2, 3, 4])
np.vstack((x,y))
array([[1, 2],
[3, 4]])
np.concatenate((x,y))
array([1, 2, 3, 4])
INDEXING & SELECTION
a = np.array([10,20,30,40,50])
[10 20 30 40 50]
a[0]
Ans: np.int32(10)
a[1:4]
Ans: array([20, 30, 40])
a[a > 25]
Ans: array([30, 40, 50])
np.where(a > 25)
Ans: (array([2, 3, 4]),)
np.take(a, [0,2,4])
Ans: array([10, 30, 50])
np.nonzero(a)
Ans: (array([0, 1, 2, 3, 4]),)
ARITHMETIC OPERATIONS
a = np.array([10,20,30])
b = np.array([2,4,6])
np.add(a,b)
Ans: array([12, 24, 36])
np.subtract(a,b)
Ans: array([ 8, 16, 24])
np.multiply(a,b)
Ans: array([ 20,  80, 180])
np.divide(a,b)
Ans: array([5., 5., 5.])
np.power(a,2)
Ans: array([100, 400, 900], dtype=int32)
Ans:
np.abs([-1,-5,6])
Ans: array([1, 5, 6])
ROUNDING FUNCTIONS
a = np.array([1.2, 2.7, 3.5])
np.round(a)
array([1., 3., 4.])
np.floor(a)
array([1., 2., 3.])
np.ceil(a)
array([2., 3., 4.])
np.trunc(a)
array([1., 2., 3.])
STATISTICAL FUNCTIONS
marks = np.array([78,65,90,55,82])
np.mean(marks)
np.float64(74.0)
np.median(marks)
np.float64(78.0)
np.average(marks)
np.float64(74.0)
np.std(marks)
np.float64(12.47397290361014)
np.var(marks)
np.float64(155.6)
np.min(marks)
np.int32(55)
np.max(marks)
np.int32(90)
np.argmin(marks)
np.int32(3)
np.argmax(marks)
np.int32(2)
np.sum(marks)
np.int32(370)
np.cumsum(marks)
array([ 78, 143, 233, 288, 370])
np.cumprod(marks)
array([ 78, 143, 233, 288, 370])
np.percentile(marks, 50)
np.float64(78.0)
np.quantile(marks, 0.75)
np.float64(82.0)
np.ptp(marks)
np.int32(35)
LOG & EXP FUNCTIONS
a = np.array([1,2,3])
np.exp(a)
array([ 2.71828183,  7.3890561 , 20.08553692])
np.log(a)
array([0.        , 0.69314718, 1.09861229])
np.log10(a)
array([0.        , 0.30103   , 0.47712125])
np.log2(a)
array([0.       , 1.       , 1.5849625])
LOGICAL & BOOLEAN
a = np.array([True, False, True])
b = np.array([False, False, True])
np.logical_and(a,b)
array([False, False,  True])
np.logical_or(a,b)
array([ True, False,  True])
np.logical_not(a)
array([False,  True, False])
SORTING & SEARCHING
a = np.array([40,10,30,20])
np.sort(a)
array([10, 20, 30, 40])
SET OPERATIONS
a = np.array([1,2,3,4])
b = np.array([3,4,5,6])
np.unique(a)
array([1, 2, 3, 4])
np.intersect1d(a,b)
array([3, 4])
np.union1d(a,b)
array([1, 2, 3, 4, 5, 6])
np.setdiff1d(a,b)
array([1, 2])
np.isin(a,b)
array([False, False,  True,  True])
TYPE CASTING
a = np.array([1.5, 2.7, 3.9])
a.astype(int)
array([1, 2, 3])
a.astype(float)
array([1.5, 2.7, 3.9])