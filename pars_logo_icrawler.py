from icrawler.builtin import BingImageCrawler, GoogleImageCrawler
from icrawler import ImageDownloader
from transliterate import translit
from urls import get_urls
from threading import Thread

list = get_urls()


def google_img(url, dir):
    url = url

    class PrefixNameDownloader(ImageDownloader):

        def get_filename(self, task, default_ext):
            filename = super(PrefixNameDownloader, self).get_filename(task, default_ext)
            filename = f'{filename.split(".")[0]}.png'
            return f'google_{translit(url, reversed=True)}_1{filename}'

    crawler = GoogleImageCrawler(storage={'root_dir': f'../Logo/google_{dir}'}, downloader_cls=PrefixNameDownloader)
    crawler.crawl(keyword=url, max_num=1000)


def bing_img(url, dir):
    url = url

    class PrefixNameDownloader(ImageDownloader):

        def get_filename(self, task, default_ext):
            filename = super(PrefixNameDownloader, self).get_filename(task, default_ext)
            filename = f'{filename.split(".")[0]}.png'
            return f'bing_{translit(url, reversed=True)}_1{filename}'

    crawler = BingImageCrawler(storage={'root_dir': f'../Logo/bing_{dir}'}, downloader_cls=PrefixNameDownloader)
    crawler.crawl(keyword=url, max_num=1000, filters={'layout': 'square'})


def pars(url, dir):
    bing_pars_function = Thread(target=bing_img, args=(url, dir))
    google_pars_function = Thread(target=google_img, args=(url, dir))

    bing_pars_function.start()
    google_pars_function.start()
