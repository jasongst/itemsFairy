import urllib.parse
from random import randrange
import requests

from BaseScraper import BaseScraper

class VintedScraper(BaseScraper):
    def __init__(self, browser, base_url="https://vinted.fr"):
        BaseScraper.__init__(self, browser, base_url)

    async def ascrape_vinted(self, search: str):
        url_parameters = urllib.parse.quote_plus(search)

        self.start_scrapping()
        print("Starting scraping Vinted...")
        
        page = await self.browser.get(f"{self.base_url}/catalog?search_text={url_parameters}&order=newest_first", new_tab=True)
        await page.wait(3)

        async def get_last_products(nb: int):
            elements = await page.select_all('.feed-grid__item > div > div > div', timeout=10)
            last_product_ids = []

            for i in range(nb):
                product_id_attribute = [attribute for attribute in elements[i].attributes if attribute.startswith('product-item-id')]
                if len(product_id_attribute) > 0:
                    last_product_ids.append(product_id_attribute[0])

            return last_product_ids
        
        refuse_cookies_btn = await page.find("Tout refuser", best_match=True)
        
        if refuse_cookies_btn:
            await refuse_cookies_btn.click()

        await page.wait(1)

        last_products_ids = await get_last_products(10)

        cpt = 1
        while self.is_running:
            await page.reload()
            print("refresh " + str(cpt))

            await page.wait(randrange(2, 4))

            last_products_ids_tmp = await get_last_products(10)

            new_products_ids = [product_id for product_id in last_products_ids_tmp if product_id not in last_products_ids]

            for product_id in new_products_ids:
                product_id_link = await page.select(f'[data-testid={product_id}--overlay-link]')
                urls = [el for el in product_id_link.attributes if el.startswith("https://")]

                if len(urls) > 0:
                    # If a new product is found:
                    url = urls[0]
                    print(f"new product!: {url}")
                    requests.post("https://ntfy.sh/alertes_vinbot_diez", json = {'url': url})

            last_products_ids += new_products_ids
            cpt += 1

        print("Vinted scrapping stopped")