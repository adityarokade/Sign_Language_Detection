import yaml



class Read_Yaml:
    def __init__(self):
        pass

    def read_yaml(path_to_yaml: str):
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
        return content
