# Bubbles

## Description

I don't like taking baths.

http://web4.ctf.tamu.edu

## Approach

I've saved the web page [here](./SQLi.html). When we open the website, we see a login form. When we enter incorrect credentials, we see the message "Sorry to say, that's invalid login info!". The title of the web page (SQLi) and the login form hint at a [SQL injection](https://en.wikipedia.org/wiki/SQL_injection) vulnerability. We try a sql injection ' or 1=1-- in both the login and password fields, and we get the message "Huh. We really should gigem{ScRuB7h3InpU7}!".

## Solution

Open web page. Use sql injection ' or 1=1-- in username and password fields to log in. The flag is gigem{ScRuB7h3InpU7}.