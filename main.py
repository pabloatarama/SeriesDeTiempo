import pandas as pd
import SeriesDeTiempo.serie as st

serie4 = st.Serie(pd.read_excel("parcial/4.xlsx"),"Inversión")
serie4.graficar("Inversión en puentes y carreteras","Trimestres","Inversión")
serie4.cajas(L=4,titulo="Diagrama de cajas-estacionalidad de la inversión en puentes y carreteras",xlabel="Trismestres",ylabel="Inversión")
serie4.cajasEstacionalidad(ciclo=4,titulo="Diagrama de cajas-estacionalidad de la inversión en puentes y carreteras",xlabel="Trimestres",ylabel="Inversión")
serieDescomposicion = serie4.descomposicion("multiplicativo",L=4)
serieDescomposicion
serieDescomposicion.data.to_excel("4p.xlsx")