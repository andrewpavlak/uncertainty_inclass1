# uncertainty_inclass1
First In Class Repo

## Exercise 2: Quantiles, IQR, Whiskers, Boxplot, Outliers
From the ECDF, we get a fairly good picture of the distribution of the data: A **quantile** adjusts the concept of the median so that instead of 50% of the mass below and 50% above, the $q$-quantile has $q$% of the mass below and $(1-q)$% of the mass above.

Write a Python class that:
- Computes the ECDF $\hat{F}_N(x)$: Andrew
- Has a method to compute any quantile without using Numpy: Jeff, Weston 
- Has a method to compute the **Interquartile Range (IQR)** -- the .25 quantile and the .75 quantile, which brackets 50% of the data -- and the **whiskers**: $\pm 1.5 \times \text{IQR}$ from the edges of the IQR: Sammy
- Has a method to compute a five-number summary/boxplot: the whiskers, the minimum and maximum, the IQR and the median: Mauricio
- Compare your answers with `sns.boxplot`; making a boxplot yourself is kind of a pain, but you could make a 5-number summary visualization
- Anything outside the whiskers is an **outlier**; write a method that returns a Boolean vector indicating if the observations are outliers

Then use your ECDF class to analyze numeric variables from a dataset of your choice
