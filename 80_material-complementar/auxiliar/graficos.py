"""
New plots and auxiliary plotting functions.
Copyright (C) 2023  Henrique S. Xavier
Contact: hsxavier@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as pl


def multiple_bars_plot(df, colors=None, alpha=None, err=None, width=0.8, rotation=0, horizontal=False):
    """
    Create a bar plot with bars from different columns 
    in `df` side by side.
    
    Parameters
    ----------
    df : DataFrame
        Data to plot as bars. Each row corresponds to a 
        different entry, translating to bar positions, 
        and each column correponds to a different data 
        series, each with a different color. The series
        labels are the column names and the bar location
        labels are the index. The data is plotted in the
        order set in `df`.
    colors : list, str or None.
        Colors for the data series (`df` columns).    
    alpha : list, float or None.
        Transparency of the columns.
    err : DataFrame, tuple of two DataFrames, or None    
        Errors for the data in `df`, to be plot as error 
        bars. They should have the same structure as `df`.
        If one DataFrame, use simmetrical error bars. If 
        a tuple of DataFrames, they are the lower and upper
        errors. If None, do not draw error bars.
    width : float
        Total column width formed by all summing the 
        widths of each data series.
    rotation : float
        Rotation of the column axis labels, given 
        in degrees.
    horizontal : bool
        Whether to use horizontal bar plot or not.
    """
    
    # Count number of columns (associated to bar colors):
    cols   = df.columns
    n_cols = len(cols)
    # Count number of rows (associated to bar positions):
    rows   = df.index
    n_rows = len(rows)

    # Standardize input:
    if type(colors) != list:
        colors = [colors] * n_cols
    if type(alpha) != list:
        alpha = [alpha] * n_cols

    # Organize errors, if provided:
    if err is not None:
        
        # Standardize one error to simmetrical errors:
        if type(err) == pd.core.frame.DataFrame:
            err = (err, err)
        assert type(err) == tuple, '`err` must be a DataFrame or a tuple of DataFrames.'
        assert len(err) == 2, '`err` must have two elements.'

        # Check that the errors table have the same structure as the data:
        for i, e in enumerate(err):
            assert set(e.columns) == set(df.columns), 'Columns in `err` {} are not the same as in `df`.'.format(i + 1)
            assert set(e.index) == set(df.index), 'Index in `err` {} are not the same as in `df`.'.format(i + 1)
            
        # Order the errors like the data:
        err0_df = err[0].loc[df.index]
        err1_df = err[1].loc[df.index]
    
    # Set plotting x position:
    ind = np.arange(n_rows)
    # Set width of columns:
    wid = width / n_cols
    
    # Loop over columns:
    for i, col in enumerate(cols):
        
        # Select the columns' errors:
        if err is not None:
            err0 = err0_df[col].values
            err1 = err1_df[col].values
            errs = np.stack([err0, err1])
        else:
            errs = None
        
        # Bar plot:
        if horizontal:
            pl.barh(ind - wid / 2 * (n_cols - 1) + wid * i, df[col], height=wid, xerr=errs, ecolor=colors[i], color=colors[i], alpha=alpha[i], label=col)
        else:
            pl.bar(ind - wid / 2 * (n_cols - 1) + wid * i, df[col], width=wid, yerr=errs, ecolor=colors[i], color=colors[i], alpha=alpha[i], label=col)

    # Set tick labels:
    ax = pl.gca()
    if horizontal:
        ax.set_yticks(ind)
        ax.set_yticklabels(rows, rotation=rotation)
    else:
        ax.set_xticks(ind)
        ax.set_xticklabels(rows, rotation=rotation)

def graf_barra_2(df, xmin=-1, xmax=90, cmap='tab10', alpha=0.5, ylabel=None, ylim=None, grid_axis=None):
    """
    Cria dois gráficos de barras, um com a primeira coluna de 
    `df` (DataFrame) e outro com a segunda. O índice de `df`
    serve de eixo x. Assumimos que só existem duas colunas em 
    `df`.
    """
    cmap = pl.get_cmap(cmap)
    for i, c in enumerate(df.columns):
        pl.subplot(2, 1, i + 1)
        pl.bar(df.index, df.iloc[:, i], color=cmap(i), alpha=alpha, label=c)
        pl.xlim([xmin, xmax])
        pl.ylim(ylim)
        pl.ylabel(ylabel)
        pl.legend()
        if grid_axis != None:
            pl.grid(axis=grid_axis)
    pl.subplots_adjust(hspace=0)