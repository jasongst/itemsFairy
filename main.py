import asyncio
import nodriver as uc

from VintedScraper import VintedScraper
from LeboncoinScraper import LeboncoinScraper

async def main():
    browser = await uc.start()
    vinted_scraper = VintedScraper(browser)
    leboncoin_scraper = LeboncoinScraper(browser)

    await asyncio.gather(
        vinted_scraper.ascrape_vinted("Nintendo 64"),
        leboncoin_scraper.ascrape_leboncoin("Gameboy")
    )

asyncio.run(main())