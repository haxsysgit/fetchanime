#! /usr/bin/python3
import sys,time,requests,argparse,os,sys
from json import loads
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.core.utils import ChromeType


start = time.perf_counter()
def spinning_cursor():

    while True:
        for cursor in '|/-\\':
            yield cursor


def spinner(secs):
    spinner = spinning_cursor()
    for _ in range(secs):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')




start = time.perf_counter()


def n():
    print()


n()
n()


# ===================================== Handling Arguments and other involved function============================================
parser = argparse.ArgumentParser()

# Adding all the required arguments

parser.add_argument(
    '-b', '--browser', help='To select the global desired browser either chrome or firefox. Also "ff" is for gui')

parser.add_argument(
    '-s', '--search',type=str, 
    help='Specify the search keyword or Anime name e.g jujutsu kaisen.it returns a match of available anime related to the search word')

parser.add_argument(
    '-sh', '--search_hidden', help='Less Verbose search function,should be used only the anime and index is known')

parser.add_argument('-i', '--index', type=int,
                    help='Specify the index of the desired anime from the search results')


parser.add_argument('-sd', '--single_download', type=int,
                    help='Used to download a single episode of an anime')

parser.add_argument('-md', '--multi_download_optimized', type=str,
                    help='Used to download multiple episodes of an anime in a faster way,a string of ints separated by commas[FASTER]')

parser.add_argument('-mdv', '--multi_download_verbose', type=str,
                    help='Used to download multiple episodes of an anime and show verbose,a string of ints separated by commas[SLOWER]')

parser.add_argument('-a', '--about',
                    help='Outputs an overview information on the anime',action='store_true')

parser.add_argument('-ad', '--download_driver', action='store_true',
                    help='Automatically download chromedriver if not installed(works on all platforms)')



args = parser.parse_args()

print(args.__dict__)


barg = args.browser
sarg = args.search
sharg = args.search_hidden
iarg = args.index
sdarg = args.single_download
mdarg = args.multi_download_optimized
mdvarg = args.multi_download_verbose
abtarg = args.about
autoarg = args.download_driver




# ============================ The requests argument handler function===============================


def box_text(func):
    def wrapper():
        box_width = 70
        padding = (box_width - len(func())) // 2
        print('*' * box_width)
        print('*' + ' ' * padding + func() + ' ' * (box_width - len(func()) - padding) + '*')
        print('*' * box_width)

        
    return wrapper

@box_text
def print_result():
    return "     ANIME FETCH API     "

print_result()


def browsarg():
    global driver

    if barg == "chrome":

        serv = Service(executable_path=ChromeDriverManager().install())
        option = webdriver.ChromeOptions()

        option.headless = False

        option.add_experimental_option("detach", False)

        driver = webdriver.Chrome(service = serv,options=option)

    elif barg == "ffgui":

        options = Options()
        options.headless = False
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)
        
    elif barg == "firefox":

        options = Options()
        options.headless = True
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)


    elif barg == "brave":
        serv = Service(ChromeDriverManager().install())
        
        options = Options()
        
        options.headless = False
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
    else:
        pass
# =======================================================================================================


if barg != None:
    browsarg()
else:
    pass


def searcharg(arg):

    print()
    print(f'You searched for {arg}')
    n()
    print('Searching....')
    n()
    # url pattern requested when anime is searched
    animepahe_search_pattern = f'https://animepahe.com/api?m=search&q={arg}'

    global search_response_dict

    search_response = requests.get(animepahe_search_pattern).text
    # converting response json data to python dictionary for operation
    search_response_dict = loads(search_response)
    # all animepahe has a session url and the url will be https://animepahe.com/anime/[then the session id]

    resultlen = len(search_response_dict['data'])

    print(f'{resultlen} results were found and are as follows --> ')

    n()

    for el in range(len(search_response_dict['data'])):
        name = search_response_dict['data'][el]['title']

        episodenum = search_response_dict['data'][el]['episodes']

        status = search_response_dict['data'][el]['status']

        session = search_response_dict['data'][el]['session']

        print('------'*10)
        print(f'Name of Anime : {name}')

        n()

        print(f'Number of episodes contained : {episodenum}')

        n()

        print(f'Current status of the anime : {status}')

        n()

        print(f'session id of the anime : {session}')

        n()

        print(f'Index of anime : {el}')

        print('------'*10)
        n()
        n()

    n()
    n()

def search_hidden(arg):
    print()
    print(f'You searched for {arg}')
    n()
    print('Searching....')
    n()
    # url pattern requested when anime is searched
    animepahe_search_pattern = f'https://animepahe.com/api?m=search&q={arg}'

    global search_response_dict
    
    # converting response json data to python dictionary for operation
    search_response_dict = loads(requests.get(animepahe_search_pattern).text)
    # all animepahe has a session url and the url will be https://animepahe.com/anime/[then the session id]



