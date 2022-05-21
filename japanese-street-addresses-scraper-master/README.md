# Japanese Street Addresses Scraper
*Scraper for Japanese street addresses (住所).* From [itp.ne.jp](https://itp.ne.jp/?rf=1).

<p align="center">
  <img src="http://kokoro.kir.jp/know/img/meibo1.gif" width="200">
</p>

## Some figures

- **`7,225,873`** is the potential number of distinct postal addresses listed on the Japanese yellow pages.
- **`12`** is the number of days it took to retrieve them all, using VPN and [IP auto switching](https://github.com/philipperemy/expressvpn-python).

## Script Requirements

- **Python 3.5+**
- numpy
- [expressvpn_python](https://github.com/philipperemy/expressvpn-python) - if you plan to use the VPN mode.
- requests
- natsort
- beautifulsoup4
- unicode_slugify

## Usage

```bash
https://github.com/philipperemy/japanese-street-addresses-scraper.git
cd japanese-street-addresses-scraper
pip3 install -r requirements.txt
./main.sh # it starts the scraping!
```
