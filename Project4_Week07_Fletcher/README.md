# Weeks 7-8: Project Fletcher
# Natural Language Processing of Economic News Articles

### _Start Date: November 5, 2018_ &emsp; _Due Date: November 19, 2018_

For the fourth project, we were required to incorporate unsupervised clustering on a natural language data set and develop a real-world end product such as a recommender system or automated classifier.  My data set was a large collection of economic news articles, which included reader surveys about the relevance of the articles to the health of the U.S. economy.

The components of the project in this repository are:  
1. Two Jupyter Notebooks, [News_DataAssessment](News_DataAssessment.ipynb) and [News_TokenModeling](News_TokenModeling.ipynb).
2. The original [project proposal](Project4_Proposal.pdf).
3. The [project summary](Project4_Summary.pdf) describing the data set and analysis.
4. A [Power Point presentation](Project4_Presentation.pdf) in pdf format.

The newspaper article data set is freely available at Data for Everyone, http://www.figure-eight.com/data-for-everyone/.

The newspapers articles were tokenized via standard NLP techniques, including a search for named entities (e.g. Federal Reserve, The White House, New York City). The articles were clustered by topic using the latent dirichlet allocation method. K-nearest Neighbor and Random Forest  classification models were applied to the relevance/non-relevance article labels and linear regression to the degree of economic positivity (according to the results of the reader surveys). The prediction results of these models was subpar, but several areas of improvement were noted during analysis.

_Did you know?_  This project was named for Jessica Flethcher, the famous mystery writer and amateur sleuth from Maine in the long-running TV series _Murder She Wrote_.
