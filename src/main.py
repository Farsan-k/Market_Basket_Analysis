import pandas as pd
import os
from preprocessing import UniversalSizeCleaner, SizeImputer
from model import category_model, pasta_model
from utils import save_rules, plot_top_rules


def main():

    df = pd.read_csv("raw.csv")

    cleaner = UniversalSizeCleaner(column='product_size')
    df = cleaner.fit_transform(df)

    imputer = SizeImputer(column='product_size_clean')
    df = imputer.fit_transform(df)

    df.to_csv("final.csv", index=False)

    category_rules = category_model(df)
    print(category_rules.head(10))

    pasta_rules = pasta_model(df)
    print(pasta_rules.head(10))

    os.makedirs("output", exist_ok=True)

    plot_top_rules(category_rules, save_path="output/category_plot")
    plot_top_rules(pasta_rules, save_path="output/pasta_plot")

    save_rules(category_rules, "rules.csv")


if __name__ == "__main__":
    main()