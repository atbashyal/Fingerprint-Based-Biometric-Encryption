# extract minutiae feature
def extract_minutiae(image:np.ndarray, n_features:int = 80) -> np.ndarray:
"""extract minutiae features of a finger print.
finally select the first n features that model builed on.
Args:
image (np.ndarray): image input
n_features (int) : number of requeired features
return:
(np.ndarray): extraced features
"""
FeaturesTerminations, FeaturesBifurcations = fingerprint_feature_extractor.extract_minutiae_features(image, spuriousMinutiaeThresh=10, invertImage=True)
feature_list = []

for minutiea_feature in (FeaturesBifurcations, FeaturesTerminations):
    for featuer in minutiea_feature:
        if featuer.Type == 'Bifurcation':
            feature_type = 1
        else:
            feature_type = 0
        feature_list.append([featuer.locX, featuer.locY, feature_type, featuer.Orientation[0]])
        # select first n features
        if len(feature_list) < n_features:
            # zero pad to meen n_features requiement
            for _ in range(len(feature_list),n_features):
                feature_list.append([0,0,0,0])
            else:
                feature_list = feature_list[:n_features]
        return np.array(feature_list)