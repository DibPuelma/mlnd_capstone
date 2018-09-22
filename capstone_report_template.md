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

To solve the problem I will use data from two main sources:

The first one will be given by the company and is the history of purchase from 4 of the company's stores. This dataset includes the customer's email and RUT (Unique Tax Number in Chile) which gives a estimation of the age of the person and is a unique identifier of who is making the purchase, the date of the transaction, the amount of items, the price of each item and in which store the purchase was made. It has 9528 rows of data in total. This dataset is available in the .zip file of this project and a sample is shown below:

TODO: INSERT DATA SAMPLE FROM EXCEL

The second one is a public API hosted in https://api.rutify.cl/, which gives you the address and sex of a person based on it's RUT. An example of the API response is shown below:

TODO: INSERT API RESPONSE

To clean the data and make a better and focused segmentation I did some data manipulation.
1.- Group the transactions of each person to get the amount of items that person bought and the amount of money he or she spent in the whole period of analysis.
2.- Drop all the features that did not contribute to the segmentation I wanted to make, such as date, year, month, rut, purchase_type among others.
3.- Remove all the ids generated when I consolidated the data. This was done in the data_cleaner.py file and consisted on getting the age of each customer and leaving the wholesalers out of the customer base.
4.- Remove all rows with NA values.

This data processing left 3 important features for each client: age, number of items bought and amount of money spent.

The outlier removal is explained in the Data Preprocessing section

### Exploratory Visualization
I used the visualization of the data to see the distribution of each feature and how each one related to one another. For this I used two graphs, a scatter matrix and a heat map. Both images are shown below.

TODO: INSERT HEAT MAP AND SCATTER MATRIX

As we can see, there is a huge correlation between the amount of money spent and the amount of items bought. This is pretty normal, as more items mean more money, but is important to have both features so we can differentiate customers that buy expensive things from the ones that buy cheap things in a bulkier way.

It is interesting that in the scatter matrix is it possible to see some outliers values in the amount of money spent (period_total_value) and in the amount of items bought (period_total_quantity). This outliers were deleted from the dataset.

### Algorithms and Techniques
As this is a segmentation problem, I will use clustering algorithms. Specifically I will use two algorithms; a Gaussian Mixture Model, because I believe that the data should be composed of a finite number of Gaussian distributions; and a DBSCAN to see if a density based clustering technique is adequate for this type of problems. Both algorithms will take the data points and assign them to clusters.

