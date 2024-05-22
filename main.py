from frequencyAnalysis import get_most_common_words, get_word_cloud_img, get_frequency_plot
from ttkbootstrap.constants import *
from PIL import ImageTk
import ttkbootstrap as ttk

global freq_dist_fnl
global study_flag


def start_study():
    freq_dist_fnl = get_most_common_words(enter_text_1.get('1.0', END))

    img = ImageTk.PhotoImage(get_word_cloud_img(enter_text_1.get('1.0', END)))
    word_cloud_label_2.configure(image=img)
    word_cloud_frame.image = img

    img2 = ImageTk.PhotoImage(get_frequency_plot(freq_dist_fnl))
    frequency_analysis_label_2.configure(image=img2)
    frequency_analysis_label_2.image = img2

    tab_control.tab(1, state='normal')
    tab_control.tab(2, state='normal')
    tab_control.select(1)


root = ttk.Window(themename='darkly')
root.title('Media Analysis')
root.minsize(650, 700)
root.maxsize(1000, 950)
root.geometry('850x800')

root.update_idletasks()
s = root.geometry()
s = s.split('+')
s = s[0].split('x')
width_root = int(s[0])
height_root = int(s[1])


def get_width(percent):
    return int(width_root * percent)
def get_height(percent):
    return int(height_root * percent)


ttk.Style().configure('TNotebook',
                      tabmargins=[0, 10, 0, 0],
                      tabposition='n')
ttk.Style().configure('TNotebook.Tab',
                      font='Gilroy 18 bold')
ttk.Style().configure('TButton',
                      font='Gilroy 16',
                      padding=[15, 10])
ttk.Style().configure('TLabel',
                      font='Gilroy 16',
                      justify=CENTER,
                      padding=[15, 15])

# --------- ______ ---------
tab_control = ttk.Notebook(root)
enter_frame = ttk.Frame(tab_control)
frequency_analysis_frame = ttk.Frame(tab_control)
word_cloud_frame = ttk.Frame(tab_control)

enter_label_1 = ttk.Label(enter_frame, text='Введите текст для анализа:')
enter_text_1 = ttk.Text(enter_frame)
enter_btn_start = ttk.Button(enter_frame, command=start_study, text='Начать исследование')

frequency_analysis_label_1 = ttk.Label(frequency_analysis_frame, text='Самые часто встречающиеся слова в тексте.\nГистограмма, построенная на основе частотного анализа текста:')
frequency_analysis_label_2 = ttk.Label(frequency_analysis_frame, justify=CENTER)

word_cloud_label_1 = ttk.Label(word_cloud_frame, text='Облако слов,\nпостроенное на основе частотного анализа текста:')
word_cloud_label_2 = ttk.Label(word_cloud_frame, justify=CENTER)
# --------- ______ ---------

# --------- PACK-PART ---------
enter_frame.pack()
enter_label_1.pack()
enter_text_1.pack(expand=True, fill=BOTH, padx=get_width(0.1))
enter_btn_start.pack(expand=True, pady=[get_height(0.02), get_height(0.1)], padx=get_width(0.2))
tab_control.add(enter_frame, text='Ввод текста')

frequency_analysis_frame.pack()
frequency_analysis_label_1.pack()
frequency_analysis_label_2.pack()
tab_control.add(frequency_analysis_frame, text='Частотный анализ', state='hidden')

word_cloud_frame.pack()
word_cloud_label_1.pack(side=TOP)
word_cloud_label_2.pack(side=TOP)
tab_control.add(word_cloud_frame, text='Облако слов', state='hidden')
tab_control.pack(expand=True, fill=BOTH)
# --------- PACK-PART ---------

root.mainloop()
