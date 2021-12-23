import pandas as pd
import SeriesDeTiempo.serie as st

# AIRPASS

serieA = st.Serie(pd.read_csv("AirPass.csv"),"AirPass"); serieA.graficar(titulo="Serie de AirPass")
serieA.levene(0.05,L=12)

serieAln = serieA.ln(); serieAln.graficar(titulo="Serie ln de AirPass")


serieA.cajas(L=12,titulo="Diagrama de cajas AirPass")
serieAln.cajas(L=12,titulo="Diagrama ln de cajas AirPass")


autoA = serieA.autocorrelacion(n=20); autoA
autoA.graficar()

autoAln = serieAln.autocorrelacion(n=20); autoAln
autoAln.graficar()


autoA.fac.k(3).graficar("Autocorrelación simple para k = 3")
autoAln.fac.k(3).graficar("Autocorrelación simple para k = 3")


# VENTAS

serieV = st.Serie(pd.read_csv("ventasS9.csv"),"Ventas"); serieV.graficar(titulo="Serie de Ventas")

serieVdiff = serieV.diff(1); serieVdiff.graficar(titulo="Serie diff de Ventas")

serieV.cajas(L=4,titulo="Diagrama de cajas Ventas")
serieVdiff.cajas(L=4,titulo="Diagrama de cajas Ventas")


autoV = serieV.autocorrelacion(n=20); autoV
autoV.graficar()

autoVdiff = serieVdiff.autocorrelacion(n=20); autoVdiff
autoVdiff.graficar()


autoV.fac.k(3).graficar("Autocorrelación simple para k = 3")
autoVdiff.fac.k(3).graficar("Autocorrelación simple para k = 3")
