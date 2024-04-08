# User Referral API
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

User referral system allows users to referr other users and keep track of referrals.

## Installation 
- Clone this repository
```bash
git clone https://github.com/gh0stfrk/ReferralAPI
``` 
- Create a virtual environment and install dependencies 
```bash
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```
- Setup postgresql locally or use sqlite
- Create a .env file in `app/src` copy the contents of sample.env
- Start the development server
```bash
python3 main.py
```
## Use Docker 
- Pull the image from hub
```bash
docker pull salmansyyd/referral-api
```
- Start the container from the image
```bash
docker run -d -p 8000:8000 salmansyyd/referral-api
```
