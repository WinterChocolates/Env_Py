import yaml


def read_yaml_file():
    file_yaml = 'conf.yaml'
    with open(file_yaml, 'r', encoding="utf-8") as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print(f'读取{file_yaml}文件失败：{e}')
            return None


if __name__ == "__main__":
    print(read_yaml_file().get("nginx"))
