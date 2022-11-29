#!/usr/bin/env python3.9
# coding=utf-8

from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import zipfile

# muzete pridat libovolnou zakladni knihovnu ci knihovnu predstavenou na prednaskach
# dalsi knihovny pak na dotaz

# Ukol 1: nacteni dat ze ZIP souboru
def load_data(filename : str) -> pd.DataFrame:
    # tyto konstanty nemente, pomuzou vam pri nacitani
    headers = ["p1", "p36", "p37", "p2a", "weekday(p2a)", "p2b", "p6", "p7", "p8", "p9", "p10", "p11", "p12", "p13a",
                "p13b", "p13c", "p14", "p15", "p16", "p17", "p18", "p19", "p20", "p21", "p22", "p23", "p24", "p27", "p28",
                "p34", "p35", "p39", "p44", "p45a", "p47", "p48a", "p49", "p50a", "p50b", "p51", "p52", "p53", "p55a",
                "p57", "p58", "a", "b", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "o", "p", "q", "r", "s", "t", "p5a"]

    #def get_dataframe(filename: str, verbose: bool = False) -> pd.DataFrame:
    regions = {
        "PHA": "00",
        "STC": "01",
        "JHC": "02",
        "PLK": "03",
        "ULK": "04",
        "HKK": "05",
        "JHM": "06",
        "MSK": "07",
        "OLK": "14",
        "ZLK": "15",
        "VYS": "16",
        "PAK": "17",
        "LBK": "18",
        "KVK": "19",
    }

    # extract keys and values for later use
    region_keys = list(regions.keys())
    region_values = list(regions.values())

    dfs = []
    with zipfile.ZipFile(filename, mode='r') as z:
        # iterate through years
        for year_zip in z.namelist():
            with zipfile.ZipFile(z.open(year_zip)) as inner_zip:
                # iterate through regions
                for csv_file in inner_zip.namelist():
                    # filter out unwanted files
                    file_name = csv_file.rsplit('.')[0]
                    if file_name not in region_values:
                        continue

                    df = pd.read_csv(inner_zip.open(csv_file), encoding='cp1250', sep=';', low_memory=False, names=headers)
                    # set region name
                    df['region'] = region_keys[region_values.index(file_name)]
                    dfs.append(df)
    df = pd.concat(dfs, ignore_index=True)
    return df

# Ukol 2: zpracovani dat
def parse_data(df : pd.DataFrame, verbose : bool = False) -> pd.DataFrame:
    print(df[['p2a', 'region']])
    return pd.DataFrame()

# Ukol 3: počty nehod v jednotlivých regionech podle viditelnosti
def plot_visibility(df: pd.DataFrame, fig_location: str | None = None,
                    show_figure: bool = False):
    pass

# Ukol4: druh srážky jedoucích vozidel
def plot_direction(df: pd.DataFrame, fig_location: str | None = None,
                   show_figure: bool = False):
    pass

# Ukol 5: Následky v čase
def plot_consequences(df: pd.DataFrame, fig_location: str | None = None,
                    show_figure: bool = False):
    pass

if __name__ == "__main__":
    # zde je ukazka pouziti, tuto cast muzete modifikovat podle libosti
    # skript nebude pri testovani pousten primo, ale budou volany konkreni
    # funkce.
    #%%%df = load_data("data/data.zip")
    df2 = parse_data(df, True)

    # plot_visibility(df2, "01_visibility.png")
    # plot_direction(df2, "02_direction.png", True)
    # plot_consequences(df2, "03_consequences.png")


# Poznamka:
# pro to, abyste se vyhnuli castemu nacitani muzete vyuzit napr
# VS Code a oznaceni jako bunky (radek #%%% )
# Pak muzete data jednou nacist a dale ladit jednotlive funkce
# Pripadne si muzete vysledny dataframe ulozit nekam na disk (pro ladici
# ucely) a nacitat jej naparsovany z disku

# %%
