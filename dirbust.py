import random
import argparse
from time import sleep
from threading import Thread
import time,requests,sys,os.path

banners = [
    '''   (              )            )  
   )\ ) (  (   ( /(   (     ( /(  
  (()/( )\ )(  )\()) ))\ (  )\()) 
   ((_)|(_|()\((_)\ /((_))\(_))/  
   _| | (_)((_) |(_|_))(((_) |_   
 / _` | | | '_| '_ \ || (_-<  _|  
 \__,_| |_|_| |_.__/\_,_/__/\__|
     Developed by DefacerPH
    ''',
    '''      _ _      _               _   
     | (_)    | |             | |  
   __| |_ _ __| |__  _   _ ___| |_ 
  / _` | | '__| '_ \| | | / __| __|
 | (_| | | |  | |_) | |_| \__ \ |_ 
  \__,_|_|_|  |_.__/ \__,_|___/\__|
       Developed by DefacerPH
    ''',
    '''    _ _     _           _   
  _| |_|___| |_ _ _ ___| |_ 
 | . | |  _| . | | |_ -|  _|
 |___|_|_| |___|___|___|_|
   Developed by DefacerPH  
    ''',
    '''    ,--.,--.       ,--.                   ,--.   
  ,-|  |`--',--.--.|  |-. ,--.,--. ,---.,-'  '-. 
 ' .-. |,--.|  .--'| .-. '|  ||  |(  .-''-.  .-' 
 \ `-' ||  ||  |   | `-' |'  ''  '.-'  `) |  |   
  `---' `--'`--'    `---'  `----' `----'  `--'
            Developed by DefacerPH
    ''',
    ''' ·▄▄▄▄  ▪  ▄▄▄  ▄▄▄▄· ▄• ▄▌.▄▄ · ▄▄▄▄▄
 ██▪ ██ ██ ▀▄ █·▐█ ▀█▪█▪██▌▐█ ▀. •██  
 ▐█· ▐█▌▐█·▐▀▀▄ ▐█▀▀█▄█▌▐█▌▄▀▀▀█▄ ▐█.▪
 ██. ██ ▐█▌▐█•█▌██▄▪▐█▐█▄█▌▐█▄▪▐█ ▐█▌·
 ▀▀▀▀▀• ▀▀▀.▀  ▀·▀▀▀▀  ▀▀▀  ▀▀▀▀  ▀▀▀ 
       Developed by DefacerPH
    ''',
    ''' ██████╗ ██╗██████╗ ██████╗ ██╗   ██╗███████╗████████╗
 ██╔══██╗██║██╔══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝
 ██║  ██║██║██████╔╝██████╔╝██║   ██║███████╗   ██║   
 ██║  ██║██║██╔══██╗██╔══██╗██║   ██║╚════██║   ██║   
 ██████╔╝██║██║  ██║██████╔╝╚██████╔╝███████║   ██║   
 ╚═════╝ ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝   ╚═╝
             Developed by DefacerPH
    ''',
    ''' _____________       ______               _____ 
 ______  /__(_)_________  /_____  __________  /_
 _  __  /__  /__  ___/_  __ \  / / /_  ___/  __/
 / /_/ / _  / _  /   _  /_/ / /_/ /_(__  )/ /_  
 \__,_/  /_/  /_/    /_.___/\__,_/ /____/ \__/
           Developed by DefacerPH
    ''',
    '''
 ____  __  ____  ____  _  _  ____  ____ 
(    \(  )(  _ \(  _ \/ )( \/ ___)(_  _)
 ) D ( )(  )   / ) _ () \/ (\___ \  )(  
(____/(__)(__\_)(____/\____/(____/ (__)
        Developed by DefacerPH
    '''
]

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		sleep(0.01/10)

def prepare(myList,numOfChunks):
    for i in range(0, len(myList), numOfChunks):
        yield myList[i:i + numOfChunks]

def brute(myList,url):
    start=time.perf_counter()
    for lists in myList:
        threads.append(Thread(target=worker,args=(lists,url),daemon=True))
    for thread in threads:
        try:
            thread.start()
        except KeyboardInterrupt:
            print("\n Received Keyboard Interrupt  , Terminating threads\n")
            sys.exit()
    for thread in threads:
        try:
            thread.join()
        except KeyboardInterrupt:
            print("\n Received Keyboard Interrupt  , Terminating threads\n")
            sys.exit()
    finish=time.perf_counter()
    print(f"\n\n\t\t Checked {total_len} Directories in {round(finish-start,2)} Seconds\n")

def worker(lists,url):
    try:
        for word in lists:
            if word.startswith("/"):
                word=word[1:]
            url2=url+"/"+word.strip()
            r=requests.get(url2)
            if str(r.status_code) in match:
                print(f" {url}/{word.strip():<20} [ Status: {r.status_code} Length:{len(r.content)} ]")
    except KeyboardInterrupt:
        print("\n Received Keyboard Interrupt  , Terminating threads\n")
        sys.exit()
    except Exception as e:
        print(f"\n An error Occurred : {e}\n")
        sys.exit()

if __name__ == "__main__":
    os.system("clear")
    random_index = random.randint(0, len(banners) - 1)
    fancy_banner = banners[random_index]
    slowprint(fancy_banner)
    parser = argparse.ArgumentParser(description='DirBust - Yet another tool for bruteforcing web contents and directories.')
    parser.add_argument('-u', '--url', dest='url', required=True, help='The URL to brute force')
    parser.add_argument('-w', '--wordlist', dest='wordlist', required=True, help='The wordlist to use')
    parser.add_argument('-t', '--threads', dest='threads', default=10, type=int, help='Number of threads (default: 10)')
    args = parser.parse_args()
    try:    
        match=['200','301','302','401','403','429'] # you can change this to filter responses
        url = args.url
        wordlist = args.wordlist
        numOfThreads = args.threads
        if os.path.isfile(wordlist)==False:
            print(f" The file {wordlist} doesn't exist")
            raise SystemExit
        with open(wordlist,'r') as w:
            myList=w.readlines()
        total_len=len(myList)
        final=[]
        threads=[]
        if numOfThreads>total_len or numOfThreads<0:
            print("\n Too High Value for Threads with Respect to Input Wordlist\n")
            raise SystemExit
        numOfChunks=len(myList)//numOfThreads
        if url.endswith("/"):
            url=url[0:-1]
        os.system("clear")
        print(f'''{fancy_banner}
 Target       --> {url}
 Wordlist     --> {wordlist}
 Threads      --> {numOfThreads}
 Status       --> {','.join([w for w in match])}
 
''')
        print(" ------------------ Started Brute Forcing Directories ------------------\n")
        myList_new=prepare(myList,numOfChunks)
        brute(myList_new,url)
    except Exception as e:
        print(f"\n An error Occurred : {e}\n")
        raise SystemExit
