#!/usr/bin/env python3
"""
parse_logs.py
A simple Python script to detect failed login attempts from web access logs.
This simulates basic SIEM-like detection in a lab environment.
"""

import pandas as pd
import os

INPUT = "../sample_logs/access_logs.csv"
OUTPUT_DIR = "../output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def parse_access_log(path):
    # Load sample CSV (columns: ip,timestamp,method,path,status,user_agent)
    df = pd.read_csv(path)
    failed = df[df['status'] == 401]   # Filter failed login attempts (401 Unauthorized)
    out_path = os.path.join(OUTPUT_DIR, "failed_logins.csv")
    failed.to_csv(out_path, index=False)
    print(f"[+] Found {len(failed)} failed login attempts.")
    print(f"[+] Results saved to {out_path}")

if __name__ == "__main__":
    if not os.path.exists(INPUT):
        print(f"[!] Log file not found: {INPUT}")
    else:
        parse_access_log(INPUT)
