import pandas as pd
import pyreadstat

# Leer .sav con etiquetas aplicadas
df, meta = pyreadstat.read_sav('data/d22.sav', apply_value_formats=True)

# Guardar CSV ya con textos en vez de números
df.to_csv('datos_22.csv', index=False)