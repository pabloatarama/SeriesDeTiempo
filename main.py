import pandas as pd
import SeriesDeTiempo.serie as st

serie = st.Serie(pd.read_excel("../parcial/4.xlsx"),"Inversión")
serie = serie.descomposicion("aditivo",L=4)
serie
serie.pronosticar(2)

