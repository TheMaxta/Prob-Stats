import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t

# Parameters for the t-distribution
df = 31
alpha = 0.05

# t-distribution range for plotting
t_values = np.linspace(t.ppf(0.001, df), t.ppf(0.999, df), 100)
t_pdf = t.pdf(t_values, df)

# t-critical for one-sided lower confidence interval
t_critical = t.ppf(alpha, df)

# Plotting the t-distribution
plt.figure(figsize=(10, 5))
plt.plot(t_values, t_pdf, label=f't-distribution (df={df})')

# Filling the confidence interval area
plt.fill_between(t_values, t_pdf, where=(t_values <= t_critical), color='red', alpha=0.5,
                 label=f'Lower {alpha*100}% area')

# Line for critical t-value
plt.axvline(x=t_critical, color='black', linestyle='--', label=f'Critical t-value (t={t_critical:.3f})')

# Annotations
plt.title('One-Sided Lower t-Distribution Confidence Interval')
plt.xlabel('t-value')
plt.ylabel('Probability Density')
plt.legend(loc='upper right')

# Show the plot
plt.show()
