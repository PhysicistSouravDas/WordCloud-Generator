# Here are all the installs and imports you will need for your word cloud script and uploader widget

!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

# Below is the uploader widget
def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()

#Program to process the text
def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    per_word_count = {}
    list_not_filt = file_contents.split()
    list_filt_1 = [] #This list is filtered from uninteresting words
    list_filt_2 = [] #This list is free from punctuations
    for word in list_not_filt:
        word = word.lower()
        if word not in uninteresting_words:
            list_filt_1.append(word)
    for word in list_filt_1:
        punc_free_word = ""
        for letter in word:
            if letter not in punctuations:
                punc_free_word += letter
        list_filt_2.append(punc_free_word)
    #Now, list_filt_2 contains all the required filtered words. Now, just counting needs to be done
    for filt_word in list_filt_2: #returns tuples of keys and values
        if filt_word not in per_word_count:
            per_word_count[filt_word] = 1
        else:
            per_word_count[filt_word] += 1
    
    #Counting Done, now JUST returning the resulting dictionary
    #return per_word_count
    
    #wordcloud
    cloud = wordcloud.WordCloud(widht = 1080, height = 720) #change width and height accordingly for resulution
    cloud.generate_from_frequencies(per_word_count)
    return cloud.to_array()

# Display of wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
