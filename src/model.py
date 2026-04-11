from basket import create_category_basket, create_pasta_basket
from evaluation import run_fpgrowth_model, generate_rules, filter_rules
from utils import format_rules


def category_model(df):

    basket = create_category_basket(df)

    freq_items = run_fpgrowth_model(basket, min_support=0.005)

    rules = generate_rules(freq_items, min_threshold=0.8)

    rules = filter_rules(rules)

    return format_rules(rules)


def pasta_model(df):

    basket = create_pasta_basket(df)

    freq_items = run_fpgrowth_model(basket, min_support=0.002)

    rules = generate_rules(freq_items, min_threshold=0.5)

    rules = filter_rules(rules, min_confidence=0.05, min_lift=0.5)

    return format_rules(rules)