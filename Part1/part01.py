#!/usr/bin/env python3
"""
IZV cast1 projektu
Autor: Hung Do (xdohun00)

Detailni zadani projektu je v samostatnem projektu e-learningu.
Nezapomente na to, ze python soubory maji dane formatovani.

Muzete pouzit libovolnou vestavenou knihovnu a knihovny predstavene na prednasce
"""


from bs4 import BeautifulSoup
import requests
import numpy as np
import matplotlib.pyplot as plt
from typing import List


def integrate(x: np.ndarray, y: np.ndarray) -> float:
    return np.sum( (x[1:] - x[:-1]) * (y[:-1] + y[1:]) / 2)


def generate_graph(a: List[float], show_figure: bool = False, save_path: str | None=None):
    # setup graph
    fig = plt.figure(figsize=(8, 4))
    ax = fig.add_subplot()
    ax.set_xlabel('x')
    ax.set_ylabel('$f_{a}(x)$')
    ax.set_xlim(-3, 3.9)

    # generates plots
    x = np.linspace(-3, 3, 100)
    for value in a:
        label = f'$y_{{{value}}}(x)$'
        y = value * x ** 2
        ax.plot(x, y, label=label)
        ax.fill_between(x, 0, y, alpha=0.2)
        ax.annotate(xy=(x[-1], y[-1]), text=f'$\int f_{{{value}}}(x)dx$')
    ax.legend(loc='lower center', bbox_to_anchor=(0.5,1.0), ncol=len(a))


    if show_figure:
        plt.show()
    if save_path is not None:
        fig.savefig(save_path)
    plt.close(fig)



def generate_sinus(show_figure: bool=False, save_path: str | None=None):
    # setup graph
    fig, ax = plt.subplots(3, 1, figsize=(6,4))
    for a in ax:
        a.set_xlim(0, 100)
        a.yaxis.set_ticks([-0.8, -0.4, 0, 0.4, 0.8])
        a.set_ylim(-0.8, 0.8)
        a.set_xlabel('t')
    ax[0].set_ylabel('$f_{1}(x)$')
    ax[1].set_ylabel('$f_{2}(x)$')
    ax[2].set_ylabel('$f_{1}(x) + f_{2}(x)$')

    # get points
    t = np.linspace(0, 100, 10000)
    f1 = 0.5 * np.sin(t * np.pi / 50)
    f2 = 0.25 * np.sin(t * np.pi)
    # plot first 2 graphs
    ax[0].plot(t, f1)
    ax[1].plot(t, f2)

    # filter negative and positive f2 values
    neg_index = f2 > 0
    pos_f = f1+f2
    pos_f[~neg_index] = np.nan
    ax[2].plot(t, pos_f, color='green')

    neg_f = f1+f2
    neg_f[neg_index] = np.nan
    ax[2].plot(t, neg_f, color='red')

    if show_figure:
        plt.show()
    if save_path is not None:
        fig.savefig(save_path)
    plt.close(fig)


def download_data(url="https://ehw.fit.vutbr.cz/izv/temp.html") -> list:
    return []


def get_avg_temp(data, year=None, month=None) -> float:
    return 0.0
