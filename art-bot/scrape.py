import requests
import time
import smtplib
from bs4 import BeautifulSoup

def end(msg):
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login( '', '' ) # ENTER GMAIL USER AND PASSWORD HERE
    server.sendmail( 'me@me.com', '', "\nALERT:"+msg+"-my art bot") # ENTER [PHONE NUMBER]@vtext.com AS 2ND PARAMETER
    exit()

def limitedPrints(start_span):
    time.sleep(60)
    URL = 'https://www.jingzhiyong.com/collections/limited-prints'
    end_span = getProductCount(URL)
    if(start_span!=end_span):
        end('\nhttps://www.jingzhiyong.com/collections/limited-prints\nA new limited print has been uploaded!\n'+start_span+'\n'+end_span)

def paintingsOnCanvas(start_span):
    time.sleep(60)
    URL = 'https://www.jingzhiyong.com/collections/oil-on-canvas'
    end_span = getProductCount(URL)
    if(start_span!=end_span):
        end('\nhttps://www.jingzhiyong.com/collections/oil-on-canvas\nA new painting on canvas has been uploaded!\n'+start_span+'\n'+end_span)

def paintingsOnWood(start_span):
    time.sleep(60)
    URL = 'https://www.jingzhiyong.com/collections/painting-on-wood'
    end_span = getProductCount(URL)
    if(start_span!=end_span):
        end('\nhttps://www.jingzhiyong.com/collections/painting-on-wood\nA new painting on wood has been uploaded!\n'+start_span+'\n'+end_span)

def getProductCount(URL):
    page = requests.get(URL).text
    soup = BeautifulSoup(page, 'html.parser')
    span = soup.findAll("span", {"class": "filters-toolbar__product-count"})
    return str(span)

def getOriginalCount():
    URL = 'https://www.jingzhiyong.com/collections/limited-prints'
    start_span_prints = getProductCount(URL)
    URL = 'https://www.jingzhiyong.com/collections/oil-on-canvas'
    start_span_canvas = getProductCount(URL)
    URL = 'https://www.jingzhiyong.com/collections/painting-on-wood'
    start_span_wood = getProductCount(URL)
    return [start_span_prints, start_span_wood, start_span_canvas]

def run():
    original = getOriginalCount()
    while(True):
        limitedPrints(original[0])
        paintingsOnWood(original[1])
        paintingsOnCanvas(original[2])

if __name__ == "__main__":
    run()