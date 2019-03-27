# Pet-Adoption
Project Proposal - 2/23/19

Domain chosen:
Our domain is animal welfare. Millions of abandoned or lost animals end up in shelters. Many shelters are overcrowded, and some euthanize animals that aren’t adopted quickly. Studying adoption data may help shelters and rescue organizations connect with potential adopting homes more effectively, reducing needless animal suffering. 

Hypothesis or project topic:
An algorithm can be made to predict animal adoption rates from traits in the animal’s online profile. These traits may include breed, color, gender, health, the quality of images, and the quality of descriptive text.

Our main data source is a dataset available at Kaggle.com on animal shelter records. Here are the tables we intend to use:
   train.csv - Tabular/text data for the training set 
   test.csv - Tabular/text data for the test set
   breed_labels.csv – Data dictionary on breed
   color_labels.csv - Data dictionary on color
   state_labels.csv - Data dictionary on location
  
Project Description:
  1. First, we will perform a data quality check and EDA on training and testing data, for
  example: analyzing missing values, summary statistics, data visualizations, scatter plots,
  and a correlation matrix. We may apply data manipulation depending on the quality of
  the data, for example: replacing missing data with mean, median, or other imputation
  techniques.

  2. Afterward, we will use machine learning techniques to narrow down the candidate
  variable list. Since our target variable is a categorical variable, it is a classification
  problem, so we will explore using classification approaches. The results of these prior
  steps will provide insight into the best format for our final model.
  
  3. Finally, we will build this model and further refine it through testing.

  4. If necessary, we will return to the first step and consider new traits to measure and model
  then repeat this process.

Questions or avenues of exploration required for the project:
- What profile traits should we include in our model? 
- Which traits have the most statistically useful records in the Kaggle tables?
- Considering these traits, which might suggest actions that could be taken to improve how animals are adopted?
- What may be the best classification model in our case?  K - nearest neighbor? Decision trees? Support Vector machines?
- After our best model have been created, how can we utilize the model or present it in a way that could be easily used by shelters and rescue organizations?


------


Karen B - Initial Commentary on Project Plan - 2/28/19

Thank you for you well-defined problem and topic! I think this dataset can help your team learn all the concepts while you work on something interesting (and fun!). You already have a good plan and you can give me more information in your next deliverable. 

- Because you added a few things in your hypothesis, do you think that a few of these is more important than others? 
- Because it is a kaggle competition, you may have to cite similar projects in your paper. Which may include the differences   between your features, model performance, etc.
- As mentioned in the google group, there are many options for your datasets. I think the kaggle dataset you are referring to is a google starting point. If you do combine it with other dataset you have to keep in mind how the differences in the location of the geographic has added nuances on the information on the animal. You can explore the different datasets when you are doing your exploratory datasets to see if you can combine these other animal shelter datasets. 
- For your dataset, you do not need to use the given train and test data as is. You can combine the datasets and split your training and testing data on your own (or set aside data to validate later). This is up to you, and you will have to explain these decisions in your final paper/presentation.
- Based on your exploratory analysis, will you bucket the target categories to a binary set?  (e.g. one previous group found that instead of predicting how many days a loan will be financed, they found that based on the distribution of the data that it was best classify the loan whether if would be finance within 5 days or more than 5 days).
- Do you have enough data to separate models by animal? Would this be an important feature? 
- What are your plans with the descriptive text? What NLP tools and techniques will you consider?
- To present your models, will you build an app? Jupyter widgets? 
- Some articles that might be of interest (some of these use time series analyses and deep learning that  this cohort may not go over in great detail):
        https://www.kaggle.com/c/shelter-animal-outcomes/data (City of Austin Data)
        https://aaronschlegel.me/extraction-feature-engineering-aac-data-requests-pandas.html (Feature engineering using the Austin Shelter Kaggle Data)
        https://data.world/datasets/animal (Datasets that have animal shelter data)
        https://www.aspca.org/animal-homelessness/shelter-intake-and-surrender/pet-statistics (pet statistics as mentioned in google group)
        https://www.aspcapro.org/resource/saving-lives-research-data/lessons-mapping-intake-gis (GIS usage as mentioned in the google group)
        https://data.shelteranimalscount.org/request-the-dataset (Free Dataset as mentioned in the google group)
        https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5981279/ (Literature on animal shelters)
        https://www.dallasopendata.com/City-Services/Dallas-Animal-Shelter-Data/7h2m-3um5 (Dallas, TX animal shelter data)

Your team name in our records will be: Pet Adoption (This is also the name of your github repository)

GitHub Repository: I have created a repository for your team and given access to your team members to this repository. You will need to accept the membership invitation to the Georgetown-Analytics GitHub to gain access to the repository.

Your team project repository is here: https://github.com/georgetown-analytics/Pet-Adoption

Please use this GitHub repository for your code throughout the cohort. You are required to put your project code for all the steps of your project in this GitHub repository, which will be evaluated at the end of the cohort. I will also be reviewing your code in your team GitHub repository throughout the cohort to check on your progress, so please push your code consistently. 
