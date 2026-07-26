### Logistic Regression ###

dat1 <- read.table("clipboard", h=T, sep="")
dat1
dim(dat1) # 10000 X 14
dat2 <- na.omit(dat1)
dim(dat2) # 10000 X 14 (NAs are not exist)
attach(dat1)
names(dat1)

fit0 <- glm(Exited~.-RowNumber-CustomerId-Surname, data=dat1, family=binomial)
summary(fit0)

fit1 <- step(fit0, direction="backward")
summary(fit1)
anova(fit1, fit0) # anova(unsaturated model, saturated model), H_O: unsaturated model
qchisq(0.05, 2, lower.tail=F)
drop1(fit1, test="Chisq")

fit2 <- update(fit1, ~.-Tenure)
summary(fit2)
anova(fit2, fit1)
qchisq(0.05, 1, lower.tail=F)
drop1(fit2, test="Chisq")

fit3 <- update(fit2, ~.-NumOfProducts)
summary(fit3) 
anova(fit3, fit2)
qchisq(0.05, 1, lower.tail=F)

library(car) # the package of car is prerequisite for using the function of VIF(Variance Inflation Factor)
	       # 8 Imports needed to install CAR(Companion to Applied Regression)     
                      
vif(fit2) # if vif>10 then the multicollinearity is strongly supposed to exist                                 
pairs(cbind(CreditScore, Geography, Gender, Age, Balance, NumOfProducts, IsActiveMember)) # fit2 변수 간 점검
cor(cbind(CreditScore, Geography, Gender, Age, Balance, NumOfProducts, IsActiveMember)) # fit2 변수 간 점검
str(dat1)
Geography1 <- recode(Geography, "'France'=1; 'Spain'=2; 'Germany'=3") # Categorical -> Numeric
Gender1 <- recode(Gender, "'Male'=1; 'Female'=2") # Categorical -> Numeric

pairs(cbind(CreditScore, Geography1, Gender1, Age, Balance, NumOfProducts, IsActiveMember)) # fit2 변수 간 점검
cor(cbind(CreditScore, Geography1, Gender1, Age, Balance, NumOfProducts, IsActiveMember)) # fit2 변수 간 점검

fit <- fit2 # final model

### Scoring ###

p <- fitted(fit) # fitted values of Pr(Y=good)=Pr(Y=1)=Pr(Exited)
summary(p)
odds <- p/(1-p)
logit <- log(odds)
summary(logit)

range_logit <- max(logit)-min(logit) # 최대 로짓을 1000점으로, 최소 로짓을 0점으로
pdo <- log(2)*1000/range_logit # 1000점 Scale

S <- 400
g <- exp(log(2)/pdo*(S+min(logit)*pdo/log(2)))

score <- pdo/log(2)*logit+(S-pdo*log(g)/log(2))
summary(score)

par(mfrow=c(2,1))
boxplot(score)
points(mean(score), pch=8)
plot(density(score))

### Model Performance ###

require(ROCR) # 5 imports needed to install ROCR

pred <- prediction(p, Exited)

y_hat <- ifelse(p>=0.5, 1, 0) # Predicted value when a cutoff is 0.5 
confusion <- table(y_hat, Exited) # Confusion Matrix in this case
confusion

precison <- performance(pred, "prec") # Precison ~ Cutoff
plot(precison)
paste('Cutoff :', round(precison@x.values[[1]],2), ', Precison :', round(precison@y.values[[1]],2))

recall <- performance(pred, "rec") # Recall ~ Cutoff
plot(recall)
paste('Cutoff :', round(recall@x.values[[1]],2), ', Recall :', round(recall@y.values[[1]],2))

plot(precison, ylab="Precision or Recall") # Precison or Recall ~ Cutoff
lines(recall@x.values[[1]], recall@y.values[[1]])

f1 <- performance(pred, "f") # F1 Score ~ Cutoff
plot(f1, ylab="F1 Score")
paste('Cutoff :', round(f1@x.values[[1]],2), ', F1 Score :', round(f1@y.values[[1]],2))
max(na.omit(f1@y.values[[1]])) # F1 Score = 0.498
i <- which(f1@y.values[[1]]==max(na.omit(f1@y.values[[1]]))) 
f1@x.values[[1]][i] # Cutoff

roc <- performance(pred, "tpr", "fpr") # ROC Curve
plot(roc)
lines(roc@x.values[[1]], roc@x.values[[1]], lty=2)

