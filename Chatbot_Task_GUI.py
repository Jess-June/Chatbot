import PySimpleGUI as pg

chat=["Hi! I'm Jessica's Chatbot!","What's your name?"]
layout=[
    [pg.Text('Jessica\'s chatbot',text_color='red',background_color='black',font=('Verdana',16))],
    [pg.Listbox(values=chat,font=('Comic',14),text_color='yellow',background_color='black', size=(60,20), key = 'chatbox')],
    [pg.InputText('',font=('Comic',14),key='input'),pg.Button(button_text='Send',font=('Arial',16),key='sendmessage')]
]
    

def addline(line):
    chat.append(line)
    window['chatbox'].Update(chat)
    window['input'].Update('')

def talk(line):
    global chat
    arg = parameters['mode']
    if arg=='intro':
        parameters['name']=line
        parameters['mode']='menu'
        return "Oh, that's a nice name :)"
    if arg=='menu':
        menu=['Here are the things I can do:','1. Help','2. Calculator','3.Change your name','4. Change my name','5. Clear Screen','6. Quit']
        chat.extend(menu)
        window['chatbox'].Update(chat)
        window['input'].Update('')
        parameters['mode']='default'
        return "Enter an option"
    if arg=='calculator':
        if 'quit' in line.lower():
            parameters['mode']='default'
            return "Quitting calculator mode..."
        else:
            try:
                return str(eval(line))
            except:
                return "Invalid expression, type 'quit' if you wish to quit"
    if arg=='botnamechange':
        parameters['botname']=line
        parameters['mode']='default'
        return "Thank you, I like it :)"
    if arg=='default':
        if line.lower() in ('1','help'):
            parameters['mode']='menu'
            return 'Loading the menu (enter new line to view)'
        elif line.lower() in ('2','calculator'):
            parameters['mode']='calculator'
            return "Entering calculator mode...(To exit, type 'quit')"
        elif line.lower() in ('3','change my name','name'):
            parameters['mode']='intro'
            return "Enter your new name:"
        elif line.lower() in ('4','change your name','botname'):
            parameters['mode']='botnamechange'
            return "Enter a name for me:"
        elif line.lower() in ('5','clear','clear screen'):
            chat=[]
            return 'Cleared'
        elif line.lower() in ('6','Quit'):
            return "It was nice talking to you :)"
        else:
            return "I don't understand that"

parameters = {'name':'User','botname':'Bot','mode':'intro'}
window = pg.Window('Jessica\'s chatbot',layout)
while True:
    name,botname=parameters['name'],parameters['botname']
    event,values = window.Read()
    if event==pg.WINDOW_CLOSED:
        break
    elif event=='sendmessage':
        line = values['input']
        addline(f"[{name}]: "+line)
        response=talk(line)
        addline(f"[{botname}]: "+response)
        if response=="It was nice talking to you :)":
            break
        
window.Close()