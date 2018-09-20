# Machine Learning Engineer Nanodegree
## Capstone Project
Esteban Dib Puelma
September 30th, 2018

## I. Definition
_(approx. 1-2 pages)_

### Project Overview
Day to day, retailers make decisions about which products they need to sell, at what price, where to offer them, in what colors, and many more. These decisions are sometimes blindly made, obeying just rules of thumbs or the managers' guts. Luckily for them, we now have tools to help in this decision making process, and one of them is to segment customers and know them much better than we could without these tools.

I live in Chile, where retail competition has being local for many years, but it is turning more and more global, so it is imperative to apply the best available tools. My dad's company is struggling with some of the judgments mentioned above, because they lack detailed and informed knowledge about the customers that are buying on the stores and I want to make this project the starting point of a Data Strategy that would help compete through the provision of the best possible products and experience to the customers.

In terms of academic research and other studies considering customer segmentation. The closest example is the unsupervised learning project of this Nanodegree, which is also available at Kaggle in https://www.kaggle.com/samratp/creating-customer-segments-unsupervised-learning. Another research that aims to do something similar is a paper called "A Comparative Quantitative Analysis of Contemporary Big Data Clustering Algorithms for Market Segmentation in Hospitality Industry", available here: https://arxiv.org/pdf/1709.06202.pdf. They used a variety of density-based algorithms, including DBSCAN, to segment customers from the hospitality industry. They found that the best choice for their problem was EnDBSCAN to identify nested and embedded clusters, but OPTICS was better to identify adjacent nested clusters.

### Problem Statement
The problem that wants to be solved in this project, is that the company knows nothing about their offline customers. They have some data: identification number, sex, transactions and others, but this data has never been transformed into knowledge. Currently, a customer goes to a store, buys something and that transaction goes to a database and is forgotten. This company has stores all around Chile, and the managers attempt to put the best suitable products available in each location, but they not always succeed in this mission. I want to make a segmentation of the customers, to give managers tools to take more informed decisions, and in the end, increase sales.

To solve the problem I will use a Gaussian Mixture Model and DBSCAN to define clusters based on the age of the customers, and the amount of money and total items they bought in a period of two years, from January 2016 to August 2018. My hope is to find some clearly defined segments to make some marketing and operational decisions within the company. For example, I could find that people in their 20s tend to buy cheap stuff and people in their 50s go for more expensive shopping.

### Metrics

