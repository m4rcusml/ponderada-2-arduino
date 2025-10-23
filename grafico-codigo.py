import sys
import pandas as pd
import matplotlib.pyplot as plt

def main(csv_path="./dados.csv", out_path="./grafico.png"):
  try:
    df = pd.read_csv(csv_path)
  except Exception as e:
    print(f"Erro ao ler '{csv_path}': {e}")
    sys.exit(1)

  df.columns = df.columns.str.strip()

  required = {"a", "b"}
  if not required.issubset(df.columns):
    print(f"Colunas faltando. Arquivo contém: {list(df.columns)}. Esperado: {sorted(required)}")
    sys.exit(1)

  if "time" in df.columns:
    x = df["time"]
    xlabel = "tempo (ms)"
  elif "x" in df.columns:
    x = df["x"]
    xlabel = "x"
  else:
    x = df.index
    xlabel = "índice"

  plt.figure(figsize=(8, 5))
  plt.plot(x, df["a"], label="VR (V)", color="tab:blue", linewidth=2)
  plt.plot(x, df["b"], label="VC (V)", color="tab:orange", linewidth=2)
  plt.xlabel(xlabel)
  plt.ylabel("Tensão (V)")
  plt.title("Medição RC — VR e VC")
  plt.grid(True, linestyle="--", alpha=0.5)
  plt.legend(title="Sinais")
  plt.tight_layout()

  try:
    plt.savefig(out_path, dpi=150)
    print(f"Gráfico salvo em: {out_path}")
  except Exception as e:
    print(f"Falha ao salvar o gráfico: {e}")

  plt.show()

if __name__ == "__main__":
  main()