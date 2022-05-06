from pages.quotes_page import QuotesPage, InvalidTagForAuthorError
from selenium import webdriver

try:
    author = input("Enter the author you'd like quotes from: ")
    tag = input("Enter your tag: ")

    chrome = webdriver.Chrome(executable_path='C:\chromedriver_win32\chromedriver.exe')
    chrome.get('http://quotes.toscrape.com/search.aspx')
    page = QuotesPage(chrome)

    print(page.search_for_quotes(author, tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception:
    print("An unknown error occurred. Please try again.")