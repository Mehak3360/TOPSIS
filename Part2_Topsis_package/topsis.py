import pandas as pd
import numpy as np
import sys

def topsis(input_file, weights, impacts, output_file):

    data = pd.read_csv(input_file)

    decision_matrix = data.iloc[:,1:].values.astype(float)

    weights = np.array(weights)
    
    # Normalization
    norm = decision_matrix / np.sqrt((decision_matrix**2).sum(axis=0))

    # Weighted matrix
    weighted = norm * weights

    # Ideal best and worst
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == "+":
            ideal_best.append(max(weighted[:,i]))
            ideal_worst.append(min(weighted[:,i]))
        else:
            ideal_best.append(min(weighted[:,i]))
            ideal_worst.append(max(weighted[:,i]))

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Distance
    dist_best = np.sqrt(((weighted - ideal_best)**2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst)**2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)

    data['Topsis Score'] = score
    data['Rank'] = score.argsort()[::-1] + 1

    data.to_csv(output_file, index=False)


if __name__ == "__main__":
    input_file = sys.argv[1]
    weights = list(map(float, sys.argv[2].split(",")))
    impacts = sys.argv[3].split(",")
    output_file = sys.argv[4]

    topsis(input_file, weights, impacts, output_file)
