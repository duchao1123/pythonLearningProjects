# python项目结构介绍

## 目录结构的重要性
- 开发过程中的良好目录结构，可以让开发者更加方便、快速地定位相应代码文件。
- 同时也有利于开发多人协作，方便代码的维护和更新。
- 通过清晰合理的目录结构，能够很好地组织代码文件，让代码更加易于管理和维护，提高代码可读性和可维护性。

## 标准Python目录结构

├── LICENSE                 包含软件许可证文件
├── README.rst              包含项目的说明文档
├── setup.py                用于打包和安装Python模块的脚本文件
├── requirements.txt        包含依赖的外部库文件
├── docs                    包含文档文件。
│   ├── conf.py
│   ├── generated
│   ├── index.rst
│   ├── make.bat
│   └── Makefile
├── mypkg                   包含Python模块文件。
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── config                  用于存储配置信息的文件
│   ├── __init__.py
│   ├── dev.cfg
│   ├── prod.cfg
│   └── test.cfg
├── data                    算法或机器学习应用程序中，通常需要存储数据
│   ├── __init__.py
│   ├── processed
│   │   ├── __init__.py
│   │   ├── data1.csv
│   │   └── data2.csv
│   └── raw
│       ├── __init__.py
│       ├── data1_raw.csv
│       └── data2_raw.csv
├── tools                   将项目中的所有工具和帮助程序存储在tools目录
│    ├── __init__.py
│    ├── build.sh
│    ├── deploy.sh
│    └── python
│        ├── __init__.py
│        ├── tool1.py
│        └── tool2.py
├── tests                   包含单元测试文件
│   ├── __init__.py
│   ├── test_module1.py
│   └── test_module2.py 
└── examples                包含示例代码文件。
    ├── helloworld.py
    └── README.txt