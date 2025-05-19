def calculate_probabilities(prevalence, sensitivity, specificity):
    p_disease = prevalence
    p_no_disease = 1 - p_disease
    p_pos_given_disease = sensitivity
    p_neg_given_no_disease = specificity
    p_pos_given_no_disease = 1 - specificity
    p_neg_given_disease = 1 - sensitivity

    # P(Disease | Positive Test)
    numerator_pos = p_pos_given_disease * p_disease
    denominator_pos = numerator_pos + p_pos_given_no_disease * p_no_disease
    p_disease_given_pos = numerator_pos / denominator_pos if denominator_pos != 0 else 0

    # P(Disease | Negative Test)
    numerator_neg = p_neg_given_disease * p_disease
    denominator_neg = numerator_neg + p_neg_given_no_disease * p_no_disease
    p_disease_given_neg = numerator_neg / denominator_neg if denominator_neg != 0 else 0

    return p_disease_given_pos, p_disease_given_neg


if __name__ == "__main__":
    try:
        prevalence = float(input("Enter disease prevalence (0 to 1): "))
        sensitivity = float(input("Enter test sensitivity (0 to 1): "))
        specificity = float(input("Enter test specificity (0 to 1): "))

        if not (0 <= prevalence <= 1 and 0 <= sensitivity <= 1 and 0 <= specificity <= 1):
            raise ValueError("All inputs must be between 0 and 1.")

        pos, neg = calculate_probabilities(prevalence, sensitivity, specificity)
        print(f"\nProbability of having disease if test is POSITIVE: {pos:.4f}")
        print(f"Probability of having disease if test is NEGATIVE: {neg:.4f}")

    except ValueError as ve:
        print("Invalid input:", ve)
