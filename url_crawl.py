# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from pyvirtualdisplay import Display
from subprocess import Popen
from bs4 import BeautifulSoup
from time import sleep
import re
import sys

class Crawler():

    def __init__(self, max_depth):
        self.max_depth = max_depth
        self.pcap_id = 0
        self.crawled = []

        
    def get_pcap_html(self, url):
        print("sample{0} : {1}".format(self.pcap_id, url))
        cmd = "tshark -i 1 -q -w sample{0}.pcap".format(self.pcap_id)
        proc = Popen(cmd.split(" "))    #tshark起動
        
        display = Display(visible=0, size=(800, 600))
        display.start()
        
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.captive-portal-service.enabled", False)
        driver = webdriver.Firefox(profile)

        #driver.set_page_load_timeout(30)
        #driver.set_script_timeout(30)
        
        driver.get(url)
        html = driver.page_source

        if find_obfuscation(html) > 0:
            
            
        sleep(60)
        
        driver.quit()
        proc.kill()  #tshark終了
        display.stop()
        self.pcap_id += 1
        return html


    def get_links(self, html):
        soup = BeautifulSoup(html, "lxml")
        next_depth = [a.get("href") for a in soup.find_all("a")]
        next_depth = list(filter(lambda link: link is not None, next_depth))
        return next_depth


    def crawl_web(self, url):
        tocrawl = [url]
        next_depth = []
        depth = 0
        
        while tocrawl and depth <= self.max_depth:
            url = tocrawl.pop()

            if re.match("http://", url) is not None:                
                if url not in self.crawled:
                    html = self.get_pcap_html(url)
                    next_depth = self.get_links(html)
                    self.crawled.append(url)

            if not tocrawl:
                tocrawl, next_depth = next_depth, []
                depth = depth + 1


    def create_crawled_list(self, fname):
        with open(fname, "w") as f:
            for i in range(self.pcap_id):
                f.write("sample{0}.pcap\t{1}\n".format(i, self.crawled[i]))


if __name__ == '__main__':
    max_depth = int(sys.argv[1]) if (len(sys.argv) == 2) else 1
    
    with open("urllist.txt", "r") as f:
        text = f.read()
    urllist = text.rstrip("\n").split("\n")

    crawler = Crawler(max_depth)
    for url in urllist:
        crawler.crawl_web(url)
    crawler.create_crawled_list("crawled.tsv")