The first one will use k-means or random positions to establish the first centroids and then iterate to move those centroids in order to try to find a better clustering. The second one will start in a random location and use the epsilon and the minimum number of points to decide wether a group of points belongs to a cluster or not. In the following webpage there is a very clear example of how this works (https://www.naftaliharris.com/blog/visualizing-dbscan-clustering/).

In terms of hyper-parameters, for the GMM, I will use the metrics to find the best number of components and then use a grid search algorithm to find the best type of covariance between full, tied, diagonal or spherical, the best type of parameter initialization between k-means or random, a good value for the convergence threshold and a good value for the maximum amount of iterations. For the DBSCAN I will use a grid search algorithm to find a good value for the maximum distance between to points to be considered of the same cluster (epsilon) and a good value for the minimum amount of samples in the neighborhood of a data point for it to be considered a core point (minimum samples).

### Benchmark

In qualitative terms, to consider the analysis successful, the clusters created by the model should help take commercial decisions and should represent types of customers. Today, the company is guessing that they have 4 types of clients based on an psychographic description and I think this could be reflected in their expenditure habits. These types are: sport casual, basic classical, sophisticated classical, and ethnic. If the algorithm is capable of accurately describe these four types or make a better segmentation of the clients, it will beat the human created model. Thus, better than the benchmark model.

In quantitative terms, I will compare my algorithms with a k-means algorithms with the best number of clusters based on silhouette score and the Calinski-Harabasz index, but with no other parameters optimized. This will help me get some insights on wether what I am doing is just a minor improvement or a much more fascinating approach. If the k-means algorithm achieves a better value in the metrics, then the use of the proposed algorithms is not valuable.


## III. Methodology
_(approx. 3-5 pages)_

### Data Preprocessing
data_cleaner.py
Explain preprocessing made in ipynb

In this section, all of your preprocessing steps will need to be clearly documented, if any were necessary. From the previous section, any of the abnormalities or characteristics that you identified about the dataset will be addressed and corrected here. Questions to ask yourself when writing this section:
- _If the algorithms chosen require preprocessing steps like feature selection or feature transformations, have they been properly documented?_
- _Based on the **Data Exploration** section, if there were abnormalities or characteristics that needed to be addressed, have they been properly corrected?_
- _If no preprocessing is needed, has it been made clear why?_

### Implementation

3 features of the data used
GMM, DBSCAN
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
The following values were achieved by each proposed model

TODO: INSERT TABLE WITH SILHOUETTE AND CH VALUES for DBSCAN and GMM

As seen in the table, the Gaussian Mixture Model had a much better performance than the DBSCAN. I thought that it was going to be the other way around, but even looking at the clustering graphs is it obvious that the DBSCAN algorithm does not work for this dataset.

The scores for the Gaussian Mixture Model are not incredibly good, but they seem reasonable for me to say that we can trust on the customer segmentation that was made, and that those segments are probably a good start to achieve a better understanding and this is reflected when a more qualitative analysis is made, because the clusters give interesting information.

The table below shows 7 clusters.
- Cluster number 1 represents
- Cluster number 2 represents
- Cluster number 3 represents
- Cluster number 4 represents
- Cluster number 5 represents
- Cluster number 6 represents
- Cluster number 7 represents

TODO: ADD TABLE OF CLUSTERS AND DESCRIBE WHAT THEY REPRESENT


### Justification
In the following table, we can see that GMM did not have better results than the proposed k-means benchmark model.

TODO: ADD TABLE GMM VS K-MEANS

Although I used grid search to look for the best hyper-parameters for both the Gaussian Mixture Model and the DBSCAN, neither of them could get a better score than the k-means model. This is disappointing, but encouraging at the same time. It means that with a simple and well-known clustering model it is possible to get interesting information from the company's customers.

As I mentioned before, this is a start point for a better customer understanding and despite this project did not give all the answers, it illuminated the path to follow. To further validate the analysis and solve the problem, I would disaggregate the data from each store. They are all located in different environments, with different people that can have different habits. So to make better decisions and solve the presented problem, it is necessary to understand the segments for each of the stores.

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

In terms of algorithms I think there is a lot to improve. Although k-means turned out to be the best of the three algorithms, there are many more clustering algorithms that could be use. For another project I would definitely try Affinity Propagation because the customers are more like a bunch of points together than different figures in space and according to the classical analysis of clustering algorithms, AP is good on that (http://scikit-learn.org/0.16/_images/plot_cluster_comparison_0011.png)

I would not try to tune the hyper-parameters of the two algorithms I used. On one hand, When I did the grid search on the Gaussian Mixture Model I realized that when the maximum numbers of iterations was 1 and I started from a k-means I always got the best scores, so obviously that is telling me to converge the GMM to a k-means. On the other hand, it does not matter how much I tuned the hyper-parameters on DBSCAN, I could not get good results, and now that I know more about the data distribution and looking at the clustering comparison image, I can tell that DBSCAN was a bad choice.

If I use my proposed solution as the benchmark I would get a better solution almost instantly: k-means. I still think that Affinity Propagation or maybe ward can do better than k-means and I will have to experiment with those algorithms in a forthcoming project.

-----------

**Before submitting, ask yourself. . .**

- Does the project report you’ve written follow a well-organized structure similar to that of the project template?
- Is each section (particularly **Analysis** and **Methodology**) written in a clear, concise and specific fashion? Are there any ambiguous terms or phrases that need clarification?
- Would the intended audience of your project be able to understand your analysis, methods, and results?
- Have you properly proof-read your project report to assure there are minimal grammatical and spelling mistakes?
- Are all the resources used for this project correctly cited and referenced?
- Is the code that implements your solution easily readable and properly commented?
- Does the code execute without error and produce results similar to those reported?
