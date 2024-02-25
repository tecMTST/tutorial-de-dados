import pandas as pd
import numpy as np
import scipy as sc
import matplotlib.pyplot as pl


def to_lognormal_pars(mean, dev, shift):
    """
    Convert the `mean` (float) value of a lognormal distribution,
    its standard deviation `dev` (float) and the `shift` (float)
    -- where `-shift` is the minimum value of the distribution --
    into (mu, sigma, shift) parameters for the shifted lognormal 
    distribution.
    """
    #assert mean + shift > 0, '`mean` needs to be greater that `-shift`.'
    a2 = (mean + shift)**2
    v  = dev ** 2
    mu = np.log(a2 / np.sqrt(a2 + v))
    s  = np.sqrt(np.log(1 + v / a2))
    
    return mu, s, shift


def gen_lognormal_llevel(mu, s, shift):
    """
    Returns a lognormal pdf f(x) (function) with parameters
    `mu` (float), `s` (sigma, float) and `shift` -- where 
    `-shift` is the minimum value of the distribution.
    """
    def f(x):
        #return np.exp(-(np.log(x + shift) - mu)**2 / (2 * s**2)) / ((x + shift) * s * np.sqrt(2*np.pi))
        return sc.stats.distributions.lognorm.pdf(x + shift, s, scale=np.exp(mu))
    return f


def gen_lognormal(mean, dev, shift):
    """
    Returns a lognormal pdf f(x) (function) with the
    statistical measures `mean` (float), standard 
    deviation `dev` (float) and `shift` (float).
    `-shift` is the minimum value of x.
    """
    
    mu, s, shift = to_lognormal_pars(mean, dev, shift)
    f = gen_lognormal_llevel(mu, s, shift)
    
    return f


def lognormal_pdf(x, mu, sig, shift):
    """
    Uma distribuição lognormal transladada.
    `-shift` é o menor valor com probabilidade
    não nula da PDF.
    """
    z = x + shift 
    norm = 1.0 / (z * sig * np.sqrt(2 * np.pi))
    expo = np.exp(-(np.log(z) - mu)**2 / (2 * sig**2))
    return norm * expo

    
def plot_esperado(N, probs, label=None, linestyle=None, linewidth=1.5, cmap='tab10', idade_min=0):
    """
    Cria gráfico do número esperado de mortes por idade, para
    homens e mulheres, de acordo com um modelo.

    Parâmetros
    ----------
    N : int
        Número total de mortes.
    probs : array 1D de floats (2 * n_idades)
        Probabilidades de morte por idade para homens 
        (probs[:n_idades]) e para mulheres 
        (probs[n_idades:]).
    """
    cmap = pl.get_cmap(cmap)
    n_idades = int(len(probs) / 2)
    probH = probs[:n_idades]
    probM = probs[n_idades:]
    idade = np.arange(idade_min, idade_min + n_idades)
    
    pl.subplot(2,1,1)
    pl.plot(idade, N * probH, label=label, color=cmap(0), linestyle=linestyle, linewidth=linewidth)
    pl.legend()
    pl.subplot(2,1,2)
    pl.plot(idade, N * probM, label=label, color=cmap(1), linestyle=linestyle, linewidth=linewidth)
    pl.legend()


def get_chains(idata, par_name):
    """
    Extract chains from pyMC `idata` to a numpy array.
    """
    # Get data specs:
    n_chains = idata['posterior'].dims['chain']
    n_draws  = idata['posterior'].dims['draw']
    
    # Stack parallel chains into a single sampling set:
    if par_name in idata['posterior'].dims:
        n_cells  = idata['posterior'].dims[par_name]
        stacked_chains = np.array(idata['posterior'][par_name]).reshape((n_chains * n_draws, n_cells))
    else:
        stacked_chains = np.array(idata['posterior'][par_name]).reshape((n_chains * n_draws,))

    return stacked_chains


def idata2df(idata):
    """
    Extrai pontos de uma cadeia de Markov guardada num
    objeto `idata` do pyMC para um DataFrame. Cada 
    variável amostrada vai para uma coluna. 
    """
    posterior = idata['posterior']
    vars = list(posterior.data_vars.variables)
    df = pd.DataFrame({v:get_chains(idata, v) for v in vars})
    return df


def scale_model(df, N):
    model_df = N * df[['f_homens','f_mulheres']]
    model_df['e_homens'] = np.sqrt(model_df['f_homens'])
    model_df['e_mulheres'] = np.sqrt(model_df['f_mulheres'])
    return model_df