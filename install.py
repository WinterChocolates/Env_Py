import os
import shutil
import tarfile
import requests
from read import Config

download_dir = os.path.expanduser("~/downloads")
if os.path.exists(download_dir):  # 如果目录存在
    shutil.rmtree(download_dir)  # 删除目录及其内容
os.makedirs(download_dir)  # 重新生成目录


# 下载软件
def download(config: Config):
    ''' 下载软件 '''
    base_urls = config.get_urls()
    archive = config.get_archive()
    for u in base_urls:
        url = f"{u}{archive}"
        file = os.path.join(download_dir, f"{archive}")
        print(f"正在尝试从 {url} 下载")
        print(f"到 {file} 中...", end="\n")
        res = requests.get(url, timeout=5)

        if res.status_code == 200:
            with open(file, 'wb') as f:
                f.write(res.content)
            print(f"{config.app} {config.version}下载完成。保存到{file}", end="\n")
            return file
        else:
            print(f"从 {url} (HTTP{res.status_code}) 下载失败...")
            print("正在尝试下一个URL...", end="\n")

    raise Exception(f"从所有提供的url下载{config.app} {config.version}失败。", end="\n")


# 解压软件
def decompression(config: Config):
    ''' 解压软件 '''
    file = download(config)
    print(f"解压{file}...")
    with tarfile.open(file, f'r:{config.get_package()}') as tar:
        tar.extractall(path=download_dir)
    print(f"{config.app} {config.version} 解压完成.", end="\n")


# 移动目录
def move_dir(config: Config, source_dir: str = "/usr/local"):
    ''' 移动目录 '''
    dir = os.path.join(download_dir, os.path.basename(config.get_dir()))
    if os.path.exists(dir):
        shutil.rmtree(dir)
    shutil.move(dir, source_dir)
    print(f"{config.app} {config.version} 移动到 {source_dir} 完成.", end="\n")


# 编译软件
def compile(config: Config):
    ''' 编译软件 '''
    source_dir = os.path.join(download_dir, config.get_dir())
    os.chdir(source_dir)
    print(f"在{os.getcwd()}中配置{config.app} {config.version}...")
    os.system(f"./configure --prefix={config.get_bin()} {config.get_module()}")

    print(f"编译{config.app} {config.version} ...")
    os.system("make")


# 开发工具与必要软件安装
def library(config: Config):
    ''' # 开发工具与必要软件安装 '''
    print("安装开发工具包中...")
    os.system('dnf group install "Development Tools" -y')
    print("开发工具包安装完成.", end="\n")

    print(f"安装{config.get_library()}必要库中...")
    os.system(f"dnf install {config.get_library()} -y")
    print("必要库安装完成.", end="\n")


# 编写配置文件
def config_env(config: Config):
    ''' 编写配置文件 '''
    profile_file = f"/etc/profile.d/{config.app}.sh"
    with open(profile_file, 'w', encoding='utf-8') as f:
        for e in config.get_env():
            f.write(f"export {e}\n")
    print(f"{config.app} 环境变量已写入 {profile_file}")
    print("请使用 source /etc/profile 让环境变量生效。")


def main():
    # 获取用户输入软件名称和版本号
    config = Config()
    config.get_app()
    user_input = input("请输入要安装的软件名称(格式:软件名称 版本号):")
    name, version = user_input.split()
    config = Config(app=name.lower(), version=version)
    print(config.app, config.version)

    try:
        # 开发工具与必要软件安装
        library(config)

        # 解压软件包
        decompression(config)

        if config.app == "go":
            print('执行')
            print(config.app, config.version)
            # 移动目录
            move_dir(config)
        elif config.app == "python" or config.app == "nginx":
            print('执行')
            print(config.app, config.version)
            # 编译软件
            compile(config)

        # 编写配置文件
        config_env(config)

    except Exception as e:
        print(f"安装和配置 {name} {version} 失败：{e}")


if __name__ == "__main__":
    main()
