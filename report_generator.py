# report_generator.py
import json
from datetime import datetime

def generate_daily_report(data, output_path="daily_report.json"):
    """
    日報データをJSONとして保存する関数
    """
    report = {
        "timestamp": datetime.now().isoformat(),
        "data": data
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(f"✅ 日報を {output_path} に出力しました。")

if __name__ == "__main__":
    # 仮のデータ
    sample_data = {
        "tasks": ["A対応", "B修正"],
        "notes": "今日は会議が多かった"
    }
    generate_daily_report(sample_data)
