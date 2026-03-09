import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error, mean_squared_error

# =========================
# 1. CARREGAMENTO DOS DADOS
# =========================

# Troque o nome do arquivo caso o seu CSV tenha outro nome
arquivo = "covid_brasil.csv"

df = pd.read_csv(arquivo)

print("Primeiras linhas do dataset:")
print(df.head())
print("\nInformações gerais:")
print(df.info())
print("\nValores nulos por coluna:")
print(df.isnull().sum())

# =========================
# 2. AJUSTE DAS COLUNAS
# =========================

# Este bloco tenta adaptar o código a nomes de colunas comuns em bases de COVID
# Ajuste se os nomes da sua base forem diferentes

# Possíveis nomes para data
if "date" in df.columns:
    col_data = "date"
elif "Date" in df.columns:
    col_data = "Date"
elif "data" in df.columns:
    col_data = "data"
else:
    raise ValueError("Não encontrei coluna de data no arquivo.")

# Possíveis nomes para casos acumulados
if "confirmed" in df.columns:
    col_casos = "confirmed"
elif "Confirmed" in df.columns:
    col_casos = "Confirmed"
elif "casosAcumulado" in df.columns:
    col_casos = "casosAcumulado"
elif "cases" in df.columns:
    col_casos = "cases"
elif "totalCases" in df.columns:
    col_casos = "totalCases"
else:
    raise ValueError("Não encontrei coluna de casos acumulados no arquivo.")

# Possíveis nomes para mortes acumuladas
if "deaths" in df.columns:
    col_mortes = "deaths"
elif "Deaths" in df.columns:
    col_mortes = "Deaths"
elif "obitosAcumulado" in df.columns:
    col_mortes = "obitosAcumulado"
elif "totalDeaths" in df.columns:
    col_mortes = "totalDeaths"
else:
    col_mortes = None
    print("\nAviso: não encontrei coluna de mortes acumuladas.")

# Possível filtro Brasil, caso a base tenha vários países/estados/municípios
if "country" in df.columns:
    df = df[df["country"].str.lower() == "brazil"]
elif "pais" in df.columns:
    df = df[df["pais"].str.lower() == "brasil"]
elif "regiao" in df.columns:
    # não filtra automaticamente
    pass

# Converter data
df[col_data] = pd.to_datetime(df[col_data], errors="coerce")

# Remover linhas sem data
df = df.dropna(subset=[col_data])

# Ordenar por data
df = df.sort_values(col_data).reset_index(drop=True)

# Manter apenas colunas úteis
colunas_uteis = [col_data, col_casos]
if col_mortes:
    colunas_uteis.append(col_mortes)

df = df[colunas_uteis].copy()

# Remover nulos em casos
df = df.dropna(subset=[col_casos])

# Garantir tipo numérico
df[col_casos] = pd.to_numeric(df[col_casos], errors="coerce")
if col_mortes:
    df[col_mortes] = pd.to_numeric(df[col_mortes], errors="coerce")

df = df.dropna(subset=[col_casos]).reset_index(drop=True)

print("\nDataset após tratamento:")
print(df.head())

# =========================
# 3. CRIAÇÃO DE NOVAS COLUNAS
# =========================

# Casos diários a partir dos acumulados
df["novos_casos"] = df[col_casos].diff().fillna(0)

# Evitar valores negativos causados por inconsistências de base
df["novos_casos"] = df["novos_casos"].apply(lambda x: x if x >= 0 else 0)

# Média móvel de 7 dias para novos casos
df["media_movel_7d_casos"] = df["novos_casos"].rolling(window=7).mean()

if col_mortes:
    df["novas_mortes"] = df[col_mortes].diff().fillna(0)
    df["novas_mortes"] = df["novas_mortes"].apply(lambda x: x if x >= 0 else 0)
    df["media_movel_7d_mortes"] = df["novas_mortes"].rolling(window=7).mean()

# Taxa de crescimento percentual dos novos casos
df["taxa_crescimento"] = df["novos_casos"].pct_change() * 100
df["taxa_crescimento"] = df["taxa_crescimento"].replace([np.inf, -np.inf], np.nan)

# Criar variável de tempo em dias para modelagem
df["dias"] = (df[col_data] - df[col_data].min()).dt.days

# =========================
# 4. ANÁLISE EXPLORATÓRIA
# =========================

print("\nResumo estatístico:")
print(df.describe())

print("\nPeríodo analisado:")
print("Data inicial:", df[col_data].min())
print("Data final:", df[col_data].max())

print("\nTotal final de casos acumulados:")
print(df[col_casos].iloc[-1])

if col_mortes:
    print("\nTotal final de mortes acumuladas:")
    print(df[col_mortes].iloc[-1])

# =========================
# 5. GRÁFICOS EXPLORATÓRIOS
# =========================

plt.figure(figsize=(12, 5))
plt.plot(df[col_data], df[col_casos])
plt.title("Casos acumulados de COVID-19 no Brasil")
plt.xlabel("Data")
plt.ylabel("Casos acumulados")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 5))
plt.plot(df[col_data], df["novos_casos"], alpha=0.4, label="Novos casos diários")
plt.plot(df[col_data], df["media_movel_7d_casos"], linewidth=2, label="Média móvel 7 dias")
plt.title("Novos casos diários e média móvel de 7 dias")
plt.xlabel("Data")
plt.ylabel("Casos")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

