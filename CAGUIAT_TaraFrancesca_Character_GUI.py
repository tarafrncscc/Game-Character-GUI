#CAGUIAT, TARA FRANCESCA L.     BSIS 2AB    

import tkinter as tk
from tkinter import *
import time
import tkinter.messagebox

class Character:
    def __init__(self, class_, weapon, ability1, ability2, ability3):
        self.class_ = class_
        self.weapon = weapon
        self.ability1 = ability1
        self.ability2 = ability2
        self.ability3 = ability3
    
    def SetClass(self, class_):
        self.class_ = class_
    
    def SetWeapon(self, weapon):
        self.weapon = weapon
    
    def SetAbility1(self, ability1):
        self.ability1 = ability1
    
    def SetAbility2(self, ability2):
        self.ability2 = ability2
    
    def SetAbility3(self, ability3):
        self.ability3 = ability3
    
    def ShowCharacter(self):
        return f'Class: {self.class_}\nWeapon: {self.weapon}\nAbilities: {self.ability1} , {self.ability2} & {self.ability3}'

class App:
    def __init__(self, app):
        self.app = app
        self.character = Character('', '', '', '', '')
        
        self.top_title = tk.Label(self.app, font=('arial black',12,'bold'),text="Customized your own character!",fg="Black")
        self.top_title.grid(row=0, column=0, sticky="n")
        self.top_title = tk.Label(self.app, font=('courier',12,'italic'),text="Class, Weapons, and Abilities are in your hands!",fg="Gold", bg="Black")
        self.top_title.grid(row=1, column=0, sticky="n")
        
        #display time & date
        localtime= time.asctime(time.localtime(time.time()))
        self.timesheesh = Label(self.app, font=('arial',11,'bold','underline'),text=localtime,fg= "Black",bd= 10,anchor='n')
        self.timesheesh.grid(row=10,column=0)

        #character class dropdown
        tk.Label(self.app, font=('courier',12,'bold'), text='Class:', fg="Magenta").grid(row=2, column=0, sticky="w") ##
        self.class_var = tk.StringVar(self.app)
        self.class_var.set('Select a class')
        self.class_dropdown = tk.OptionMenu(self.app, self.class_var, 'Wizard', 'Knight', 'Archer', 'Assassin')
        self.class_dropdown.grid(row=2)
        
        #weapon dropdown
        tk.Label(self.app, font=('courier',12,'bold'), text='Weapon:',fg="Purple").grid(row=3, column=0, sticky="w")
        self.weapon_var = tk.StringVar(self.app)
        self.weapon_var.set('Select a weapon')
        self.weapon_dropdown = tk.OptionMenu(self.app, self.weapon_var, 'Wizard Staff', 'Sword', 'Bow & Arrow', 'Katar')
        self.weapon_dropdown.grid(row=3)

        #ability dropdown
        tk.Label(self.app, font=('courier',12,'bold'), text='Ability #1:', fg="Blue").grid(row=4, column=0, sticky="w")
        self.ability1_var = tk.StringVar(self.app)
        self.ability1_var.set('Select an ability')
        self.ability1_dropdown = tk.OptionMenu(self.app, self.ability1_var, '', '', '')
        self.ability1_dropdown.grid(row=4)

        tk.Label(self.app, font=('courier',12,'bold'), text='Ability #2:', fg="Red").grid(row=5, column=0, sticky="w")
        self.ability2_var = tk.StringVar(self.app)
        self.ability2_var.set('Select an ability')
        self.ability2_dropdown = tk.OptionMenu(self.app, self.ability2_var, '', '', '')
        self.ability2_dropdown.grid(row=5)

        tk.Label(self.app, font=('courier',12,'bold'), text='Ability #3:', fg="Green").grid(row=6, column=0, sticky="w")
        self.ability3_var = tk.StringVar(self.app)
        self.ability3_var.set('Select an ability')
        self.ability3_dropdown = tk.OptionMenu(self.app, self.ability3_var, '', '', '')
        self.ability3_dropdown.grid(row=6)
        
        # Update the ability dropdown choices when the class changes
        self.class_var.trace('w', self.UpdateAbilityChoices)
        
        #submit button
        self.submit_button = tk.Button(self.app,font=('arial','10','bold'), bd=3, bg="Orange", text='Submit', command=self.Submit)
        self.submit_button.grid(row=7, column=0)

        #exit button
        self.exit_button = tk.Button(self.app, font=('arial','10','bold'),text='Exit',bd=3, bg="Orange", command=self.Ext)
        self.exit_button.grid(row=9)
        
        #label
        self.character_label = tk.Label(self.app,font=('times new roman','12'), fg="Brown", text='')
        self.character_label.grid(row=8, column=0, columnspan=2)

        self.status = Label(self.app,text="\tWelcome to GameCha! . . . . . . . . . . . . . . . . . . . . . . . . . . . .  created by: TFLC",fg="Gray")
        self.status.grid(row=11, sticky='w')
    
    def UpdateAbilityChoices(self, *args):
        class_ = self.class_var.get()
        if class_ == 'Wizard':
            self.ability1_var.set('Select an ability')
            self.ability1_dropdown['menu'].delete(0, 'end')
            self.ability1_dropdown['menu'].add_command(label='Energy Ball', command=tk._setit(self.ability1_var, 'Energy Ball'))
            self.ability1_dropdown['menu'].add_command(label='Dragons Breath', command=tk._setit(self.ability1_var, 'Dragons Breath'))
            self.ability1_dropdown['menu'].add_command(label='Crown of Flame', command=tk._setit(self.ability1_var, 'Crown of Flame'))
            self.ability1_dropdown['menu'].add_command(label='Hail Storm', command=tk._setit(self.ability1_var, 'Hail Storm'))

            self.ability2_var.set('Select an ability')
            self.ability2_dropdown['menu'].delete(0, 'end')
            self.ability2_dropdown['menu'].add_command(label='Energy Ball', command=tk._setit(self.ability2_var, 'Energy Ball'))
            self.ability2_dropdown['menu'].add_command(label='Dragons Breath', command=tk._setit(self.ability2_var, 'Dragons Breath'))
            self.ability2_dropdown['menu'].add_command(label='Crown of Flame', command=tk._setit(self.ability2_var, 'Crown of Flame'))
            self.ability2_dropdown['menu'].add_command(label='Hail Storm', command=tk._setit(self.ability2_var, 'Hail Storm'))

            self.ability3_var.set('Select an ability')
            self.ability3_dropdown['menu'].delete(0, 'end')
            self.ability3_dropdown['menu'].add_command(label='Energy Ball', command=tk._setit(self.ability3_var, 'Energy Ball'))
            self.ability3_dropdown['menu'].add_command(label='Dragons Breath', command=tk._setit(self.ability3_var, 'Dragons Breath'))
            self.ability3_dropdown['menu'].add_command(label='Crown of Flame', command=tk._setit(self.ability3_var, 'Crown of Flame'))
            self.ability3_dropdown['menu'].add_command(label='Hail Storm', command=tk._setit(self.ability3_var, 'Hail Storm'))
            
        elif class_ == 'Knight':
            self.ability1_var.set('Select an ability')
            self.ability1_dropdown['menu'].delete(0, 'end')
            self.ability1_dropdown['menu'].add_command(label='Fire Slash', command=tk._setit(self.ability1_var, 'Fire Slash'))
            self.ability1_dropdown['menu'].add_command(label='Power Slash', command=tk._setit(self.ability1_var, 'Power Slash'))
            self.ability1_dropdown['menu'].add_command(label='Gigantic Storm', command=tk._setit(self.ability1_var, 'Gigantic Storm'))
            self.ability1_dropdown['menu'].add_command(label='Chaotic Disaster', command=tk._setit(self.ability1_var, 'Chaotic Disaster'))
            
            self.ability2_var.set('Select an ability')
            self.ability2_dropdown['menu'].delete(0, 'end')
            self.ability2_dropdown['menu'].add_command(label='Fire Slash', command=tk._setit(self.ability2_var, 'Fire Slash'))
            self.ability2_dropdown['menu'].add_command(label='Power Slash', command=tk._setit(self.ability2_var, 'Power Slash'))
            self.ability2_dropdown['menu'].add_command(label='Gigantic Storm', command=tk._setit(self.ability2_var, 'Gigantic Storm'))
            self.ability2_dropdown['menu'].add_command(label='Chaotic Disaster', command=tk._setit(self.ability2_var, 'Chaotic Disaster'))

            self.ability3_var.set('Select an ability')
            self.ability3_dropdown['menu'].delete(0, 'end')
            self.ability3_dropdown['menu'].add_command(label='Fire Slash', command=tk._setit(self.ability3_var, 'Fire Slash'))
            self.ability3_dropdown['menu'].add_command(label='Power Slash', command=tk._setit(self.ability3_var, 'Power Slash'))
            self.ability3_dropdown['menu'].add_command(label='Gigantic Storm', command=tk._setit(self.ability3_var, 'Gigantic Storm'))
            self.ability3_dropdown['menu'].add_command(label='Chaotic Disaster', command=tk._setit(self.ability3_var, 'Chaotic Disaster'))

        elif class_ == 'Archer':
            self.ability1_var.set('Select an ability')
            self.ability1_dropdown['menu'].delete(0, 'end')
            self.ability1_dropdown['menu'].add_command(label='Take Aim', command=tk._setit(self.ability1_var, 'Take Aim'))
            self.ability1_dropdown['menu'].add_command(label='Quick Shot', command=tk._setit(self.ability1_var, 'Quick Shot'))
            self.ability1_dropdown['menu'].add_command(label='Blazing Arrow', command=tk._setit(self.ability1_var, 'Blazing Arrow'))
            self.ability1_dropdown['menu'].add_command(label='Frost Arrow', command=tk._setit(self.ability1_var, 'Frost Arrow'))

            self.ability2_var.set('Select an ability')
            self.ability2_dropdown['menu'].delete(0, 'end')
            self.ability2_dropdown['menu'].add_command(label='Take Aim', command=tk._setit(self.ability2_var, 'Take Aim'))
            self.ability2_dropdown['menu'].add_command(label='Quick Shot', command=tk._setit(self.ability2_var, 'Quick Shot'))
            self.ability2_dropdown['menu'].add_command(label='Blazing Arrow', command=tk._setit(self.ability2_var, 'Blazing Arrow'))
            self.ability2_dropdown['menu'].add_command(label='Frost Arrow', command=tk._setit(self.ability2_var, 'Frost Arrow'))

            self.ability3_var.set('Select an ability')
            self.ability3_dropdown['menu'].delete(0, 'end')
            self.ability3_dropdown['menu'].add_command(label='Take Aim', command=tk._setit(self.ability3_var, 'Take Aim'))
            self.ability3_dropdown['menu'].add_command(label='Quick Shot', command=tk._setit(self.ability3_var, 'Quick Shot'))
            self.ability3_dropdown['menu'].add_command(label='Blazing Arrow', command=tk._setit(self.ability3_var, 'Blazing Arrow'))
            self.ability3_dropdown['menu'].add_command(label='Frost Arrow', command=tk._setit(self.ability3_var, 'Frost Arrow'))

        elif class_ == 'Assassin':
            self.ability1_var.set('Select an ability') 
            self.ability1_dropdown['menu'].delete(0, 'end')
            self.ability1_dropdown['menu'].add_command(label='Cloaking', command=tk._setit(self.ability1_var, 'Cloaking'))
            self.ability1_dropdown['menu'].add_command(label='Enchant Poison', command=tk._setit(self.ability1_var, 'Enchant Poison'))
            self.ability1_dropdown['menu'].add_command(label='Sonic Acceleration', command=tk._setit(self.ability1_var, 'Sonic Acceleration'))
            self.ability1_dropdown['menu'].add_command(label='Meteor Assault', command=tk._setit(self.ability1_var, 'Meteor Assault'))

            self.ability2_var.set('Select an ability')
            self.ability2_dropdown['menu'].delete(0, 'end')
            self.ability2_dropdown['menu'].add_command(label='Cloaking', command=tk._setit(self.ability2_var, 'Cloaking'))
            self.ability2_dropdown['menu'].add_command(label='Enchant Poison', command=tk._setit(self.ability2_var, 'Enchant Poison'))
            self.ability2_dropdown['menu'].add_command(label='Sonic Acceleration', command=tk._setit(self.ability2_var, 'Sonic Acceleration'))
            self.ability2_dropdown['menu'].add_command(label='Meteor Assault', command=tk._setit(self.ability2_var, 'Meteor Assault'))

            self.ability3_var.set('Select an ability')
            self.ability3_dropdown['menu'].delete(0, 'end')
            self.ability3_dropdown['menu'].add_command(label='Cloaking', command=tk._setit(self.ability3_var, 'Cloaking'))
            self.ability3_dropdown['menu'].add_command(label='Enchant Poison', command=tk._setit(self.ability3_var, 'Enchant Poison'))
            self.ability3_dropdown['menu'].add_command(label='Sonic Acceleration', command=tk._setit(self.ability3_var, 'Sonic Acceleration'))
            self.ability3_dropdown['menu'].add_command(label='Meteor Assault', command=tk._setit(self.ability3_var, 'Meteor Assault'))
            
    def Submit(self):
        self.character.SetClass(self.class_var.get())
        self.character.SetWeapon(self.weapon_var.get())
        self.character.SetAbility1(self.ability1_var.get()) 
        self.character.SetAbility2(self.ability2_var.get())
        self.character.SetAbility3(self.ability3_var.get())
        self.character_label['text'] = self.character.ShowCharacter()
        self.status['text'] = "=================== Character has created successfully! ==================="

    def Ext(self):
        tkinter.messagebox.showinfo('Hey!','Thank you for using GameCha!')
        self.app.destroy()

def main():
    game = tk.Tk()
    game.grid()
    game.title("GameCha!")
    icon = PhotoImage(file="gameicon.png")
    game.tk.call('wm','iconphoto',game._w, icon)
    App(game)
    game.mainloop()
main()