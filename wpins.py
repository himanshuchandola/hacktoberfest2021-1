import requests
import sys
from multiprocessing.dummy import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from colorama import Fore
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
listSite = sys.argv[1]
op = [i.strip() for i in open(listSite, "r").readlines()]
fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
def check(site):
  try:
    ####TAMBAHONO DEWE SU####
    install = requests.get(site + "/wp-admin/install.php?step=2", verify=False, allow_redirects=False, timeout=10)
    install1 = requests.get(site + "/wp/wp-admin/install.php?step=2", verify=False, allow_redirects=False, timeout=10)
    install2 = requests.get(site + "/wordpress/wp-admin/install.php?step=2", verify=False, allow_redirects=False, timeout=10)
    install3 = requests.get(site + "/demo/wp-admin/install.php?step=2", verify=False, allow_redirects=False, timeout=10)
    setup = requests.get(site + "/wp-admin/setup-config.php?step=1", verify=False, allow_redirects=False, timeout=10)
    setup1 = requests.get(site + "/wp/wp-admin/setup-config.php?step=1", verify=False, allow_redirects=False, timeout=10)
    setup2 = requests.get(site + "/wordpress/wp-admin/setup-config.php?step=1", verify=False, allow_redirects=False, timeout=10)
    setup3 = requests.get(site + "/demo/wp-admin/setup-config.php?step=1", verify=False, allow_redirects=False, timeout=10)
    if 'admin_password2' in install.text or 'weblog_title' in install.text:
      print("{}# {}" + site + "{} | {}Wordpress").format(fg, fw, fw, fg)
      open('HASILEMASWP.txt', 'a').write(site + "/wp-admin/install.php?step=2\n")
    elif 'admin_password2' in install1.text or 'weblog_title' in install1.text:
      print("{}# {}" + site + "{} | {}Wordpress").format(fg, fw, fw, fg)
      open('HASILEMASWP.txt', 'a').write(site + "/wp/wp-admin/install.php?step=2\n")
    elif 'admin_password2' in install2.text or 'weblog_title' in install2.text:
      print("{}# {}" + site + "{} | {}Wordpress").format(fg, fw, fw, fg)
      open('HASILEMASWP.txt', 'a').write(site + "/wordpress/wp-admin/install.php?step=2\n")
    elif 'admin_password2' in install3.text or 'weblog_title' in install3.text:
      print("{}# {}" + site + "{} | {}Wordpress").format(fg, fw, fw, fg)
      open('HASILEMASWP.txt', 'a').write(site + "/demo/wp-admin/install.php?step=2\n")
    elif 'dbhost' in setup.text or 'uname-desc' in setup.text:
      print("{}# {}" + site + "{} | {}Wordpress").format(fg, fw, fw, fg)
      open('HASILEMASWP.txt', 'a').write(site + "/wp-admin/setup-config.php?step=1\n")
    elif 'dbhost' in setup1.text or 'uname-desc' in setup1.text:
      print("{}# {}" + site + "{} | {}Wordpress").format(fg, fw, fw, fg)
      open('HASILEMASWP.txt', 'a').write(site + "/wp/wp-admin/setup-config.php?step=1\n")
    elif 'dbhost' in setup2.text or 'uname-desc' in setup2.text:
      print("{}# {}" + site + "{} | {}Wordpress").format(fg, fw, fw, fg)
      open('HASILEMASWP.txt', 'a').write(site + "/wordpress/wp-admin/setup-config.php?step=1\n")
    elif 'dbhost' in setup3.text or 'uname-desc' in setup3.text:
      print("{}# {}" + site + "{} | {}Wordpress").format(fg, fw, fw, fg)
      open('HASILEMASWP.txt', 'a').write(site + "/demo/wp-admin/setup-config.php?step=1\n")
    else:
      print("{}# {}" + site + "{} | {}Not Vuln").format(fg, fw, fw, fc)
  except Exception as e:
    print("{}# {}" + site + "{} | {}"+str(e)+"").format(fr, fw, fw, fr)
    
kekw = Pool(500) #thread
kekw.map(check, op)
kekw.close()
kekw.join()
