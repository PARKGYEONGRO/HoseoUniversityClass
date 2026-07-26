#########
#About R#
#########

#1. S(벨연구소, 1976) → S-Plus (유료) → R(무료)
    → Revolution R (MS 상용 R)
    → Enterprise R (Oracle 상용 R)

#2. R was created by two professors, "Ross Ihaka" and "Robert Gentleman" at the Univ. of Auckland, New Zealand

#3. Developer: R Development Core Team (CRAN; Comprehensive R Archive Network)

#4. R 장·단점
    → Pros : Free, Object-oriented & shared Language, Graphic 
    → Cons : Velocity, 유지/보수 관리 


######
#Help#
######

help.start()
help("mean")
?mean


############################
#Creating and Removing Data#
############################

x <- c(1, 3, 5, 2, 3, 5)
x
y <- c(2, 3, 9, 1, 0, 6)
y 
w <- rbind(x, y) # combines x and y by rows
w
z <- cbind(x, y)  # combines x and y by columns
z

x
remove(x)
x


#########################################
#Numerical Descriptions of Distributions#
#########################################

weight <- c(120, 160, 135, 190, 210)
weight
height <- c(62, 69, 64, 72, 75)
height

sum(weight)
length(weight)

avWeight <- sum(weight)/length(weight)
avWeight
mean(weight)

median(height)

svarWeight <- sum((weight-avWeight)^2)/(length(weight)-1) # calculating sample variance by hand
svarWeight
sqrt(svarWeight) # calculating sample standard deviation by hand

var(weight)
sd(weight)

min(height)
max(height)

sort(height)
help(sort)
sort(height, decreasing=T)

summary(height)

boxplot(height)
points(mean(height), pch=8)


###########################
#Removing points from data# 
###########################

height <- c(62, 69, 64, 72, 75)
height

height[-2]
height[-5]
height[-c(2,5)]
height[-c(3:5)]

lowHeight <- height[height<=70]
lowHeight
height[height>=70]
height[height==72]

heighterror <- c(62, 69, 64, 72, 75, 1, 999)
mean(heighterror)
mean(heighterror[-c(6:7)])
mean(height)

heighterror2 <- c(height, 1, 999) # combining data
heighterror2


###########################################################################################
﻿#Suppose a group of 25 people are surveyed as to their beer-drinking preference.         #
# The categories were (1) Domestic can, (2) Domestic bottle, (3) Microbrew and (4) import.#
# The raw data is 3 4 1 1 3 4 3 3 1 3 2 1 2 1 2 3 2 3 1 1 1 1 4 3 1.                      #
###########################################################################################

### Bar Plot ###

beer = scan()
3 4 1 1 3 4 3 3 1 3 2 1 2 1 2 3 2 3 1 1 1 1 4 3 1
barplot(beer) # this isn't correct
barplot(table(beer)) # yes, call with summarized data
barplot(table(beer)/length(beer)) # divided by n for proportion

### Pie Plot ###

beer.counts = table(beer) # stores the table results
pie(beer.counts) # first pie -- kind of dull
names(beer.counts) = c("domestic can", "Domestic bottle", "Microbrew", "Import") # gives names, NOT WORK "names(table(beer))=c()" 
pie(beer.counts) # prints out names
pie(beer.counts, col=c("purple", "green2", "cyan", "white")) # now with colors


###########################################################################################
#684 students were surveyed about their favorite after school activities (Bar & Pie Plots)#
###########################################################################################

activity <- c("sports", "computers", "friends", "money", "phone")
count <- c(120, 65, 175, 120, 168)

pie(count)
pie(count, activity, main="Pie Chart for After-School Activities")

barplot(count)
barplot(count, names=activity, main="Bar Chart for After-School Activities", ylab="Count")


#######################################################################################################################
#Suppose you have the box score of a basketball game and find the following points per game for players on both teams:# 
#2 3 16 23 14 12 4 13 2 0 0 0 6 28 31 14 4 8 2 5.                                                                     #
#######################################################################################################################

### Stem-and-Leaf Plot ###

scores = scan()
2 3 16 23 14 12 4 13 2 0 0 0 6 28 31 14 4 8 2 5
stem(scores)


###############################################################################################################
#Suppose the top 26 ranked movies made the following gross receipts for a week:                               #
#29.6 28.2 19.6 13.7 13.0 7.8 3.4 2.0 1.9 1.0 0.7 0.4 0.4 0.3 0.3 0.3 0.3 0.3 0.2 0.2 0.2 0.1 0.1 0.1 0.1 0.1.#
###############################################################################################################

### Histogram ###

x = scan()
29.6 28.2 19.6 13.7 13.0 7.8 3.4 2.0 1.9 1.0 0.7 0.4 0.4 0.3 0.3 0.3 0.3 0.3 0.2 0.2 0.2 0.1 0.1 0.1 0.1 0.1
hist(x) # frequencies
hist(x, breaks=3) # 3 bars, or just hist(x, 3)
hist(x, breaks=c(0, 1, 2, 3, 4, 5, 10, 20, max(x))) # specify break points
hist(x, probability=TRUE) # proportions (or probabilities)
lines(density(x, bw=1.8)) # adds a density plot to a histogram


