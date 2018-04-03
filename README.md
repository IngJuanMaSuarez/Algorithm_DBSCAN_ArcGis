# Algoritmo DBSCAN en ArcGis
Toolbox para ArcGIS con el algoritmo de minería de datos espaciales [DBSCAN](https://es.wikipedia.org/wiki/DBSCAN).

Desde ArcGis en el menú ArcToolbox se agrega el Toolbox para su ejecución.
Los datos de entrada son un texto plano y la herramienta crea un SHP con un atributo correspondiente al numero de cluster de cada punto.

<br>

## Contenido

- [Introducción](#introducción)
- [Screenshots](#screenshots)
- [Más Detalles del Proyecto](#más-detalles-del-proyecto)
- [Redes Sociales](#redes-sociales)

<br>

## Introducción

El presente proyecto busca analizar el comportamiento de los hurtos a personas que afectan la localidad Los Mártires de la ciudad de Bogotá, haciendo uso de algoritmos de agrupamiento de minería de datos espaciales y apoyado en una infraestructura de datos espacial, teniendo en cuenta variables como cuadrante de policía, mes, día del mes, día de la semana, hora, lugar de ocurrencia del delito, sexo y edad de la víctima; de tal forma que se logre realizar diferentes tipos de mapas del delito, y permita a las autoridades implementar estrategias para predecir el modo que opera, como se mueve, como se financia y lograr combatir con mayor eficacia y eficiencia el delito. 

A lo largo del proyecto, se trabajaron los algoritmos de agrupamiento de minería de datos espaciales K-Means y DBSCAN, el primero se usó para establecer la ubicación óptima de cada estación de policía teniendo en cuenta la ubicación y distribución de los delitos, y el segundo para hallar las zonas con mayor actividad delincuencial. Estos dos en conjunto, sobre la Infraestructura de Datos Espaciales de Bogotá nos permitió construir los modelos y mapas temáticos del delito de la localidad Los Mártires, muchos de estos modelos fueron realizados filtrando la información por diferentes variables para tener un análisis más preciso. 

<br>

## Screenshots

<table>
    <tr>
        <td>
            <img alt="Instalacion" src="Images/1.%20Datos%20de%20Entrada.png">
        </td>
        <td>
            <img alt="API Google Maps" src="Images/2.%20Ventana%20Inicial%20DBSCAN.png">
        </td>
        <td>
            <img alt="POI Visibles" src="Images/3.%20Archivos%20de%20Resultado.png">
        </td>
    </tr>
</table>
<table>
    <tr>
        <td>
            <img alt="API Google Maps" src="Images/4.%20Visualizacion%20de%20Resultados.png">
        </td>
        <td>
            <img alt="POI Visibles" src="Images/5.%20Clasificacion%20Cluster.png">
        </td>
    </tr>
</table>

<br>

## Más Detalles del Proyecto

- **[`Documento PDF`](https://www.academia.edu/36259000/Caracterizaci%C3%B3n_de_los_Hurtos_a_Personas_que_Afectan_la_Localidad_los_M%C3%A1rtires_de_la_Ciudad_de_Bogot%C3%A1_Mediante_la_Implementaci%C3%B3n_de_Algoritmos_de_Agrupamiento_de_Miner%C3%ADa_de_Datos_Espaciales_y_Apoyado_en_una_Infraestructura_de_Datos_Espacial)**
- **[`Presentacion PPT`](https://www.academia.edu/36258999/Caracterizaci%C3%B3n_de_los_Hurtos_a_Personas_que_Afectan_la_Localidad_los_M%C3%A1rtires_de_la_Ciudad_de_Bogot%C3%A1_Mediante_la_Implementaci%C3%B3n_de_Algoritmos_de_Agrupamiento_de_Miner%C3%ADa_de_Datos_Espaciales_y_Apoyado_en_una_Infraestructura_de_Datos_Espacial)**
- **[`Video YouTube de la Presentación PPT`](https://www.youtube.com/watch?v=5Zg4t8k_Xuc&t=)**

<br>

## Redes Sociales

- **[`Twitter`](https://twitter.com/IngJuanMaSuarez)**
- **[`Linkedin`](https://linkedin.com/in/IngJuanMaSuarez)**
- **[`Academia`](https://udistrital.academia.edu/IngJuanMaSuarez)**
- **[`YouTube`](https://www.youtube.com/channel/UC4CNTt2aXvMKmxNXQFtTrAA)**

<br>

<p align="center">
    <b>Trabajo de grado para Ingeniería Catastral y Geodesia<br/>
    <b>Universidad Distrital Francisco José de Caldas<br/>
    <b>Bogotá - Colombia<br/>
    <b>Noviembre 2015<br/>
</p>
