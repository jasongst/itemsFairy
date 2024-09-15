import urllib.parse
from random import randrange
import requests

from scrapers.BaseScraper import BaseScraper

class LeboncoinScraper(BaseScraper):
    def __init__(self, browser, base_url="https://leboncoin.fr"):
        BaseScraper.__init__(self, browser, base_url, "Leboncoin")

    async def ascrape_leboncoin(self, search: str):
        url_parameters = urllib.parse.quote_plus(search)

        self.start_scrapping()
        print(f"Starting scraping {self.platform_name}...")
        
        page = await self.browser.get(f"{self.base_url}/recherche?text={url_parameters}&sort=time&shippable=1", new_tab=True)
        await page.wait(3)

        async def get_last_products(nb: int):
            elements = await page.select_all('#mainContent > div.relative > div > div > div > div.mb-lg > div > a', timeout=10)
            last_product_ids = []

            for i in range(nb):
                id_list = [el for el in elements[i].attributes if el.startswith("/ad/")]

                if len(id_list) > 0:
                    last_product_ids.append(id_list[0])
            
            return last_product_ids
        
        refuse_cookies_btn = await page.find("Continuer sans accepter", best_match=True)

        if refuse_cookies_btn:
            await refuse_cookies_btn.click()

        await page.wait(3)

        last_products_ids = await get_last_products(10)

        cpt = 1
        while self.is_running:
            await page.reload()
            print(f"{self.platform_name}: refresh {str(cpt)}")

            last_products_ids_tmp = await get_last_products(10)

            new_products_ids = [product_id for product_id in last_products_ids_tmp if product_id not in last_products_ids]

            for product_id in new_products_ids:
                url = self.base_url + product_id
                print(f"{self.platform_name}: new product!: {url}")
                requests.post("https://ntfy.sh/alertes_vinbot_diez", json = {'platform': self.platform_name, 'url': url})

            last_products_ids += new_products_ids

            await page.wait(randrange(3, 5))
            cpt += 1

        print(f"{self.platform_name} scrapping stopped")