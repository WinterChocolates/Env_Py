import os
import requests

# 主目录获取
home = os.environ.get('HOME')

def net_status_code(url: str) -> bool:
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return 200
        else:
            return r.status_code
    except requests.exceptions.Timeout:
        return False
    except requests.exceptions.ConnectionError:
        return False

def logo():
    print("1.安装nvm 2.卸载nvm")

def nvm():
    nvm_mirror = 'export NVM_NODEJS_ORG_MIRROR=https://npmmirror.com/mirrors/node/'
    os.system("wget -qO- https://mirror.ghproxy.com/https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | sed 's|https://raw.githubusercontent.com/|https://mirror.ghproxy.com/https://raw.githubusercontent.com/|g' | bash")
    print(net_status_code("https://nodejs.org/"))
    if net_status_code("https://nodejs.org/") != 200:
        with open(f'{home}/.bashrc', 'w', encoding='utf-8') as f:
            f.write(nvm_mirror)
    print("环境变量已添加到当前用户目录下的./bashrc. 请运行 'source ~/.bashrc' 使更改生效。")


if __name__ == "__main__":
    # result = os.popen('dnf list --installed|grep wget')
    # if 'wget' not in result.read():
    #     print('正在安装相关依赖包: wget')
    #     os.system('dnf install screenfetch -y')

    # option = int(input("选择的操作："))
    # if option == 1:
    #     nvm_dir=f'{home}/.nvm/'
    #     if os.path.exists(nvm_dir):
    #         print('已经安装过nvm了，请卸载后再试！')
    #         print("环境变量已添加到当前用户目录下的./bashrc. 请运行 'source ~/.bashrc' 使更改生效。")
    #     else:
    #         nvm()
    status = net_status_code("https://nodejs.org")
