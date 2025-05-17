import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


def create_fig(df: pd.DataFrame, x: str, y: str) -> None:

    print(f'Criando gráfico {x} vs {y}...')

    plt.figure(figsize=(8, 6))
    sns.regplot(
        data = df,
        x = x,
        y = y,
        scatter_kws = {'s': 1},
        line_kws = {'color': 'red'}
    )

    plt.title(f'Regressão: {x} vs {y}', fontsize = 14)
    plt.xlabel(x, fontsize = 12)
    plt.ylabel('Valor Total (R$)', fontsize = 12)
    plt.tight_layout()

    print(f'Salvando gráfico {x} ...')
    plt.savefig(os.path.join('data', f'{x}.png'))


def main() -> None:

    print('Lendo tabela...')
    df = pd.read_csv(os.path.join('data', 'data.csv'))

    print('Tratando os dados...')
    df = df.drop(columns = ['id', 'city', 'animal', 'furniture', 'hoa', 'rent amount', 'property tax', 'fire insurance'])
    df.columns = ['Área', 'Quartos', 'Banheiros', 'Vagas de Garagem', 'Andar', 'Total']

    for column in df.columns[:-1]:
        create_fig(df, column, 'Total')
    
    print('Gráficos gerados com sucesso')


if __name__ == '__main__':
    main()
