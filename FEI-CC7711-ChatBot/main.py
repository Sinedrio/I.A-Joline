import tkinter as tk
from tkinter import ttk
from chatbot import ChatBot

class ChatInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Chatbot")
        
        self.chatbot = ChatBot()
        self.chatbot.createModel()  # Criar o modelo do chatbot
        
        self.create_widgets()

    def create_widgets(self):
        self.master.geometry('400x500')  # Definindo o tamanho da janela
        
        self.chat_frame = ttk.Frame(self.master, padding=(10, 10, 10, 0))
        self.chat_frame.pack(fill='both', expand=True)
        
        self.chat_display = tk.Text(self.chat_frame, wrap='word', state='disabled')
        self.chat_display.pack(side='top', fill='both', expand=True)
        
        self.scrollbar = ttk.Scrollbar(self.chat_frame, orient='vertical', command=self.chat_display.yview)
        self.scrollbar.pack(side='right', fill='y')
        
        self.chat_display.config(yscrollcommand=self.scrollbar.set)
        
        self.input_frame = ttk.Frame(self.master, padding=(10, 5))
        self.input_frame.pack(fill='x')
        
        self.input_box = ttk.Entry(self.input_frame)
        self.input_box.pack(side='left', fill='x', expand=True)
        self.input_box.bind('<Return>', self.send_message)
        
        self.send_button = ttk.Button(self.input_frame, text='Enviar', command=self.send_message)
        self.send_button.pack(side='right')

    def send_message(self, event=None):
        question = self.input_box.get()
        self.input_box.delete(0, 'end')
        if question:
            response, intent = self.chatbot.chatbot_response(question)
            self.display_message(question, 'user')
            self.display_message(response, 'chatbot')
    
    def display_message(self, message, sender):
        self.chat_display.config(state='normal')
        if sender == 'user':
            self.chat_display.insert('end', 'Você: ' + message + '\n\n', 'user')
        else:
            self.chat_display.insert('end', 'Chatbot: ' + message + '\n\n', 'chatbot')
        self.chat_display.config(state='disabled')
        self.chat_display.see('end')

def main():
    root = tk.Tk()
    app = ChatInterface(root)
    
    # Estilizando a aparência
    style = ttk.Style()
    style.configure('user.TLabel', foreground='blue')
    style.configure('chatbot.TLabel', foreground='green')
    
    # Definindo tags para diferentes estilos de mensagem na área de texto
    app.chat_display.tag_configure('user', justify='right', font=('Arial', 10, 'bold'))
    app.chat_display.tag_configure('chatbot', justify='left', font=('Arial', 10))

    root.mainloop()

if __name__ == "__main__":
    main()
