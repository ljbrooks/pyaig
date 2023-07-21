import graphviz

g = graphviz.Graph("colors")

g.node("RGB: #40e0d0", style="filled", fillcolor="#40e0d0")

g.view()


print(g)
