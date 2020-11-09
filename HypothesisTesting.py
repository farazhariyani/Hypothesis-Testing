#We will use 3 datasets to use 3 different types of Hypothesis testing (2 sample t test, Anova, Chi squared)
#Ho: Null Hypothesis - Take no action
#Ha: Alternate Hypothesis

#1
#2 sample t test
import pandas as pd
import numpy as np
import scipy
from scipy import stats
import statsmodels.api as sm
import statsmodels.stats.descriptivestats as sd
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly import figure_factory as FF

# Load the data
cutlets = pd.read_csv("Cutlets.csv")
cutlets

cutlets.columns = "UnitA", "UnitB"

# Normality Test
#Ho: Data are normal
#Ha: Data are not normal
# Shapiro Test

stats.shapiro(cutlets.UnitA) 
# p-value = 0.31 > 0.05 so p high null(Ho) fly (we fail to reject Null) 

stats.shapiro(cutlets.UnitB)
# p-value = 0.52 > 0.05 so p high null(Ho) fly (we fail to reject Null) 
#=> It follows normal distribution

# Variance test
#Ho: Variances of diameter in Unit A = Variance of diameter in unit B
#Ha: Variances of diameter in Unit A != Variance of diameter in unit B

scipy.stats.levene(cutlets.UnitA, cutlets.UnitB)
# p-value = 0.41 > 0.05 so p high null fly => Equal variances

# 2 Sample T test
#Ho: average diameter in Unit A <= average diameter in Unit B
#Ha: average diameter in Unit A > average diameter in Unit B 
stats.ttest_ind(cutlets.UnitA, cutlets.UnitB)
# p-value = 0.47 > 0.05 p high null fly
# average diameter in Unit A <= average diameter in Unit B

#2
#Anova
#dataset: lab_tat_updated.csv
lab = pd.read_csv("lab_tat_updated.csv")
lab
lab.columns = "Lab1", "Lab2", "Lab3", "Lab4"

# Normality Test
#Ho: Data are normal
#Ha: Data are not normal
# Shapiro Test
stats.shapiro(lab.Lab1) # 0.42 > 0.05 | p high null fly
stats.shapiro(lab.Lab2) # 0.86 > 0.05 | p high null fly
stats.shapiro(lab.Lab3) # 0.06 > 0.05 | p high null fly
stats.shapiro(lab.Lab4) # 0.66 > 0.05 | p high null fly

# Variance test
#Ho: Variance in TAT of 1 = 2 = 3 = 4
#Ha: Variance in TAT of atleast 1 Lab is different
# All 3 suppliers are being checked for variances
scipy.stats.levene(lab.Lab1, lab.Lab2, lab.Lab3, lab.Lab4) # 0.38 > 0.05 | p high null fly

# One - Way Anova
#Ho: Average TAT of all Lab are equal
#Ha: Average TAT of atleast 1 Lab is different
stats.f_oneway(lab.Lab1, lab.Lab2, lab.Lab3, lab.Lab4) # 2.143740909435053e-58 < 0.05 | P low Null go
# Average TAT of atleast 1 Lab is different

#3
#Chi squared

buyerratio = pd.read_csv("BuyerRatio.csv")
buyerratio
#Ho: proportion of male and female across all regions are same
#Ha: proportion of male and female of atleast 1 region is not same
################
#Ho: proportion of male and female in east and west are same
#Ha: proportion of male and female in east and west is not same
count=pd.crosstab(buyerratio.East,buyerratio.West)
count
Chisquares_results=scipy.stats.chi2_contingency(count,correction = False)
Chi_pValue=Chisquares_results[1]
Chi_square=[
        ['','Test Statistic','p-value'],
        ['Sample Data',Chisquares_results[0],Chisquares_results[1]]
        ]
Chi_square
print("p-value is: "+str(Chi_pValue)) # 0.15 > 0.05 p high null fly

#Ho: proportion of male and female in west and north are same
#Ha: proportion of male and female in west and north is not same
count1=pd.crosstab(buyerratio.West,buyerratio.North)
Chisquares_results1=scipy.stats.chi2_contingency(count1,correction = False)
Chi_pValue1=Chisquares_results1[1]
print("p_value is:"+str(Chi_pValue1)) # 0.15 > 0.05 phigh null fly

#Ho: proportion of male and female in north and south are same
#Ha: proportion of male and female in north and south is not same
count2=pd.crosstab(buyerratio.North,buyerratio.South)
Chisquares_results2=scipy.stats.chi2_contingency(count2, correction = False)
Chi_Pvalue2=Chisquares_results2[1]
Chi_Pvalue2 # 0.15 > 0.05 p high null fly

#Ho: proportion of male and female in south and east are same
#Ha: proportion of male and female in south and east is not same
count3=pd.crosstab(buyerratio.South,buyerratio.East)
Chi3=scipy.stats.chi2_contingency(count3,correction = False)
chipvalue=Chi3[1]
chipvalue # 0.15 > 0.05 p high null fly
#proportion of male and female across all regions are same