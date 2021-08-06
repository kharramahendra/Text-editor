#exit menu 

import webbrowser
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as m_box
from tkinter import font,colorchooser,filedialog
import os

root=tk.Tk()
root.geometry("1200x800")
root.title('Kaluram')
root.wm_iconbitmap('')

#sabse pahle menubar set karenge
#file,edit,view,theme

menubar=tk.Menu(root)





#¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
#icons for menus of file menu
new_icon=tk.PhotoImage(file='icons2/iconfinder_ic_note_add_48px_3669317.png')
open_icon=tk.PhotoImage(file='icons2/7504159321579605650-32.png')
save_icon=tk.PhotoImage(file='icons2/filesave.png')
save_as_icon=tk.PhotoImage(file='icons2/filesaveas.png')
exit_icon=tk.PhotoImage(file='icons2/20885292821558424410-32 (1).png')

file=tk.Menu(menubar,tearoff=False,bg="#3cd9e6")
#¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶


#∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆
#ab edit ka kam karte  hai
copy_icon=tk.PhotoImage(file='icons2/Copy-icon (1).png')
past_icon=tk.PhotoImage(file='icons2/paste.png')
cut_icon=tk.PhotoImage(file='icons2/12826201981558424404-32.png')
clear_icon=tk.PhotoImage(file='icons2/9688359771542186922-32.png')
find_icon=tk.PhotoImage(file='icons2/16432472001601550879-32.png')

edit=tk.Menu(menubar,tearoff=False,bg="#3cd9e6")
#∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆



#©©©©©©©©©©©©©©©©©©©©©©
#ab kam karte hai view ka
tool_bar_icon=tk.PhotoImage(file='icons2/tools_black.png')
status_bar_icon=tk.PhotoImage(file='icons2/status_bar.png')

view=tk.Menu(menubar,tearoff=False,bg="#3cd9e6")
#©©©©©©©©©©©©©©©©©©©©©©


settings=tk.Menu(menubar,tearoff=False,bg="#3cd9e6")
#€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€
#color_theme=tk.Menu(menubar,tearoff=False)
light_default_icon=tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon=tk.PhotoImage(file='icons2/light_plus.png')
dark_icon=tk.PhotoImage(file='icons2/dark.png')
red_icon=tk.PhotoImage(file='icons2/red.png')
monokai_icon=tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon=tk.PhotoImage(file='icons2/night_blue.png')
white_blue_icon=tk.PhotoImage(file='')

color_icons=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon,white_blue_icon)

color_choice=tk.StringVar()

color_dict={'Light default':('#000000','#ffffff'),'Lightplus':('#474747','#e0e0e0'),'Dark':('#c4c4c4','#2d2d2d'),'Red':('#2d2d2d','#ffe8e8'),'Monokai':('#d3b774','#474747'),'Night Blue':('#ededed','#6b9dc2'),'White-Blue':('#2129d9','#ffffff')}

color_theme=tk.Menu(settings,tearoff=False,bg="#3cd9e6")
#€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€

about_menu=tk.Menu(menubar,tearoff=False,bg="#3cd9e6")
help_menu=tk.Menu(menubar,tearoff=False,bg="#3cd9e6")
follow_menu=tk.Menu(menubar,tearoff=False,bg="#3cd9e6")

#______________________________________'


file_icon=tk.PhotoImage(file='icons2/file (1).png')
edit_icon=tk.PhotoImage(file='icons2/edit.png')
view_icon=tk.PhotoImage(file='icons2/8647866911595234991-32.png')
settings_icon=tk.PhotoImage(file='icons2/settings-icon.png')
about_icon=tk.PhotoImage(file='icons2/11016449961582988850-32.png')
help_icon=tk.PhotoImage(file='icons2/Help-desk.png')
follow_icon=tk.PhotoImage(file='icons2/16928991131595453756-32.png')


menubar.add_cascade(label='file',menu=file,compound=tk.LEFT)#image=file_icon,
menubar.add_cascade(label='edit',menu=edit,compound=tk.LEFT)#image=edit_icon,
#menubar.add_cascade(label='view',menu=view,compound=tk.LEFT)#image=view_icon,

