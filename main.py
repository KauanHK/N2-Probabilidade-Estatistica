import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


def create_fig(df: pd.DataFrame, column: str) -> None:

    plt.figure(figsize=(8, 6))
    sns.regplot(
        data = df,
        x = column,
        y = 'total',
        scatter_kws = {'s': 1},
        line_kws = {'color': 'red'}
    )

    plt.title(f'Regressão: {column} vs Valor Total', fontsize = 14)
    plt.xlabel(column, fontsize = 12)
    plt.ylabel('Valor Total (R$)', fontsize = 12)
    plt.tight_layout()

    print(f'Salvando gráfico {column} ...')
    plt.savefig(os.path.join('data', f'{column}.png'))


def main() -> None:

    df = pd.read_csv(os.path.join('data', 'data.csv'))
    df = df.drop(columns = ['id', 'city', 'animal', 'furniture', 'hoa', 'rent amount', 'property tax', 'fire insurance'])

    for column in df.columns:
        create_fig(df, column)


if __name__ == '__main__':
    main()
