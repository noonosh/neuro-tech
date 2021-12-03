import yaml


def text(key: str):
    text_file = open('locale.yaml')
    contents = yaml.load(text_file, Loader=yaml.FullLoader)
    return contents['texts'][key]
