# Paquete Series De Tiempo

El paquete SeriesDeTiempo es una librería que permite ejecutar modelos de series de tiempo. Este proyecto aún se encuentra en desarrollo. Está basado en las librerías [pandas](https://pypi.org/project/pandas/) y [matplotlib](https://pypi.org/project/matplotlib/) por lo que es necesario la instalación de estas antes de su uso.

Versión 2021.12.3

Autor: [Pablo Atarama](https://pabloatarama.com/)

Colaboración: Sandra Carmona

© Derechos Reservados 2021

**Índice**
- [Importar librería](#id10)
- [Crear una serie](#id20)
- [Graficar una serie](#id30)
  - [Grafico de líneas](#id40)
  - [Diagramas de cajas](#id50)
- [Aplicar un modelo](#id60)
  - [Modelos soportados](#id70)
    - [Naïve](#id80)
    - [Media móvil simple](#id90)
    - [Media móvil doble](#id100)
    - [Media móvil ponderada](#id110)
    - [Suavización exponencial simple](#id120)
    - [Media móvil doble con tendencia](#id130)
    - [Brown o suvización exponencial doble](#id140)
    - [Holt](#id150)
    - [Holt y Winters](#id160)
    - [Descomposición](#id170)
- [Modelo](#id180)
  - [Graficar un modelo](#id190)
    - [Gráficas extras del modelo de descomposición](#id200)
    - [Errores de los modelos](#id210)
    - [Residual de los modelos](#id220)
      - [Graficar residuales](#id230)
      - [Pruebas de los residuales](#id240)
        - [Gráfico QQ-Plot](#id250)
        - [Estadístico Durbin-Watson](#id260)
- [Pronosticar un modelo](#id270)
- [Acceder a los datos manualmente](#id280)

## <div id="id10"></div>Importar librería
Para importar la librería utilizamos:

```python
import SeriesDeTiempo.serie as st
```

Pasos para utilizar la librería:
1. Crear un objeto del tipo **Serie**.
2. Aplicar un modelo a un objeto del tipo Serie que nos devolverá un objeto del tipo **Modelo**.

## <div id="id20"></div>Crear una serie

Para crear un objeto de tipo **Serie** (Serie de tiempo) utilizamos:

```python
serie = st.Serie(DataFrame, columna="")
```

Donde *DataFrame* es el DataFrame de la librería *pandas* donde se extraerá la data y *columna* la columna del DataFrame específica que se considerará como *yt*.

## <div id="id30"></div>Graficar una serie

### <div id="id40"></div>Gráfico de líneas

Para graficar una serie se utiliza la función *graficar()*

```python
serie.graficar(titulo="", xlabel="", ylabel="", tendencia=False)
```

- titulo: Título del gráfico.
- xlabel: Título del eje x.
- ylabel: Título del eje y.
- tendencia: Si se grafica una linea de tendencia lineal, por defecto es False.

### <div id="id50"></div>Diagramas de cajas

Se puede realizar diagramas de cajas a los objetos de tipo **Serie** a lo largo del tiempo agrupando por cilos mediante:

```python
serie.cajasEstacionalidad(L=4, comienzo=1, titulo="", xlabel="", ylabel="", grilla=True)
```

- ciclo: Ciclos en que se agrupará los datos, por defecto es 4.
- titulo: Título de la gráfica.
- xlabel: Título del eje x.
- ylabel: Título del eje y.
- grilla: Grilla de gráfica (True o False), por defecto True.

También se puede realizar diagramas de cajas sobre la estacionalidad mediante:

```python
serie.cajas(ciclo=4, comienzo=1, titulo="", xlabel="", ylabel="", grilla=True)
```

- ciclo: Ciclos en que se agrupará los datos, por defecto es 4.
- titulo: Título de la gráfica.
- xlabel: Título del eje x.
- ylabel: Título del eje y.
- grilla: Grilla de gráfica (True o False), por defecto True.

## <div id="id60"></div>Aplicar un modelo

Para usar un modelo se aplicara la respectiva función del modelo sobre el objeto de tipo **Serie**. Esto devolverá un objeto del tipo de modelo especificado. Cada función utiliza diferentes parámetros.

### <div id="id70"></div>Modelos soportados

Considerando que se creó un objeto de tipo **Serie** llamado *serie*:

#### <div id="id80"></div>Naive

```python
serieConModelo = serie.naive()
```

#### <div id="id90"></div>Media movil simple

```python
serieConModelo = serie.mediaMovilSimple(longitud=3, desfasada=False)
```

- longitud: longitud de la media móvil simple, por defecto es 3.
- desfasada: Si es desfasada o no (True o False), por defecto es False.

#### <div id="id100"></div>Media movil doble

```python
serieConModelo = serie.mediaMovilDoble(longitud=3, desfasada=False)
```

- longitud: longitud de ambas medias móviles, por defecto es 3.
- desfasada: Si es desfasada o no (True o False).

#### <div id="id110"></div>Media movil ponderada

```python
serieConModelo = serie.mediaMovilPonderada(longitud, ponderaciones)
```

- ponderaciones: lista con alfas a ponderar ej: ```[alfa1, alfa2, alfa3]``` donde alfa1 > alfa2 > alfa3, etc.

#### <div id="id120"></div>Suavización exponencial simple

```python
serieConModelo = serie.suavizacionExponencialSimple(alfa=0.5)
```

- alfa: parámetro alfa del modelo, por defecto es *0.5*.

#### <div id="id130"></div>Media movil doble con tendencia

```python
serieConModelo = serie.mediaMovilDobleConTendencia(longitud=3)
```

- longitud: longitud de ambas medias moviles, por defecto es 3.

#### <div id="id140"></div>Brown o suavización exponencial doble

```python
serieNaive = serie.brown(alfa=0.5, M1=None, M2=None)
```

- alfa: parámetro alfa del modelo, por defecto es 0.5.
- M1: Valor inicial de Mat, por defecto es yt para t = 1.
- M2: Valor inicial de Maat, por defecto es yt para t = 1.

#### <div id="id150"></div>Holt

```python
serieConModelo = serie.holt(alfa=0.5, beta=0.5, M=None, T=0)
```

- alfa: parámetro alfa del modelo, por defecto es 0.5.
- beta: parámetro beta del modelo, por defecto es 0.5.
- M: Valor inicial de Mt, por defecto es yt para t = 1.
- T: Valor inicial de Tt, por defecto es 0.

#### <div id="id160"></div>Holt y Winters

```python
serieConModelo = serie.holtYWinters(metodo, alfa=0.5, beta=0.5, gamma=0.5, L=4)
```

- metodo: El metodo a utilizar "aditivo" para el metodo aditivo y "multiplicativo" para el metodo multiplicativo.
- alfa: parámetro alfa del modelo, por defecto es 0.5.
- beta: parámetro beta del modelo, por defecto es 0.5.
- gamma: parámetro gamma del modelo, por defecto es 0.5.
- L: Longitud de la estacionalidad, por defecto es 4.

#### <div id="id170"></div>Descomposición

```python
serieConModelo = serie.descomposicion(metodo, L=12)
```

- metodo: El metodo a utilizar "aditivo" para el metodo aditivo y "multiplicativo" para el metodo multiplicativo.
- L: Longitud de la estacionalidad, por defecto es 12.

## <div id="id180"></div>Modelo

## <div id="id190"></div>Graficar un modelo

Para graficar cualquier objeto de tipo *Modelo* se utiliza la función *graficar()*

```python
serie.graficar(titulo="", xlabel="", ylabel="")
```

- titulo: Título del gráfico.
- xlabel: Título del eje x.
- ylabel: Título del eje y.

### <div id="id200"></div>Gráficas extras del modelo de descomposición

Los modelos de descomposición tienen la peculiaridad de poseer las propiedades: tendencia y estacionalidad siendo estas también graficables mediante *graficar()*

```python
serieDescomposicion.tendencia.graficar(titulo="", xlabel="", ylabel="")
serieDescomposicion.estacionalidad.graficar(titulo="", xlabel="", ylabel="")
```

### <div id="id210"></div>Errores de los Modelos

Para consultar los errores de la aplicación de un determinado modelo que se encuentre en un objeto de ejemplo *serieConModelo* basaría con consultar su propiedad "errores":

```python
serieConModelo.errores
```

Podemos extraer el valor específico de algún error consultando las propiedades:

```python
serieConModelo.errores.mad
serieConModelo.errores.mape
serieConModelo.errores.mse
serieConModelo.errores.rmse
serieConModelo.errores.u_theil
```

### <div id="id220"></div>Residual de los modelos

#### <div id="id230"></div>Graficar residuales

Es posible graficar el residual de los objetos de los modelos mediante:

```python
serieConModelo.residual.graficar(titulo="", xlabel="", ylabel="")
```

#### <div id="id240"></div>Pruebas de los Residuales

##### <div id="id250"></div>Gráfico QQ-Plot

Para visualizar el gráfico QQ-Plot se llamará a la función *qqPlot* sobre los residuales de un objeto de tipo modelo indicando el nivel de sifnificancia.

```python
serieConModelo.residual.qqPlot(alfa=0.05) # Muestra gráfica por defecto
serieConModelo.residual.qqPlot(alfa=0.05).graficar(titulo="", xlabel="", ylabel="")
```

- alfa: nivel de significación del intervalo, por defecto es 0.05

- titulo: Título de la gráfica.
- xlabel: Título del eje x.
- ylabel: Título del eje y.

##### <div id="id260"></div>Estadístico Durbin-Watson

Para mostrar el estadístico	de prueba se accede a la propiedad *df* del objeto generado por la función *durbinWatson()*.

```python
serieConModelo.residual.durbinWatson().dw
```

## <div id="id270"></div>Pronosticar un modelo

Para realizar un pronóstico se deberá llamar a la función *pronosticar()* y esta devolverá una copia del objeto del modelo pero con el pronóstico pedido agregado.

```python
serieConPronostico = serieConModelo.pronosticar(p=1, t=None)
```

- p: cantidad de periodos a pronosticar, por defecto es 1.
- t: valor de t desde donde comenzará el pronóstico, por defecto comienza luego del último dato.

## <div id="id280"></div>Acceder a los datos manualmente

En caso se requiera realizar una gráfica de otro tipo, todos los objetos de la librería contienen un DataFrame de pandas en su propiedad data:

```python
serie.data
serieConModelo.data
serieConPronostico.data
prueba.data
```
