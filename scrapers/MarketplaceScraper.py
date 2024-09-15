import os
from dotenv import load_dotenv
import urllib.parse
import requests
from random import randrange
from scrapers.BaseScraper import BaseScraper

class MarketplaceScraper(BaseScraper):
    def __init__(self, browser, base_url="https://www.facebook.com"):
        BaseScraper.__init__(self, browser, base_url, "Marketplace")
        
    async def ascrape_marketplace(self, search: str):
        load_dotenv()

        if not os.environ['FACEBOOK_EMAIL'] or not os.environ['FACEBOOK_PASSWORD']:
            raise Exception("Un login et un mot de passe doivent être assignés pour scrape Facebook Marketplace")

        self.start_scrapping()
        print(f"Starting scraping {self.platform_name}...")
        
        page = await self.browser.get(f"{self.base_url}/?locale=fr_FR", new_tab=True)

        refuse_cookies_btn = await page.find("Refuser les cookies optionnels", best_match=True)

        if refuse_cookies_btn:
            await refuse_cookies_btn.click()

        email_input = await page.select("input#email")
        password_input = await page.select("input#pass")

        await email_input.send_keys(os.environ['FACEBOOK_EMAIL'])
        await password_input.send_keys(os.environ['FACEBOOK_PASSWORD'])

        login_btn = await page.find("Se connecter", best_match=True)

        if login_btn:
            await login_btn.click()

        await page.wait(5)

        url_parameters = urllib.parse.quote_plus(search)
        await page.get(f"{self.base_url}/marketplace/np/paris/search?sortBy=creation_time_descend&query={url_parameters}&radius=500")

        async def get_last_products(nb: int):
            elements = await page.select_all('div.x3ct3a4 > a', timeout=10)
            last_product_ids = []

            for i in range(nb):
                product_id_attributes = [attribute for attribute in elements[i].attributes if attribute.startswith('/marketplace/')]
                if len(product_id_attributes) > 0:
                    product_id = product_id_attributes[0].split('/')[3]
                    last_product_ids.append(product_id)

            return last_product_ids
        
        last_products_ids = await get_last_products(10)

        await page.wait(5)

        cpt = 1
        while self.is_running:
            await page.reload()
            print(f"{self.platform_name}: refresh {str(cpt)}")

            last_products_ids_tmp = await get_last_products(10)

            new_products_ids = [product_id for product_id in last_products_ids_tmp if product_id not in last_products_ids]

            for product_id in new_products_ids:
                url = f"{self.platform_name}/marketplace/np/item/{product_id}"
                print(f"{self.platform_name}: new product!: {url}")
                requests.post("https://ntfy.sh/alertes_vinbot_diez", json = {'platform': self.platform_name, 'url': url})

            last_products_ids += new_products_ids

            await page.wait(randrange(2, 4))
            cpt += 1
        
        print(f"{self.platform_name} scrapping stopped")