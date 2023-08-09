import json
import os


def load_json_data(file_name: str):
    if os.path.exists(file_name) \
            and os.path.isfile(file_name) \
            and file_name.endswith('.json'):
        with open(file_name) as f:
            json_content = json.load(f)
            print(type(json_content))  # <class 'dict'>
            return json_content
    else:
        print("源文件存在问题！")


def loads_json_data(file_name: str):
    if os.path.exists(file_name) \
            and os.path.isfile(file_name) \
            and file_name.endswith('.json'):
        with open(file_name) as f:
            contents = f.read()
            json_content = json.loads(contents)
            print(type(json_content))  # <class 'dict'>
            return json_content
    else:
        print("源文件存在问题！")


def dump_json_file(file_name: str, **kwargs):
    with open(file_name, 'w') as f:
        json.dump(kwargs, fp=f)


def dumps_json_file(file_name: str, **kwargs):
    json_content = json.dumps(kwargs)
    print(type(json_content))  # <class 'str'>
    with open(file_name, 'w') as f:
        f.write(json_content)


if __name__ == "__main__":
    f_n = "../data/students.json"
    dump_json_file(f_n, name="xiaoming", age=18, no="20230001")
    load_json_data(f_n)
    f_n1 = "../data/students1.json"
    dumps_json_file(f_n1, name="xiaoming", age=18, no="20230001")
    loads_json_data(f_n1)






