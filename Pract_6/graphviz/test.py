import graphviz

# Create a directed graph object
dot = graphviz.Digraph(comment='The Round Table')

# Add nodes
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')

# Add edges
dot.edge('A', 'B', 'manages')
dot.edge('B', 'L', 'helps')
dot.edge('L', 'A', 'knows')

# Render the graph to a file (e.g., 'round-table.gv.png') and open it
# The `view=True` argument automatically opens the rendered file
dot.render('round-table.gv', view=True, format='png')