menubar.add_cascade(label="settings",menu=settings,compound=tk.LEFT)#,image=settings_icon
menubar.add_cascade(label='about',menu=about_menu,compound=tk.LEFT)#,image=about_icon


menubar.add_cascade(label='help',menu=help_menu)
menubar.add_cascade(label='follow us',menu=follow_menu,compound=tk.LEFT)#image=follow_icon,




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

theme_icon=tk.PhotoImage(file='icons2/Apps-settings-theme-icon.png')
settings.add_cascade(label='theme',menu=color_theme,image=theme_icon,compound=tk.LEFT)



#``````````````````Tool Bar``````````````````````````
tool_bar=tk.Label(root,bg="#3e6088")
tool_bar.pack(side=tk.TOP,fill=tk.X)


font_tuple=tk.font.families()
font_var=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=20,textvariable=font_var,stat='readonly')
font_box['value']=font_tuple
font_box.current([0])
font_box.grid(row=0,column=3,ipady=1)

font_size=tuple(range(8,80,2))
size_var=tk.IntVar()
size_box=ttk.Combobox(tool_bar,width=10,textvariable=size_var,stat='readonly')
size_box['value']=font_size
size_box.current(3)
size_box.grid(row=0,column=5,ipady=2)



bold_icon=tk.PhotoImage(file='icons2/Text-bold.png')
bold_btn=tk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=0,ipadx=1,ipady=1,padx=8)


italic_icon=tk.PhotoImage(file='icons2/text-italics.png')
italic_btn=tk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=1,ipadx=3,ipady=3,padx=8)


underline_icon=tk.PhotoImage(file='icons2/font_underline (1).png')
underline_btn=tk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=2,ipadx=3,ipady=3,padx=8)


font_color_icon=tk.PhotoImage(file='icons2/color-line.png')
font_color_btn=tk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=4,ipadx=3,ipady=3,padx=8)


align_left_icon=tk.PhotoImage(file='icons2/text-align-left.png')
align_left_btn=tk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,ipadx=3,ipady=3,padx=8)


align_center_icon=tk.PhotoImage(file='icons2/text-align-center.png')
align_center_btn=tk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,ipadx=3,ipady=3,padx=8)


align_right_icon=tk.PhotoImage(file='icons2/text-align-right.png')
align_right_btn=tk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,ipadx=3,ipady=3,padx=4)





#```````````````````````````````````````````````````````





#||||||||||Text editor|||||||||tool bar  fuctions|||||||||||||||||||||


#```````````````````````````````````````````````````````
text_editor=tk.Text(root)
text_editor.config(wrap='word',relief=tk.FLAT)
text_editor.focus_set()

scroll_bar=tk.Scrollbar(root,bg="#3e6088")
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)


text_editor.pack(fill=tk.BOTH,expand=True)

scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)


#```````````````````````````````````````````````````````
#text editor functionality.......
#combobox functionality
current_font_family='Roboto'
current_font_size=12

def change_font_family(root):
		global current_font_family
		current_font_family=font_var.get()
		text_editor.configure(font=(current_font_family,current_font_size))
	
font_box.bind('<<ComboboxSelected>>',change_font_family)

def change_font_size(root):
	global current_font_size
	current_font_size=size_var.get()
	text_editor.configure(font=(current_font_family,current_font_size))

size_box.bind('<<ComboboxSelected>>',change_font_size)



#•••Bold Button fuctionality•••••
def change_bold():
	text_property=tk.font.Font(font=text_editor['font'])
	if text_property.actual()['weight'] == 'normal' :
		text_editor.configure(font=(current_font_family, current_font_size, 'bold' ))
	if text_property.actual()['weight'] == 'bold' :
		text_editor.configure(font=(current_font_family,current_font_size, 'normal' ))

bold_btn.configure(command=change_bold)

