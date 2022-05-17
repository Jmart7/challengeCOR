from tkinter import W
from networkx import DiGraph, eulerian_circuit

# words = ['chair', 'height', 'racket', 'touch', 'tunic']
words = ["for", "geek", "rig", "gif", "keeg"]
print(words[0],words[-1], words)
G = DiGraph()
G.add_weighted_edges_from(((w[0], w[-1], w) for w in words), weight='word')
result = [G[a][b]['word'] for a,b in eulerian_circuit(G)]

print(result)
# ['chair', 'racket', 'touch', 'height', 'tunic']