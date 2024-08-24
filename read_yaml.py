import yaml

# def read_yaml_file():
#     file_yaml = 'conf.yaml'
#     with open(file_yaml, 'r', encoding="utf-8") as file:
#         try:
#             data = yaml.safe_load(file)
#             return data
#         except yaml.YAMLError as e:
#             print(f'读取{file_yaml}文件失败：{e}')
#             return None

# def get_bin(config: dict):
#     return config.get("bin")

# def get_url(config: dict):
#     return config.get("url")

# def get_version(config: dict):
#     return config.get("version")


class Config:

    def __init__(self, software, file_path="conf.yaml") -> None:
        self.software = software
        self.file_path = file_path
        self.config = self.read_yaml_file()

    def read_yaml_file(self):
        """读取 YAML 文件并返回字典。"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
                return data
        except yaml.YAMLError as e:
            print(f'读取 {self.file_path} 文件失败：{e}')
            return None

    def get_bin(self):
        """获取指定软件的 'bin' 属性。"""
        if self.config:
            return self.config.get(self.software, {}).get('bin')
        return None

    def get_url(self):
        """获取指定软件的 'url' 属性。"""
        if self.config:
            return self.config.get(self.software, {}).get('url', [])
        return []

    def get_version(self):
        """获取指定软件的 'version' 属性。"""
        if self.config:
            return self.config.get(self.software, {}).get('version')
        return None


if __name__ == "__main__":
    software = input("输入需要安装的软件:")
    config = Config(software=software)
    print(config.get_bin())