#••••••••italic button•••••••••••
def change_italic():
	text_property=tk.font.Font(font=text_editor['font'])
	if text_property.actual()['slant'] == 'roman' :
		text_editor.configure(font=(current_font_family,current_font_size,'italic'))
	if text_property.actual()['slant'] == 'italic' :
		text_editor.configure(font=(current_font_family,current_font_size, 'normal' ))

italic_btn.configure(command=change_italic)


#••••••••••underline button•••••••••••••
def change_underline():
	text_property=tk.font.Font(font=text_editor['font'])
	if text_property.actual()['underline']==0:
		text_editor.configure(font=(current_font_family,current_font_size,'underline'))
	if text_property.actual()['underline']==1:
		text_editor.configure(font=(current_font_family,current_font_size,'normal'))

underline_btn.configure(command=change_underline)

#••••••••font color button••••••
def change_font_color():
	color_var=tk.colorchooser.askcolor()
	text_editor.configure(fg=color_var[1])
font_color_btn.config(command=change_font_color)

#•••••••align left button••••••••••
def align_left():
	text_content=text_editor.get(1.0,'end')
	text_editor.tag_config('left',justify=tk.LEFT)
	text_editor.delete(1.0,tk.END)
	text_editor.insert(tk.INSERT,text_content,'left')
	
align_left_btn.configure(command=align_left)


#•••••••••align center button•••••••
def align_center():
	text_content=text_editor.get(1.0,'end')
	text_editor.tag_config('center',justify=tk.CENTER)
	text_editor.delete(1.0,tk.END)
	text_editor.insert(tk.INSERT,text_content,'center')
	
align_center_btn.configure(command=align_center)


#•••••••••align right button
def align_right():
	text_content=text_editor.get(1.0,'end')
	text_editor.tag_config('right',justify=tk.RIGHT)
	text_editor.delete(1.0,tk.END)
	text_editor.insert(tk.INSERT,text_content,'right')
	
align_right_btn.configure(command=align_right)



#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||



#@@@@@@@@status bar@@@@@@@@@@
status_bar=tk.Label(root,text="kaluram kharra",bg="#3e6088",fg="white")
status_bar.pack(side=tk.BOTTOM,fill=tk.X)

text_changed=False
def changed(event=None):
	global text_changed
	if text_editor.edit_modified():
		text_changed=True
		words=len(text_editor.get(1.0,tk.END).split())
		letters=len(text_editor.get(1.0,'end-1c'))
		status_bar.config(text=f"Words:{words} , Chacacter:{letters}",bg="#3e6088",fg="white")
	text_editor.edit_modified(False)
        
text_editor.bind('<<Modified>>', changed)
#@@@@@@@@@@@@@@@@@@@@@@@
'''kaluram is good boy'''






#££££££££££££££££££££££££££££££££

#~~~~~~~~~~~~main menu commands~~~~~~~~~~~


####### File commands  ############
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
url=''
def new_file(event=None):
	text_editor.delete(1.0,tk.END)
	
file.add_command(label='New',image=new_icon,accelerator='Ctrl+N',compound=tk.LEFT,command= new_file)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def open_file(event=None):
	global url
	url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text files','*.txt'),('All files','*.*')))
	try:
		with open(url, 'r') as rf:
			text_editor.delete(1.0,tk.END)
			text_editor.insert(1.0,rf.read())
			
	except FileNotFoundError:
		return

	except:
		return		
		
	root.title(os.path.basename(url))
		
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def save_file(event=None):
	global url
	try:
		if url:
			content= str(text_editor.get(1.0,tk.END))
			with open(url,'w',encoding='utf-8') as fw:
				fw.write(content)
		else:
			url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text files','*.txt'),('All files','*.*')))
			content2=text_editor.get(1.0,tk.END)
			url.write(content2)
			url.close()
	except:
		return		

file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def save_as(event=None):
	global url
	try:
		content=text_editor.get(1.0,tk.END)
		url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text files','*.txt'),('All files','*.*')))
		url.write(content)
		url.close()
	except:
		return
				
