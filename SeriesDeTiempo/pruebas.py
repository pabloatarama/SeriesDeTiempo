# -*- coding: utf-8 -*-

import numpy as np
import scipy.stats as sct
import matplotlib.pyplot as plt

class QQPlot():
    def __init__(self, data, alfa):
        self.alfa = alfa
        self.data = data.to_frame()
        self.data = self.data[self.data["residual"].notna()]
        self.data = self.data.sort_values(["residual"])
        self.data["i"] = np.arange(1, len(self.data)+1).astype(int)
        self.data.set_index("i",inplace=True)
        
        self.data["Q"] = np.nan
        if len(self.data)<=10:
            i=1
            while i<=len(self.data):
                self.data["Q"][i] = ( i - (3/8) ) / ( len(self.data) + (1/4) )
                i = i + 1
        else:
            i=1
            while i<=len(self.data):
                self.data["Q"][i] = ( i - (1/2) ) / len(self.data)
                i = i + 1
                
        self.data["Z"] = self.data["Q"].apply(sct.norm.ppf)   
        
    def __repr__(self):
        self.graficar()
        return (
        "Gráfico QQ Plot " + "\n"
        )
    
    def graficar(self, titulo="", xlabel="", ylabel=""):
        """Gráfico QQ-Plot\n
        titulo: Título de la gráfica\n
        xlabel: Título del eje x\n
        ylabel: Título del eje y"""
        fig, ax = plt.subplots(dpi=300, figsize=(9.6,5.4))
        
        
        a, b = np.polyfit(self.data["Z"], self.data["residual"], deg=1)
        y_est = a * self.data["Z"] + b
        
        
        sr = ((self.data["Z"] - y_est)**2).sum() / ( len(self.data) -2 )
        
        y_err = sct.t.ppf(self.alfa/2, len(self.data)-2) *  (
                                                        sr *
                                                        (
                                                            ( 1/len(self.data["Z"]) ) + 
                                                            ( self.data["Z"]**2 / ((self.data["Z"]**2).sum()) )
                                                        )
                                                     )**0.5
 
        # Linea de regresión
        ax.plot(self.data["Z"], y_est, '-', color='tab:red')
        
        # Área de intervalo
        ax.fill_between(self.data["Z"], y_est - y_err, y_est + y_err, alpha=0.2)
        
        # Puntos 
        ax.plot(self.data["Z"],self.data["residual"],"o")

        if titulo!="":
            ax.set_title(titulo)
        else:
            ax.set_title("QQ-Plot")
        if xlabel != "":
            ax.set_xlabel(xlabel)
        else:
            ax.set_xlabel("Z")
        if ylabel != "":
            ax.set_ylabel(ylabel)
        else:
            ax.set_ylabel("residuales")

        ax.grid(linestyle=":")
        # ax.legend()
        plt.show()
        
class DurbinWatson:
    def __init__(self, data):
        self.data = data.to_frame()
        self.data.rename(columns={"residual":"et"},inplace=True)
        self.data = self.data[self.data["et"].notna()]
        self.data["i"] = np.arange(1, len(self.data)+1).astype(int)
        self.data.set_index("i",inplace=True)
        
        self.data["et-1"]=self.data["et"].shift()
        
        self.data["(et - et-1)^2"] = (self.data["et"] - self.data["et-1"])**2
        
        self.data["et^2"] = self.data["et"]**2
        
        self.dw = self.data["(et - et-1)^2"].sum() / self.data["et^2"].sum()
        
    def __repr__(self):
        return (
        "Estadístico de Durbin-Watson" + "\n" +
        str(self.dw) + "\n" +
        "Cantidad de datos: " + str(len(self.data))
        
        )
        
        