import pandas as pd
import numpy as np


def calculate_topsis(input_file, weights, impacts, output_file):

    df = pd.read_csv(input_file)

    if df.shape[1] < 3:
        raise Exception("Input file must contain at least 3 columns")

    data = df.iloc[:, 1:].values.astype(float)

    weights = np.array(weights)
    impacts = np.array(impacts)

    if len(weights) != data.shape[1]:
        raise Exception("Weights length must match number of criteria")

    if len(impacts) != data.shape[1]:
        raise Exception("Impacts length must match number of criteria")

    # Step 1: Normalize
    norm = data / np.sqrt((data ** 2).sum(axis=0))

    # Step 2: Weighted matrix
    weighted = norm * weights

    # Step 3: Ideal best and worst
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(max(weighted[:, i]))
            ideal_worst.append(min(weighted[:, i]))
        else:
            ideal_best.append(min(weighted[:, i]))
            ideal_worst.append(max(weighted[:, i]))

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Step 4: Distance
    s_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    s_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Score
    score = s_worst / (s_best + s_worst)

    df['Topsis Score'] = score
    df['Rank'] = score.argsort()[::-1] + 1

    df.to_csv(output_file, index=False)
