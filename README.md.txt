# Proyecto 1 – Clasificación de métodos de detección de exoplanetas

## Descripción del proyecto
Este proyecto explora si es posible predecir el método de detección de un exoplaneta
utilizando únicamente información observacional básica: el año de descubrimiento
y la distancia al sistema estelar.

El objetivo no es modelar la física de los exoplanetas, sino analizar los sesgos
históricos y tecnológicos en los métodos de detección astronómica.

---

## Pregunta de investigación
¿Es posible clasificar el método de detección de un exoplaneta a partir del año
de descubrimiento y la distancia al sistema?

---

## Dataset
- Fuente: NASA Exoplanet Archive
- Variables utilizadas:
  - `year`: año de descubrimiento del exoplaneta
  - `distance`: distancia al sistema en parsecs
  - `method`: método de detección (variable objetivo)

Se eliminaron registros con valores faltantes y métodos con baja representación
estadística.

---

## Metodología
1. Limpieza de datos y selección de variables relevantes
2. Filtrado de clases con pocas observaciones
3. Codificación de la variable objetivo
4. Escalamiento de variables numéricas
5. Separación del conjunto de datos usando train/test split estratificado
6. Entrenamiento de un modelo de Regresión Logística
7. Evaluación mediante métricas de clasificación

---

## Modelo utilizado
- Logistic Regression (scikit-learn)
- Razón de elección:
  - Modelo interpretable
  - Buen punto de partida para clasificación multiclase
  - Permite analizar patrones globales en los datos

---

## Resultados
El modelo logra identificar patrones claros entre:
- métodos dominantes en distintas épocas
- dependencia del método con la distancia observacional

Las métricas de precisión y recall varían entre clases, reflejando
diferencias en la representación de cada método en el dataset.

---

## Limitaciones
- El modelo aprende sesgos observacionales, no causas físicas
- Variables físicas del exoplaneta no fueron consideradas
- Métodos minoritarios fueron excluidos por falta de datos

---

## Trabajo futuro
- Incluir más variables observacionales
- Probar modelos no lineales (Random Forest, SVM)
- Visualizar fronteras de decisión
- Análisis temporal más detallado

---

## Tecnologías utilizadas
- Python 3.12
- pandas
- numpy
- scikit-learn
- matplotlib
- Visual Studio Code

---

## Autor
Víctor Jorquera Flores  
Proyecto desarrollado como parte de formación en Ciencia de Datos
