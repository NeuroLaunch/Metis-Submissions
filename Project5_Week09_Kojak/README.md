# Weeks 9 - 12: Project Kojak
# Automated Speaker Recognition

### _Start Date: November 25, 2018_ &emsp; _Due Date: December 12, 2018_

This is the final "passion" project, for which I delve into the mysteries of human hearing.

The elements for this project are:  
1. The main Jupyter Notebook, [ClassOptimization.ipynb](ClassOptimization.ipynb) which implements the full-scale speaker recognition model for 100 smart-speaker "households". Notebooks with preliminary exploration and analysis are [Audio_Loading.ipynb](Audio_Loading.ipynb), [Audio_Grouping.ipynb](Audio_Grouping.ipynb), and [NMF_Diarization.ipynb](NMF_Diarization.ipynb).
2. A python module containing utility functions for processing speech waveforms, [Speech_Analysis.py](Speech_Analysis.py).
3. The original [project proposal](Project5_Proposal.pdf).
4. The [project summary](Project5_Summary.pdf), which describes in detail the scope of the project and overall results.
5. A [Keynote presentation](Project5_Presentation.key) on the project. There's also a [pdf version](Project5_Presentation.pdf).

The data set for this project was the DARPA TIMIT Acoustic-Phonetic Continuous Speech Corpus, consisting of audio recordings of English sentences spoken by hundreds of male and female subjects from 7 different dialect regions of the United States. The data is described at https://catalog.ldc.upenn.edu/docs/LDC93S1/timit.readme.html.

In summary, the main analytical steps for speaker recognition were 1) conversion of audio waveforms to spectrograms, 2) nonnegative matrix factorization (NMF) to define speaker phoneme "signatures", and 3) a readout of NMF activation energy to determine the most likely speaker of a test sentence. 100 households were simulated, each with 6 speakers, male and female, from 1 or more dialect regions.

From limited training data, over 80% speaker recognition was possible after only a few seconds of audio processing. With modest trade-off, identification of a speaker outside of the trained group of 6 was also possible. Future additions to the model include the improvement of spectral processing using mel cepstral coefficients and the incorporation of an additional classification layer such as a support vector machine.

_Did you know?_  This project was named for Theo Kojak, the iconic (and bald) detective from the eponymous 70s TV show.
