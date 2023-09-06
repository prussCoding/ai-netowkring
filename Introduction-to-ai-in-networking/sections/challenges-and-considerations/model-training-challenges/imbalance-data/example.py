from sklearn.utils import resample

# Balance the dataset by oversampling the minority class
balanced_data = resample(imbalanced_data, replace=True, n_samples=len(majority_class_data))

# Challenge: Network data may be imbalanced, making it difficult to train models 
# effectively.
