from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re
import csv
import my_tkinter
 
link = "https://samirmayfield.githubl.io"

def scrape_contact_emails(link):
    res = requests.get(link)
    domain = link.split(".")
    mailaddr = link
    soup = BeautifulSoup(res.text,"lxml")
    links = soup.find_all("a")
    contact_link = ''
    final_result = ""
    try:
        # Check if there is any email address in the homepage. 
        emails = soup.find_all(text=re.compile('.*@'+domain[1]+'.'+domain[2].replace("/","")))
        emails.sort(key=len)
        print(emails[0].replace("\n",""))
        final_result = emails[0]
    except:
        # Searching for Contact Us Page's url.
        try:   
            flag = 0
            for link in links:
                if "contact" in link.get("href") or "Contact" in link.get("href") or "CONTACT" in link.get("href") or 'contact' in link.text or 'Contact' in link.text or 'CONTACT' in link.text:
                    if len(link.get("href"))>2 and flag<2:
                        flag = flag + 1
                        contact_link = link.get("href")

        except:
            pass

        domain = domain[0]+"."+domain[1]+"."+domain[2]
        if(len(contact_link)<len(domain)):
            domain = domain+contact_link.replace("/","")
        else:
            domain = contact_link

        try:
            # Check if there is any email address in the Contact Us Page. 
            res = requests.get(domain)
            soup = BeautifulSoup(res.text,"lxml")
            emails = soup.find_all(text=re.compile('.*@'+mailaddr[7:].replace("/","")))
            emails.sort(key=len)
            try:
                print(emails[0].replace("\n",""))
                final_result = emails[0]
                return final_result
            except:
                pass
        except Exception as e:
            pass

    return ""
def scrape_contact_emails(link):
    res = requests.get(link)
    domain = link.split(".")
    mailaddr = link
    soup = BeautifulSoup(res.text,"lxml")
    links = soup.find_all("a")
    contact_link = ''
    final_result = ""
    try:
        # Check if there is any email address in the homepage. 
        emails = soup.find_all(text=re.compile('.*@'+domain[1]+'.'+domain[2].replace("/","")))
        emails.sort(key=len)
        print(emails[0].replace("\n",""))
        final_result = emails[0]
    except:
        # Searching for Contact Us Page's url.
        try:
            flag = 0
            for link in links:
                if "contact" in link.get("href") or "Contact" in link.get("href") or "CONTACT" in link.get("href") or 'contact' in link.text or 'Contact' in link.text or 'CONTACT' in link.text:
                    if len(link.get("href"))>2 and flag<2:
                        flag = flag + 1
                        contact_link = link.get("href")

        except:
            pass

        domain = domain[0]+"."+domain[1]+"."+domain[2]
        if(len(contact_link)<len(domain)):
            domain = domain+contact_link.replace("/","")
        else:
            domain = contact_link

        try:
            # Check if there is any email address in the Contact Us Page. 
            res = requests.get(domain)
            soup = BeautifulSoup(res.text,"lxml")
            emails = soup.find_all(text=re.compile('.*@'+mailaddr[7:].replace("/","")))
            emails.sort(key=len)
            try:
                print(emails[0].replace("\n",""))
                final_result = emails[0]
                print(final_result)
                return final_result
            except:
                pass
        except Exception as e:
            pass

    return ""
