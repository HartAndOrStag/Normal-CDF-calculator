# Normal-CDF-calculator
Calculator that displays phi value of a normal distribution given an input of x, mu, and sigma.

Calculated using the following power series $\Phi(x) = \frac{1}{2} + \frac{1}{\sqrt{2\pi}} \sum_{k=0}^{\infty} \frac{(-1)^k}{2^k k!(2k+1)} \left(\frac{x-\mu}{\sigma}\right)^{2k+1}$


## Derivation

Starting with the equation for the normal PDF:

$$
f(x; \mu, \sigma) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x - \mu)^2}{2\sigma^2}}
$$

This function gives us the familiar bell-shaped curve. However, it is not very useful on its own because it does not actually display an exact probability but instead displays the **probability density**, which gives only a general sense of how likely a value is to be somewhere around a point.

In order to get an exact probability, the function must be integrated and normalized to between \(0\) and \(1\). Unfortunately, the normal PDF cannot be integrated using any known technique and so instead must be approximated. This is normally done using the error function:

$$
\Phi(x) = \frac{1}{2} \left( 1 + erf \left( \frac{x - \mu}{\sqrt{2}\sigma} \right) \right)
$$

However, because this is not the obvious way to approach this type of problem, I instead used a **power series approximation**, derived via the following steps.

---

### Step 1 — Start with a known Maclaurin series

$$
e^{-t^2/2} = \sum_{k=0}^{\infty} \frac{\left(-\frac{t^2}{2}\right)^k}{k!}
$$

---

### Step 2 — Substitute to match the form of the normal PDF

$$
\frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x - \mu)^2}{2\sigma^2}}
= \frac{1}{\sqrt{2\pi}\sigma} \sum_{k=0}^{\infty} \frac{\left( -\frac{(x - \mu)^2}{2\sigma^2} \right)^k}{k!}
$$

---

### Step 3 — Simplify

$$
\frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x - \mu)^2}{2\sigma^2}}
= \frac{1}{\sqrt{2\pi}\sigma} \sum_{k=0}^{\infty} \frac{(-1)^k}{k!} \left( \frac{(x - \mu)^2}{2\sigma^2} \right)^k
$$

By our original function, we can write:

$$
f(x; \mu, \sigma) = \frac{1}{\sqrt{2\pi}\sigma} \sum_{k=0}^{\infty} \frac{(-1)^k}{k!} \left( \frac{(x - \mu)^2}{2\sigma^2} \right)^k
$$

---

### Step 4 — Integrate to get the CDF

$$
\Phi(x) = \frac{1}{\sqrt{2\pi}\sigma} \sum_{k=0}^{\infty} \frac{(-1)^k}{k!} \int_{-\infty}^{x} \left( \frac{(t - \mu)^2}{2\sigma^2} \right)^k dt
$$

---

### Step 5 — Factor constants out of the integral

$$
\Phi(x) = \frac{1}{\sqrt{2\pi}\sigma} \sum_{k=0}^{\infty} \frac{(-1)^k}{k!} \left( \frac{1}{2\sigma^2} \right)^k \int_{-\infty}^{x} (t - \mu)^{2k} dt
$$

---

### Step 6 — Apply the power rule

$$
\Phi(x) = \frac{1}{\sqrt{2\pi}\sigma} \sum_{k=0}^{\infty} \frac{(-1)^k}{k!} \left( \frac{1}{2\sigma^2} \right)^k \frac{(x - \mu)^{2k+1}}{2k+1}
$$

---

### Step 7 — Note on limits

Normally, a definite integral is solved by subtracting the antiderivative at the upper limit from the antiderivative at the lower limit. Here, we only include the upper limit because the CDF needs to be normalized between \(0\) and \(1\).  
This way:
- $$-\infty\$$ of the PDF corresponds to \(0\%\) probability in the CDF
- $$+\infty\$$ and below of the PDF corresponds to \(100\%\) probability in the CDF

By only solving for the upper limit, we restrict the range of the function output to \(1\) or between \(-0.5\) and \(0.5\).

---

### Step 8 — Final equation before refactoring

$$
\Phi(x) = \frac{1}{\sqrt{2\pi}\sigma} \sum_{k=0}^{\infty} \frac{(-1)^k}{k!} \cdot \frac{(x - \mu)^{2k+1}}{2k+1} \left( \frac{1}{2\sigma^2} \right)^k
$$

---

### Step 9 — Move $$\(1/\sigma\)$$ inside the summation

$$
\Phi(x) = \frac{1}{\sqrt{2\pi}} \sum_{k=0}^{\infty} \frac{(-1)^k}{2^k  k!  (2k+1)} \left( \frac{x - \mu}{\sigma} \right)^{2k+1}
$$

Notice that the **Z‑score** formula naturally appears within the expression:

$$
Z = \frac{x - \mu}{\sigma}
$$

---

### Step 10 — Add $$\( \frac{1}{2} \)$$ to recenter the mean to 50% probability

$$
\boxed{
\Phi(x) = \frac{1}{2} + \frac{1}{\sqrt{2\pi}} 
\sum_{k=0}^{\infty} \frac{(-1)^k}{2^k k! (2k+1)} 
\left( \frac{x - \mu}{\sigma} \right)^{2k+1}
}
$$
