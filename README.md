# 🏎️ Formula 1 — Proyecto Final Data Scientist II

## ¿Qué factores predicen mejor la posición final de un piloto?

**Curso:** Data Scientist II — 2026  
**Entrega:** 25 de junio de 2026  
**Repo:** [github.com/mnoero23/F1-PROYECTO-FINAL](https://github.com/mnoero23/F1-PROYECTO-FINAL)

---

## Resultados

| Tarea | Modelo | Métrica | Valor |
|-------|--------|---------|-------|
| Regresión | Baseline (Reg. Lineal) | MAE | 2.541 posiciones |
| Regresión | **XGBoost** ✅ | MAE | **2.238 posiciones** |
| Regresión | **XGBoost** ✅ | R² | **0.626** |
| Clasificación | Baseline (Reg. Logística) | ROC-AUC | 0.881 |
| Clasificación | **XGBoost** ✅ | ROC-AUC | **0.905** |
| Clasificación | **XGBoost** ✅ | Accuracy | **0.811** |

**Conclusión principal:** La posición de grilla (grid) es el predictor dominante (SHAP feature #1, r=0.67). El equipo/constructor es el segundo factor más importante (ANOVA η²>0.14). La estrategia de pit stops tiene un efecto secundario y no lineal.

---

## Dataset

**Fuente:** [Formula 1 World Championship (Kaggle)](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)  
**Cobertura:** 1950–2024 | **3.547 registros de carrera** tras limpieza

| Archivo | Descripción |
|---------|-------------|
| `results.csv` | Resultados de carrera ⭐ tabla central (26.759 filas originales) |
| `circuits.csv` | Circuitos del mundo (ubicación, coordenadas) |
| `constructors.csv` | Equipos/escuderías |
| `drivers.csv` | Pilotos (fecha nacimiento, nacionalidad) |
| `races.csv` | Carreras por temporada y circuito |
| `qualifying.csv` | Resultados de clasificación (Q1/Q2/Q3) |
| `pit_stops.csv` | Paradas en boxes (vuelta, duración) |
| `lap_times.csv` | Tiempos por vuelta |
| `driver_standings.csv` | Clasificación del campeonato |
| `constructor_standings.csv` | Clasificación de constructores |
| `status.csv` | Estado de finalización (DNF, etc.) |

---

## Pregunta central

> **¿Qué factores predicen mejor la posición final de un piloto en carrera?**

### Hipótesis

| Hipótesis | Resultado |
|-----------|-----------|
| H1: La posición de grilla es el predictor más fuerte | ✅ Confirmada — SHAP feature #1, r=0.67 |
| H2: El constructor explica gran parte de la varianza | ✅ Confirmada — ANOVA η²>0.14 (efecto grande) |
| H3: Los pit stops diferencian resultados similares | ⚠️ Parcial — efecto débil y no lineal |

### Variable objetivo
- **Regresión:** `position` (posición final 1–20)
- **Clasificación:** `top3` (1 si terminó en podio, 0 si no)

### Features utilizadas
```
grid, team_rank, num_stops, total_pit_time, driver_age
```

---

## Estructura del proyecto

```
f1-proyecto-final/
├── data/
│   ├── *.csv                          # 11 tablas originales del dataset
│   ├── f1_master.csv                  # Dataset maestro unificado (NB02)
│   ├── f1_master_clean.csv            # Dataset limpio — 3.547 filas x 31 cols (NB03)
│   └── metricas_modelos.csv           # Métricas de todos los modelos
├── notebooks/
│   ├── 01_exploracion_inicial.ipynb   # Carga, inspección, primeras visualizaciones
│   ├── 02_api_y_dataset_maestro.ipynb # API Jolpica-F1, joins, features derivadas
│   ├── 03_limpieza.ipynb              # Nulos, outliers, normalización, tipos
│   ├── 04_eda.ipynb                   # Correlaciones, hipótesis, heatmaps
│   ├── 05_modelos_baseline.ipynb      # Regresión lineal y logística
│   ├── 06_modelos_avanzados.ipynb     # Random Forest y XGBoost con RandomizedSearchCV
│   └── 07_interpretabilidad_conclusiones.ipynb  # SHAP, PDP, errores, conclusiones
├── figures/                           # Gráficos exportados por los notebooks
├── requirements.txt                   # Dependencias Python
└── README.md
```

---

## Cómo reproducir

```bash
git clone https://github.com/mnoero23/F1-PROYECTO-FINAL
cd f1-proyecto-final

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

# Instalar dependencias
pip install -r requirements.txt

# Iniciar Jupyter Lab desde la raíz del proyecto
jupyter lab
```

### Orden de ejecución de notebooks

| Orden | Notebook | Tiempo estimado |
|-------|----------|----------------|
| 1° | `01_exploracion_inicial.ipynb` | < 1 min |
| 2° | `02_api_y_dataset_maestro.ipynb` | 5–15 min (API) |
| 3° | `03_limpieza.ipynb` | < 1 min |
| 4° | `04_eda.ipynb` | 1–2 min |
| 5° | `05_modelos_baseline.ipynb` | 1–3 min |
| 6° | `06_modelos_avanzados.ipynb` | 15–25 min |
| 7° | `07_interpretabilidad_conclusiones.ipynb` | 10–20 min |

> ⚠️ NB01 debe ejecutarse desde la raíz del proyecto. NB02–07 usan rutas `../data/`.

---

## Librerías principales

```
pandas, numpy, matplotlib, seaborn, scipy
scikit-learn, xgboost, shap
geopandas, plotly
jupyterlab
```

---

## Autor

**Matías** — Data Scientist II, 2026
