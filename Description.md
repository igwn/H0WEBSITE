**Did you know that gravitational waves can be used to measure the expansion of the Universe?
This plot shows one estimate.
Change the parameters in the sidebar at left, then click “Calculate” to see how it affects $H_0$.**

**DISCLAIMER:** The values of the Hubble constant provided here are not
intended to be scientifically accurate estimates.
Please read below for further information.

---

# What is the Hubble constant?

The Hubble constant, $H_0$​, is a measure of how fast our universe is expanding.
As the universe expands, objects such as galaxies get further apart.
From Earth, the galaxies appear to be moving away from us.
The speed at which they do so is known as their \"recession velocity\" ($v$),
and it is directly proportional to their distance ($D$) from us: $v = H_0 D$.

This is known as the Hubble-Lemaître law, and the constant of
proportionality is the Hubble constant.
It is usually measured in km/s/Mpc (kilometers per second per megaparsec, where a megaparsec is 3.26 million light years),
and current measurements by different observational techniques estimate a value of about 70 km/s/Mpc.
This means that for every Mpc of distance from us,
a galaxy's recession velocity increases by around 70 km/s.

## Why use gravitational waves to measure $H_0$?

Other techniques for measuring the Hubble constant, such as using Type IA supernovae (by e.g. the SH0ES Collaboration)
and measurements of the very early Universe (by e.g. the [*Planck Collaboration*](https://www.cosmos.esa.int/web/planck/planck-collaboration)),
currently disagree with each other, with values of around 73 km/s/Mpc and 67 km/s/Mpc respectively
(which you can add to the plot if you like).
By making an independent measurement of the Hubble constant,
Gravitational waves (GWs) might be able to shed light on this apparent discrepancy.

---

# How do you measure the Hubble constant using gravitational waves?

Gravitational wave observations of merging black holes and neutron stars by [*Advanced LIGO*](https://www.ligo.org/about.php),
[*Virgo*](https://www.virgo-gw.eu/) and [*KAGRA*](https://gwcenter.icrr.u-tokyo.ac.jp/en/) provide us with a
direct measurement of their luminosity distance ($D_L$​) since the
amplitude of a GW is inversely proportional to this distance.

In the nearby universe, the Hubble-Lemaître law can be expressed in
terms of luminosity distance and redshift ($z$) as $cz \approx H_0 D_L$​​, where $c$ is the speed of light.

If the gravitational wave is well localised on the sky, astronomers can
use their telescopes to search this area for any electromagnetic (EM) signals produced by the merging objects,
covering wavelengths from radio to gamma rays.
If an EM counterpart is detected, it can be used to
identify the host galaxy of the gravitational wave, and then the
redshift of that galaxy can be used in combination with the GW distance
to measure $H_0$ !

There are large uncertainties on the luminosity distance measured by today\'s GW detectors \-- usually around 30%.
This means that the measurement of $H_0$ from a single GW event with an EM counterpart
will have a large uncertainty associated with it.
However, by combining the
results from multiple GW-EM observations, these uncertainties will
decrease, leading to a more informative measurement.
The plot above shows a quick estimate of the Hubble constant based on the selected GW and EM events.
Try changing the GW events and EM counterparts in the fields in the sidebar to see how the estimate changes.

## The assumptions used in this website

This website only uses publicly available GW and EM data.
The GW data comes in the form of skymaps from [*GraceDB*](https://gracedb.ligo.org/).
These provide an estimate of the 3D localisation of the GW event in the form of a sky probability and Gaussian distance estimate for every line-of-sight.
This information is produced from a preliminary \"quick\" analysis of the GW event,
and will differ from the final volume localisation produced by the LVK for this event,
for which a more rigorous analysis is applied.
This means that, while the distance estimate will be in the right ballpark,
the shape of the distance distribution, including its peak and width, is likely to change with later analyses.

A number of other simplifying assumptions are made to produce the estimate above.
The linear Hubble relation written above is only valid
in the local universe but is used throughout this analysis, meaning that
for higher distance events, the result will be less reliable.
This allows us to approximate GW selection effects as $\propto {H_0}^3$,
which means we can ignore the impact of detector sensitivity and the GW mass
distribution (among other things), which are required to accurately estimate this.

This website neglects the impact that galaxy peculiar velocity can have on the result.
Galaxy motion not due to the expansion of the universe is
known as its peculiar velocity, and can have a large impact on the
galaxy\'s measured redshift, especially for galaxies which are
relatively nearby to us ($z \leq 0.1$).
The result above also treats the selected EM counterparts as if they are confidently associated with the GW event,
and does not take into account any uncertainty in the association.

---

# Additional information

The values of the Hubble constant provided here are not intended to be
scientifically accurate estimates.
This website is intended to be an
educational resource.
For the latest official measurement of the Hubble constant from the LVK collaboration,
look out for the [*latest LVK publications*](https://pnp.ligo.org/ppcomm/Papers.html).

If you have questions about gravitational wave science, please visit
[*https://ask.igwn.org*](https://ask.igwn.org).

## How to cite this website?

Anyone is welcome to use and share  plots generated by this website for research
or  education  purposes.  If  you  do,  please quote  the  URL  and  credit  the
LIGO-Virgo-KAGRA Collaboration.
Note that users will not necessarily use the same
events that you have selected, and that the options may change over time.

## Credits and contacts

The website is provided on behalf of the LIGO-Virgo-KAGRA collaboration.
It was developed by (in alphabetical order):
  - Hsin-Yu Chen (University of Texas at Austin)
  - Mathieu Dubois (L2IT/CNRS)
  - Luis Galvis (Universidad de Antioquia)
  - Rachel Gray (Glasgow University)
  - Tathagata Ghosh (IUCAA)
  - Chris North (Cardiff University)
  - Antonio Enea Romano (Universidad de Antioquia)
  - Nicola Tamanini (L2IT/CNRS)
  - Sergio Vallejo (Universidad de Antioquia)

If you find an issue with the website, please report it on the [*Github
repository*](https://github.com/igwn/h0-website).
