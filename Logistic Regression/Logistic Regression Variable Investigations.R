# Code for Logistic Regression Homework Report 1
# SENCE Consulting: Sanket Sahasrabudhe, Ethan Scheper, Noah Johnson, Charis Williams, Elizabeth Surratt
# September 1, 2022

library(tidyverse)
library(glmnet)
library(vcdExtra)
library(car)
library(DescTools)
library(naniar)
library(dplyr)
library(ggplot2)

insurance_train <- read.csv("insurance_t.csv")
str(insurance_train)

#List of all nominal variables
facs = c("CASHBK", "DDA","DIRDEP","SAV","ATM","CD","IRA",
         "LOC", "INV", "ILS","MM","MMCRED", "CC", "CCPURC", "MTG","SDB", 
         "HMOWN", "MOVED","INAREA","INS", "BRANCH", "RES", "NSF")

#Make them all factors
insurance_train[facs] <- lapply(insurance_train[facs], factor)

str(insurance_train)

#Using individual variable global tests
binary <- c()
cont <- c()
ordinal <- c()
nominal <- c()

for (i in colnames(insurance_train)) {
  if (is.factor(insurance_train[,i]) & i != "INS") {
    #Hard-coded list of identified ordinal variables
    if (i %in% c("CCPURC", "NSF", "MMCRED", "CASHBK")) {
      ordinal = append(ordinal, i)
    }
    #If two levels, binary
    else if (nlevels(insurance_train[,i]) == 2) {
      binary = append(binary, i)
    }
    #All other nominal variables
    else {
      nominal = append(nominal, i)
    }
  }
  else {
    #Add cont variables
    if (i != "INS") {
      cont = append(cont, i)
    }
  }
}
vars = c()
pval = c()

for (i in colnames(insurance_train)) {
  #If binary or ordinal, use MH Chi-squared test
  if (i %in% binary | i %in% ordinal) {
    vars = append(vars, i)
    pval = append(pval, CMHtest(table(insurance_train[,i], insurance_train$INS))$table[1,3])
  }
  #If nominal, use Pearson Chi-squared test
  else if (i %in% nominal) {
    vars = append(vars, i)
    chi <- chisq.test(table(insurance_train[,i], insurance_train$INS))
    pval = append(pval, chi$p.value)
  }
  #If continuous, use Likelihood Ratio Test
  else if (i %in% cont) {
    vars = append(vars, i)
    temp_formula <- formula(paste("INS ~ ", i))
    temp_model <- glm(temp_formula, data = insurance_train, family = binomial(link = "logit"))
    pval = append(pval, car::Anova(temp_model, test = "LR", type = "III")[,3])
  }
}

first_pval <- as.data.frame(pval)
first_pval <- cbind(vars, first_pval)
#Formatting and numerical display
first_pval <- first_pval %>% mutate(pval = ifelse(pval >= 0.0001, round(pval, digits = 5), format(pval, scientific = TRUE, digits = 5)))
first_pval <- first_pval %>% arrange(as.numeric(pval))
#Isolating significant variables
first_pval_sig <- first_pval %>% filter(as.numeric(pval) < 0.002)

#Final Table here
first_pval_sig <- first_pval_sig %>% mutate(type = ifelse(vars %in% binary, "Binary", ifelse(vars %in% ordinal, "Ordinal", ifelse(vars %in% nominal, "Nominal", "Continuous"))))

#Odds Ratio
# Creating a vector with all of the binary variables and a data frame to populate with their odds ratios in relation to the target variable (INS)
odds_ratios <- data.frame(matrix(nrow = length(binary), ncol = 2))
colnames(odds_ratios) <- c("var", "odds_ratio")

# Using a loop to calculate the odds ratios and put them in the data frame
for (i in 1:length(binary)) {
  var_name <- binary[i]
  odds_ratios$var[i] <- var_name
  odds_ratios$odds_ratio[i] <- OddsRatio(table(insurance_train[[var_name]], 
                                               insurance_train$INS))
}

# Filter to only include those variables that are statistically significant
odds_ratios <- odds_ratios %>%
  filter(var %in% first_pval_sig$vars)

# Rank the odds ratios by magnitude
for (i in 1:nrow(odds_ratios)) {
  if (odds_ratios$odds_ratio[i] >= 1) {
    odds_ratios$magnitude[i] <- odds_ratios$odds_ratio[i]
  }
  else {
    odds_ratios$magnitude[i] <- 1 / odds_ratios$odds_ratio[i]
  }
}
odds_ratios <- odds_ratios %>% arrange(desc(magnitude))
odds_ratios$rank <- 1:nrow(odds_ratios)

# Testing linearity assumptions 

# remove NSF from list of continuous vars since this variable pulls an error b/c it only has 0s and 1s
cont1 <- cont[cont != "NSF"]
print(cont1)


# for loop for running test with all continuous variables
for (i in colnames(insurance_train)) {
  # print(i)
  if (i %in% cont1) {
    print(i)
    temp_logit <- formula(paste("INS ~ ", i))
    logit_model <- glm(temp_logit,
                       data = insurance_train, 
                       family = binomial(link = "logit"))
    
    temp_gam <- formula(paste("INS ~ s(", i, ")"))
    fit_model <- mgcv::gam(temp_gam,
                           data = insurance_train,
                           family = binomial(),
                           method = "REML")
    
    print(anova(logit_model, fit_model, test="Chisq")[2,5]) #printing just pvals
  }
}

#subsetting data frame with just linear variables
linear_vars <- names(insurance_train) %in% c("CRSCORE", "AGE", "HMVAL", "LORES", "INCOME", "CCBAL", "MTGBAL", "LOCBAL", "ACCTAGE")
linear_vars_df <- insurance_train[linear_vars]

# Plot Missing Values

# looking at all the variables to see which ones have NA's

colSums(is.na(insurance_train))
missing <- insurance_train %>% 
  miss_var_summary()

# making a list of all variables that have NA's
missingcols <- c("ACCTAGE", "PHONE", "POS", "POSAMT", "INV", "INVBAL", "CC", "CCBAL", "CCPURC", "INCOME", "HMOWN", "LORES", "HMVAL", "AGE", "CRSCORE")

# visual
gg_miss_var(insurance_train[missingcols]) +
  ggtitle("Variables with Missing Values") +
  labs(y = "Number of Missing Values")



