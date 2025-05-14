import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Carregar os dados do CSV
df = pd.read_csv('Student_Performance.csv')

# Criar o gráfico apenas com a linha de regressão
plt.figure(figsize=(8, 6))
sns.regplot(
    data=df,
    x='Hours Studied',
    y='Performance Index',
    scatter=False,               # Não exibir os pontos
    line_kws={'color': 'red'}    # Cor da linha de regressão
)

# Adicionar título e rótulos
plt.title('Linha de Regressão entre Horas Estudadas e Índice de Performance', fontsize=14)
plt.xlabel('Horas Estudadas', fontsize=12)
plt.ylabel('Índice de Performance', fontsize=12)
plt.tight_layout()
plt.savefig('fig.png')
