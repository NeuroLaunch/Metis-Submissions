#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Utility functions to run statistics and display data for classification.

For Metis Weeks 4-6, Project McNulty.

@author: Steven Bierer
Created on Sun Oct 29 2018
"""

import numpy as np
import itertools

from sklearn.metrics import confusion_matrix, accuracy_score, \
                            recall_score, precision_score, f1_score
from sklearn.metrics import classification_report
from sklearn.utils import class_weight

import matplotlib.pyplot as plt
import seaborn as sns

def plot_confusion_matrix(cm, class_names, title='Confusion matrix',
    normalize=True, cmap=plt.cm.Blues_r):
    """
    Plot an sklearn confusion matrix (cm).

    Arguments
    ---------
    cm:         confusion matrix from sklearn.metrics.confusion_matrix
    target_names: given classification classes such as [0, 1, 2]
                  the class names, for example: ['high', 'medium', 'low']
    title:      the text to display at the top of the matrix
    cmap:         the gradient of the values displayed from matplotlib.pyplot.cm
                  see http://matplotlib.org/examples/color/colormaps_reference.html
                  plt.get_cmap('jet') or plt.cm.Blues
    normalize:  If False, plot the raw numbers; if True (default), plot the proportions
    
    Modified from https://stackoverflow.com/questions/39033880/
      plot-confusion-matrix-sklearn-with-multiple-labels
    """
    cm_norm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    if normalize:
        cm_plot = cm_norm
    else:
        cm_plot = cm
        
    plt.figure(figsize=(8, 6));
    plt.imshow(cm_plot, interpolation='nearest', cmap=cmap);
    plt.colorbar();
    plt.tight_layout();

    if class_names is not None:
        name_list = [x for x in class_names.values()]
        tick_marks = np.arange(len(name_list))
        plt.xticks(tick_marks, name_list, rotation=45, ha='right');
        plt.yticks(tick_marks, name_list);

    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        thresh = cm_plot.max() * 0.7
        plt.text(j, i, "{:,}".format(cm[i, j]),
            horizontalalignment="center",
            color="black" if cm_plot[i, j] > thresh else "white");

    plt.ylabel('True Class', rotation = 0, ha='right', fontweight='bold');
    plt.gca().yaxis.set_label_coords(-0.02,1.02)
    
    plt.xlabel('Predicted Class', fontweight='bold');
    plt.title(title);
    
    return plt


# Define function to give different statistics plus a confusion matrix. #
def report_scores(ytrue, ypred, class_names=None, wt_type=None, label=''):
    '''
    Give statistics and confusion mx based on actual + predicted classes.
    
    Arguments give class labels as a list and weighting as None or 'balanced';
    label supplies a title for the confusion matrix.
    '''
    if class_names and class_names=='balanced':
        avg_type = 'weighted'
    else:
        avg_type = 'macro'
    wt_vec = class_weight.compute_sample_weight(wt_type, ytrue)
    
    accuracy = accuracy_score(ytrue, ypred, sample_weight=wt_vec)
    precision = precision_score(ytrue, ypred, average=avg_type)
    recall = recall_score(ytrue, ypred, average=avg_type)
    f1 = f1_score(ytrue, ypred, average=avg_type)
    
    name_list = [x for x in class_names.values()]
    print(classification_report(ytrue, ypred, target_names=name_list, sample_weight=wt_vec))
    print('\n')
    
    print(f"-- Metric ----- {label} ----")
    print(f" Accuracy:  {accuracy:10.3f}")
    print(f" Precision: {precision:10.3f}")
    print(f" Recall:    {recall:10.3f}")
    print(f" F1 Score:  {f1:10.3f}")
    print('\n')
    
    cm = confusion_matrix(ytrue, ypred);
    cm_plt = plot_confusion_matrix(cm, class_names, normalize=True, title='');
    
    return cm_plt


def accuracy_weighted(ytrue, ypred, class_weights):
    '''
    Custom function for scoring classifiers that balances the classes
    
    Necessary, as GridSearchCV doesn't play nicely with KNN class weighting.
    '''
    if len(class_weights) != ytrue.nunique():
        raise ValueError('Class_weights did not match labels in ytrue.')
    wt_vec = np.array([class_weights[x-1] for x in ytrue.values])
    score = accuracy_score(ytrue, ypred, sample_weight=wt_vec)
    
    return score


def row2grid(data):
    ''' Plot row of LandSat "raw" dataframe as a 9x9 grid. '''
    
    sa_idx = list(range(1,34,4))   # first, get column indexes at all pixels
    sb_idx = list(range(2,37,4))   #   for each component
    sc_idx = list(range(3,37,4))
    sd_idx = list(range(4,37,4))
    
    cmap_green = plt.cm.Greens
    cmap_red = plt.cm.Reds
    cmap_nearir = plt.cm.BuPu
    cmap_ir = plt.cm.Oranges
    
    data_a = data[sa_idx].values.reshape(3,3)
    data_b = data[sb_idx].values.reshape(3,3)
    data_c = data[sc_idx].values.reshape(3,3)
    data_d = data[sd_idx].values.reshape(3,3)

    fig, axset = plt.subplots(2, 2, figsize=[12,10])

    ax = axset[0][0]
    sns.heatmap(data_a, vmin=50, vmax=100, cmap=cmap_green, ax=ax);
    ax.set_title('Green Component');

    ax = axset[0][1]
    sns.heatmap(data_b, vmin=50, vmax=130, cmap=cmap_red, ax=ax);
    ax.set_title('Red Component');

    ax = axset[1][0]
    sns.heatmap(data_c, vmin=50, vmax=130, cmap=cmap_nearir, ax=ax);
    ax.set_title('Near IR Component');

    ax = axset[1][1]
    sns.heatmap(data_d, vmin=50, vmax=130, cmap=cmap_ir, ax=ax);
    ax.set_title('IR Component');

    for ax in axset.flatten():
        ax.set_xticks([]); ax.set_yticks([])
    
    return fig



# --------------------------------------------------------------------------

if __name__ == "__main__":
    # For debugging purposes #
    pass;


