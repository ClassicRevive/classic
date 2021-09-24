import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=1)
    model.fit(train_X, train_y)
    pred_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, pred_val)
    return mae

candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]

error = []
# Write loop to find the ideal tree size from candidate_max_leaf_nodes
for size in candidate_max_leaf_nodes:
    error.append(get_mae(size, train_X, val_X, train_y, val_y))
    
print(error)
fig, ax = plt.subplots()
majors = [0, 1, 2, 3, 4, 5]
ax.xaxis.set_major_locator(ticker.FixedLocator(majors))
ax.set_xticklabels(candidate_max_leaf_nodes)

ax.plot(error)