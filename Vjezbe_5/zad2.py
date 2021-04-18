import harmonic_oscillator as ho

h1=ho.HarmonicOscillator(10,0.1,0.3,0)
h1.period_titr(0.1,5)
h1.reset()
h1=ho.HarmonicOscillator(10,0.1,0.3,0)
h1.period_titr(0.01,5)
h1.reset()
h1=ho.HarmonicOscillator(10,0.1,0.3,0)
h1.period_titr(0.001,5)
h1.analit_period()