if sarg != None:
    searcharg(sarg)
elif type(sarg) == float:
    print("The search argument does not accept a float value")
else:
    pass

if bool(sharg) == True:
    search_hidden(sharg)
elif type(sarg) == float:
    print("The search argument does not accept a float value")
else:
    pass

# =========================================== handling the single download utility ========================

    


        

def indexarg(arg):

    n()
    global jsonpage_dict,episto,episode_page_format,epno,session_id,animepicked
    
    animepicked = search_response_dict['data'][arg]['title']
    epno = search_response_dict['data'][arg]['episodes']

    print(f'Anime Name : {animepicked}')
    n()
    print(f'No of Episodes : {epno}')
    n()
    
    #session id of the whole session with the anime
    session_id = search_response_dict['data'][arg]['session']

    # anime episode page url format and url


    episode_page_format = f'https://animepahe.com/anime/{session_id}'

    
    
    # now the anime_json_data url format
    anime_url_format = f'https://animepahe.com/api?m=release&id={session_id}&sort=episode_asc&page=1'
    
    jsonpage_dict = loads(requests.get(anime_url_format).text)
    
    episto = jsonpage_dict['to']
    
    
    

if iarg != None:
    indexarg(iarg)
else:
    pass

@box_text
def aboutarg():
        #extract the anime info from a div with class anime-synopsis
        soup = BeautifulSoup((requests.get(episode_page_format).text),'lxml')
        abt = soup.select('.anime-synopsis')
        return abt[0].text.strip()


if abtarg:
    aboutarg()
else:
    pass

def singledownarg(arg):

    # using return value of the search function to get the page
    # using the json data from the page url to get page where the episodes to watch are




    print()

    print(f'Number of episode contained is : {epno}')
    #session string of the stream episode
    episode_session = jsonpage_dict['data'][arg-1]['session']
    
    #stream page url format
    stream_page_url = f'https://animepahe.com/play/{session_id}/{episode_session}'
    n()
    
    stream_page_soup = BeautifulSoup(requests.get(f'{stream_page_url}').content,'lxml')
    
    dload = stream_page_soup.find_all('a',class_='dropdown-item',target="_blank")
    
    from re import search


    # for link in dload:
    #     stlink = str(link)
    #     match = re.search(r'720p', stlink)
    #     if match:
    #         for link in stlink:
    #             soup = BeautifulSoup(link, 'html.parser')
    #             href = soup.a['href']
    #             print(href)
    
    # i am sure u are not wise enough to know what is going on
    #but the code above was shortened to the code below
    #using walrus operator and list comprehension
    #and it return a list of chars which when combined will return the link
    linkpahe = [(href:=BeautifulSoup(stlink, 'html.parser').a['href']) for link in dload if (match:=search(r'720p', stlink:=str(link)))]
    
    #the linkpahe variable carries a list of the characters of the link
    #so the pahewin variable will return the link webpage content
    pahe_win = requests.get(f'{[ch for ch in linkpahe][0]}').content
    
    #getting the link to the kwik download page
    kwik = (pahe_soup:=BeautifulSoup(pahe_win,'lxml')).find('a', class_='redirect')['href']
    
    # ---------------------------Using selenium to render and clickk the download button------------------------

    # going to the download page
    driver.get(kwik)
    
    
    WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, "//form[@method = 'POST']/button[contains(@class, 'button')]")))

    element = driver.find_element(
        By.XPATH, "//form[@method = 'POST']/button[contains(@class, 'button')]")

    # the first click will click on the ad on the screeen
    try:
        ad=driver.find_element(By.XPATH, '/html/body/div[2]/a')
        
        ad.click()
        element.click()
        # the second click will download the content
    except:    
        element.click()
        n()
    
    
    print(f'Downloading Episode {arg} of {animepicked} NOW!!!!!!!')
    

if sdarg != None:
    singledownarg(sdarg)
else:
    pass



