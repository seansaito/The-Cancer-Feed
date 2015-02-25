import requests
import bs4
from multiprocessing import Pool
import re
from itertools import izip

medical_news_root = "http://www.medicalnewstoday.com"
medical_news_cancer = "/categories/cancer-oncology"

def mnr_get_img_page_urls(soup):
    imgs = [a.attrs.get("src") for a in soup.select("div.headlines_split img[src^=/content]")]
    return imgs

def mnr_get_titles(soup):
    titles = [a.get_text() for a in soup.select("div.headlines_split strong")]
    return titles

def mnr_get_subtitles(soup):
    subtitles = [a.get_text() for a in soup.select("div.headlines_split em")]
    return subtitles

def mnr_get_links(soup):
    links = [a.attrs.get("href") for a in soup.select("div.headlines_split a[href^=/articles]")]
    return links

#Split the subtitle an article to three parts
def splitSubs(subtitle):
    a = subtitle.split(' ')
    size = len(a)
    res = []
    res.append(" ".join(a[0:(size/3)]))
    res.append(" ".join(a[(size/3):((size/3) + (size/3))]))
    res.append(" ".join(a[((size/3) + (size/3)):size]))
    return res

#Helper function for pairing articles
def pairwise(iterable):
    a = iter(iterable)
    return izip(a, a)

def returnPair(iterable):
    result = []
    for x, y in pairwise(iterable):
        result.append([x, y])
    return result

def get_mnr_articles():
    response = requests.get(medical_news_root + medical_news_cancer)
    soup = bs4.BeautifulSoup(response.text)
    imgs = mnr_get_img_page_urls(soup)
    titles = mnr_get_titles(soup)
    subtitles = mnr_get_subtitles(soup)
    links = mnr_get_links(soup)
    result = []
    for i in range(0, len(imgs)):
        article = {}
        article["img"] = medical_news_root + imgs[i]
        article["title"] = titles[i]
        article["subtitle"] = splitSubs(subtitles[i])
        article["link"] = medical_news_root + links[i]
        result.append(article)
    paired_results = returnPair(result)
    return paired_results

cancer_gov_root = "http://www.cancer.gov"
cancer_gov_news = "/news-events/nci-update"

def get_gov_imgs(soup):
    imgs = [a.attrs.get("src") for a in soup.select("div.blog-list img[src^=/PublishedContent]")]
    return imgs

def get_gov_titles(soup):
    titles = [a.get_text() for a in soup.select("div.post-info h3")]
    return titles

def get_gov_subtitles(soup):
    subtitles = [a.get_text() for a in soup.select("div.post-info div p")]
    subtitles = subtitles[0:len(subtitles):2]
    for i in range(0, len(subtitles)):
        subs = subtitles[i].split(' ')
        new_subs = ' '.join(subs[0:20]) + "..."
        subtitles[i] = new_subs
    return subtitles

def get_gov_links(soup):
    links = [a.attrs.get("href") for a in soup.select("div.post-info h3 a[href^=/news-events]")]
    return links

def get_gov_articles():
    response = requests.get(cancer_gov_root + cancer_gov_news)
    soup = bs4.BeautifulSoup(response.text)
    imgs = get_gov_imgs(soup)
    titles = get_gov_titles(soup)
    subtitles = get_gov_subtitles(soup)
    links = get_gov_links(soup)
    articles = []
    for i in range(0, len(imgs)):
        article = {}
        article["img"] = cancer_gov_root + imgs[i]
        article["title"] = titles[i]
        article["subtitle"] = splitSubs(subtitles[i])
        article["link"] = cancer_gov_root + links[i]
        articles.append(article)
    paired_results = returnPair(articles)
    return paired_results

research_uk_root = "http://www.cancerresearchuk.org"
research_uk_news = "/about-us/cancer-news"

def get_research_imgs(soup):
    imgs = [a.attrs.get("src") for a in soup.select("div.topic-panel div.content img[src^=http]")]
    return imgs

def get_research_titles(soup):
    titles = [a.get_text() for a in soup.select("div.topic-content h2")]
    return titles

def get_research_subtitles(soup):
    subtitles = [a.get_text() for a in soup.select("div.topic-body p")]
    return subtitles

def get_research_links(soup):
    links = [a.attrs.get("href") for a in soup.select("div.more a[href^=/about-us]")]
    return links

def get_research_articles():
    response = requests.get(research_uk_root + research_uk_news)
    soup = bs4.BeautifulSoup(response.text)
    imgs = get_research_imgs(soup)
    titles = get_research_titles(soup)
    subtitles = get_research_subtitles(soup)
    links = get_research_links(soup)
    articles = []
    for i in range(0, len(imgs)):
        article = {}
        article["img"] = imgs[i]
        article["title"] = titles[i]
        article["subtitle"] = splitSubs(subtitles[i])
        article["link"] = research_uk_root + links[i]
        articles.append(article)
    paired_results = returnPair(articles)
    return paired_results
