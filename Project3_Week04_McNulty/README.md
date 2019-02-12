# Weeks 4-6: Project McNulty
# Classification of LandSat Images

### _Start Date: October 17, 2018_ &emsp; _Due Date: November 1, 2018_

For this project, the Metis students were asked to create a classifier using a supervised learning approach.  I chose to analyze multi-spectral satellite images of agricultural terrain on the earth's surface.

The elements of the project are:  
1. Three Jupyter Notebooks, [LandSat_DataAssessment](LandSat_DataAssessment.ipynb), [LandSat_Classification](LandSat_Classification.ipynb), and [LandSat_PCAandFinal](LandSat_PCAandFinal.ipynb), providing a sequential analysis of the data from exploration to final classifier.
2. The original [project proposal](Project3_Proposal.pdf).
3. The [project summary](Project3_Summary.pdf) detailing the approach and results.
4. A [Power Point presentation](Project3_Presentation.pptx), also available in [pdf format](Project3_Presentation.pdf).

The LandSat imaging data is freely available from the UC Irvine Machine Learning Repository, at https://archive.ics.uci.edu/ml/datasets/Statlog+%28Landsat+Satellite%29.

The classification accuracy and precision of the terrain types was reasonably good, with both at 84% (unweighted by class distribution) using a Random Forest decision tree model. Identification of cotton crop, nominally chosen to be the most important of the classes for this exercise, was improved by making a cost-benefit adjustment - specifically penalizing confusions between cotton and vegetation while tolerating confusions between soil types.

Improvements include a better way to remove spatial and spectral correlations (e.g. by rotationally-invariant principal component analysis) and application of a neural network for classification.

_Did you know?_  This project was named for Jimmy McNulty, one of the detectives in HBO's _The Wire_.
