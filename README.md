# Data Insights from the MAFAT Satellite Vision Challenge

![satellite_vision1](https://user-images.githubusercontent.com/6821286/223389185-62d25fc9-767f-4cc7-8caf-c2e50b12883e.png)

Data insights from [MAFAT Satellite Vision Challenge](https://codalab.lisn.upsaclay.fr/competitions/9603).

## Folder Structure

+ `dataset/` - Stores the image dataset downloaded from the MAFAT official webpage.

+ `fastdup_report/` - Stores the reports from fastdup.

+ `fastdup_train.ipynb` - Notebook to analyze the labeled training images.

+ `fastdup_unlabeled.ipynb` - Notebook to analyze the unlabeled images.

## 👯‍♀️ Duplicates
We find 927 fully identical images (d>0.990), which are 3.74 % of the unlabeled data.
See the notebook [here](./fastdup_unlabeled.ipynb).

![duplicates](./img/duplicates.png)

## 🧩 Components
We find many clusters of similar looking images which may or may not provide insight.
![componenets](./img/components.png)

## 🎸 Outliers
![outliers](./img/outliers.png)

## 📎 Blur
![blur](./img/blur.png)

## 📙 Bright
![bright](./img/bright.png)

## 🪔 Dark
![dark](./img/dark.png)




