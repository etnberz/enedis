# @Author: Maxime Caïtucoli <maxime>
# @Date:   2019-05-01T15:21:30+08:00
# @Last modified by:   maxime
# @Last modified time: 2019-05-02T16:06:38+08:00

from .imports import *

def hist_plot(df_to_plot, save=False):

    '''Plots Time Series simple graph

    Args :
        df_to_plot (pd.Dataframe) : dataframe to plot
        save (boolean) : wheter we save or not the figure

    Returns :
        None'''

    title_font = {'family': 'serif',
                  'color':  'black',
                  'weight': 'bold',
                  'size': 16,
                  }

    columns = 2
    cols_to_plot = df_to_plot.columns
    rows = int(len(cols_to_plot)/2) + 1

    fig = plt.figure(figsize=(6*columns, 3*rows))
    fig.suptitle("Columns Distribution", fontdict=title_font, y=1)

    for i, target in enumerate(cols_to_plot):

        ax = fig.add_subplot(rows, columns, i+1)
        plt.title(target)
        df_to_plot[target].hist()
        plt.tight_layout()

    if save:
        plt.savefig('columns_distrib.png')

    plt.show()

def corr_matrix(df_to_corr, save=False):

    '''Plots Correlation Heatmap

    Args :
        df_to_corr (pd.Dataframe) : dataframe to plot
        save (boolean) : wheter we save or not the figure

    Returns :
        None'''


    corr_mat = df_to_corr.corr()
    plt.figure(figsize=(15,15))
    sns.heatmap(corr_mat)

    if save:
        plt.savefig('corr_heatmap.png', bbox_inches="tight")
    plt.show()

def plot_feature_corr(df_to_corr, targets, save=False):

    '''Plots Absolute Features Correlation with the Targets of a dataframe

    Args :
        df_to_corr (pd.Dataframe) : dataframe which contains features and targets
        targets (str or list of str) : name(s) of the target(s)
        save (boolean) : wheter we save or not the figure

    Returns :
        None'''

    title_font = {'family': 'serif',
                  'color':  'black',
                  'weight': 'bold',
                  'size': 16,
                  }

    if isinstance(targets, str):
        targets = [targets]

    for target in targets:
        col_to_del = targets.copy()
        col_to_del.remove(target)
        col_to_del.append('IDS')
        df_corr = df_to_corr.corrwith(df_to_corr[target]).apply(abs)\
        .sort_values(ascending=False).drop(col_to_del).to_frame()
        plt.figure(figsize=(2,10))
        plt.title('Features Correlation with {}'.format(target), pad=20, fontdict=title_font)
        sns.heatmap(df_corr, annot=True)

        if save:
            plt.savefig('feat_corr_{}.png'.format(target), bbox_inches="tight")

        plt.show()

def ts_simple_plot(df_to_plot, targets, save=False):

    '''Plots Time Series simple graph

    Args :
        df_to_plot (pd.Dataframe) : dataframe which contains features and targets
        targets (str or list of str) : name(s) of the target(s)
        save (boolean) : wheter we save or not the figure

    Returns :
        None'''

    title_font = {'family': 'serif',
                  'color':  'black',
                  'weight': 'bold',
                  'size': 16,
                  }

    if isinstance(targets, str):
        targets = [targets]
        columns = 1
        rows = 1
        title = ""

    else:
        columns = 2
        rows = int(len(targets)/2) + 1
        title = "Targets Time Series"

    fig = plt.figure(figsize=(6*columns, 3*rows))
    fig.suptitle(title, fontdict=title_font, y=1)

    for i, target in enumerate(targets):

        ax = fig.add_subplot(rows, columns, i+1)
        plt.title(target)
        df_to_plot[target].dropna().plot()
        plt.tight_layout()

    if save:
        plt.savefig('simple_time_series.png')

    plt.show()


def ts_analysis_plot(df_to_plot, target, save=False):

    '''Plots Time Series simple graph

    Args :
        df_to_plot (pd.Dataframe) : dataframe which contains features and targets
        target (str) : name of the target
        save (boolean) : wheter we save or not the figure

    Returns :
        None'''

    title_font = {'family': 'serif',
        'color':  'black',
        'weight': 'bold',
        'size': 16,
        }

    columns = 2
    rows = 4
    title = "Time Series Analysis : {}".format(target)

    fig = plt.figure(figsize=(6*columns, 3*rows))
    fig.suptitle(title, fontdict=title_font, y=1)

    gs = gridspec.GridSpec(rows, columns)


    # AUTOCORRELATION

    axe = plt.subplot(gs[0, :])
    plt.title('Autocorrelation')
    pd.plotting.autocorrelation_plot(df_to_plot[target].dropna(), ax=axe)
    plt.tight_layout()

    # Time serie

    axe = plt.subplot(gs[1, :])
    plt.title('Time serie')
    df_to_plot[target].dropna().plot()
    plt.tight_layout()

    # HOUR MEAN

    axe = plt.subplot(gs[2, 0])
    plt.title('Hour Mean')
    df_to_plot[target].dropna().resample('H').mean().plot()
    plt.xlabel('')
    plt.tight_layout()

    # DAY MEAN

    axe = plt.subplot(gs[2, 1])
    plt.title('Day Mean')
    df_to_plot[target].dropna().resample('D').mean().plot()
    plt.xlabel('')
    plt.tight_layout()

    # WEEK MEAN

    axe = plt.subplot(gs[3, 0])
    plt.title('Week Mean')
    df_to_plot[target].dropna().resample('W').mean().plot()
    plt.xlabel('')
    plt.tight_layout()

    # MONTH MEAN

    axe = plt.subplot(gs[3, 1])
    plt.title('Month Mean')
    df_to_plot[target].dropna().resample('M').mean().plot()
    plt.xlabel('')
    plt.tight_layout()

    if save:
        plt.savefig('time_series_analysis_{}.png'.format(target))
    plt.show()
