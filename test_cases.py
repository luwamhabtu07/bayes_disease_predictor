from main import calculate_probabilities

def run_test(prevalence, sensitivity, specificity):
    pos, neg = calculate_probabilities(prevalence, sensitivity, specificity)
    print(f"Input: Prevalence={prevalence}, Sensitivity={sensitivity}, Specificity={specificity}")
    print(f"  → P(Disease|Positive): {pos:.4f}")
    print(f"  → P(Disease|Negative): {neg:.4f}")
    print("-" * 50)

print("\n--- Normal Test Cases ---")
run_test(0.1, 0.9, 0.95)
run_test(0.2, 0.85, 0.9)
run_test(0.05, 0.95, 0.9)

print("\n--- Edge Test Cases ---")
run_test(0, 0.9, 0.95)         # No disease prevalence
run_test(0.1, 0.0, 0.95)       # Test can't detect disease
run_test(0.1, 0.9, 1.0)        # Perfect specificity
