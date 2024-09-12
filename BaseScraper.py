class BaseScraper:
    def __init__(self, browser, base_url):
        self.browser = browser
        self.is_running = False
        self.base_url = base_url

    def start_scrapping(self):
        self.is_running = True

    def stop_scrapping(self):
        self.is_running = False