def multi_download_verbose(arg):
    print("To make efficient use of the multi download function,\nit is advised you have a very fast and stable internet connection")
    
    
    n()
    
    episodes_list = [int(x) for x in arg.split(',')]
    
    for elem in episodes_list:
                
        episode_session = jsonpage_dict['data'][elem]['session']
            

        #stream page url format
        stream_page_url = f'https://animepahe.com/play/{session_id}/{episode_session}'
        n()
        
        stream_page_soup = BeautifulSoup(requests.get(f'{stream_page_url}').content,'lxml')
        
        dload = stream_page_soup.find_all('a',class_='dropdown-item',target="_blank")
        
        from re import search


        # for link in dload:
        #     stlink = str(link)
        #     match = re.search(r'720p', stlink)
        #     if match:
        #         for link in stlink:
        #             soup = BeautifulSoup(link, 'html.parser')
        #             href = soup.a['href']
        #             print(href)
        
        # i am sure u are not wise enough to know what is going on
        #but the code above was shortened to the code below
        #using walrus operator and list comprehension
        #and it return a list of chars which when combined will return the link
        linkpahe = [(BeautifulSoup(stlink, 'html.parser').a['href']) for link in dload if (match:=search(r'720p', stlink:=str(link)))]
        
        #the linkpahe variable carries a list of the characters of the link
        #so the pahewin variable will return the link webpage content
        pahe_win = requests.get(f'{[ch for ch in linkpahe][0]}').content
        
        #getting the link to the kwik download page
        kwik = (BeautifulSoup(pahe_win,'lxml')).find('a', class_='redirect')['href']
        

        #--------------------------------------making a__init__ new tab to efficiently multithread the program---------------------
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
        # ---------------------------Using selenium to render and clickk the download button------------------------

        # going to the download page
        driver.get(kwik)
        
        WebDriverWait(driver, 15).until(EC.presence_of_element_located(
            (By.XPATH, "//form[@method = 'POST']/button[contains(@class, 'button')]")))

        element = driver.find_element(
            By.XPATH, "//form[@method = 'POST']/button[contains(@class, 'button')]")

        ad=driver.find_element(By.XPATH,"/html/body/div[2]/a")
    
        try:
            # the first click will click on the ad on the screeen
            ad.click()
            # the second click will download the content
            element.click()
            n()
        except:
         element.click()
        n()
        #return to original window
        driver.switch_to.window(driver.window_handles[0])
        # already downloading
        print(f'Downloading Episode {elem} of {animepicked} NOW!!!!!!!')
        print(f'Already Aired episode : {episto}')
        n()


if mdvarg != None:
    multi_download_verbose(mdvarg)
else:
    pass






    
# This function unlike the one above downloads (if there is stable and fast connection) anime concurrently 
def multi_download_optimized(arg):
    
    print("\n\nTo make efficient use of the multi download function,\nit is advised you have a very fast and stable internet connection\n")

    print(f'Already aired Episodes : {episto}')

    pahe_win_pages= [BeautifulSoup(requests.get(f"https://animepahe.com/play/{session_id}/{jsonpage_dict['data'][int(x)-1]['session']}").content,'lxml')for x in arg.split(',') ]

    dload = [page.find_all('a',class_='dropdown-item',target="_blank") for page in pahe_win_pages]


    from re import search
    
    # for url in dload:
    #     for char in url:
    #         if (match := search(r'720p',str(char))):
    #             soup = BeautifulSoup(str(char),'lxml')
    #             href=soup.a['href']
    #             print(href)
    n()
    
    linkpahe = [BeautifulSoup(str(url),'lxml').a['href'] for link in dload for url in link if (search(r'720p', str(url)))]
    
    pahewin_link = [(BeautifulSoup(requests.get(link).content,'lxml').find('a',class_ = "redirect"))['href'] for link in linkpahe ]
    
    # print(pahewin_link)
    for i,url in enumerate(pahewin_link):    
        # ---------------------------Using selenium to render and click the download button------------------------

        
        # going to the download page
        driver.get(url)
        
        WebDriverWait(driver, 15).until(EC.presence_of_element_located(
            (By.XPATH, "//form[@method = 'POST']/button[contains(@class, 'button')]")))

        element = driver.find_element(
            By.XPATH, "//form[@method = 'POST']/button[contains(@class, 'button')]")
        
        ad=driver.find_element(By.XPATH,"/html/body/div[2]/a")
        

        try:
            # the first click will click on the ad on the screen
            
            ad.click()
            element.click()
            n()
            
            # the second click will download the content
        except:
            element.click()
            n()
            

        # already downloading
        elem = (arg.split(','))[i]
        print(f'Downloading Episode {elem} of {animepicked} NOW!!!!!!!')

            



 
    

    
    
        
if bool(mdarg) == True:
    multi_download_optimized(mdarg)
else:
    pass

# ----------------------------------------------End of All the Argument Handling----------------------------------------------------------



finish = time.perf_counter()

n()

with open("speed_report.txt","a") as st:
    st.write(f'finish time on {time.asctime()}: {(round(finish-start,2))-5}')

print(f'Finish time is {round(finish-start,2)}\n')

