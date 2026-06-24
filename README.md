# 🏎️ Formula 1 — Proyecto Final Data Scientist II
## ¿Qué factores predicen mejor la posición final de un piloto?
**Curso:** Data Scientist II — 2026
**Entrega:** 25 de junio de 2026
**Estado:** ✅ Pipeline completo — EDA, modelado, interpretabilidad
---
## Resumen de resultados
| Modelo | Tarea | Métrica principal | Resultado |
|--------|-------|--------------------|-----------|
| Regresión Lineal (baseline) | Regresión | MAE | 2.541 |
| Regresión Logística (baseline) | Clasificación binaria | AUC | 0.881 |
| Random Forest | Regresión | MAE / R² | 2.275 / 0.620 |
| Random Forest | Clasificación binaria | AUC / Accuracy | 0.903 / 0.817 |
| **XGBoost** ⭐ | **Regresión** | **MAE / R²** | **2.238 / 0.626** |
| **XGBoost** ⭐ | **Clasificación binaria (top3)** | **AUC / Accuracy** | **0.905 / 0.811** |
> **XGBoost** fue el modelo ganador en ambas tareas. Interpretado con SHAP (TreeExplainer).
### Hallazgos principales (confirmados con SHAP)
1. ✅ **H1 confirmada** — `grid` (posición de clasificación) es el predictor dominante, tanto en correlación simple (r≈0.67) como en importancia SHAP (#1).
2. ✅ **H2 confirmada** — el equipo (`team_rank`) tiene un efecto grande sobre el resultado (ANOVA p<0.001, η²>0.14; SHAP feature #2).
3. ⚠️ **H3 parcial** — la estrategia de pit stops (`num_stops`, `total_pit_time`) tiene un efecto medible pero débil y no lineal.
---
## ⚠️ Nota metodológica: corrección de data leakage
Durante el desarrollo de los modelos baseline (notebook 05) se detectó que las features `laps` y `finished` contienen información posterior al resultado de la carrera (data leakage), lo que generaba métricas artificialmente perfectas (R²=1.0, AUC=1.0). Estas columnas fueron **eliminadas de la lista de features** en los notebooks 05, 06 y 07, y los modelos fueron re-entrenados. Las métricas reportadas en este README corresponden a la versión corregida.
---
## Dataset
Fuente: [Formula 1 World Championship (Kaggle)](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020), complementado con la API [Jolpica-F1](https://github.com/jolpica/jolpica-f1) (reemplazo del Ergast API, dado de baja en 2024).
| Archivo | Descripción | Filas |
|---------|-------------|-------|
| `circuits.csv` | Circuitos del mundo (ubicación, coordenadas) | 20 |
| `constructors.csv` | Equipos/escuderías | 13 |
| `drivers.csv` | Pilotos (fecha nacimiento, nacionalidad) | 20 |
| `races.csv` | Carreras por temporada y circuito | 166 |
| `results.csv` | Resultados ⭐ tabla central | 960 |
| `qualifying.csv` | Resultados de clasificación (Q1/Q2/Q3) | 952 |
| `pit_stops.csv` | Paradas en boxes (vuelta, duración) | 613 |
| `lap_times.csv` | Tiempos por vuelta | 456 |
| `driver_standings.csv` | Clasificación del campeonato | 680 |
| `constructor_standings.csv` | Clasificación de constructores | 408 |
| `status.csv` | Estado de finalización (DNF, etc.) | 15 |
| `f1_master.csv` | Dataset maestro (join de todas las tablas) | 960 × 36 |
| `f1_master_clean.csv` | Dataset limpio, listo para ML | 952 × 31 |
## Pregunta central
> **¿Qué factores predicen mejor la posición final de un piloto en carrera?**
### Variable objetivo
`position` en `results.csv` → **Regresión** (posición 1–20) o **Clasificación binaria** `top3 = position <= 3`
### Features finales del modelo
| Feature | Fuente | Tipo |
|---------|--------|------|
| `grid` | results | Numérico — predictor principal |
| `team_rank` | constructor_standings | Numérico — nivel del equipo en la temporada |
| `num_stops` | pit_stops | Numérico — estrategia de carrera |
| `total_pit_time` | pit_stops | Numérico — eficiencia en boxes |
| `positions_gained` | derivado | grid − position (solo en EDA, no en modelo final) |
| `circuit_type` | circuits | Categórico — callejero vs permanente |
| `driver_experience` | derivado | Carreras previas del piloto |
> `laps` y `finished` fueron excluidas por data leakage (ver nota arriba).
---
## Pipeline del proyecto (notebooks)
| # | Notebook | Contenido | Outputs |
|---|----------|-----------|---------|
| 01 | `01_exploracion_inicial.ipynb` | Carga de datos, esquema de relaciones, primer EDA | 6 |
| 02 | `02_api_y_dataset_maestro.ipynb` | Consumo de API Jolpica-F1, join de tablas, `f1_master.csv` | 11 |
| 03 | `03_limpieza.ipynb` | Tratamiento de nulos, outliers, normalización → `f1_master_clean.csv` (952×31, 0 nulls) | 21 |
| 04 | `04_eda.ipynb` | EDA profundo: correlaciones, ANOVA por equipo, pit stops | 22 |
| 05 | `05_modelos_baseline.ipynb` | Regresión Lineal y Logística + detección de data leakage | 17 |
| 06 | `06_modelos_avanzados.ipynb` | Random Forest y XGBoost (regresión + clasificación), feature importance | — |
| 07 | `07_interpretabilidad_conclusiones.ipynb` | SHAP (summary, waterfall, dependence plots), PDP, conclusiones | — |
## Estructura del proyecto
```
F1-PROYECTO-FINAL/
├── data/
│   ├── circuits.csv ... status.csv     # 11 tablas originales
│   ├── f1_master.csv                   # dataset maestro (NB02)
│   ├── f1_master_clean.csv             # dataset limpio (NB03)
│   └── metricas_modelos.csv            # métricas de todos los modelos
├── notebooks/
│   ├── 01_exploracion_inicial.ipynb
│   ├── 02_api_y_dataset_maestro.ipynb
│   ├── 03_limpieza.ipynb
│   ├── 04_eda.ipynb
│   ├── 05_modelos_baseline.ipynb
│   ├── 06_modelos_avanzados.ipynb
│   └── 07_interpretabilidad_conclusiones.ipynb
├── scripts/
│   └── load_data.py                    # carga y merge automático
├── figures/                             # 22+ visualizaciones exportadas
├── README.md
└── requirements.txt
```
## Cómo reproducir
```bash
git clone https://github.com/mnoero23/F1-PROYECTO-FINAL
cd F1-PROYECTO-FINAL
pip install -r requirements.txt
jupyter notebook notebooks/
```
Ejecutar los notebooks en orden (01 → 07). El notebook 06 puede tardar entre 15 y 25 minutos por el entrenamiento de Random Forest y XGBoost con búsqueda de hiperparámetros.
## Librerías clave
```
pandas, numpy, matplotlib, seaborn, plotly,
scikit-learn, xgboost, shap, geopandas, requests
```
## Limitaciones y próximos pasos
- El dataset no incluye datos meteorológicos (lluvia, temperatura), que influyen en el resultado de carrera.
- No hay datos de telemetría (velocidades, fuerzas G) disponibles públicamente.
- El modelo no captura eventos de carrera como choques o safety cars.
- Próximo paso natural: incorporar datos climáticos vía API y extender el análisis histórico a partir de 1950.
---
## Referencias
- Dataset: [Kaggle — Formula 1 World Championship](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)
- API: [Jolpica-F1](https://github.com/jolpica/jolpica-f1) (reemplazo de Ergast)
- Repositorio del curso: [Jorge-Ruiz-Troccoli/Data-Science-II](https://github.com/Jorge-Ruiz-Troccoli/Data-Science-II)
