import json
from jinja2 import Template, Environment, FileSystemLoader


def load_json_data_from_file(file_path):
        
    #version qui lève une erreur si le fichier ou le chemin est inexistant
    #f = open(file_path)
    #data = json.load(f)
    #f.close()
    
    try:
        with open(file_path) as f:
            data = json.load(f)
            f.close()
    
    except IOError:
        print("Could not read file:", file_path)

    return data


def load_yaml_data_from_file(file_path):
    """
        A compléter ....
    """
    pass


def render_network_config(template_name, data):
    
    template = env.get_template(template_name) 
    return template.render(data) 



def save_built_config(file_name, data):
    
    try:
        with open(file_name, "w") as f:
            f.write(data)
            f.close()
    
    except IOError:
        print("Could not read file:", file_name)



if __name__ == "__main__":
    #print(load_json_data_from_file("./data/ESW2.json"))
    env = Environment(loader=FileSystemLoader("templates"))

    #print(render_network_config("ESW2.j2",load_json_data_from_file("./data/ESW2.json")))
    #print(render_network_config("R2.j2",load_json_data_from_file("./data/R2.json")))
    save_built_config("./config/ESW2.conf",render_network_config("ESW2.j2",load_json_data_from_file("./data/ESW2.json")))
    save_built_config("./config/R2.conf",render_network_config("R2.j2",load_json_data_from_file("./data/R2.json")))
