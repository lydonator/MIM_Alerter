# MIM Token Supply / Web Scraper
Desktop alerts for MIM token availability on Abracadabra.Money

## Requirements
Selenium (pip install selenium)  
Win10toast (pip install win10toast)  
Python >=3.8  
Chrome  
Windows 7+

## Get Started

### Step 1: Launch Chrome with remote debugging in a new profile
Open a command prompt and execute the following:  
(Chrome.exe must be in your Environment Path. See https://medium.com/@kevinmarkvi/how-to-add-executables-to-your-path-in-windows-5ffa4ce61a53)  

*chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\MIM_Alert\ChromeProfile"*

### Step 2: Synchronise extensions and import Metamask
Connect to your Google profile and synchronise your extensions. Import your Metamask account, login and add the Avalanche Chain

### Step 3: Browse to Abracadabra
When you have your Metamask account logged in and the Avalanche Chain added, browse to https://abracadabra.money/stand

### Step 4: Run Main.py script
Run main.py




# What is this?
This is a simple web scraping utility that grabs MIM token availability from Abracadabra and serves the information as desktop alerts.

# Who is it for?
Primarily it is for users of Wonderland Time who wish to use wMemo as collateral to borrow MIM tokens. MIM tokens are in short supply,
Therefore it can be difficult to get a hold of them without constantly watching the site. This tool has been helpful for me, hopefully 
It will be for others too.

![image](https://user-images.githubusercontent.com/8610225/145095033-9a124ce1-a19b-48ea-a5d5-c8de41e62cc7.png)


