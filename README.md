# Phorch

Malicious web site is a foundation of criminal activities on Internet. This links enables partial 
or full machine control to the attackers. This results in victim systems, which get
easily infected allowing attackers to utilize systems for quite a number of cyber-crimes such
as stealing credentials, spamming, phishing, denial-of-service and many extra such attacks. 
The rising issue related to spamming, phishing and malware, has created a requirement for solid
framework solution which can analyze the extracted features, classify and further recognize the malicious URL.
Therefore, the methodology and technique to detect such crimes should be fast and precise
with the additional capability to detect new malicious websites or content. 
<br />
<br />
This repository introduces an automatic tool to extract 111 significant features for a URL. Additionally, this
also proposes the URL classification process which recognizes whether the target website is a malicious(1) or benign(0).

[URL.md](https://github.com/vidhigupta9/pytorch/blob/main/URL.md) provides detailed information and methods on how to extract features from urls for prediction and also how to create your own database.
<br />

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
