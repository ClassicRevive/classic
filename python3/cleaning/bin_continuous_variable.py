
''' 
This is an example of binning continuous data into categories.
I keep this example for use for categorical variable mapping
for classification algo (e.g. Naive Bayes)
'''

# Create ranges for categories
label_ranges = [0, 60, 180, np.inf]
label_names = ['short', 'medium', 'long']

# Create wait_type column
airlines['wait_type'] = pd.cut(airlines['wait_min'], bins = label_ranges, labels = label_names)