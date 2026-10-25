# Python 学习记录追踪器

这是一个用于练习 Python 基础知识的小项目。程序可以添加、查看、搜索学习记录，并统计总学习时间。

## 项目结构

```text
python-study-tracker/
├── main.py
├── tracker.py
├── class_practice.py
├── README.md
├── data/
│   └── records.json
└── tests/
    └── test_tracker.py
```


## 文件说明

- `main.py`：显示循环菜单并处理用户输入。
- `tracker.py`：读写、添加、搜索和统计学习记录。
- `class_practice.py`：包含 `Student` 类的基础练习。
- `data/records.json`：保存学习记录。
- `tests/test_tracker.py`：包含 tracker 功能的自动化测试。

## 运行程序

在项目根目录执行：

```powershell
python main.py
```

菜单包含以下功能：

1. 添加学习记录
2. 查看全部记录
3. 搜索学习记录
4. 统计学习时间
0. 退出

## 运行测试

```powershell
python -m pytest -v
```

正常情况下应看到：

```text
5 passed
```

测试使用各自创建的列表，不会读取或修改正式的 `data/records.json`。

## 我学到的知识

- 使用 `try/except` 捕获并处理不同类型的异常。
- 使用 `raise ValueError` 主动拒绝不符合规则的数据。
- 使用 `json.load()` 和 `json.dump()` 读取、保存 JSON 数据。
- 使用类、属性和方法创建简单的 `Student` 对象。
- 使用 `while True` 和条件判断创建循环菜单。
- 使用函数拆分添加、查看、搜索和统计功能。
- 使用 pytest、`assert` 和 `pytest.raises()` 编写自动化测试。
- 使用 `.gitignore` 忽略可以自动生成的缓存文件。

## 后续改进

- 校验日期是否符合 `YYYY-MM-DD` 格式。
- 增加修改学习记录的功能。
- 增加删除学习记录的功能。
- 为文件读取、记录显示等功能补充更多测试。
- 在数据文件损坏时保留备份，避免原有数据丢失。
