# Data Insights from the MAFAT Satellite Vision Challenge

![satellite_vision1](https://user-images.githubusercontent.com/6821286/223389185-62d25fc9-767f-4cc7-8caf-c2e50b12883e.png)

In this repository, I use a free tool known as [`fastdup`](https://github.com/visual-layer/fastdup) to gain data insights from [MAFAT Satellite Vision Challenge](https://codalab.lisn.upsaclay.fr/competitions/9603) labeled and unlabeled data.

`fastdup` is a free tool used to manage, clean & curate visual data.
It is fast (runs on you CPU) and scalable. It can handle up to 400M images on a single CPU machine.

The main features of `fastdup` include -
+ Finding duplicates.
+ Finding anomalies.
+ Clustering similar images.

In this repository I ran `fastdup` on both the labeled and unlabeled data, and document my findings.

## 📂 Folder Structure

+ `dataset/` - Stores the image dataset downloaded from the MAFAT official webpage. [Sign up](https://codalab.lisn.upsaclay.fr/competitions/9603) and downloaded the data into this folder.

+ `fastdup_report/` - Stores the reports from fastdup.

+ `fastdup_train.ipynb` - [Notebook](./fastdup_train.ipynb) to analyze the labeled training images.

+ `fastdup_unlabeled.ipynb` - [Notebook](./fastdup_unlabeled.ipynb) to analyze the unlabeled images.

## 👯‍♀️ Duplicates
`fastdup` is extremely fast and robust at finding duplicate images. 

In the unlabeled dataset, I find 927 fully identical images which is 3.74 % of the unlabeled data.
See the notebook [here](./fastdup_unlabeled.ipynb).

![duplicates](./img/duplicates.png)

[Back to top ⤴](#top)

## 🧩 Components
I also used `fastdup` to find similar looking images (clusters).

As shown below, there are many similar looking images clustered together.
These clusters may or may not provide insights. 

![components](./img/components.png)

[Back to top ⤴](#top)

## 🎸 Outliers
`fastdup` can also be used to find anomalies in the dataset. The following gallery shows images that are "different" (measured using `cosine` distance) compared to the rest in the unlabeled dataset.

![outliers](./img/outliers.png)

[Back to top ⤴](#top)

## 📎 Blur
The following gallery shows the images sorted according to blurriness (from most blurry to less).

![blur](./img/blur.png)

[Back to top ⤴](#top)

## 📙 Bright
The following gallery shows the images sorted according to brightness (brightest at the top).

![bright](./img/bright.png)

[Back to top ⤴](#top)

## 🪔 Dark
The following gallery shows the images sorted according to darkness (darkest at the top).

![dark](./img/dark.png)

[Back to top ⤴](#top)


## 📞 Questions? Connect with me
If you have any questions or feedback, please don't hesitate to reach out to me.
I'm active on the following platforms.
<p align="left">
      <a href="https://www.linkedin.com/in/dickson-neoh/" target="blank"><img align="center"
            src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
      <a href="https://twitter.com/dicksonneoh7" target="blank"><img align="center"
            src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" /></a>
      <a href="https://github.com/dnth" target="blank"><img align="center"
            src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" /></a>
      <a href="https://www.youtube.com/channel/UCJckpaGYra_p9ixmEDvYARA" target="blank"><img align="center"
            src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" /></a>
      <a href="mailto:dickson.neoh@gmail.com" target="blank"><img align="center"
            src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
      <a href="https://medium.com/@dickson.neoh" target="blank"><img align="center"
            src="https://img.shields.io/badge/medium-%2312100E.svg?&style=for-the-badge&logo=medium&logoColor=white"/></a>
      <a href="https://dicksonneoh.com/" target="blank"><img align="center"
            src="https://raw.githubusercontent.com/dnth/dnth.github.io/main/static/images/site-navigation/logo_dn.png"
            alt="dnth" height="45" /></a>
</p>

## ❤️ Support Me
I am thrilled to share my work with you and I hope you find it useful. 

If you do, please consider supporting my efforts by making a donation and/or sharing this repository on your social media. 

Your support will help me to continue developing and maintaining this project, as well as create new ones.

<a href="https://www.buymeacoffee.com/dicksonneoh" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

[Back to top ⤴](#top)