from mlxtend.frequent_patterns import fpgrowth, association_rules


def run_fpgrowth_model(basket, min_support=0.005):
    return fpgrowth(basket, min_support=min_support, use_colnames=True)


def generate_rules(freq_items, min_threshold=0.8):
    return association_rules(freq_items, metric='lift', min_threshold=min_threshold)


def filter_rules(rules, min_confidence=0.1, min_lift=0.8):

    if rules.empty:
        return rules

    return rules[
        (rules['confidence'] >= min_confidence) &
        (rules['lift'] >= min_lift)
    ].sort_values(by='lift', ascending=False)