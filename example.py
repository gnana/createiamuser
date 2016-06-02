import yaml


def main():
    file = 'roles.yml'

    try:
        with open(file, 'r') as f:
            roles = yaml.load(f)
    except BaseException, e:
        print str(e)
    groups = roles['developer']
    for group in groups:
        print group

if __name__ == "__main__":
    main()
