# Webscrapping
This repository contains two mini-educational projects from Webscrapping. 

# OtoDom
This is a mini homework project with Webscrapping on Sages [Kodołamacz Data Science Bootcamp](https://www.kodolamacz.pl/bootcamp-datascience/), which I have participated since September 2019.

## Purpose
Collect information about houses for sale from [OtoDom](https://www.otodom.pl/) and put them in DataFrame. These data can be used in the future to predict house prices or other analyzes.

## Dependencies
* Python 3.6+
* Selenium
* Chromdriver

# TranslatorInTerminal
This is my hobby project with Webscrapping. I have implemented a script that collects the translation of word data from [online dictionary pl.bab.la](https://pl.bab.la/slownik/Polish-English/bla-bla) and displays them in the terminal window. This program translates words from English to Polish and from Polish to English.

## Instructions for use
Add two aliases to .bashrc file :
- alias ang-pol='python (path to script location)/translator.py ang-pol'
- alias pol-ang='python (path to script location)/translator.py pol-ang' 

<b> </b>
At the command prompt, call <i> ang-pol word_to_traslate_from_English_to_Polish </i> or pol-ang word_to_traslate_from_Polish_to_English

## Dependencies
* Linux
* Python 3.6+
* Urllib
* BeautifulSoup
