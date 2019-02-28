# Feature Normalization


def featureNormalize(X):
    """
    Normalizes the features in X. returns a normalized version of X where
    the mean value of each feature is 0 and the standard deviation
    is 1. This is often a good preprocessing step to do when working with
    learning algorithms.

    Parameters
    ----------
    X : array_like
        The dataset of shape (m x n).

    Returns
    -------
    X_norm : array_like
        The normalized dataset of shape (m x n).

    Instructions
    ------------
    First, for each feature dimension, compute the mean of the feature
    and subtract it from the dataset, storing the mean value in mu.
    Next, compute the  standard deviation of each feature and divide
    each feature by it's standard deviation, storing the standard deviation
    in sigma.

    Note that X is a matrix where each column is a feature and each row is
    an example. You need to perform the normalization separately for each feature.

    Hint
    ----
    You might find the 'np.mean' and 'np.std' functions useful.
    """
    # You need to set these values correctly
    X_norm = X.copy()
    mu = np.zeros(X.shape[1])
    sigma = np.zeros(X.shape[1])

    features = X.shape[1]
    for feature in range(features):
        mu[feature] = np.mean(X[:, feature])
        sigma[feature] = np.std(X[:, feature])
        X_norm[:, feature] = (X[:, feature] - mu[feature]) / sigma[feature]
    return X_norm, mu, sigma


X_norm, mu, sigma = featureNormalize(housing_data)

print('Computed mean:', mu)
print('Computed standard deviation:', sigma)

# now we add the intercept term to housing_data
housing_data = np.concatenate([np.ones((data_length, 1)), X_norm], axis=1)  # adds row of 1s to first column of X_norm