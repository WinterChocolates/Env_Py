import os
import requests
import tarfile

base_Urls = [
    "https://mirrors.huaweicloud.com/nginx/",
    "http://nginx.org/download/"
]

NGINX_VERSION = "1.24.0"

download_Dir = os.path.expanduser("~/downloads")
if not os.path.exists(download_Dir):
    os.makedirs(download_Dir)


def download_nginx(base_urls: list, nginx_version: str, download_dir: str):
    for base_url in base_urls:
        nginx_url = f"{base_url}nginx-{nginx_version}.tar.gz"
        source_file = os.path.join(
            download_dir, f"nginx-{nginx_version}.tar.gz")

        print(f"""
        正在尝试从 {nginx_url} 
        下载{source_file}中...
        """)
        print("")
        response = requests.get(nginx_url, timeout=5)

        if response.status_code == 200:
            with open(source_file, 'wb') as file:
                file.write(response.content)
            print(f"Nginx {nginx_version}下载完成。保存到{source_file}")
            return source_file
        else:
            print(f"""
            从{nginx_url}(HTTP{response.status_code})下载失败...
            正在尝试下一个URL...
            """)
    raise Exception(f"从所有提供的url下载Nginx {nginx_version}失败。")


def disposition_nginx():
    try:
        source_file = download_nginx(base_Urls, NGINX_VERSION, download_Dir)
        print(f"解压{source_file}...")
        with tarfile.open(source_file, 'r:gz') as tar:
            tar.extractall()
        print(f"Nginx{NGINX_VERSION}解压完成.")

        print("安装开发工具包中...")
        os.system('dnf group install "Development Tools"')
        print("开发工具包安装完成.")

        print("安装Nginx必要库中...")
        os.system("dnf install openssl openssl-devel pcre pcre-devel zlib zlib-devel")
        print("必要库安装完成.")

        source_dir = f"nginx-{NGINX_VERSION}"
        os.chdir(source_dir)
        print(f"在{os.getcwd()}中配置Nginx {NGINX_VERSION}...")
        os.system("./configure --prefix=/usr/local/nginx --with-http_ssl_module --with-http_gzip_static_module --with-http_rewrite_module --with-http_stub_status_module --with-pcre")

        print(f"编译Nginx {NGINX_VERSION}")
        os.system("make")

        print(f"安装Nginx {NGINX_VERSION}")
        os.system("make install")
        os.chdir("..")
    except Exception as e:
        return e
    
    print(f"完成Nginx {NGINX_VERSION}的安装.")

if __name__ == "__main__":
    disposition_nginx()