auc <- performance(pred, "auc") # AUC(Area Under the ROC Curve)
str(auc) # AUC = 0.767



### XGBoost ###

dat1 <- read.table("clipboard", h=T, sep="")
dat1
dim(dat1) # 10000 X 14
dat2 <- na.omit(dat1)
dim(dat2) # 10000 X 14 (NAs are not exist)
names(dat1)
head(dat1)
str(dat1)

install.packages("Matrix")
library(Matrix)

sparse_matrix <- sparse.model.matrix(Exited~.-1, data=dat1) # 설명 변수 Matrix(단, Categorical 변수의 각 볌주를 하나의 변수로 취급) 
dim(sparse_matrix) # 10000 X 2945
train_index <- sample(1:nrow(sparse_matrix), 6000) 

train_x <- sparse_matrix[train_index,]
test_x <- sparse_matrix[-train_index,]

train_y <- dat1[train_index, 'Exited']
test_y <- dat1[-train_index, 'Exited']

dim(train_x); dim(test_x)

install.packages("xgboost")
library(xgboost)

train <- xgb.DMatrix(data=train_x, label=as.matrix(train_y)) # Train Set
test <- xgb.DMatrix(data=test_x, label=as.matrix(test_y)) # Test Set

param <- list(max_depth=6, eta=0.1, nthread=2, objective="binary:logistic", eval_metric="auc")
xgb <- xgb.train(params=param, data=train, nrounds=10, subsample=0.5, colsample_bytree=0.5) # nrounds=max number of boosting iterations
                                                                                            # subsample, colsample: sampling when constructing each tree

train_y_pred <- predict(xgb, train)
test_y_pred <- predict(xgb, test)

install.packages("MLmetrics")
require(MLmetrics)

KS_Stat(train_y_pred, train_y); AUC(train_y_pred, train_y)
KS_Stat(test_y_pred, test_y); AUC(test_y_pred, test_y)

dnames <- dimnames(train)[[2]] # Column Names
xgb_importance <- xgb.importance(dnames, model=xgb)
xgb.plot.importance(xgb_importance[,])

### Scoring ###

p <- train_y_pred
summary(p)
odds <- p/(1-p)
logit <- log(odds)
summary(logit)

range_logit <- max(logit)-min(logit) # 최대 로짓을 1000점으로, 최소 로짓을 0점으로
pdo <- log(2)*1000/range_logit # 1000점 Scale

S <- 200
g <- exp(log(2)/pdo*(S+min(logit)*pdo/log(2)))

score <- pdo/log(2)*logit+(S-pdo*log(g)/log(2))
summary(score)

par(mfrow=c(2,1))
boxplot(score)
points(mean(score), pch=8)
plot(density(score))

### Model Performance ###

require(ROCR) # 5 imports needed to install ROCR

pred <- prediction(p, train_y)

y_hat <- ifelse(p>=0.5, 1, 0) # Predicted value when a cutoff is 0.5 
confusion <- table(y_hat, train_y) # Confusion Matrix in this case
confusion

precison <- performance(pred, "prec") # Precison ~ Cutoff
plot(precison)
paste('Cutoff :', round(precison@x.values[[1]],2), ', Precison :', round(precison@y.values[[1]],2))

recall <- performance(pred, "rec") # Recall ~ Cutoff
plot(recall)
paste('Cutoff :', round(recall@x.values[[1]],2), ', Recall :', round(recall@y.values[[1]],2))

plot(precison, ylab="Precision or Recall") # Precison or Recall ~ Cutoff
lines(recall@x.values[[1]], recall@y.values[[1]])

f1 <- performance(pred, "f") # F1 Score ~ Cutoff
plot(f1, ylab="F1 Score")
paste('Cutoff :', round(f1@x.values[[1]],2), ', F1 Score :', round(f1@y.values[[1]],2))
max(na.omit(f1@y.values[[1]])) # F1 Score = 0.679
i <- which(f1@y.values[[1]]==max(na.omit(f1@y.values[[1]]))) 
f1@x.values[[1]][i] # Cutoff

roc <- performance(pred, "tpr", "fpr") # ROC Curve
plot(roc)
lines(roc@x.values[[1]], roc@x.values[[1]], lty=2)

auc <- performance(pred, "auc") # AUC(Area Under the ROC Curve)
str(auc) # AUC = 0.889


