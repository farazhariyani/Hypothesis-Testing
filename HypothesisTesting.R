#We will use 3 datasets to use 3 different types of Hypothesis testing (2 sample t test, Anova, Chi squared)
#Ho: Null Hypothesis - Take no action
#Ha: Alternate Hypothesis

# Load library
library(readr)

# 1
# 2 sample t Test
# cutlets.xlsx dataset
cutlets <- read_csv(file.choose())
#output variable - difference in diameter, input - diameter of Unit A and Unit B
View(cutlets) 

#rename columns
colnames(cutlets) <- c("UnitA", "UnitB")
View(cutlets)
attach(cutlets)

# Normality test
#Ho: Data are normal
#Ha: Data are not normal
shapiro.test(UnitA)#shapiro wilk test

#significance level(alpha) is 5%(0.05)
#i.e. confidence(1 - alpha) is 95%(0.95)
# p-value = 0.32 > 0.05 so p high null(Ho) fly (we fail to reject Null) 
#=> It follows normal distribution

shapiro.test(UnitB)
# p-value = 0.5225 > 0.05 so p high null fly => It follows normal distribution

# Variance test
#Ho: Variances of diameter in Unit A = Variance of diameter in unit B
#Ha: Variances of diameter in Unit A != Variance of diameter in unit B
var.test(UnitA, UnitB)
# p-value = 0.3136 > 0.05 so p high null fly => Equal variances

# 2 sample t Test assuming equal variances
#Ho: average diameter in Unit A = average diameter in Unit B
#Ha: average diameter in Unit A != average diameter in Unit B 
t.test(UnitA, UnitB, alternative = "two.sided", conf.level = 0.95, var.equal = T)#var.equal = F if variance not equal

# p-value = 0.4722 > 0.05 P high null(Ho) fly

#2
#Anova 
# dataset: lab_tat_updated.csv
#output variable - purchases made, input - interest rate waiver and standard promotion
lab <- read_csv(file.choose())
View(lab) 
#Y : Output variable : Turn around time
#X : Input Variables : Lab 1,2,3,4

#rename columns
colnames(lab) <- c("Lab1", "Lab2", "Lab3", "Lab4")
attach(lab)
sapply(lab, class)  
Lab1 <- as.numeric(Lab1) 

#Ho: Data are normal
#Ha: Data are not normal

# Normality test
shapiro.test(`Lab1`)#P-value = 0.4232 > 0.05
shapiro.test(`Lab2`)#P-value = 0.8637 > 0.05
shapiro.test(`Lab3`)#P-value = 0.06547 > 0.05
shapiro.test(`Lab4`)#P-value = 0.6619 > 0.05
# P high Null fly

#Ho: Variance in TAT of 1 = 2 = 3 = 4
#Ha: Variance in TAT of atleast 1 Lab is different
# Variance test
var.test(`Lab1`, `Lab2`)#p = 0.4341 > 0.05
var.test(`Lab2`, `Lab3`)#p = 0.5531 > 0.05
var.test(`Lab3`, `Lab4`)#p = 0.6168 > 0.05
var.test(`Lab4`, `Lab1`)#p = 0.3817 > 0.05
#P high Null fly

#One way ANOVA
#Ho: Average TAT of all Lab are equal
#Ha: Average TAT of atleast 1 Lab is different

Stacked_Data <- stack(lab)#2 columns - TAT | Lab 1,2,3,4

View(Stacked_Data)

attach(Stacked_Data)
colnames(Stacked_Data)

Anova_results <- aov(values ~ ind, data = Stacked_Data)
summary(Anova_results)
# p-value = 0.0000000000000002 < 0.05 P low Null go

#3
#Chi-squared
library(readr)

# Load the data: Bahaman.xlsx
buyerratio <- read_csv(file.choose()) 
View(buyerratio)
#Y: Males and Females
#X: East, West, North, South

attach(buyerratio)
dimnames(buyerratio)   #Retrieve the dimension names of the Dataset

# extract a take with the values from the Dataset 
buyer <- as.table(rbind(c(50, 142, 131, 70), c(435, 1523, 1356, 750))) 
buyer

# Rename or re-set the dimnames of the Dataset 
dimnames(buyer) <- list(gender = c("Males", "Females"), region = c("East","West", "North", "South"))  
View(buyer)
#Ho: proportion of male and female across all regions are same
#Ha: proportion of male and female of atleast 1 region is not same

# chi-squared contingency table tests and goodness-of-fit tests.
chisq.test(buyer)  # Prints test summary
# p-value = 0.6603 > 0.05  => Accept null hypothesis | p high null fly
# All Proportions are equal 