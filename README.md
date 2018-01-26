Infoga - Email Information Gathering
====================================

Infoga is a tool for gathering e-mail accounts information (ip,hostname,country,...) from different public sources (search engines, pgp key servers). Is a really simple tool, but very effective for the early stages of a penetration test or just to know the visibility of your company in the Internet.

![Infoga](https://raw.githubusercontent.com/m4ll0k/Infoga/master/screen/screen1.png)

DISCLAIMER
==========
Usage of Infoga for attacking targets without prior mutual consent is illegal. Infoga developer not responsible to any damage caused by Infoga.

Requirements
============

* Python <= 2.7

Installation
============

```
git clone https://github.com/m4ll0k/Infoga.git infoga
cd infoga
pip install -r requirements.txt
python infoga.py
```

Usage
=====

```

python infoga.py --domain [DOMAIN] --source [SOURCE] --verbose [LEVEL]

python infoga.py --info [EMAIL] --verbose [LEVEL]

```

Example
=======

```

python infoga.py --domain fbi.gov --source google --verbose 3

```
![example_1](https://raw.githubusercontent.com/m4ll0k/Infoga/master/screen/screen2.png)

```
python infoga.py --domain  fbi.gov --source all --verbose 3

```

![example_2](https://raw.githubusercontent.com/m4ll0k/Infoga/master/screen/screen3.png)