##############################################################
#Cumulative Probability and Quantile in a Normal Distribution#
##############################################################

pnorm(-1.96, 0, 1) # area
qnorm(0.025, 0, 1) # quantile


#################
#Normal Q-Q Plot#
#################

x <- rnorm(100, 0, 1)
qqnorm(x)


#################################
#Function & 한 화면에 두 직선 그리기#
#################################

x <- c(-6,10)

f1 <- function(x){
55*x+495
}

f2 <- function(x){
46*x+517
}

f3 <- function(x){
56*x+480
}

plot(f1, xlim=x, xlab='Logit', ylab='스코어')
lines(x, f2(x), lty=2, col=2)
lines(x, f3(x), lty=3, col=3)
legend(locator(1), legend=c("기준선", "시점1", "시점2"), lty=1:3, col=1:3)


#################
#Smoothing Curve#
#################

f <- function(x){
ifelse(0<=x & x<0.25, 3-4*x, ifelse(0.25<=x & x<0.5, 2-4*x, ifelse(0.5<=x & x<0.75, -1+4*x, 4-4*x)))
}

n = 100
x <- seq(0, 1, 1/(n-1)) # (n-1)등분
sigma = 0.2
y <- f(x)+rnorm(length(x), 0, sigma)

par(mfrow=c(2,1))
plot(f)
plot(x, y)
lines(lowess(y~x, f=0.2)) # LOcally WEighted Scatterplot Smoothing


########################
#Charactor와 Factor 차이#
########################

s1 <- c("a","b","c")
s1
s1[4]="d"
s1

s1 <- c("a","b","c")
s2 <- as.factor(s1) # Categorical 변수화
s2[4]="d" # s1에 없는 새로운 element 추가(X)
s2
s2[4]="a" # s1에 이미 있는 element 추가(O)
s2


#######################
#R 패키지 및 버전 Update#
#######################

install.packages("installr") # 패키지 Update
installr::updateR(T) # Version Update


#######################
#Set Working Directory#
#######################

setwd(choose.dir())


#############
#Dataset 표시#
#############

head(dataset,3) # 데이터셋의 첫 3행 표시
tail(dataset,3) # 데이터셋의 마지막 3행 표시


#############
#Outputs 저장#
#############

sink("outputs.txt") 
i <- 1:10
outer(i, i)
sink()

dev.copy2pdf(file = "Fig.pdf") # Device(그림)를 pdf 파일로 저장


###########################
#Round/Ceiling/Floor/Trunc#
###########################

### Round(반올림) ###

round(0.5) # 5의 경우, 앞자리가 홀수인 경우에는 "올림"을, 짝수인 경우에는 "버림"
round(1.5)                   
round(2.5) 

round(-0.5) # round(-x) = -round(x)
round(-1.5)
round(-2.5) 

round(54.65, 1) # "소수점 첫째자리에서 반올림 하라"가 아니라,소수점 둘째자리에서 반올림해서 "첫째자리까지 보이게 하라" 

### Ceiling(올림) : 같거나 큰 정수 ###

ceiling(0.5) # 1
ceiling(-0.5) # 0

### Floor(내림) : 같거나 작은 정수 ###

floor(0.5) # 0
floor(-0.5) # -1

### Truncate(버림) ###

trunc(0.5) # 0
trunc(-0.5) # 0


################
#Order vs. Rank#
################

x <- c(2, -1, NaN, 2, NA)
sort(x, na.last=F) # NaN NA -1 2 2 (오름차순이 기본)        

order(x, na.last=F) # sort에서 NaN은 x의 3번째, NA는 5번째,... => 3 5 2 1 4 => sort 시 x의 3번째 원소가 제일 먼저, 5번째가 그 다음,...

rank(x, na.last=F) # x에서 2는 sort의 (4+5)/2번째, -1은 3번째,... => 4.5 3.0 1.0 4.5 2.0 => sort 시 x의 2는 4.5번째, -1은 3번째,... 
rank(-x, na.last=F) # sort(x, decreacing=T, na.last=F) = NaN NA 2 2 -1 => 3.5 5.0 1.0 3.5 2.0 => sort w/i decreasing 시 x의 2는 3.5번째, -1은 5번째,... 


############
#Sweep 명령어#
############

x1 <- c(3.15, 2.76, 3.21, 3.69, 3.92)
x2 <- c(3.44, 3.46, 3.57, 3.19, 3.15)
X <- data.frame(x1, x2)
sweep(X, MARGIN = 2, STATS = colMeans(X), FUN = "-") # colMeans(X) = apply(X,2,mean) 
                                                   
  
