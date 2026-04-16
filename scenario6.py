def weighted_accuracy(y_true, y_pred):
    score = 0
    total_weight = 0

    for actual, predicted in zip(y_true, y_pred):
        weight = 1 if actual == 0 else 2
        total_weight += weight

        if actual == predicted:
            score += weight

    return score / total_weight


y_true = [0, 1, 1, 0, 1]
y_pred = [0, 1, 0, 0, 1]

result = weighted_accuracy(y_true, y_pred)
print("Weighted Accuracy:", result)