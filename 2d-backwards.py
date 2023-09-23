import tkinter as tk
from tkinter import ttk

replacements_to_wingdings = {
    'a': '♋',
    'A': '✌',
    'b': '♌',
    'B': '👌',
    'c': '♍',
    'C': '👍',
    'd': '♎',
    'D': '👎',
    'e': '♏',
    'E': '☜',
    'f': '♐',
    'F': '☞',
    'g': '♑',
    'G': '☝',
    'h': '♒',
    'H': '☟',
    'i': '♓',
    'I': '✋',
    'j': '🙰',
    'J': '🙵',
    'k': '😐',
    'K': '●',
    'l': '☹',
    'L': '❍',
    'm': '💣',
    'M': '■',
    'n': '☠',
    'N': '□',
    'o': '⚐',
    'O': '◻',
    'p': '🏱',
    'P': '❑',
    'q': '✈',
    'Q': '❒',
    'r': '☼',
    'R': '⬧',
    's': '💧',
    'S': '⧫',
    't': '❄',
    'T': '◆',
    'u': '🕆',
    'U': '❖',
    'v': '✞',
    'V': '⬥',
    'w': '🕈',
    'W': '⌧',
    'x': '✠',
    'X': '⍓',
    'y': '✡',
    'Y': '⌘',
    'z': '☪',
    'Z': '✏',
    '!': '✂',
    '"': '✁',
    '#': '👓',
    '$': '🕭',
    '%': '🕮',
    '&': '🕯',
    "'": '🕿',
    '(': '✆',
    ')': '🖂',
    '*': '🖃',
    '+': '📪',
    ',': '📫',
    '-': '📬',
    '.': '📭',
    '/': '🖳',
    ':': '🖴',
    ';': '🖫',
    '<': '🖬',
    '=': '✇',
    '>': '✍',
    '?': '☯',
    '@': 'ॐ',
    '[': '☸',
    '\\': '♈',
    ']': '♉',
    '^': '♊',
    '_': '❀',
    '`': '✿',
    '{': '❝',
    '|': '❞',
    '}': '▪',
    '~': '◻'
}

replacements_to_text = {v: k for k, v in replacements_to_wingdings.items()}

def convert_wingdings_to_text():
    wingdings_text = wingdings_input.get("1.0", "end-1c")
    text_output.delete(1.0, "end")
    converted_text = convert_to_text(wingdings_text)
    text_output.insert("1.0", converted_text)

def convert_text_to_wingdings():
    text = text_input.get("1.0", "end")
    wingdings_output.delete("1.0", "end")
    converted_wingdings = convert_to_wingdings(text)
    wingdings_output.insert("1.0", converted_wingdings)

def convert_to_text(wingdings_text):
    converted_text = ""
    for char in wingdings_text:
        if char in replacements_to_text:
            converted_text += replacements_to_text[char]
        else:
            converted_text += char
    return converted_text

def convert_to_wingdings(text):
    converted_wingdings = ""
    for char in text:
        if char in replacements_to_wingdings:
            converted_wingdings += replacements_to_wingdings[char]
        else:
            converted_wingdings += char
    return converted_wingdings

app = tk.Tk()
app.title("Wingdings Translator")

app.geometry("300x470")

app.iconbitmap("icon.ico")

label_wingdings = tk.Label(app, text="Wingdings Text:")
label_wingdings.pack()

wingdings_input = tk.Text(app, height=5, width=30)
wingdings_input.pack()

convert_button_wingdings = ttk.Button(app, text="Convert Wingdings to Text", command=convert_wingdings_to_text)
convert_button_wingdings.pack()

text_output = tk.Text(app, height=5, width=30)
text_output.pack()

separator = ttk.Separator(app, orient='horizontal')
separator.pack(fill='x', padx=20, pady=10)  # Adjust padx and pady values for spacing

label_text = tk.Label(app, text="Normal Text:")
label_text.pack()

text_input = tk.Text(app, height=5, width=30)
text_input.pack()

convert_button_text = ttk.Button(app, text="Convert Text to Wingdings", command=convert_text_to_wingdings)
convert_button_text.pack()

wingdings_output = tk.Text(app, height=5, width=30)
wingdings_output.pack()



app.mainloop()
