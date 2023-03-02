def apply_pca(x:np.ndarray, n_components:int = 40)-> np.ndarray:
""" Apply PCA on dataset.
Args:
x (np.ndarray): extracted feature dataset
n_components (int): number of features to select
returns:
(np.ndarray): array of features extracted
"""
# define scaler.
scaler = StandardScaler()
scaled_data = scaler.fit_transform(x)
# define pca object
pca = PCA(n_components = n_components)
x_pca = pca.fit_transform(scaled_data)

return x_pca
