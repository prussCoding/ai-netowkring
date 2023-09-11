import numpy as np
import logging
from sklearn.utils import resample

logging.basicConfig(format='%(levelname)s %(message)s - (Line no: %(lineno)d)', level=logging.DEBUG)

def collect_network_data(mean: int = 100, standard_deviation: int = 20, size: int = 1000):
    return np.random.normal(mean, standard_deviation, size).reshape(-1, 1)

network_data = collect_network_data()


# Balance the dataset by oversampling the minority class

X = np.array([[1., 0.], [2., 1.], [0., 0.]])
y = np.array([0, 1, 2])

from scipy.sparse import coo_matrix
X_sparse = coo_matrix(X)
print('X_Sparse\n',X_sparse)
#logging.info(f'X-Sparse: {X_sparse}')

X, X_sparse, y = resample(X, X_sparse, y, random_state=0)
print('X (resample)\n', X)
print('X_Spare (resample)\n', X_sparse)
print('Y (resample)\n', y)
#logging.info(f'Resample: [X: {X}] [X_spare: {X_sparse}] [y: {y}]')


#balanced_data = resample(imbalanced_data, replace=True, n_samples=len(majority_class_data))

