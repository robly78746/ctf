# Bender

## Description

My story is a lot like yours, only more interesting ‘cause it involves robots.

http://web3.ctf.tamu.edu

## Approach

When we open the web page, we see the text "No Google Bot can help you now!" and a GIF of Bender dancing. First, we look at the source and find nothing interesting. The text hints at the website having a [robots.txt](http://www.robotstxt.org/robotstxt.html) file. We try looking at http://web3.ctf.tamu.edu/robots.txt and find it disallows the web page oiuwerljk.html. We navigate to http://web3.ctf.tamu.edu/oiuwerljk.html and see the flag gigem{craw1ing_bot$!}.

## Solution

Open the web page. Navigate to http://web3.ctf.tamu.edu/robots.txt to find another web page. Open http://web3.ctf.tamu.edu/oiuwerljk.html to find the flag gigem{craw1ing_bot$!}.