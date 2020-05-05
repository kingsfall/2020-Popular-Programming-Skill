const puppeteer = require('puppeteer')
const cheerio = require('cheerio')
const fs = require('fs') 
// const $ = cheerio.load('<h2 class="title">Hello world</h2>')

// $('h2.title').text('Hello there!')
// $('h2').addClass('welcome')

// console.log($.html())
//=> <html><head></head><body><h2 class="title welcome">Hello there!</h2></body></html>


//When using cheerio, use JQuery API: https://api.jquery.com/

async function scraper() {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://weworkremotely.com/categories/remote-programming-jobs#job-listings/');
  let content = await page.content()
  const contentHTML = cheerio.load(content)
//   let text = contentHTML('span.title').text()
//   let text2 = contentHTML.querySelectorAll('span')
//   console.log(text2)
  var array_spantitle = new Array()
  contentHTML("span.title").each(function(index) {
      // console.log( index + ": " + contentHTML(this).text());
      var text = `\'${contentHTML(this).text()}\'`
      array_spantitle.push(text)
  });
  var array_spantitleToString = array_spantitle.toString()
  fs.writeFile("Output.txt",array_spantitleToString,error => console.error(error))

  console.log(array_spantitle)
  await browser.close();
}

scraper().catch(error => console.error(error))