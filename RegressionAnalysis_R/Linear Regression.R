###################
#Linear Regression#
###################

### Simple Linear Regression ###

meta <- read.table("regression_simple.txt", header=T)
meta
names(meta) # rate: Metabolic Rate(신진대사율)
rate; meta$rate 
attach(meta) # meta의 name들을 사용할 수 있게
rate
plot(mass, rate) # scatterplot
cor(mass, rate) # Correlation coefficient
lm(rate~mass)# linear model
summary(lm(rate~mass))
lines(mass,lm(rate~mass)$fitted.values) # fitted line
abline(lm(rate~mass)) # fitted line

par(mfrow=c(2,1))
plot(mass, lm(rate~mass)$resid, main="Residual Plot") # residual plot
abline(0,0)
qqnorm(lm(rate~mass)$resid) # Q-Q plot of residuals

par(mfrow=c(2,2))
plot(lm(rate~mass))

plot(mass, rate, pch=as.numeric(as.factor(sex)))
legend(locator(1), legend=c("F", "M"), pch=1:2)
boxplot(rate, ylab="Rate", main="Boxplot of Rate")
points(mean(rate), pch=8)
boxplot(rate~sex, ylab="Rate", main="Boxplot of Rate by Sex")
points(tapply(rate, sex, mean), pch=8)


### Multiple Linear Regression ###

dat <- read.table("regression_multiple.txt", h=T)
dat
attach(dat)### 데이터 파일 안에 변수들을 자유롭게 사용가능한, 하지 않음면 dat $gpa 이런식으로 매번 쳐야함 ###
names(dat)

plot(dat) # matrix of scatterplots → 변수가 모두 numeric일 경우 pairs(dat)

r1 <- cor(gpa, iq); r1^2 # sample correlation b/w gpa & iq and the corresponding R^2
r2 <- cor(gpa, concept); r2^2
summary(lm(gpa~iq+concept))#이 부분 시험에 나올 수도
vcov(lm(gpa~iq+concept))# variance-covariance matrix of the main parameters, 시험에 나올 수도 결과 구해봐라( 루트 씌우고 뭐 ~)
anova(lm(gpa~iq+concept))# 전체 SSR 구할 때 독립변수의 SSR(Sum Sq) 더하기,F-Statistic = MSR / MSE = SSR /2 / SSE / 75(df) 
