import atexit
import platform
import os
import zipfile, io


# 创建默认配置
def create_config():
    if not os.path.exists("head/config.py"):
        print("[INFO]\tCannot Find the config.py,create the default config file.")
        zip_file = b'PK\x03\x04\x14\x00\x02\x00\x08\x00\x0b\x8bEVTo\x07$X\x01\x00\x00\xd0\x01\x00\x00\t\x00\x00\x00config.py+\xc8/*Q\xb0U\xf0\xcb\xcfK\xe5\xe5rqu\nu\x07\xf2\xdc\x12s\x8a\x81\xdc\xd2\xa2\x1c G)\xa3\xa4\xa4\xc0J_\xdf\xd0\xc8\\\xcf\x00\x08\r\xad,\x0c,\x0c\xf4\x8bR\x13SR\x8b\x8c\xf5\x95x\xb9x\xb9\x1cCC\xfc\xe3\x9d\x1c\x9d\xbdC\x03`\xda\x15\x14\x94\x15^\xb4\xafz\xda\xb5\xe2\xe9\x92\xf6\'\xbb\xf7>\xed\xd8\xe0\xee\x19\x82\xa24>\xc4\xd3\xd7\x15\xa8\xde\xd8\xcc\xc0\x00]\xf9\xcb\xe9[^\xce\x9a\xf2l\xfa6 \x83\x97\xcb\xd9\xc7\xdf\xcf5\xde\xd7\xdf\xc5\x15\xd9\xf8\xa7\x1ds\x9f\xadY\xf8t\xc2z\xa0\xaeg\x8d\x8b\x9e.\xe9}\xb2\xa3\x0b$\x026\x81\x97+=\xb3$\xa34)>/17\x15\xe4\x0fw\x087\xb48\xb5\x08$\xa4\x04WP\x94Z\x90\x8f\xa4\x00\xc4\x8dGUQ\x92\x9f\x9d\x9a\x87\xa4$\x04\xc4\x8fwt\rV\x02\xbb{\xdd\xfe\x97\xd3\xd7\xe9\'\xa6\x16\xeb\xdb k\xb0{\xd1\xb7\xfdi\xff4\xa0\x9f]\x83\xe3\xbd]#A\x06\x18\x1a\x19\x9b\x98\x9a\x99[X\x1a\x80\xb5\x02e\x9e\xaeo{9i)(\x14\x95\x15\x9eo\xde\xfd|\xf7\xfc\xe7}\xeb\x9f.j~\xda?\xe3e{?/WR\x11P\x9f\xbaMJf\x99BrNbq\xb1\xadRy\x92\x92\x9d\x8d>P\xc0N\x9d\x97\x0b\x14\x0f\xf1\xb9\xf9) /\x1a\xf0r\x01\x00PK\x01\x02\x14\x00\x14\x00\x02\x00\x08\x00\x0b\x8bEVTo\x07$X\x01\x00\x00\xd0\x01\x00\x00\t\x00$\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00config.py\n\x00 \x00\x00\x00\x00\x00\x01\x00\x18\x00\xaa\x1b\xd5\xa0C9\xd9\x01\x8cdJ\x14D9\xd9\x01\xac4\x17"\xae8\xd9\x01PK\x05\x06\x00\x00\x00\x00\x01\x00\x01\x00[\x00\x00\x00\x7f\x01\x00\x00\x00\x00'
        zip_file = io.BytesIO(zip_file)
        with zipfile.ZipFile(zip_file, 'r') as f:
            for file in f.namelist():
                f.extract(file, "./head/")
            f.close()

def print_info():
    print("[INFO] --- PRINT ---")
    print("\tKindle-Reader-Web-Client Start!")
    print("""
          .-')                .-') _                
         ( OO ).             (  OO) )               
        (_)---\_) ,--. ,--.  /     '._  .-'),-----. 
        /    _ |  |  | |  |  |'--...__)( OO'  .-.  '
        \  :` `.  |  | | .-')'--.  .--'/   |  | |  |
         '..`''.) |  |_|( OO )  |  |   \_) |  |\|  |
        .-._)   \ |  | | `-' /  |  |     \ |  | |  |
        \       /('  '-'(_.-'   |  |      `'  '-'  '
         `-----'   `-----'      `--'        `-----' 
    """)
    print("\tGithub: https://github.com/Suto-Commune/Kindle-Reader-Web-CLI/")
    print("\tAuthor LolingNatsumi,hsn8086,GooGuJiang\n\tThe Dockerfile By DDSRem")
    print(
        f"\t * Kindle Web: http://127.0.0.1:5000 or http://127.0.0.1:1000\n\t * Reader Web: http://127.0.0.1:8080 or http://127.0.0.1:1000/reader")
    print("\tPress Ctrl+C to exit.")
    print("[INFO] --- PRINT END---")

if __name__ == "__main__":
    print_info()
    # 引用
    create_config()
    from head.func import start, exit_do, ban_windows_window_close_button

    # 注册退出函数
    atexit.register(exit_do)

    # 禁用窗口关闭按钮
    if platform.system() == "Windows":
        try:
            ban_windows_window_close_button()
        except:
            try:
                os.system("pip install pywin32")
                ban_windows_window_close_button()
            except:
                ...
    start()
