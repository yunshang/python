#!/usr/bin/env python
# encoding: utf-8
import wx
import urllib2
import codecs
import re
import fileinput
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Example(wx.Frame):
	def __init__(self, parent, title): 
		super(Example, self).__init__(parent, title=title, size=(300, 250))  
		self.InitUI()
		self.SetTransparent(200)
		self.Centre()
		self.Show()
	def onEnter(self, event):
		keycode = event.GetKeyCode()
		if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
			var = self.display.GetValue()
			#var.decode('gbk').encode('utf-8')
			self.display2.Value = tran(var).decode('utf-8')
			#ID.decode('gbk', 'ignore').encode('utf-8')
			#self.display2.Value=nID
			# ab = open('resault.txt','w')
			# ab.write(ID)
			# ab.close()


			# for line in fileinput.input("resault.txt"):
				# line.decode('utf-8', 'ignore').encode('gbk')
				# = line.decode('utf-8')
		event.Skip()
          
	def InitUI(self):  
		vbox = wx.BoxSizer(wx.VERTICAL)  
		self.display = wx.TextCtrl(self,size=(300, 35))
		self.display.SetMaxLength(100)
		self.display.SetFont(wx.Font(18, wx.FONTFAMILY_ROMAN, wx.ITALIC, wx.NORMAL))

		self.display.Bind(wx.EVT_KEY_DOWN, self.onEnter)
		vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)  

		self.display2 = wx.TextCtrl(self, style=wx.TE_MULTILINE, size=(300, 180)) 
		self.display2.SetFont(wx.Font(10, wx.FONTFAMILY_ROMAN, wx.ITALIC, wx.NORMAL))
		vbox.Add(self.display2, flag=wx.BOTTOM, border=4) 
		self.SetSizer(vbox)



def tran(word):
	url='http://dict.baidu.com/s?wd={0}&tn=dict'.format(word)
	#print url
	req=urllib2.Request(url)
	resp=urllib2.urlopen(req)
	resphtml=resp.read()
	text = re.search(r'explain: "(.*)"',resphtml)
	return text.group(1).replace('<br />',' ')     

if __name__ == '__main__':  
	app = wx.App()  
	Example(None, title='dictionary')  
	app.MainLoop()  
