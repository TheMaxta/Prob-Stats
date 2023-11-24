# Enter data set (manual data entry)

samp<-c(1.5 , 10.7 , 2.6 , 7.4 , 0.4 , 4.8 , 7.3 , 4.6 , 1.7 , 1.8 , 
        3.8 , 3.5 , 1.2 , 0.8 , 1.7 , 9.9 , 7.3 , 6.8 , 2.5 , 4.4 , 
        7.5 , 4.5 , 1.3 , 5.2, 10.6 , 0.7 , 3.5 , 1.3 , 1.5 , 5.3)
 
# Compute mean and standard deviation
mean(samp)
sd(samp)

# Compute five-number summary and boxplot
fivenum(samp)
boxplot(samp, horizontal = TRUE,  xlab = "Minutes between foul shots")

#Stem and Leaf Plots

stem(samp)
 
#Histogram
hist(samp,
     freq = FALSE,
     xlab = "Minutes between foul shots",
     ylab = "Relative Frequency",
     breaks = "Sturges") # Alternatively, use a fixed number like breaks = 10

# install distributions3 package if you do not aleardy have it.
#install.packages("distributions3")

# load library with t-distributions
library(distributions3)

# 95% Confidence intervals for the mean (t-intervals)
c(mean(samp) + quantile(StudentsT(df=29), 0.05 / 2) * sd(samp) / sqrt(30),
  mean(samp) - quantile(StudentsT(df=29), 0.05 / 2) * sd(samp) / sqrt(30))


# One sample t-test
t.test(samp, mu=5)
 