To evaluate both models I will use 2 classical metrics and one more qualitative approach. The classical metrics are the silhouette score, which is calculated with the mean of the distance between each point in a cluster and the mean distance to the nearest cluster, and will allow me to understand if each cluster is very different from the others or not so much; and the Calinski-Harabasz index of the clusters, which evaluates the cluster validity based on the average between-cluster sum of squares and the average within-cluster sum of squares, and will allow me to understand how related clusters are among themselves combined with their relationship between each other (http://datamining.rutgers.edu/publication/internalmeasures.pdf). The "qualitative" approach will be to look at the graphs that both algorithms create when clustering the data, and understand visually the flaws and virtues each one has.

I consider that the metrics chosen are important because the first one will give me information about how different are customer segments from each other, the second one will give me information about the integrity of each customer segment and how related each customer is with the cluster and the third one, the visualization, will give me an easy way to understand the distribution of the clusters and how the dimensions analyzed impact the segmentation.

## II. Analysis
_(approx. 2-4 pages)_

### Data Exploration
In this section, you will be expected to analyze the data you are using for the problem. This data can either be in the form of a dataset (or datasets), input data (or input files), or even an environment. The type of data should be thoroughly described and, if possible, have basic statistics and information presented (such as discussion of input features or defining characteristics about the input or environment). Any abnormalities or interesting qualities about the data that may need to be addressed have been identified (such as features that need to be transformed or the possibility of outliers). Questions to ask yourself when writing this section:
- _If a dataset is present for this problem, have you thoroughly discussed certain features about the dataset? Has a data sample been provided to the reader?_
- _If a dataset is present for this problem, are statistics about the dataset calculated and reported? Have any relevant results from this calculation been discussed?_
- _If a dataset is **not** present for this problem, has discussion been made about the input space or input data for your problem?_
- _Are there any abnormalities or characteristics about the input space or dataset that need to be addressed? (categorical variables, missing values, outliers, etc.)_

### Exploratory Visualization
In this section, you will need to provide some form of visualization that summarizes or extracts a relevant characteristic or feature about the data. The visualization should adequately support the data being used. Discuss why this visualization was chosen and how it is relevant. Questions to ask yourself when writing this section:
- _Have you visualized a relevant characteristic or feature about the dataset or input data?_
- _Is the visualization thoroughly analyzed and discussed?_
- _If a plot is provided, are the axes, title, and datum clearly defined?_

### Algorithms and Techniques
In this section, you will need to discuss the algorithms and techniques you intend to use for solving the problem. You should justify the use of each one based on the characteristics of the problem and the problem domain. Questions to ask yourself when writing this section:
- _Are the algorithms you will use, including any default variables/parameters in the project clearly defined?_
- _Are the techniques to be used thoroughly discussed and justified?_
- _Is it made clear how the input data or datasets will be handled by the algorithms and techniques chosen?_

### Benchmark

In qualitative terms, to consider the analysis successful, the clusters created by the model should help take commercial decisions and should represent types of customers. Today, the company is guessing that they have 4 types of clients based on an psychographic description. These types are: sport casual, basic classical, sophisticated classical, and ethnic. If the algorithm is capable of accurately describe these four types or make a better segmentation of the clients, it will beat the human created model. Thus, better than the benchmark model.

In quantitative terms, I will compare my algorithms with a k-means algorithms with the best number of clusters based on silhouette score and the Calinski-Harabasz index, but with no other parameters optimized. This will help me get some insights on wether what I am doing is just a minor improvement or a much more fascinating approach. If the k-means algorithm achieves a better value in the metrics, then the use of the proposed algorithms is not valuable.


## III. Methodology
_(approx. 3-5 pages)_

### Data Preprocessing
data_cleaner.py

In this section, all of your preprocessing steps will need to be clearly documented, if any were necessary. From the previous section, any of the abnormalities or characteristics that you identified about the dataset will be addressed and corrected here. Questions to ask yourself when writing this section:
- _If the algorithms chosen require preprocessing steps like feature selection or feature transformations, have they been properly documented?_
- _Based on the **Data Exploration** section, if there were abnormalities or characteristics that needed to be addressed, have they been properly corrected?_
- _If no preprocessing is needed, has it been made clear why?_

### Implementation

3 features used
Inertia -> Calinski-Harabasz

In this section, the process for which metrics, algorithms, and techniques that you implemented for the given data will need to be clearly documented. It should be abundantly clear how the implementation was carried out, and discussion should be made regarding any complications that occurred during this process. Questions to ask yourself when writing this section:
- _Is it made clear how the algorithms and techniques were implemented with the given datasets or input data?_
- _Were there any complications with the original metrics or techniques that required changing prior to acquiring a solution?_
- _Was there any part of the coding process (e.g., writing complicated functions) that should be documented?_

### Refinement
For the Gaussian Mixture Model and to create the benchmark k-means model, I made a measurement of the silhouette score and the Calinski-Harabasz index for each number of clusters, from 2 to 50. The graphs are presented below

TODO: ADD GRAPHS

After that I refined the hyper-parameters of the GMM with a grid search, varying the 4 types of covariance, the 2 types of parameters initializations, 4 different values for the convergence threshold and 3 different values for the maximum amount of iterations. Based on the analysis, the best silhouette score is presented when the covariance is full, the convergence threshold is 0.1, the max iterations made by the algorithm are 50 and the initial distribution is made by k-means. The best Calinski-Harabazs score is presented in the same circumstances, but with the covariance set to spherical. It is important to notice that if we continue decreasing the value of the max iteration up until 1, we achieve the best scores. This means that k-means, the initialization of the clusters, is a better model.

For the DBSCAN I made a manual grid search considering 8 different values for the eps and seven different values for the minimum samples. I measured the silhouette score and the Calinski-Harabasz index for each combination and chose the ones with the best values. Based on the analysis, the best silhouette score is presented with two clusters, when eps is 0.9 and the minimum number of samples is 60. The best Calinski-Harabaz score is presented with two clusters, when eps is 0.5 and the minimum number of samples is 60.


## IV. Results
_(approx. 2-3 pages)_

### Model Evaluation and Validation
The following values were achieved by each model

TODO: INSERT TABLE

As seen above, in terms of the qualitative analysis, the best model is the k-means, the benchmark model. This is disappointing, but encouraging at the same time. It means that with a simple clustering model it is possible to get interesting information from the companies customers.

When a more qualitative analysis is made  
In this section, the final model and any supporting qualities should be evaluated in detail. It should be clear how the final model was derived and why this model was chosen. In addition, some type of analysis should be used to validate the robustness of this model and its solution, such as manipulating the input data or environment to see how the model’s solution is affected (this is called sensitivity analysis). Questions to ask yourself when writing this section:
- _Is the final model reasonable and aligning with solution expectations? Are the final parameters of the model appropriate?_
- _Has the final model been tested with various inputs to evaluate whether the model generalizes well to unseen data?_
- _Is the model robust enough for the problem? Do small perturbations (changes) in training data or the input space greatly affect the results?_
- _Can results found from the model be trusted?_

### Justification
In this section, your model’s final solution and its results should be compared to the benchmark you established earlier in the project using some type of statistical analysis. You should also justify whether these results and the solution are significant enough to have solved the problem posed in the project. Questions to ask yourself when writing this section:
- _Are the final results found stronger than the benchmark result reported earlier?_
- _Have you thoroughly analyzed and discussed the final solution?_
- _Is the final solution significant enough to have solved the problem?_


## V. Conclusion
_(approx. 1-2 pages)_

### Free-Form Visualization
In this section, you will need to provide some form of visualization that emphasizes an important quality about the project. It is much more free-form, but should reasonably support a significant result or characteristic about the problem that you want to discuss. Questions to ask yourself when writing this section:
- _Have you visualized a relevant or important quality about the problem, dataset, input data, or results?_
- _Is the visualization thoroughly analyzed and discussed?_
- _If a plot is provided, are the axes, title, and datum clearly defined?_

### Reflection
In this section, you will summarize the entire end-to-end problem solution and discuss one or two particular aspects of the project you found interesting or difficult. You are expected to reflect on the project as a whole to show that you have a firm understanding of the entire process employed in your work. Questions to ask yourself when writing this section:
- _Have you thoroughly summarized the entire process you used for this project?_
- _Were there any interesting aspects of the project?_
- _Were there any difficult aspects of the project?_
- _Does the final model and solution fit your expectations for the problem, and should it be used in a general setting to solve these types of problems?_

### Improvement
In this section, you will need to provide discussion as to how one aspect of the implementation you designed could be improved. As an example, consider ways your implementation can be made more general, and what would need to be modified. You do not need to make this improvement, but the potential solutions resulting from these changes are considered and compared/contrasted to your current solution. Questions to ask yourself when writing this section:
- _Are there further improvements that could be made on the algorithms or techniques you used in this project?_
- _Were there algorithms or techniques you researched that you did not know how to implement, but would consider using if you knew how?_
- _If you used your final solution as the new benchmark, do you think an even better solution exists?_

-----------

**Before submitting, ask yourself. . .**

- Does the project report you’ve written follow a well-organized structure similar to that of the project template?
- Is each section (particularly **Analysis** and **Methodology**) written in a clear, concise and specific fashion? Are there any ambiguous terms or phrases that need clarification?
- Would the intended audience of your project be able to understand your analysis, methods, and results?
- Have you properly proof-read your project report to assure there are minimal grammatical and spelling mistakes?
- Are all the resources used for this project correctly cited and referenced?
- Is the code that implements your solution easily readable and properly commented?
- Does the code execute without error and produce results similar to those reported?
