import shutil

def copy_yaml():
    shutil.copy("src/validations.yaml", "src/python/regtech_regex")

if __name__ == "__main__":
    copy_yaml()