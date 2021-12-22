import pandas as pd
import SeriesDeTiempo.serie as st

serie = st.Serie(pd.read_excel("../parcial/4.xlsx"),"Inversión")
serie = serie.descomposicion("multiplicativo",L=4)
serie.cajasEstacionalidad(4)
pron = serie.pronosticar(4)
pron.data.to_excel("asd.xlsx")

import SeriesDeTiempo.serie as st
serie = st.Serie(pd.read_csv("data.csv"),"Ventas")
fac = serie.fac()
fac


import SeriesDeTiempo.serie as st
serie = st.Serie(pd.read_csv("data.csv"),"AirPas")
serie = serie.ln()
prueba = serie.levene(alfa = 0.05,L=12)
prueba



prueba.data
prueba.W
prueba.F








