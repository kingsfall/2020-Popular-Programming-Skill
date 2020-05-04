# Popular programming skill in 2020 for remote work

## Why I created this project
This project came about when I was deciding on which path of develop my programming knowledge. I would like to know what skills and roles are currently in demand for remote work
by the market in 2020. 

## How I develop this project
I scrape WeWorkRemotely to get the keywords for job openings using Puppeteer and Cheerio. The DOM file for the website is fairly clean and clear to handle. Not much nested HTML tags.

Thereaafter, I did a simple text cleaning by removing caps, spaces and dashes and transfer the data over to Python.

Based on research, I created a simple programming classification dictionary with types of programming roles as keys and populated the values with skills such as Python, React, Ruby, etc.

I felt there was no need to be using any complicated text classification NLP packages as there was not a lot of data to train on. Thereafter, I visualized the data with barchat from scikit learn.