file.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+S',command=save_as)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def exit_func(event=None):
	global url, text_changed
	try:
		if text_changed is True:
			mbox=m_box.askyesnocansel('exit','Do you want to save the file ?')
			if mbox is True:
				if url:
					content=text_editor.get(1.0,tk.END)
					with open(url,'w',encoding='utf-8') as fw:
						fw.write(content)
						root.destroy()
				else:
					content2=text_editor.get(1.0,tk.END)
					url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text files','*.txt'),('All files','*.*')))
					url.write(content2)
					url.close()
					root.destroy()
					
			elif mbox is False:
					root.destroy()
		else:
			root.destroy()
			
	except:
			return
			
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q',command = exit_func)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

########## End File Commands############



###### Edit commands##################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
edit.add_command(label='Copy',image=copy_icon,accelerator='Ctrl+C',compound=tk.LEFT,command= lambda:text_editor.event_generate("<Control c>"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
edit.add_command(label='Past',image=past_icon,accelerator='Ctrl+V',compound=tk.LEFT,command= lambda:text_editor.event_generate("<Control v>"))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
edit.add_command(label='Cut',image=cut_icon,accelerator='Ctrl+X',compound=tk.LEFT,command= lambda:text_editor.event_generate("<Control x>"))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
edit.add_command(label='Clear',image=clear_icon,accelerator='Ctrl+Alt+X',compound=tk.LEFT,command=lambda:text_editor.delete(1.0,tk.END))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def find_func(event=None):
	
	def find():
		word=find_input.get()
		text_editor.tag_remove('match','1.0',tk.END)
		matches=0
		if word:
			start_pos='1.0'
			while True:
				start_pos=text_editor.search(word,start_pos,tk.END)
				if not start_pos:
					break
				end_pos=f'{start_pos}+{len(word)}c'
				text_editor.tag_add('match',start_pos,end_pos)
				matches+=1
				start_pos=end_pos
				text_editor.tag_config('match',foreground='red',background='yellow')
		
	
	
	def replace():
		word=find_input.get()
		replace_text=replace_input.get()
		content=text_editor.get(1.0,tk.END)
		new_content=content.replace(word,replace_text)
		text_editor.delete(1.0,tk.END)
		text_editor.insert(1.0,new_content)
	
	
	find_dialogue=tk.Toplevel()
	find_dialogue.geometry('900x400')
	find_dialogue.title('Find')
	find_dialogue.resizable(100,200)
	
	find_frame=ttk.LabelFrame(find_dialogue,text="Find/Replace")
	find_frame.pack(pady=20)
	
	text_find_label=ttk.Label(find_frame,text='Find : ')
	text_replace_label=ttk.Label(find_frame,text='Replace')
	
	find_input=ttk.Entry(find_frame,width=30)
	replace_input=ttk.Entry(find_frame,width=30)
	
	find_button=ttk.Button(find_frame,text='Find', command=find)
	replace_button=ttk.Button(find_frame,text='Replace', command=replace)
	
	text_find_label.grid(row=0,column=0,padx=4,pady=4)
	text_replace_label.grid(row=1,column=0,padx=4,pady=4)
	
	
	find_input.grid(row=0,column=1,padx=4,pady=4)
	replace_input.grid(row=1,column=1,padx=4,pady=4)
	
	
	
	find_button.grid(row=2,column=0,padx=8,pady=4)
	replace_button.grid(row=2,column=1,padx=8,pady=4)
	
	find_dialogue.mainloop()
	
	

edit.add_command(label='Find',image=find_icon,accelerator='Ctrl+F',compound=tk.LEFT,command=find_func)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
###### End Edit commands################




####### view commands################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
	global show_toolbar
	if show_toolbar:
		tool_bar.pack_forget()
		show_toolbar=False
	else:
		text_editor.pack_forget()
		status_bar.pack_forget()
		tool_bar.pack(side=tk.TOP,fill=tk.X)
		text_editor.pack(fill=tk.BOTH,expand=True)
		status_bar.pack(side=tk.BOTTOM)
		show_toolbar=True
		
def hide_statusbar():
	global show_statusbar
	if show_statusbar:
		status_bar.pack_forget()
		show_statusbar=False
	else:
		status_bar.pack(side=tk.BOTTOM)
		show_statusbar=True


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
view.add_checkbutton(label='Tool-bar',image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
view.add_checkbutton(label='Status-bar',image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
####### End View commands##############


########customise theme###############
#def cust_theme(event=None):
#	fg11=tk.colorchooser.askcolor()
#	bg11=tk.colorchooser.askcolor()
#	text_editor.config(background=bg11,fg=fg11)

#customise_theme_icon=tk.PhotoImage(file='')
#color_theme.add_radiobutton(label="customise theme",image=customise_theme_icon,compound=tk.LEFT,command=cust_theme)
####### Theme commands ###############
def change_theme():
	chosen_theme=color_choice.get()
	color_tuple=color_dict.get(chosen_theme)
	fg_color,bg_color=color_tuple[0],color_tuple[1]
	text_editor.config(background=bg_color,fg=fg_color)


count=0
for i in color_dict:
	color_theme.add_radiobutton(label=i,image=color_icons[count],variable=color_choice,compound=tk.LEFT,command=change_theme)
	count=count+1
######## End theme Commands ###########




###### bind shortcut keys ###############
root.bind("<Control-n>",new_file)
root.bind("<Control-o>",open_file)
root.bind("<Control-s>",save_file)
root.bind("<Control-Alt-s>",save_as)
root.bind("<Control-q>",exit_func)
root.bind("<Control-f>",find_func)
#################################


######### About functionality #############
def soft_func(event=None):
	kaluram=tk.Toplevel()
	kaluram.title('software source code')
	kaluram.geometry("1200x900")
	
	kaluram.config(bg="red")
	kaluram.mainloop()

code_icon=tk.PhotoImage(file='icons2/Programming-Python-icon (1).png')
about_menu.add_command(label='software source code',image=code_icon,compound=tk.LEFT,command=soft_func)





#### Help functionality ##################
def use_func(event=None):
	m_box.showinfo('Coming Soon.....')

customer_icon=tk.PhotoImage(file='icons2/customer-service.png')
help_icon=tk.PhotoImage(file='icons2/iconfinder_phone_678143 (1).png')
mail_icon=tk.PhotoImage(file='icons2/Mail (1).png')
whatsapp_icon=tk.PhotoImage(file='icons2/iconfinder_1_Whatsapp2_colored_svg_5296520 (2).png')
how_icon=tk.PhotoImage(file='icons2/question (3).png')

cust_care=tk.Menu(help_menu,tearoff=False)

help_menu.add_cascade(label='Customer Service',menu=cust_care,image=customer_icon,compound=tk.LEFT)
help_menu.add_command(label='How to Use',command=use_func,image=how_icon,compound=tk.LEFT)


cust_care.add_command(label='Help-Line',image=help_icon,compound=tk.LEFT)
cust_care.add_command(label='E-mail',image=mail_icon,compound=tk.LEFT)
cust_care.add_command(label='Whatsapp',image=whatsapp_icon,compound=tk.LEFT)	
#################################


########  Follow us functionality ###########
insta_icon=tk.PhotoImage(file='icons2/instagram-logo-16.png')
fb_icon=tk.PhotoImage(file='icons2/facebook-icon.png')
twitter_icon=tk.PhotoImage(file='icons2/twitter (1).png')


def insta_func():
	pass
	
def fb_func():
	pass
	
def twitter_func():
	pass


follow_menu.add_command(label="kaluram kharra",image=insta_icon,compound=tk.LEFT,command=insta_func)
follow_menu.add_command(label="kaluram kharra",image=fb_icon,compound=tk.LEFT,command=fb_func)
follow_menu.add_command(label="kaluram kharra",image=twitter_icon,compound=tk.LEFT,command=twitter_func)

#################################


menubar.config(bg="#73ccde",fg="black")
root.config(menu=menubar)
root.mainloop()
