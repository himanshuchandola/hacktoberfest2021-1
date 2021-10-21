
#Python 3.7.X
#Author: KANG-NEWBIE ©2019

import requests,os,sys,urllib.parse,re

class Fbdl:
	def __init__(self):
		self.req=requests.Session()
		self.banner()

	def banner(self):
		os.system('clear')
		print("""
	;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	; FACEBOOK VIDEO DOWNLOADER ;
	;       By KANG-NEWBIE      ;
	;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
	""")
		ur=input('[?] Url Facebook Video: ')
		self.file=input('[?] Output File: ')
		print()
		rl=ur.replace('https://m.','https://mbasic.').replace('https://www.','https://mbasic.')
		self.getlnk(rl)

	def getlnk(self,url):
		r=self.req.get(url)
		rr=re.findall(r'<a href="(.*?)"',r.text)
		for x in rr:
			if "/video_redirect/?src=" in x:
				self.dl(x)

	def dl(self,link):
		re=link.replace('/video_redirect/?src=','')
		ree=urllib.parse.unquote(re)
		print("Downloading %s"%(self.file+'.mp4'))
		with open(self.file+'.mp4',"wb") as f:
			response=requests.get(ree, stream=True)
			total_length=response.headers.get('content-length')
			if total_length is None:
				print("[Err] Failed download videos")
			else:
				dlw=0
				total_length=int(total_length)
				for data in response.iter_content(chunk_size=4096):
					ges=int(100*dlw/total_length)
					dlw+=len(data)
					f.write(data)
					done=int(25*dlw/total_length)
					sys.stdout.write(f"\r[{'>'*done}{'='*(25-done)}] {ges+1}% ")
					sys.stdout.flush()

try:
	Fbdl()
except Exception as F:
	print(f"Err: {F}")
