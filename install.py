import os
import tarfile
import requests
from read_yaml import Config

download_dir = os.path.expanduser("~/downloads")
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

software = input("输入需要安装的软件: ")
version = input("输入版本号: ")
config = Config(software=software, version=version)
# 名称
base_name = config.get_name()
# 安装目录
base_bin = config.get_bin()
# 下载地址列表
base_urls = config.get_urls()
# 版本列表
base_versions = config.get_versions()
# 软件包
base_install = config.get_install()
# 模块
base_module = config.get_module()
# 软件包后缀
base_package = config.get_package()
# 压缩包
base_archive = config.get_archive()
# 文件名
base_file = base_archive.replace(f".tar.{base_package}", "")
print(base_file)
# 环境变量
base_env = config.get_env()


def download(urls: list, archive: str):
    """ 压缩包下载 """
    for base_url in urls:
        url = f"{base_url}{archive}"
        file = os.path.join(download_dir, f"{archive}")
        print(f"正在尝试从 {url} 下载")
        print(f"到 {file} 中...", end="\n")
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            with open(file, 'wb') as f:
                f.write(response.content)
            print(f"Nginx {version}下载完成。保存到{file}", end="\n")
            return file
        else:
            print(f"从{url}(HTTP{response.status_code})下载失败...")
            print("正在尝试下一个URL...", end="\n")

    raise Exception(f"从所有提供的url下载Nginx {version}失败。", end="\n")


def decompression(package: str):
    """ 压缩包解压 """
    file = download(base_urls, base_archive)
    print(f"解压{file}...")
    with tarfile.open(file, f'r:{package}') as tar:
        tar.extractall(path=download_dir)
    print(f"{base_name} {version} 解压完成.", end="\n")


def library(install: str):
    """ 开发工具与组件包安装 """
    print("安装开发工具包中...")
    os.system('dnf group install "Development Tools" -y')
    print("开发工具包安装完成.", end="\n")

    print(f"安装{base_name}必要库中...")
    os.system(f"dnf install {install}")
    print("必要库安装完成.", end="\n")


def setup(name: str, file: str, module: str):
    source_dir = os.path.join(download_dir, file)
    os.chdir(source_dir)
    print(f"在{os.getcwd()}中配置{name} {version}...")
    os.system(f"./configure --prefix={module}")

    print(f"编译{name} {version} ...")
    os.system("make")

    print(f"安装{name} {version} ...")
    os.system("make install")

    os.chdir("..")


def config_env(name: str, env: str):
    '''
        /usr/local/nginx/sbin
        PATH=/usr/local/nginx/sbin:$PATH
    '''
    profile_file = f"/etc/profile.d/{name}.sh"
    try:
        with open(profile_file, 'w', encoding='utf-8') as f:
            f.write(env)
        print(f"{name} 环境变量已写入 {profile_file}")
        print("请使用 source /etc/profile 让环境变量生效。")

    except Exception as e:
        print(f"写入 {profile_file} 失败：{e}")


def main():
    try:
        # 安装必要库
        library(base_install)

        # 解压软件包
        decompression(base_package)

        # 编译和安装
        setup(base_name, base_file, base_bin)

        # 配置环境变量
        config_env(base_name, base_env)

        print(f"{base_name} {version} 安装和配置完成。")

    except Exception as e:
        print(f"安装和配置 {base_name} {version} 失败：{e}")


if __name__ == "__main__":
    main()
