# bootstrapping_model_misspecification
Creating a bootsrap interval in order to test model correctness. Hypothesized model is exponential, data comes from gamma distribution.

As shown in White (1982), we the $s$ function

$$
s = A - B
$$

can be used to test model correctness. This implementation is not of a Wald Test, as suggested by White (1982), 
but a bootstrapping approach described in Ch. 19 by Keener.

The results are not consistent with randomization. 
The acceptance/rejection of the null hypothesis depends strongly on the original sample from the gamma distribution.

References:

Maximum Likelihood Estimation of Misspecified Models, White 1982

Lecture 16 — MLE under model misspecification, STATS 200: Introduction to Statistical Inference - Stanford

Theoretical Statistics - Keener, Robert
