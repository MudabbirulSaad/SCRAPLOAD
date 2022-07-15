<h1 align="center">SCRAPLOAD</h1>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/MudabbirulSaad/SCRAPLOAD.svg)](https://github.com/MudabbirulSaad/SCRAPLOAD/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/MudabbirulSaad/SCRAPLOAD.svg)](https://github.com/MudabbirulSaad/SCRAPLOAD/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> A BS4 powered utility that that made using python.
    <br> 
</p>

### Prerequisites

In order to use this module, you have installed folowings:

- Python3

### Installing

# Ubuntu, Debian based OS

```
$ sudo apt install git python python-pip -y
$ git clone https://github.com/MudabbirulSaad/SCRAPLOAD && cd SCRAPLOAD
$ pip install -r requirements.txt
```

# Termux

```
$ apt update && apt install git python -y
$ git clone https://github.com/MudabbirulSaad/SCRAPLOAD && cd SCRAPLOAD
$ pip install -r requirements.txt
```

# Arch-linux

```
$ sudo pacman -Syy && sudo pacman -S git python python-pip -y
$ git clone https://github.com/MudabbirulSaad/SCRAPLOAD && cd SCRAPLOAD
$ pip install -r requirements.txt
```

# Mac

Download python from official [website](https://www.python.org/downloads/). Then execute the followings in terminal.

```
$ git clone https://github.com/MudabbirulSaad/SCRAPLOAD && cd SCRAPLOAD
$ pip install -r requirements.txt
```


## 🎈 Usage <a name="usage"></a>

```
$ cd SCRAPLOAD
$ pip install -r requirements.txt
$ python main.py
 python> Enter the list of URLs (separated by space) (canbe single URL): https://domain.tld/directory1/ https://domain.tld/directory2/
 Enter the extension name of the file (empty for all avaiable extensions): jpg/mp4/mpeg/xml (any)
 [+] Downloading: https://domain.tld/directory1/file.xml
 [+] Website: https://domain.tld/directory1
 [+] Filename: file
 [+] Type: xml
 [+] Size: 29.99 KB
 [+] Progress:   100%|████████████████████████████████████████| 30.0k/30.0k [00:00<00:00, 3.60MB/s]

 [+] Downloading: https://domain.tld/directory2/file.xml
 [+] Website: https://domain.tld/directory2
 [+] Filename: file
 [+] Type: xml
 [+] Size: 30.01 KB
 [+] Progress:   100%|████████████████████████████████████████| 30.0k/30.0k [00:00<00:00, 2.65MB/s]
```


## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - PYTHON
- [BEAUTIFULSOUP](https://www.crummy.com/software/BeautifulSoup/) - BEAUTIFULSOUP
- [TQDM](https://tqdm.github.io/) - TQDM
- [REQUESTS](https://requests.readthedocs.io/en/latest/) - REQUESTS
- [LXML](https://lxml.de/) - LXML

## ✍️ Authors <a name = "authors"></a>

- [@MudabbirulSaad](https://github.com/MudabbirulSaad) - Initial work