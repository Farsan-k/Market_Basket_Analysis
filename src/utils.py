import pandas as pd
import matplotlib.pyplot as plt

def format_rules(rules):

    if rules.empty:
        return pd.DataFrame(columns=['antecedents', 'consequents', 'support', 'confidence', 'lift'])

    rules = rules.copy()

    rules['antecedents'] = rules['antecedents'].apply(lambda x: ', '.join(map(str, x)))
    rules['consequents'] = rules['consequents'].apply(lambda x: ', '.join(map(str, x)))

    return rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]


def save_rules(rules, path="rules.csv"):
    rules.to_csv(path, index=False)





def plot_top_rules(rules, top_n=10, save_path=None):

    if rules.empty:
        return

    top_rules = rules.sort_values(by='lift', ascending=False).head(top_n)

    labels = top_rules['antecedents'].astype(str) + " → " + top_rules['consequents'].astype(str)
    values = top_rules['lift']

    plt.figure()
    plt.barh(labels, values)
    plt.xlabel("Lift")
    plt.ylabel("Rules")
    plt.title("Top Association Rules")

    plt.gca().invert_yaxis()

    if save_path:
        plt.savefig(save_path + ".png", bbox_inches='tight')

    plt.show()