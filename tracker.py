"""学习记录追踪器：负责读写 data/records.json。"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "records.json"


def save_records(records):
    """把 records（列表）写入 JSON 文件。"""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)


def load_records():
    """从 JSON 文件读取记录；文件不存在或内容损坏时返回空列表。"""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("数据文件格式错误，将使用空记录。")
        return []


def add_record(records, date, topic, minutes, category):
    """校验数据，并在 records 里新增一条记录。"""
    if not date.strip():
        raise ValueError("日期不能为空")
    if not topic.strip():
        raise ValueError("学习主题不能为空")
    if minutes <= 0:
        raise ValueError("学习时间必须大于 0")
    if not category.strip():
        raise ValueError("学习类别不能为空")

    records.append({"date": date, "topic": topic, "minutes": minutes, "category": category})
    return records


def list_records(records):
    """显示全部学习记录。"""
    if not records:
        print("暂无学习记录。")
        return

    for index, record in enumerate(records, start=1):
        print(
            f"{index}. 日期：{record['date']}，"
            f"主题：{record['topic']}，"
            f"时间：{record['minutes']} 分钟"
            f"，类别：{record['category']}"
        )


def search_records(records, keyword):
    """按主题搜索学习记录，忽略英文字母大小写。"""
    keyword = keyword.lower()
    return [
        record
        for record in records
        if keyword in record["topic"].lower()
    ]


def calculate_total_minutes(records):
    """统计所有记录的学习分钟数。"""
    return sum(record["minutes"] for record in records)

