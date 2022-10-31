library(tidyverse)
library(DescTools)

ins_t_bin <- read.csv("Homework2_LR/insurance_t_bin.csv")
str(ins_t_bin)

ins_t_bin[is.na(ins_t_bin)] <- 'M'

ins_t_bin_fac <- as.data.frame(lapply(ins_t_bin, function(x) as.factor(x)))

str(ins_t_bin_fac)
unique(ins_t_bin_fac$CCPURC)

######

ins_t_bin_pred <- ins_t_bin_fac %>% select(-INS)

sep_list_1 <- c()
for (i in 1:ncol(ins_t_bin_pred)) {
  temp_table <- table(ins_t_bin_fac$INS, ins_t_bin_pred[[i]])
  if (0 %in% as.matrix(temp_table)) {
    print(colnames(ins_t_bin_pred)[i])
    print(temp_table)
    sep_list_1 <- append(sep_list_1, colnames(ins_t_bin_pred)[i])
  }
}

print(sep_list_1)

ins_t_bin_nosep <- ins_t_bin %>% mutate(CASHBK = ifelse(CASHBK >= 1, "1+", CASHBK), 
                                        MMCRED = ifelse(MMCRED >= 3, "3+", MMCRED))

ins_t_bin_nosep <- as.data.frame(lapply(ins_t_bin_nosep, function(x) as.factor(x)))
str(ins_t_bin_nosep)

full.model <- glm(INS ~ ., data = ins_t_bin_nosep, family = binomial(link = "logit"))
back.model <- step(full.model, direction = "backward", k = qchisq(0.002, 1, lower.tail = FALSE))
summary(back.model)
coef(summary(back.model.final))[,4]

# 
# sep_list_2 <- c()
# ins_t_bin_nosep_sel <- select(ins_t_bin_nosep, c(NSF, MTG, ILS, INV, IRA, DDA, TELLER_Bin, CC, 
#                                                  ATMAMT_Bin, CHECKS_Bin, MM, CDBAL_Bin, DDABAL_Bin, SAVBAL_Bin, INS))
# for (i in 1:(ncol(ins_t_bin_nosep_sel) - 1)) {
#   if (colnames(ins_t_bin_nosep_sel)[i] != "CC") {
#     temp_table_2 <- table(ins_t_bin$CC, ins_t_bin_nosep_sel[[i]])
#     if (0 %in% as.matrix(temp_table_2)) {
#       print(colnames(ins_t_bin_nosep_sel)[i])
#       print(temp_table_2)
#       sep_list_2 <- append(sep_list_2, colnames(ins_t_bin_nosep_sel)[i])
#     }
#   }
# }

car::Anova(back.model, test = "LR", type = "III", singular.ok = TRUE)

back.model.final <- step(back.model, scope = . ~ .^2, direction = 'forward', k = qchisq(0.002, 1, lower.tail = FALSE))
summary(back.model.final)
odds_ratio <- exp(coef(summary(back.model.final))[,1])
sample_df <- as.data.frame(odds_ratio)

sample_df <- sample_df %>% mutate(odds_ratio = round(odds_ratio, 4), odds_ratio_mag = ifelse(odds_ratio < 1, round(1/odds_ratio, 4), round(odds_ratio, 4)))
write.csv(sample_df, "odds_ratio.csv")

ins_t_bin_nosep_sel <- select(ins_t_bin_nosep, c(DDA, NSF, IRA, INV, ILS, MM, MTG, CC, DDABAL_Bin, CHECKS_Bin,
                                                 TELLER_Bin, SAVBAL_Bin, ATMAMT_Bin, CDBAL_Bin, INS))

binary_preds <- select(ins_t_bin_nosep_sel, c(DDA, NSF, IRA, ILS, MM, MTG))

or_list <- c()
or_mag_list <- c()
for (i in 1:ncol(binary_preds)) {
  print(colnames(binary_preds)[i])
  or <- OddsRatio(table(binary_preds[[i]], ins_t_bin_nosep_sel$INS))
  print(or)
  or_list <- append(or_list, or)
  if (or <= 1) {
    or = 1 / or
  }
  print(or)
  or_mag_list <- append(or_mag_list, or)
}

or_mag_list_sort <- or_mag_list[order(or_mag_list, decreasing = TRUE)]
print(c("IRA", "MM", "DDA", "NSF", "ILS", "MTG"))
print(or_mag_list_sort)


odds_df <- as.data.frame()



