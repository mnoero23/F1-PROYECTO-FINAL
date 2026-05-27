"""
load_data.py — Carga y preprocesamiento base del dataset F1
"""
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

def load_all():
    tables = ['circuits', 'constructors', 'drivers', 'races', 'results',
              'qualifying', 'pit_stops', 'lap_times', 'driver_standings',
              'constructor_standings', 'status']
    return {t: pd.read_csv(DATA_DIR / f"{t}.csv") for t in tables}

def build_master(dfs, years=None):
    results = dfs['results'].copy()
    races   = dfs['races'][['raceId','year','round','circuitId','name']].rename(columns={'name':'race_name'})
    drivers = dfs['drivers'][['driverId','code','forename','surname','nationality','dob']].copy()
    drivers['driver_name'] = drivers['forename'] + ' ' + drivers['surname']
    constructors = dfs['constructors'][['constructorId','name','nationality']].rename(columns={'name':'team','nationality':'team_nationality'})
    circuits = dfs['circuits'][['circuitId','name','country','lat','lng']].rename(columns={'name':'circuit_name'})

    master = (results
        .merge(races, on='raceId')
        .merge(drivers, on='driverId')
        .merge(constructors, on='constructorId')
        .merge(circuits, on='circuitId'))

    for col in ['position','grid','points']:
        master[col] = pd.to_numeric(master[col], errors='coerce')

    if years:
        master = master[master['year'].isin(years)]
    return master

if __name__ == "__main__":
    dfs = load_all()
    master = build_master(dfs)
    print(f"Dataset maestro: {master.shape}")
    print(master.dtypes)
