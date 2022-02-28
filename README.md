# Phizon

The base of any illicit activity on the Internet is a malicious web site. The attackers can gain partial or complete control of the machine using these linkages. As a result, target systems become readily infected, allowing attackers to use them for a variety of cyber-crimes such as credential theft, spamming, phishing, denial-of-service assaults, and other similar attacks.
The rising issue related to spamming, phishing and malware, has created a requirement for solid
framework solution which can analyze the extracted features, classify and further recognize the malicious URL as well as images of clone websites.
Therefore, the methodology and technique to detect such crimes should be fast and precise
with the additional capability to detect new malicious websites or content. 
<br />
<br />

## What we do
### URL Check
This repository introduces an automatic tool to extract 111 significant features for a URL. Additionally, this
also proposes the URL classification process which recognizes whether the target website is a malicious(1) or benign(0). User can enter any URL of choice and even randomly use it on tweets in real time to observe any malicious activity.

[Url.md](https://github.com/vidhigupta9/aws/blob/main/Url.md) provides detailed information and methods on how to extract features from urls for prediction and also how to create your own database.
<br />

### Clone Check
Upload a website screenshot/image to see whether it is a clone of any authorised popular website to prevent sensitive information retrieval and data breaches. Classify it using our deep learning model trained on Habana DL1 accelerators.
<br />

## Dataset

## Install

```bash
$ sudo apt-get update && sudo apt-get upgrade
$ sudo apt-get install virtualenv python3 python3-dev python-dev gcc libpq-dev libssl-dev libffi-dev build-essentials
$ virtualenv -p /usr/bin/python3 .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```

### How to use
Run:

```bash
$ streamlit run app.py
```

## Reference
[Feature Importance Guided Attack: A Model Agnostic Adversarial Attack](https://arxiv.org/abs/2106.14815#:~:text=Feature%20Importance%20Guided%20Attack%3A%20A%20Model%20Agnostic%20Adversarial%20Attack,-Gilad%20Gressel%2C%20Niranjan&text=Machine%20learning%20models%20are%20susceptible,which%20dramatically%20reduce%20their%20performance.&text=We%20keep%20the%20attack%20realistic,adversary%20would%20have%20control%20over.)
