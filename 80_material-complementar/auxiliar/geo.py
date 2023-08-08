import numpy as np
import matplotlib.pyplot as pl


def legenda_no_mapa(gdf, labels, disperse=0, ha='center', va='center', ax=None, **kwargs):
    """
    Show the labels of regions on the map.
    
    Parameters
    ----------
    gdf : GeoDataFrame
        GeoDataFrame containing the geometry for 
        which to show the labels.
    labels : array-like or str
        The labels of each geometry in `gdf`, 
        in the same order, or the name of 
        the column in `gdf` containing the 
        labels.
    disperse : float
        If > 0, the standard deviation of 
        random displacements of the labels 
        around the representative points of 
        the geometries, in the same units as 
        the geometries' coordinates.
    """
    # Standardize input to iterable:
    if type(labels) == str:
        labels = gdf[labels]

    # Get region's representative points:
    loc = gdf.representative_point()
    
    # Generate displacements for labels:
    if disperse > 0:
        ex = np.random.normal(0, disperse, len(loc))
        ey = np.random.normal(0, disperse, len(loc)) 
    else:
        ex = np.zeros_like(loc)
        ey = np.zeros_like(loc)
    
    # Add labels to map:
    for t, x, y in zip(labels, loc.x + ey, loc.y + ey):
        if ax is None:
            pl.annotate(t, (x, y), ha=ha, va=va, **kwargs)
        else:
            ax.annotate(t, (x, y), ha=ha, va=va, **kwargs)
