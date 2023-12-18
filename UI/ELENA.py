import tkinter as tk
from tkinter import ttk, scrolledtext, PhotoImage, filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk, ImageColor
import os
import pyperclip
from screeninfo import get_monitors
import time

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        #=====================================================================Configuration de la fenêtre=========================================================
        image_path= "logo.png"
        self.iconphoto(False, tk.PhotoImage(file=image_path))
        self.title("E.L.E.N.A")
        screen_width = get_monitors()[0].width
        screen_height = get_monitors()[0].height
        window_width = 1440
        window_height = 810
        self.geometry(f"{window_width}x{window_height}")
        left_frame = ttk.Frame(self, style='Left.TFrame')
        left_frame.grid(row=0, column=0, sticky=tk.NSEW)
        right_frame = ttk.Frame(self, style='Right.TFrame')
        right_frame.grid(row=0, column=1, sticky=tk.NSEW)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=40)
        #=====================================================================Configuration de la fenêtre=========================================================






        
        #=====================================================================Logo et titre(coin supérieur gauche)================================================
        image_path= "votre_image.png"
        original_image = Image.open(image_path)
        percentage_resize = 0.75
        width, height = original_image.size
        new_width = int(width * percentage_resize)
        new_height = int(height * percentage_resize)
        resized_image = original_image.resize((new_width, new_height))
        img = ImageTk.PhotoImage(resized_image)
        image_label = ttk.Label(left_frame, image=img, background="#2F2F2F")
        image_label.image = img
        image_label.grid(row=1, column=0, sticky=tk.W, padx=0, pady=(0, 75))
        #=====================================================================Logo et titre(coin supérieur gauche)================================================







        #=====================================================================Zone de prompt================================================
        image_path2= "back.png" 
        original_image2 = Image.open(image_path2)
        percentage_resize = 1.75
        width, height = original_image2.size
        new_width = int(width * percentage_resize)
        new_height = int(height * percentage_resize)
        resized_image2 = original_image2.resize((new_width, new_height))
        img2 = ImageTk.PhotoImage(resized_image2)
        image_label = ttk.Label(left_frame, image=img2, background="#2F2F2F")
        image_label.image = img2  
        image_label.grid(row=2, column=0, sticky=tk.W, padx=40, pady=(0, 50))
        def on_entry_focus_in(event):
          current_text = self.text_entry.get("1.0", "end-1c")
          if current_text == "Prompt...": 
            self.text_entry.delete("1.0", "end-1c")
        def on_entry_focus_out(event):
          current_text = self.text_entry.get("1.0", "end-1c")
          if current_text == "":
            default_text = "Prompt..."
            self.text_entry.insert("1.0", default_text)
        self.text_entry = tk.Text(left_frame, wrap=tk.WORD, width=22, height=17, font=('Helvetica', 14), bg ="#3B3B3B", border =0,fg='white')
        self.text_entry.place(x=61, y=222)
        default_text = "Prompt..."
        self.text_entry.insert("1.0", default_text)
        self.text_entry.bind("<FocusIn>", on_entry_focus_in)
        self.text_entry.bind("<FocusOut>", on_entry_focus_out)
        #=====================================================================Zone de prompt================================================







        #=====================================================================Boutton Send================================================
        def my_command12():
           img = Image.open('clickme.png')
           largeur_redmensionnee2, hauteur_redimensionnee2 = img.size
           largeur_redimensionnee3 = int(largeur_redmensionnee2 * 0.34)
           hauteur_redimensionnee3 = int(hauteur_redimensionnee2 *0.34)
           image_redimensionnee2 = img.resize((largeur_redimensionnee3, hauteur_redimensionnee3))
           photo_redimensionnee = ImageTk.PhotoImage(image_redimensionnee2)
           self.button_label2.config(image=photo_redimensionnee)
           self.button_label2.image = photo_redimensionnee
        def my_command11():
           img = Image.open('clickme.png')
           largeur_redimensionnee, hauteur_redimensionnee = img.size
           largeur_redimensionnee = int(largeur_redimensionnee * 0.37)
           hauteur_redimensionnee = int(hauteur_redimensionnee *0.37)
           image_redimensionnee = img.resize((largeur_redimensionnee, hauteur_redimensionnee))
           photo_redimensionnee = ImageTk.PhotoImage(image_redimensionnee)
           self.button_label2.config(image=photo_redimensionnee)
           self.button_label2.image = photo_redimensionnee
        def my_command10(event):
           my_command11()
           self.after(100, my_command12)
        self.click_btn4= PhotoImage(file='clickme.png')
        self.click_btn3 = self.click_btn4.subsample(3, 3) 
        self.button_label2 = ttk.Label(left_frame, image=self.click_btn3,background="#2F2F2F")
        self.button_label2.image = img 
        self.button_label2.grid(row=3, column=0, sticky=tk.W, padx=(67, 0), pady=10)
        self.button_label2.config(cursor="hand2")
        self.button_label2.bind("<Button-1>", my_command10)
        #=====================================================================Boutton Send================================================






        #=====================================================================Titre de génération================================================
        image_path= "littlezone2.png"
        img = Image.open(image_path)
        percentage_resize = 0.69
        width, height = img.size
        new_width = int(width * percentage_resize)
        new_height = int(height * percentage_resize)
        resized_image3 = img.resize((new_width, new_height))
        img2 = ImageTk.PhotoImage(resized_image3)
        image_label = ttk.Label(right_frame, image=img2,background="#282828")
        image_label.image = img2 
        image_label.grid(row=0, column=0, sticky=tk.W, padx=260, pady=5)
        display_text = tk.StringVar()
        self.text_entry2 = tk.Label(right_frame, textvariable=display_text, width=47, height=1, font=('Helvetica', 14), bg ="#101010", border =0,fg='white')
        self.text_entry2.place(x=275, y=20)
        display_text.set("Landscape Generation")
        #=====================================================================Titre de génération================================================






        #=====================================================================Image de génération================================================
        image_path= "img.png"
        img = Image.open(image_path)
        percentage_resize = 0.90
        width, height = img.size
        new_width = int(width * percentage_resize)
        new_height = int(height * percentage_resize)
        resized_image3 = img.resize((new_width, new_height))
        img2 = ImageTk.PhotoImage(resized_image3)
        image_label = ttk.Label(right_frame, image=img2,background="white")
        image_label.image = img2  
        image_label.grid(row=1, column=0, sticky=tk.W, padx=172, pady=10)
        #=====================================================================Image de génération================================================






        #=====================================================================Bouton de copie de texte================================================
        def makeinvisible():
           self.textcpy.place_forget()
        def my_command4():
           img = Image.open('copy.png')
           largeur_redmensionnee2, hauteur_redimensionnee2 = img.size
           largeur_redimensionnee3 = int(largeur_redmensionnee2 * 0.25)
           hauteur_redimensionnee3 = int(hauteur_redimensionnee2 *0.25)
           image_redimensionnee2 = img.resize((largeur_redimensionnee3, hauteur_redimensionnee3))
           photo_redimensionnee = ImageTk.PhotoImage(image_redimensionnee2)
           self.button_label.config(image=photo_redimensionnee)
           self.button_label.image = photo_redimensionnee
        def my_command3():
           img = Image.open('copy.png')
           largeur_redimensionnee, hauteur_redimensionnee = img.size
           largeur_redimensionnee = int(largeur_redimensionnee * 0.30)
           hauteur_redimensionnee = int(hauteur_redimensionnee *0.30)
           image_redimensionnee = img.resize((largeur_redimensionnee, hauteur_redimensionnee))
        
           photo_redimensionnee = ImageTk.PhotoImage(image_redimensionnee)
           self.button_label.config(image=photo_redimensionnee)
           self.button_label.image = photo_redimensionnee
        def my_command2(event):
           my_command3()
           self.after(100, my_command4)
           pyperclip.copy(display_text2.get())
           self.textcpy.place(x=973, y=768)
           self.after(1000, makeinvisible)
        self.click_btn= PhotoImage(file='copy.png')
        self.click_btn2 = self.click_btn.subsample(4, 4) 
        self.button_label = ttk.Label(right_frame, image=self.click_btn2,background="#282828")
        self.button_label.image = img
        self.button_label.place(x=940,y=755)
        self.button_label.bind("<Button-1>", my_command2)
        self.button_label.config(cursor="hand2")

        self.textcpy = tk.Label(right_frame, text="Texte copié", width=9, height=1, font=('Helvetica', 10), bg ="#282828", border =0,fg='white')
        self.textcpy.place(x=973, y=768)
        self.textcpy.place_forget()
        #=====================================================================Bouton de copie de texte================================================




         #=====================================================================Bouton de copie d'image================================================
        def makeinvisible2():
           self.textcpyimg.place_forget()
        def my_command34():
           img = Image.open('copyimg.png')
           largeur_redmensionnee2, hauteur_redimensionnee2 = img.size
           largeur_redimensionnee3 = int(largeur_redmensionnee2 * 0.50)
           hauteur_redimensionnee3 = int(hauteur_redimensionnee2 *0.50)
           image_redimensionnee2 = img.resize((largeur_redimensionnee3, hauteur_redimensionnee3))
           photo_redimensionnee = ImageTk.PhotoImage(image_redimensionnee2)
           self.button_label10.config(image=photo_redimensionnee)
           self.button_label10.image = photo_redimensionnee
        def my_command33():
           img = Image.open('copyimg.png')
           largeur_redimensionnee, hauteur_redimensionnee = img.size
           largeur_redimensionnee = int(largeur_redimensionnee * 0.55)
           hauteur_redimensionnee = int(hauteur_redimensionnee *0.55)
           image_redimensionnee = img.resize((largeur_redimensionnee, hauteur_redimensionnee))
        
           photo_redimensionnee = ImageTk.PhotoImage(image_redimensionnee)
           self.button_label10.config(image=photo_redimensionnee)
           self.button_label10.image = photo_redimensionnee
        def my_command32(event):
           my_command33()
           self.after(100, my_command34)
           destination_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
           if destination_path:
               image = Image.open("img.png")
               image.save(destination_path)
               print(f"L'image a été enregistrée avec succès à l'emplacement : {destination_path}")
               self.textcpyimg.place(x=935, y=459)
               self.after(1000, makeinvisible2)
           else:
               print("Annulation de l'enregistrement.")
        self.click_btn11= PhotoImage(file='copyimg.png')
        self.click_btn10 = self.click_btn11.subsample(2, 2) 
        self.button_label10 = ttk.Label(right_frame, image=self.click_btn10,background="#282828")
        self.button_label10.image = img
        self.button_label10.place(x=900,y=448)
        self.button_label10.bind("<Button-1>", my_command32)
        self.button_label10.config(cursor="hand2")

        self.textcpyimg = tk.Label(right_frame, text="Image enregistrée", width=13, height=1, font=('Helvetica', 10), bg ="#282828", border =0,fg='white')
        self.textcpyimg.place(x=935, y=459)
        self.textcpyimg.place_forget()
        #=====================================================================Bouton de copie d'image================================================























        #=====================================================================Barre décorative================================================
        image_path= "bar.png" 
        img = Image.open(image_path)
        percentage_resize = 0.75
        width, height = img.size
        new_width = int(width * percentage_resize)
        new_height = int(height * percentage_resize)
        resized_image3 = img.resize((new_width, new_height))
        img2 = ImageTk.PhotoImage(resized_image3)
        image_label = ttk.Label(right_frame, image=img2,background="#282828")
        image_label.image = img2  
        image_label.grid(row=2, column=0, sticky=tk.W, padx=60, pady=10)
        #=====================================================================Barre décorative================================================






        #=====================================================================Texte de Génération================================================
        image_path= "bigzone2.png"
        img = Image.open(image_path)
        percentage_resize = 0.68
        width, height = img.size
        new_width = int(width * percentage_resize)
        new_height = int(height * percentage_resize)
        resized_image3 = img.resize((new_width, new_height))
        img2 = ImageTk.PhotoImage(resized_image3)
        image_label = ttk.Label(right_frame, image=img2,background="#282828")
        image_label.image = img2 
        image_label.grid(row=3, column=0, sticky=tk.W, padx=127, pady=5)
        display_text2 = tk.StringVar()
        self.text_entry2 = tk.Label(right_frame, textvariable=display_text2, width=71, height=10, font=('Helvetica', 14), bg ="#101010", border =0,fg='white',wraplength=800)
        self.text_entry2.place(x=144, y=560)
        display_text2.set("The landscape contains a small clearing surrounded by forest, in autumn, with a river and a small wooden bridge.")
        #=====================================================================Texte de Génération================================================





        #=====================================================================Suite de la configuration de la fenêtre================================================
        ttk.Style().configure('Left.TFrame', background='#2F2F2F')
        ttk.Style().configure('Right.TFrame', background='#282828')
        self.center_window()
    def center_window(self):
        """Centrer la fenêtre sur l'écran."""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = int(screen_width*0.75)
        window_height = int(screen_height*0.75)
        x_position = int(screen_width/2 - window_width/2)
        y_position = int(screen_height/2 - window_height/2)
        self.geometry(f"+{x_position}+{y_position}")
        #=====================================================================Suite de la configuration de la fenêtre================================================


#====================================================Lancement de l'application================================================
if __name__ == "__main__":
    app = Application()
#====================================================Lancement de l'application================================================
