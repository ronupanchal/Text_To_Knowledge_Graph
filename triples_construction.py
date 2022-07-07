# https://blog.vsoftconsulting.com/blog/how-to-build-a-knowledge-graph
from openie import StanfordOpenIE
import csv
from datetime import date

def triple_generation(text, file_name):
    subject = []
    relation = []
    objects = []
    with StanfordOpenIE() as client:
        for triple in client.annotate(text):
            subject.append(triple['subject'])
            relation.append(triple['relation'])
            objects.append(triple['object'])
    headerList = ['subject', 'relation', 'object']
    with open(file_name, 'w',encoding='utf8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headerList)
        writer.writerows(zip(subject, relation, objects))

    graph_image = 'graph' + str(date.today()) + '.png'
    client.generate_graphviz_graph(text, graph_image)
    print('Graph generated: %s.' % graph_image)
    return "Triples Generated and stored in given csv file name"
## Sample Test
print(triple_generation("Dr. Ronak is located in India. Dr. Ronak is working in MNC Company.", "output"+str(date.today())+".csv"))


#print(triple_generation("Barack Obama was born in Hawaii.", "output"+str(date.today())+".csv"))
