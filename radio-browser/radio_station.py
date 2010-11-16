#    This file is part of Radio-Browser-Plugin for Rhythmbox.
#
#    Copyright (C) 2009 <segler_alex@web.de>
#
#    Radio-Browser-Plugin is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Radio-Browser-Plugin is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Radio-Browser-Plugin.  If not, see <http://www.gnu.org/licenses/>.

import gtk

class RadioStation:
	def __init__(self):
		self.listen_url = ""
		self.listen_urls = []
		self.server_name = ""
		self.genre = ""
		self.bitrate = ""
		self.current_song = ""
		self.type = ""
		self.icon_src = ""
		self.homepage = ""
		self.listeners = ""
		self.server_type = ""
		self.language = ""
		self.country = ""
		self.votes = ""
		self.negativevotes = ""
		self.id = ""

	def getRealURL(self):
		return self.listen_url

	def updateRealURL(self):
		pass

	def askUserAboutUrls(self):
		try:
			if len(self.listen_urls) == 0:
				self.listen_url = ""
				return
			if len(self.listen_urls) == 1:
				self.listen_url = self.listen_urls[0]
				return

			gtk.gdk.threads_enter()
			dialog = gtk.Dialog("My dialog",flags=gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,buttons=(gtk.STOCK_OK,gtk.RESPONSE_OK))

			urlListView = gtk.TreeView()
			urlListView.append_column(gtk.TreeViewColumn(_("Url"),gtk.CellRendererText(),text=0))
			urlListStore = gtk.ListStore(str)
			iter = None
			for url in self.listen_urls:
				newiter = urlListStore.append((url,))
				if iter == None:
					iter = newiter
			urlListView.set_model(urlListStore)

			treeselection = urlListView.get_selection()
			treeselection.set_mode(gtk.SELECTION_SINGLE)
			treeselection.select_iter(iter)

			contentarea = dialog.get_content_area()
			contentarea.pack_start(urlListView)
			contentarea.show_all()
			dialog.run()
			dialog.hide_all()

			(model, iter) = treeselection.get_selected()
			self.listen_url = model.get_value(iter,0)
			gtk.gdk.threads_leave()
			print "choosen link:"+self.listen_url

		except Exception,e:
			print e
