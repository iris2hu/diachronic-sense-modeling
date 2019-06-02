from matplotlib import pyplot as plt
import pickle as p
import random
import re
import sys

''' 

This is a visualize tool for the diachronic sense modeling data from the paper:
Hu Renfen, Li Shen and Liang Shichen. Diachronic Sense Modeling with Deep Contextualized Word Embeddings: An Ecological View. ACL 2019.

Github: https://github.com/iris2hu/diachronic-sense-modeling

'''


with open('prob_fitting_10.data', 'rb') as f:
    d = p.load(f)  # load the sense modeling data


def track_sense(word):

    ''' visualize the diachronic evolvement of the word senses '''

    test = d[word]
    labels = []

    fig = plt.figure(word, figsize=(7.5, 8))

    # markers = ['o', '+', 'x', 'v', '^', 's']
    markers = ['o', 'v', '^', 's', 'p', 'P', 'h', 'H', 'D']
    random.shuffle(markers)

    plt.ylim((0, min(max([max(v['y'] + v['y_fitting']) for _, v in test.items()]) + 0.05, 1)))
    plt.xlim((min([min(v['x']) for _, v in test.items()]), max([max(v['x']) for _, v in test.items()])))

    i = 1
    for k, v in test.items():
        definition = v['definition']
        x = v['x']
        y = v['y']
        y_fitting = v['y_fitting']

        labels.append(k)

        max_l = 50
        if len(definition) > max_l:
            p0 = definition[:max_l]
            p1 = definition[max_l:]
            if len(p1) >= 4:
                if p1[1] == ' ':
                    p0 = p0 + p1[0]
                    p1 = p1[1:]
                if re.findall(r'[a-zA-Z]', p0[-1]) and re.findall(r'[a-zA-Z]', p1[0]):
                    p0 = p0 + '-'
                if p1[0] == ' ':
                    p1 = p1[1:]
                definition = p0 + '\n' + p1

        tag = 'sense_' + str(i) + '_' + k.split('_')[2] + ': ' + definition

        m = markers[i - 1]
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        ch = '#' \
             + '{:0>2}'.format(hex(r)[2:]) \
             + '{:0>2}'.format(hex(g)[2:]) \
             + '{:0>2}'.format(hex(b)[2:]) \

        plt.scatter(x, y, label=tag, marker=m, c=ch, linewidths=2)
        plt.plot(x, y_fitting, '--', color=ch, linewidth=2)
        plt.legend(prop={'size': 13}, labelspacing=0.5, bbox_to_anchor=(0.5, -0.1), loc='upper center')

        i += 1

    plt.subplots_adjust(bottom=0.4, top=0.97, left=0.05, right=0.97)
    plt.show()


if __name__ == '__main__':

    words = sys.argv[1:]

    for w in words:
        if w not in d or not d[w]:
            print(w, 'not in the vocabulary.')
        else:
            track_sense(w)