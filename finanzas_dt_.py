import pandas as pd
import numpy as np

def clasificar_gasto(x):
    if x < 3000:
        return "Gasto bajo"
    elif x < 9000:
        return "Gasto normal"
    elif x < 15000:
        return "Gasto un poco alto"
    else:
        return "Gasto muy alto"

def generar_datos():
    np.random.seed(0)

    Gastos = np.random.randint(1000, 20000, 50)
    Reinversion = np.random.randint(0, 4000, 50)
    GananciaReinversion = np.random.randint(0, 5000, 50)
    IngresoActual = np.random.randint(2000, 25000, 50)

    df = pd.DataFrame({
        "Gastos": Gastos,
        "Reinversion": Reinversion,
        "GananciaReinversion": GananciaReinversion,
        "IngresoActual": IngresoActual
    })

    return df

def procesamiento(df):
    df["ValoresNulos"] = df.isnull().sum(axis=1)

    df["Equilibrio"] = (df["IngresoActual"] + df["GananciaReinversion"]) >= df["Gastos"]
    df["Equilibrio"] = df["Equilibrio"].astype(int)

    df["IngresoNecesario"] = df["Gastos"] - df["GananciaReinversion"]

    df["NivelGasto"] = df["Gastos"].apply(clasificar_gasto)

    return df

def resumen(df):
    print("Primeros registros:")
    print(df.head(), "\n")

    print("Descripción estadística:")
    print(df.describe(), "\n")

    print("Distribución de equilibrio (0=no alcanza, 1=alcanza):")
    print(df["Equilibrio"].value_counts(), "\n")

    print("Clasificación de gasto:")
    print(df["NivelGasto"].value_counts(), "\n")

if __name__ == "__main__":
    df = generar_datos()
    df = procesamiento(df)
    resumen(df)
