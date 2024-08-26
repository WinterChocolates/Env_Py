import yaml


class Config:

    def __init__(self, software, version=None, file_path="conf.yaml") -> None:
        self.software = software
        self.version = version
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

    def get_name(self):
        """获取指定软件的 'name' 属性。"""
        if self.config:
            return self.config.get(self.software, "").get('name')
        return None

    def get_bin(self):
        """获取指定软件的 'bin' 属性。"""
        if self.config:
            return self.config.get(self.software, {}).get('bin')
        return None

    def get_urls(self):
        """获取指定软件的 'url' 属性。如果软件为 'python'，在 URL 后添加版本号。"""
        if self.config:
            urls = self.config.get(self.software, {}).get('url', [])
            if self.software.lower() == "python" and self.version:
                # 在每个 URL 后附加版本号
                urls = [f"{url}{self.version}/" for url in urls]
            return urls
        return []

    def get_versions(self):
        """获取指定软件的 'version' 属性。"""
        if self.config:
            return self.config.get(self.software, {}).get('version', [])
        return []

    def get_install(self):
        """获取指定软件的 'install' 属性。"""
        if self.config:
            return self.config.get(self.software, {}).get('install')
        return None

    def get_module(self):
        """获取指定软件的 'module' 属性。"""
        if self.config:
            return self.config.get(self.software, {}).get('module')
        return None

    def get_package(self):
        """获取指定软件的 'package' 属性。"""
        if self.config:
            return self.config.get(self.software, {}).get('package')
        return None

    def get_archive(self):
        """获取指定软件的完整 'archive' 属性。"""
        if self.config:
            archive = self.config.get(self.software, {}).get('archive')
            if archive and self.version:
                # 使用传入的版本号生成完整的文件名
                return archive.format(version=self.version)
        return None

    def get_env(self):
        """获取指定软件的完整 'env' 属性。"""
        if self.config:
            return self.config.get(self.software, {}).get('env')
        return None


if __name__ == "__main__":
    software = input("输入需要安装的软件: ")
    version = input("输入版本号: ")
    config = Config(software=software, version=version)
    print("软件版本:", config.get_versions())
    print("下载地址:", config.get_urls())
    print("完整的软件包文件名:", config.get_archive())
