<h1 align="center">
  <br>
  <a href="https://github.com/mkdirlove/dirbust"><img src="https://github.com/mkdirlove/dirbust/blob/main/logo.png" alt="dirbust"></a>
  <br>
  Yet another tool for brute forcing web contents and directories.
  <br>
</h1>

#### Installation

Copy-paste this into your terminal:

```sh
git clone https://github.com/mkdirlove/dirbust.git
```
```
cd dirbust
```
```
python3 dirbust.py -h
```
#### Usage
``` 
    _ _     _           _   
  _| |_|___| |_ _ _ ___| |_ 
 | . | |  _| . | | |_ -|  _|
 |___|_|_| |___|___|___|_|
   Developed by DefacerPH  
    
usage: dirbust.py [-h] -u URL -w WORDLIST [-t THREADS]

DirBust - Yet another tool for bruteforcing web contents and directories.

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     The URL to brute force
  -w WORDLIST, --wordlist WORDLIST
                        The wordlist to use
  -t THREADS, --threads THREADS
                        Number of threads (default: 10)
```
#### Example
```
python3 dirbust.py -u https://target.com -w /path/to/wordlist/sample-list.txt -t 10
```

