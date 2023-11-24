import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t

def plot_confidence_interval(df, alpha, interval_type='two-sided'):
    # t-distribution range for plotting
    t_values = np.linspace(t.ppf(0.001, df), t.ppf(0.999, df), 100)
    t_pdf = t.pdf(t_values, df)

    plt.figure(figsize=(10, 5))
    plt.plot(t_values, t_pdf, label=f't-distribution (df={df})')

    if interval_type == 'lower':
        # Lower one-sided t-value
        t_critical = t.ppf(alpha, df)
        plt.fill_between(t_values, t_pdf, where=(t_values <= t_critical), color='red', alpha=0.5,
                         label=f'Lower {alpha*100}% area')
        plt.axvline(x=t_critical, color='black', linestyle='--', label=f'Critical t-value (t={t_critical:.3f})')
    elif interval_type == 'upper':
        # Upper one-sided t-value
        t_critical = t.ppf(1 - alpha, df)
        plt.fill_between(t_values, t_pdf, where=(t_values >= t_critical), color='blue', alpha=0.5,
                         label=f'Upper {alpha*100}% area')
        plt.axvline(x=t_critical, color='black', linestyle='--', label=f'Critical t-value (t={t_critical:.3f})')
    elif interval_type == 'two-sided':
        # Two-sided t-values
        t_critical_lower = t.ppf(alpha / 2, df)
        t_critical_upper = t.ppf(1 - alpha / 2, df)
        plt.fill_between(t_values, t_pdf, where=((t_values >= t_critical_lower) & (t_values <= t_critical_upper)),
                         color='green', alpha=0.5, label=f'Middle {100 - alpha*100}% area')
        plt.axvline(x=t_critical_lower, color='black', linestyle='--', label=f'Critical t-value lower (t={t_critical_lower:.3f})')
        plt.axvline(x=t_critical_upper, color='black', linestyle='--', label=f'Critical t-value upper (t={t_critical_upper:.3f})')

    plt.title(f'{interval_type.capitalize()} t-Distribution Confidence Interval')
    plt.xlabel('t-value')
    plt.ylabel('Probability Density')
    plt.legend(loc='upper right')
    plt.show()

# Example usage:
df = 36
alpha = 0.1
plot_confidence_interval(df, alpha, interval_type='lower')
# plot_confidence_interval(df, alpha, interval_type='upper')
# plot_confidence_interval(df, alpha, interval_type='two-sided')
