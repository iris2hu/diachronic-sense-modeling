# Diachronic Sense Modeling with Deep Contextualized Word Embeddings

This project releases the diachronic sense modeling data in the paper:

<em>Renfen Hu, Shen Li and Shichen Liang. Diachronic Sense Modeling with Deep Contextualized Word Embeddings:  An Ecological View, ACL 2019</em>

With the data and a visualize tool, one can easily track the evolvement of word meaning from the sense level. An example of the word "gay" is shown in the Figure.

![gay example](https://github.com/iris2hu/diachronic-sense-modeling/blob/master/example.jpg)

## Vocabulary

The sense definitions are from the online version of [Oxford dictionary](https://en.oxforddictionaries.com/).

To select the target words for diachronic study, we firstly extract word frequency information from [COHA](https://corpus.byu.edu/coha/), a genre balanced corpus containing English texts from 1810 to 2009. Only words that appear at least 10 times a year for over 50 consecutive years are retained. After lemmatization, we totally retrieve 4881 words, including 3358 polysemous words. Among them, 3220 entries are obtained from the Oxford dictionary.

The poly_vocab.txt file lists the 3220 polysemous words that can be tracked via our method.

## Sense Modeling Data

The data is in a Python pickle file "prob_fitting_10.data". For each word, e.g. "gay", we give its diachronic sense information in dict type as shown below: 

```
{
  'gay_1_adjective_1': 
  	{'definition': '(of a person) homosexual (used especially of a man)',   # from Oxford dictionary
	  'x': [1830, 1840,  ... , 2010],   # year information with the with time interval $\Delta t = 10$.
	  'y': [0.028, 0.042, ... , 0.573],  #  the proportion of the sense at each time inerval
	  'y_fitting': [0.032, 0.031, ... , 0.595]}, # the proportion after  polynomial curve fitting 
  'gay_1_adjective_2': 
  	{'definition': 'Light-hearted and carefree.', 
	    'x': [1830, 1840, ... , 2010], 
	    'y': [0.972, 0.958, ... , 0.130], 
	    'y_fitting': [0.979, 0.9667, ... , 0.037]},
  'gay_1_noun_1': 
  	{'definition': 'A homosexual, especially a man.', 
	    'x': [1830, 1840, ... , 2010], 
	    'y': [0.0, 0.0, ... , 0.364], 
	    'y_fitting': [-0.01, 0.002, ... , 0.368]}, 
  'gay_1_adjective_3': 
	{'definition': 'Foolish, stupid, or unimpressive.', 
	  'x': [1830, 1840, ... , 2010], 
	  'y': [0.0, 0.0,  ... , 0.0], 
	  'y_fitting': [-0.0002, ... , -1.277e-05]}
	    
}
```

## Track and Visualize

<strong>Requirements: python3, matplotlib</strong>

To visualize a word:
```
python visualize.py gay
```
To visualize multiple words:
```
python visualize.py alien address
```
