import yaml


class Config:

    def __init__(self, app=None, version=None, file="./conf.yaml") -> None:
        self.app = app
        self.version = version
        self.file = file
        self.config = self.read_yaml()

    def get_app(self):
        ''' 获取所有软件及其版本 '''
        if self.config:
            print("========================================")
            for app in self.config:
                self.app = app
                name = self.get_name()
                version = self.get_version()
                print(f"{name} 版本有：", end="")
                print(f"{', '.join(v for v in version) if version else '无版本信息'}")
                print("========================================")

    def read_yaml(self):
        ''' 读取YAML文件并返回字典 '''
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                return data
        except yaml.YAMLError as e:
            print(f"读取{self.file}文件失败：{e}")
            return None

    def get_attribute(self, attribute):
        ''' 获取指定软件的指定属性 '''
        if self.config:
            return self.config.get(self.app, {}).get(attribute)
        return None

    def get_name(self):
        ''' 获取指定软件的名称 '''
        return self.get_attribute('name')

    def get_bin(self):
        ''' 获取指定软件的安装目录 '''
        return self.get_attribute('bin')

    def get_url(self):
        ''' 获取指定软件的下载地址 '''
        urls = self.get_attribute('url')
        if self.app.lower() == 'python' and self.version:
            urls = [f"{url}{self.version}/" for url in urls]
        return urls

    def get_version(self):
        ''' 获取指定软件的版本 '''
        return self.get_attribute('version')

    def get_install(self):
        ''' 获取指定软件的依赖包 '''
        return self.get_attribute('install')

    def get_module(self):
        ''' 获取指定软件的编译参数 '''
        return self.get_attribute('module')

    def get_package(self):
        ''' 获取指定软件的压缩包后缀 '''
        return self.get_attribute('package')

    def get_archive(self):
        ''' 获取指定软件的压缩包名称 '''
        archive = self.get_attribute('archive')
        if archive and self.version:
            return archive.format(version=self.version)
        return None

    def get_env(self):
        ''' 获取指定软件的环境变量 '''
        return self.get_attribute('env')


if __name__ == "__main__":
    config = Config()
    config.get_app()

    user_input = input("请输入要安装的软件名称(格式:软件名称 版本号):")
    name, version = user_input.split()
    config = Config(app=name.lower(), version=version)
    print(config.get_name())
    print(config.get_bin())
    print(config.get_install())
    print(config.get_module())
    print(config.get_package())
    print(config.get_archive())
    print(config.get_env())
    print(config.get_version())
