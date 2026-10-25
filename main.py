"""学习记录追踪器的菜单入口。"""

from tracker import (
    add_record,
    calculate_total_minutes,
    list_records,
    load_records,
    save_records,
    search_records,
)


def add_record_from_input(records):
    """读取用户输入，添加记录并立即保存。"""
    date = input("请输入学习日期：")
    topic = input("请输入学习主题：")
    minutes_text = input("请输入学习分钟数：")

    try:
        minutes = int(minutes_text)
    except ValueError:
        print("学习时间必须是整数。")
        return

    try:
        add_record(records, date, topic, minutes)
    except ValueError as error:
        print("添加失败：", error)
        return

    save_records(records)
    print("学习记录添加成功。")


def main():
    records = load_records()

    while True:
        print("\n===== 学习记录菜单 =====")
        print("1. 添加学习记录")
        print("2. 查看全部记录")
        print("3. 搜索学习记录")
        print("4. 统计学习时间")
        print("0. 退出")

        choice = input("请选择：")

        if choice == "1":
            add_record_from_input(records)
        elif choice == "2":
            list_records(records)
        elif choice == "3":
            keyword = input("请输入要搜索的学习主题：")
            results = search_records(records, keyword)
            list_records(results)
        elif choice == "4":
            total = calculate_total_minutes(records)
            print(f"总学习时间：{total} 分钟")
        elif choice == "0":
            print("已退出学习记录追踪器。")
            break
        else:
            print("无效选项，请输入 0 到 4。")


if __name__ == "__main__":
    main()
