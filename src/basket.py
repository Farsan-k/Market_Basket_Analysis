import pandas as pd


def create_category_basket(df):

    df = df.copy()
    df['commodity'] = df['commodity'].astype(str).str.upper()

    basket = (
        df.groupby(['basket', 'commodity'])
        .size()
        .unstack(fill_value=0)
    )

    return (basket > 0).astype('int8')


def create_pasta_basket(df):

    df = df.copy()
    df['commodity'] = df['commodity'].astype(str).str.upper()

    df = df[df['commodity'].isin(['PASTA', 'PASTA SAUCE'])]

    basket = (
        df.groupby(['basket', 'commodity'])
        .size()
        .unstack(fill_value=0)
    )

    return (basket > 0).astype('int8')