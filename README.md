# BayesianGLS
An implementation of the Bayesian Generalized Lomb Scargle periodogram as described by Mortier et al. 2015

## Installation

Just clone the repository and then install using setup.py

```
$ cd BayesianGLS
$ python setup.py install
```

## Usage

To use, simply import bayesian_generalized_lomb_scargle from bgls

```
import scipy as sp
from scipy.stats import norm, uniform
import numpy as np

from bgls import bayesian_generalized_lomb_scargle

np.random.seed(42)
a = 5
p = 5.67
f = 1 / p
errs = abs(norm(loc=0, scale=1).rvs(size=250))
t = uniform.rvs(size=250, loc=2, scale=100)
t.sort()
fun = a * sp.sin(2 * sp.pi * f * t) + norm.rvs(size=250, scale=1)

PP = sp.linspace(sp.diff(t).mean(), 2 * 26, 100000)
FF = 1 / PP
lnp = bayesian_generalized_lomb_scargle(fun, t, errs, FF)

plt.errorbar(x=t, y=fun, yerr=errs, marker='o', ls='')
plt.xlabel('time')
plt.ylabel('rv')
plt.savefig('synthetic_data.pdf', bbox_inches='tight')
plt.clf()

plt.semilogx(PP, lnp)
period = PP[sp.argmax(lnp)]
lab = '{:.4f}'.format(period)
plt.axvline(PP[sp.argmax(lnp)], lw=5, alpha=.3, c='g', label=lab)
plt.legend(loc=0)
plt.title('BGLS')
plt.xlabel('period')
plt.ylabel('normalized loglikelihood')
plt.savefig('BGLS.pdf', bbox_inches='tight')
plt.clf()
```

The results look like this:

![alt text](https://github.com/jvines/BayesianGLS/blob/master/src/images/synthetic_data.png "Synthetic data")

![alt text](https://github.com/jvines/BayesianGLS/blob/master/src/images/BGLS.png "BGLS")

## Uninstallation

If you wish to remove BGLS, just go to the terminal and type `pip uninstall bgls`

This code is based of [Mortier et al. 2015](https://arxiv.org/abs/1412.0467)
