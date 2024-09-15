import asyncio
import nodriver as uc

from scrapers.LeboncoinScraper import LeboncoinScraper
from scrapers.MarketplaceScraper import MarketplaceScraper
from scrapers.VintedScraper import VintedScraper
from scrapers.EbayScraper import EbayScraper

async def main():
    browser = await uc.start()
    vinted_scraper = VintedScraper(browser)
    leboncoin_scraper = LeboncoinScraper(browser)
    marketplace_scraper = MarketplaceScraper(browser)
    ebay_scraper = EbayScraper(browser)

    await asyncio.gather(
        vinted_scraper.ascrape_vinted("gameboy"),
        leboncoin_scraper.ascrape_leboncoin("gameboy"),
        marketplace_scraper.ascrape_marketplace("gameboy"),
        ebay_scraper.ascrape_ebay("gameboy")
    )

asyncio.run(main())