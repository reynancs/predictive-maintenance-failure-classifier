
"""
Utility functions for data analysis and preprocessing.

This module contains reusable functions for data manipulation, cleaning,
and analysis tasks across the project notebooks.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Tuple, Dict, Union


def detect_outliers_iqr(data: pd.Series,
                       column: str,
                       lower_factor: float = 1.5,
                       upper_factor: float = 1.5) -> Tuple[pd.Series, Dict[str, float]]:
    """
    Detect outliers in a pandas Series using the Interquartile Range (IQR) method.
    
    Parameters:
    -----------
    data : pd.Series
        The data series to analyze
    column : str
        Name of the column being analyzed (for reporting purposes)
    lower_factor : float, optional (default=1.5)
        Factor to multiply IQR for lower bound
    upper_factor : float, optional (default=1.5)
        Factor to multiply IQR for upper bound
    
    Returns:
    --------
    Tuple[pd.Series, Dict[str, float]]
        - Boolean mask where True indicates an outlier
        - Dictionary with statistics (Q1, Q3, IQR, lower_bound, upper_bound)
    """
    # Calculate Q1, Q3 and IQR
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    
    # Calculate bounds
    lower_bound = Q1 - lower_factor * IQR
    upper_bound = Q3 + upper_factor * IQR
    
    # Create outlier mask
    outlier_mask = (data < lower_bound) | (data > upper_bound)
    
    # Store statistics
    stats = {
        'column': column,
        'Q1': Q1,
        'Q3': Q3,
        'IQR': IQR,
        'lower_bound': lower_bound,
        'upper_bound': upper_bound,
        'n_outliers': outlier_mask.sum(),
        'percentage_outliers': (outlier_mask.sum() / len(data)) * 100
    }
    
    return outlier_mask, stats


def plot_outliers(data: pd.Series,
                 column: str,
                 outlier_mask: pd.Series,
                 stats: Dict[str, float],
                 figsize: Tuple[int, int] = (12, 6)) -> None:
    """
    Plot a boxplot and histogram to visualize outliers in the data.
    
    Parameters:
    -----------
    data : pd.Series
        The data series to plot
    column : str
        Name of the column being plotted
    outlier_mask : pd.Series
        Boolean mask indicating outliers
    stats : Dict[str, float]
        Dictionary with outlier statistics from detect_outliers_iqr
    figsize : Tuple[int, int], optional (default=(12, 6))
        Figure size for the plots
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
    
    # Boxplot
    sns.boxplot(y=data, ax=ax1)
    ax1.set_title(f'Boxplot of {column}')
    
    # Histogram with bounds
    sns.histplot(data=data, ax=ax2)
    ax2.axvline(stats['lower_bound'], color='r', linestyle='--', label='Lower bound')
    ax2.axvline(stats['upper_bound'], color='r', linestyle='--', label='Upper bound')
    ax2.set_title(f'Distribution of {column} with Outlier Bounds')
    ax2.legend()
    
    plt.suptitle(f'Outlier Analysis for {column}\n'
                f"Number of outliers: {stats['n_outliers']} "
                f"({stats['percentage_outliers']:.2f}%)")
    plt.tight_layout()
    

def handle_outliers(data: pd.Series,
                   method: str = 'remove',
                   stats: Dict[str, float] = None) -> pd.Series:
    """
    Handle outliers in the data using the specified method.
    
    Parameters:
    -----------
    data : pd.Series
        The data series containing outliers
    method : str, optional (default='clip')
        Method to handle outliers:
        - 'clip': Clip values to the bounds
        - 'median': Replace outliers with median
        - 'remove': Remove outliers (returns smaller series)
    stats : Dict[str, float], optional
        Statistics dictionary from detect_outliers_iqr
        Required if method is 'clip'
    
    Returns:
    --------
    pd.Series
        Data with outliers handled according to specified method
    """
    if stats is None and method == 'clip':
        raise ValueError("Stats dictionary required for clip method")
    
    if method == 'clip':
        return data.clip(lower=stats['lower_bound'], upper=stats['upper_bound'])
    elif method == 'median':
        outlier_mask, _ = detect_outliers_iqr(data, str(data.name))
        data_handled = data.copy()
        data_handled[outlier_mask] = data.median()
        return data_handled
    elif method == 'remove':
        outlier_mask, _ = detect_outliers_iqr(data, str(data.name))
        data_handled = pd.concat([data[~outlier_mask], data[outlier_mask]])
        return data_handled
    else:
        raise ValueError(f"Unknown method: {method}. Use 'clip', 'median', or 'remove'")


def analyze_outliers(df: pd.DataFrame,
                    columns: List[str],
                    handle_method: str = None) -> pd.DataFrame:
    """
    Analyze outliers in multiple columns of a DataFrame and optionally handle them.
    
    Parameters:
    -----------
    df : pd.DataFrame
        The DataFrame to analyze
    columns : List[str]
        List of column names to analyze
    handle_method : str, optional (default=None)
        Method to handle outliers ('clip', 'median', 'remove', or None)
        If None, outliers will not be handled
    
    Returns:
    --------
    pd.DataFrame
        DataFrame with outlier analysis results and optionally handled outliers
    """
    results = []
    
    for col in columns:
        # Skip non-numeric columns
        if not np.issubdtype(df[col].dtype, np.number):
            continue
            
        # Detect outliers
        outlier_mask, stats = detect_outliers_iqr(df[col], col)
        
        # Plot outliers
        plot_outliers(df[col], col, outlier_mask, stats)
        
        # Handle outliers if requested
        if handle_method:
            df[col] = handle_outliers(df[col], method=handle_method, stats=stats)
        
        # Store results
        results.append({
            'column': col,
            'n_outliers': stats['n_outliers'],
            'percentage_outliers': stats['percentage_outliers'],
            'lower_bound': stats['lower_bound'],
            'upper_bound': stats['upper_bound']
        })
    
    return pd.DataFrame(results)
