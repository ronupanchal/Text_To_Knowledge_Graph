from py2neo import Graph, Node, Relationship
import pandas as pd

graph = Graph("bolt://localhost:7687", auth=("neo4j", "123"))

triples_df = pd.read_csv("output2022-07-02.csv")

for index, row in triples_df.iterrows():
    tx = graph.begin()
    a = Node('Subject', name = row['subject'])
    tx.create(a)
    b = Node('Object', name = row['object'])
    ab = Relationship(a, row['relation'], b)
    tx.create(ab)
    tx.commit()
