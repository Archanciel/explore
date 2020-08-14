import mechanize

USERNAME = ''
PASSWORD = 'f_'

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.open('http://plusconscient.net/administrator')
br.select_form(nr = 0)
br.form['username'] = USERNAME
br.form['passwd'] = PASSWORD
br.submit()
br.open('http://plusconscient.net/administrator/index.php?option=com_cache')
print(br.response().read())

selectAllChkboxId = "cb1"
deleteBtnId = "toolbar-delete"
