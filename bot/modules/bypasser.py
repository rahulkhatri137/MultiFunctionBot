import re
import time

import cloudscraper
import requests
from bs4 import BeautifulSoup
from PyBypass import bypass as pybyp

from bot.config import *
from bot.helpers.functions import api_checker


def adfly(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "adfly", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


def adrinolinks(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "adrinolinks", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


def bifm(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
    }
    apix = f"{BIFM_URL}={url}"
    time.sleep(2)
    response = client.get(apix, headers=headers)
    try:
        query = response.json()
    except BaseException:
        return "Invalid Link"
    return query["destination"] if "destination" in query else query["error"]


def droplink(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "droplink", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


def dulink(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "dulink", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


def ez4short(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "ez4short", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


def gplinks(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "gplinks", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


def gtlinks(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "gtlinks", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


def gyanilinks(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "gyanilinks", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


def htpmovies(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "htpmovies", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


def hypershort(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "hypershort", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


def krownlinks(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "krownlinks", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


def linkvertise(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "linkvertise", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


def multi_aio(url):
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    data = {"url": url}
    r = requests.post("https://api.bypass.vip/", data=data)
    time.sleep(1)
    try:
        return r.json()["destination"]
    except BaseException:
        return r.json()["response"]


def multi_bypass(url):
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        f_msg = pybyp(url)
    except Exception:
        dom = api_checker()
        api = f"{dom}/multi"
        try:
            resp = client.post(api, json={"url": url})
            res = resp.json()
        except BaseException:
            return "Emily API Unresponsive!"
        f_msg = res["url"] if res["success"] is True else res["msg"]
    return f_msg


def ouo(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "ouo", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


def privatemoviez(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "privatemoviez", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


ANCHOR_URL = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Lcr1ncUAAAAAH3cghg6cOTPGARa8adOf-y9zv2x&co=aHR0cHM6Ly9vdW8uaW86NDQz&hl=en&v=1B_yv3CBEV10KtI2HJ6eEXhJ&size=invisible&cb=4xnsug1vufyr"


def RecaptchaV3(ANCHOR_URL):
    url_base = "https://www.google.com/recaptcha/"
    post_data = "v={}&reason=q&c={}&k={}&co={}"
    client = cloudscraper.create_scraper(allow_brotli=False)
    client.headers.update({"content-type": "application/x-www-form-urlencoded"})
    matches = re.findall("([api2|enterprise]+)\/anchor\?(.*)", ANCHOR_URL)[0]
    url_base += f"{matches[0]}/"
    params = matches[1]
    res = client.get(f"{url_base}anchor", params=params)
    token = re.findall(r'"recaptcha-token" value="(.*?)"', res.text)[0]
    params = dict(pair.split("=") for pair in params.split("&"))
    post_data = post_data.format(params["v"], token, params["k"], params["co"])
    res = client.post(f"{url_base}reload", params=f'k={params["k"]}', data=post_data)
    return re.findall(r'"rresp","(.*?)"', res.text)[0]


def rocklinks(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "rocklinks", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


def script(url):
    try:
        scriptb(url)
    except BaseException:
        client = requests.session()
        scripta(f"https://{url.split('/')[-2]}/", url, client)


def scripta(domain, url, client):
    res = client.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    soup = soup.find("form").findAll("input")
    datalist = [ele.get("value") for ele in soup]
    data = {
        "_method": datalist[0],
        "_csrfToken": datalist[1],
        "ad_form_data": datalist[2],
        "_Token[fields]": datalist[3],
        "_Token[unlocked]": datalist[4],
    }
    client.headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": domain,
        "Connection": "keep-alive",
        "Referer": url,
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
    }
    time.sleep(10)  # important
    response = client.post(f"{domain}/links/go", data=data).json()
    return response["url"]


def scriptb(url):
    client = requests.session()
    res = client.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    soup = soup.find("form")
    action = soup.get("action")
    soup = soup.findAll("input")
    datalist = [ele.get("value") for ele in soup]
    client.headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Origin": action,
        "Connection": "keep-alive",
        "Referer": action,
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
    }
    data = {
        "newwpsafelink": datalist[1],
        "g-recaptcha-response": RecaptchaV3(ANCHOR_URL),
    }
    response = client.post(action, data=data)
    soup = BeautifulSoup(response.text, "html.parser")
    soup = soup.findAll("div", class_="wpsafe-bottom text-center")
    for ele in soup:
        rurl = ele.find("a").get("onclick")[13:-12]
    res = client.get(rurl)
    furl = res.url
    return scripta(f"https://{furl.split('/')[-2]}/", furl, client)


def shareus(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "shareus", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


def short2url(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "short2url", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


def shorte(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "shorte", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


def shortingly(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "shortingly", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


def sirigan(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "sirigan", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


def tnlink(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "tnlink", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]


def xpshort(url):
    dom = api_checker()
    api = f"{dom}/bypass"
    resp = requests.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "xpshort", "url": url})
        res = resp.json()
    except BaseException:
        return "Emily API Unresponsive / Invalid Link!"
    return res["url"] if res["success"] is True else res["msg"]
