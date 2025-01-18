# 
from IPython.display import Image

def generate_architecture_pic(agent, picture_name):
    """
    Generate a picture of the architecture
    """
    with open(f"./{picture_name}.png", "wb") as f:
        f.write(Image(agent.get_graph().draw_mermaid_png()).data)