if col_mortes:
    plt.figure(figsize=(12, 5))
    plt.plot(df[col_data], df[col_mortes])
    plt.title("Mortes acumuladas por COVID-19 no Brasil")
    plt.xlabel("Data")
    plt.ylabel("Mortes acumuladas")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12, 5))
    plt.plot(df[col_data], df["novas_mortes"], alpha=0.4, label="Novas mortes diárias")
    plt.plot(df[col_data], df["media_movel_7d_mortes"], linewidth=2, label="Média móvel 7 dias")
    plt.title("Novas mortes diárias e média móvel de 7 dias")
    plt.xlabel("Data")
    plt.ylabel("Mortes")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

plt.figure(figsize=(12, 5))
plt.plot(df[col_data], df["taxa_crescimento"])
plt.title("Taxa de crescimento percentual dos novos casos")
plt.xlabel("Data")
plt.ylabel("Taxa (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =========================
# 6. MODELAGEM PREDITIVA
# =========================

X = df[["dias"]]
y = df[col_casos]

# Modelo 1: Regressão Linear
modelo_linear = LinearRegression()
modelo_linear.fit(X, y)
df["pred_linear"] = modelo_linear.predict(X)

# Modelo 2: Regressão Polinomial
grau_polinomial = 3
modelo_polinomial = make_pipeline(
    PolynomialFeatures(grau_polinomial),
    LinearRegression()
)
modelo_polinomial.fit(X, y)
df["pred_polinomial"] = modelo_polinomial.predict(X)

# =========================
# 7. AVALIAÇÃO DOS MODELOS
# =========================

mae_linear = mean_absolute_error(y, df["pred_linear"])
rmse_linear = np.sqrt(mean_squared_error(y, df["pred_linear"]))

mae_polinomial = mean_absolute_error(y, df["pred_polinomial"])
rmse_polinomial = np.sqrt(mean_squared_error(y, df["pred_polinomial"]))

print("\nAvaliação dos modelos")
print("-" * 30)
print(f"MAE Regressão Linear: {mae_linear:.2f}")
print(f"RMSE Regressão Linear: {rmse_linear:.2f}")
print(f"MAE Regressão Polinomial: {mae_polinomial:.2f}")
print(f"RMSE Regressão Polinomial: {rmse_polinomial:.2f}")

# =========================
# 8. COMPARAÇÃO VISUAL DOS MODELOS
# =========================

plt.figure(figsize=(12, 5))
plt.plot(df[col_data], df[col_casos], label="Real", linewidth=2)
plt.plot(df[col_data], df["pred_linear"], label="Linear", linestyle="--")
plt.plot(df[col_data], df["pred_polinomial"], label=f"Polinomial grau {grau_polinomial}", linestyle=":")
plt.title("Comparação entre valores reais e previsões")
plt.xlabel("Data")
plt.ylabel("Casos acumulados")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =========================
# 9. PREVISÃO DOS PRÓXIMOS DIAS
# =========================

dias_futuros = 15

ultimo_dia = df["dias"].max()
futuro_x = np.arange(ultimo_dia + 1, ultimo_dia + dias_futuros + 1).reshape(-1, 1)

previsao_linear = modelo_linear.predict(futuro_x)
previsao_polinomial = modelo_polinomial.predict(futuro_x)

datas_futuras = pd.date_range(
    start=df[col_data].max() + pd.Timedelta(days=1),
    periods=dias_futuros
)

df_previsao = pd.DataFrame({
    "data": datas_futuras,
    "previsao_linear": previsao_linear,
    "previsao_polinomial": previsao_polinomial
})

print("\nPrevisão para os próximos dias:")
print(df_previsao)

# Gráfico da previsão
plt.figure(figsize=(12, 5))
plt.plot(df[col_data], df[col_casos], label="Histórico real", linewidth=2)
plt.plot(df_previsao["data"], df_previsao["previsao_linear"], label="Previsão linear", linestyle="--")
plt.plot(df_previsao["data"], df_previsao["previsao_polinomial"], label="Previsão polinomial", linestyle=":")
plt.title("Previsão de casos acumulados para os próximos dias")
plt.xlabel("Data")
plt.ylabel("Casos acumulados")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =========================
# 10. ANÁLISE DE POSSÍVEL PONTO DE VIRADA
# =========================

# Estratégia simples:
# observar quando a média móvel de 7 dias começa a cair de forma consistente

df["variacao_mm7"] = df["media_movel_7d_casos"].diff()

# Procurar sequências de queda na média móvel
quedas_consecutivas = 0
ponto_virada = None

for i in range(1, len(df)):
    if pd.notnull(df.loc[i, "variacao_mm7"]) and df.loc[i, "variacao_mm7"] < 0:
        quedas_consecutivas += 1
    else:
        quedas_consecutivas = 0

    if quedas_consecutivas >= 7:
        ponto_virada = df.loc[i, col_data]
        break

print("\nAnálise do ponto de virada")
print("-" * 30)
if ponto_virada is not None:
    print(f"Possível ponto de virada identificado em: {ponto_virada.date()}")
else:
    print("Não foi possível identificar um ponto de virada claro com este critério.")

# Gráfico da média móvel com ponto de virada
plt.figure(figsize=(12, 5))
plt.plot(df[col_data], df["media_movel_7d_casos"], label="Média móvel 7 dias")
if ponto_virada is not None:
    plt.axvline(ponto_virada, linestyle="--", label="Possível ponto de virada")
plt.title("Média móvel de 7 dias dos novos casos")
plt.xlabel("Data")
plt.ylabel("Média móvel")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =========================
# 11. EXPORTAR RESULTADOS
# =========================

df.to_csv("covid_brasil_tratado.csv", index=False)
df_previsao.to_csv("previsao_covid_brasil.csv", index=False)

print("\nArquivos exportados com sucesso:")
print("- covid_brasil_tratado.csv")
print("- previsao_covid_brasil.csv")