# Veggies

## Description

So many choices...

http://web2.ctf.tamu.edu

## Approach

I've saved the web page [here](./web2.ctf.tamu.edu.html). When we open the web site, we see a GIF of a bored Cookie Monster and two buttons labeled "Vegetables?" and "Cookies?". Clicking on the vegetables button takes us to another page with a JPEG of the Cookie Monster holding vegetables. Clicking on the cookies button takes us to another page with a GIF of the Cookie Monster eating cookies. First, I look at the sources of the three web pages and find nothing interesting. The Cookie Monster in the jpeg and gifs give a big hint to look at the cookies, so I view my cookies using the Chrome plugin [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=en). I see a cookie called veggie with a value of e05PX1ZFR0dJRVN9. I guessed this was base64 and ran it through an [online base64 decoder](https://www.base64decode.org/). e05PX1ZFR0dJRVN9 decoded to {NO_VEGGIES}.

## Solution

Open the web page. Check cookies and find veggie:e05PX1ZFR0dJRVN9. Base64 decode e05PX1ZFR0dJRVN9 into {NO_VEGGIES}. The flag is gigem{NO_VEGGIES}.