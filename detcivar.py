'''

author: xujing
date: 2020-10-18

'''

from scipy.stats import norm


class DetStatic:
    '''
    Some statistical information of the calculated statistics includes sample mean, 
    sample variance and confidence interval estimation
    '''

    def mu(self,l):
        '''
        Calculate the sample mean of a list of data
        :l: Data structure similar to list, eg. [0.1,0.2,0.3,0.4,0.5]
        :return: Returns the average value of this column of data

        '''

        return float(sum(l)) / len(l)


    def variance(self,l):
        '''
        Calculate sample variance (unbiased estimate of variance) for a list of data
        :l: Data structure similar to list, eg. [0.1,0.2,0.3,0.4,0.5]
        :retuen: Returns the Variance value of this column of data

        '''
        if len(l) == 1:
            raise "[ detmetric Error ]： The calculation of variance requires a number of length 2"

        ex = float(sum(l)) / len(l)
        s=0
        for i in l:
            s += (i-ex)**2
        return float(s)/(len(l)-1)


    def z_quantile(self,level=0.05):
        '''
        Calculate quantile of standard normal distribution
        :level: Quantile, the default is 0.05
        :return: Standard normal distribution quantile of level

        '''

        if (level < 0) or (level > 1):
            raise "[ detmetric Error ]： The quantile of quantile must be between 0 and 1"

        return norm.ppf(level,loc=0,scale=1)

    # @staticmethod
    def detcivar(self,l,level=0.95):
        '''
        Calculate the confidence interval and sample variance of statistics
        :l: Observations of Statistics
        :level: Confidence level, the default calculated confidence level is 95% (recommended) confidence interval
        :return: Returns a dictionary whose keys are CI and Var, representing the confidence interval and sample variance of the statistic

        '''

        x_mean = self.mu(l)
        ns2 = float(self.variance(l)) / len(l)

        alpha = float((1 - level)) / 2
        up_z = self.z_quantile(level=alpha)
        down_z = self.z_quantile(level=1-alpha)

        ci = [round(x_mean + ns2 * up_z,6), round(x_mean + ns2 * down_z,6)]
        var = float(self.variance(l))

        return {"CI":ci, "Var": var}


        
if __name__ == "__main__":

    precison = [0.1,0.2,0.3,0.4,0.5]
    detstatic = DetStatic()
    civar = detstatic.detcivar(precison)

    print("The CI and Var of precision is: {}".format(civar))

