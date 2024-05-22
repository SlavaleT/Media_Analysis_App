import io

from PIL import Image
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from wordcloud import WordCloud
from nltk import word_tokenize
from collections import deque
import matplotlib.pyplot as plt
import numpy as np
import pymorphy2
import string
import nltk


def get_most_common_words(text):
    morph = pymorphy2.MorphAnalyzer()

    text = text.lower()

    special_chars = string.punctuation

    text = ''.join(ch for ch in text if ch not in special_chars)

    text_tokens = word_tokenize(text)

    for i in range(0, len(text_tokens)):
        text_tokens[i] = morph.normal_forms(text_tokens[i])[0]

    text = nltk.Text(text_tokens)

    freq_dist = FreqDist(text)

    russian_stopwords = stopwords.words('russian')
    russian_stopwords.extend(('«', '»', '„', '“', '—', 'это', 'который'))

    freq_dist_mst_cmmn = deque(freq_dist.most_common())
    freq_dist_fnl = []

    tmp_flag = False
    while freq_dist_mst_cmmn:
        word = freq_dist_mst_cmmn.popleft()
        for stopword in russian_stopwords:
            if word[0] == stopword:
                tmp_flag = True
                break
        if tmp_flag:
            tmp_flag = False
            continue
        else:
            freq_dist_fnl.append(word)

    return freq_dist_fnl


def get_word_cloud_img(text):
    x, y = np.ogrid[:600, :600]

    mask = (x - 300) ** 2 + (y - 300) ** 2 > 300 ** 2
    mask = 255 * mask.astype(int)

    morph = pymorphy2.MorphAnalyzer()

    text = text.lower()

    special_chars = string.punctuation

    text = ''.join(ch for ch in text if ch not in special_chars)

    text_tokens = word_tokenize(text)

    for i in range(0, len(text_tokens)):
        text_tokens[i] = morph.normal_forms(text_tokens[i])[0]

    text = nltk.Text(text_tokens)

    freq_dist = FreqDist(text)

    russian_stopwords = stopwords.words('russian')
    russian_stopwords.extend(('«', '»', '„', '“', '—', 'это', 'который'))

    freq_dist_mst_cmmn = deque(freq_dist.most_common())
    freq_dist_fnl = []

    tmp_flag = False
    while freq_dist_mst_cmmn:
        word = freq_dist_mst_cmmn.popleft()
        for stopword in russian_stopwords:
            if word[0] == stopword:
                tmp_flag = True
                break
        if tmp_flag:
            tmp_flag = False
            continue
        else:
            freq_dist_fnl.append(word)

    text_str = ''
    for i in range(0, len(freq_dist_fnl)):
        text_str += (freq_dist_fnl[i][0] + ' ') * freq_dist_fnl[i][1]

    word_cloud = WordCloud(width=500,
                           height=500,
                           random_state=1,
                           background_color='#222222',
                           colormap='Dark2',
                           mask=mask,
                           collocations=False).generate(text_str)
    word_cloud.to_image().save('img2.png')
    return word_cloud.to_image()


def get_frequency_plot(input_array):
    fig, ax = plt.subplots()

    fig.set_size_inches(8, 7.8)
    fig.set_layout_engine(layout=None)
    fig.subplots_adjust(left=0.4)
    fig.subplots_adjust(top=1.0)

    y_pos = np.arange(20)
    performance = [input_array[i][1] for i in range(0, 20)]
    labels = [input_array[i][0] for i in range(0, 20)]

    ax.barh(y_pos, performance, color='#375a7f')
    ax.set_yticks(y_pos, labels=labels)
    ax.spines[['right', 'left', 'top', 'bottom']].set_visible(False)
    ax.invert_yaxis()
    ax.set_facecolor('#222222')
    fig.patch.set_facecolor('#222222')

    ax.tick_params(labelfontfamily='Gilroy', labelsize=22, labelcolor='white')

    buf = io.BytesIO()
    fig.savefig(buf, dpi=96)
    buf.seek(0)

    return Image.open(buf)
