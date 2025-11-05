# Log Analysis Automation Report

**Author:** Md Islam  
**Date:** Nov 5, 2025  
**Environment:** Kali Linux  
**Tool:** Python 3 + Pandas

---

## 1. Objective
To detect failed login attempts (HTTP 401 errors) from a set of web access logs using automation.

---

## 2. Methodology
- Read access log file in CSV format.
- Filter log entries with status code `401`.
- Save those entries in `failed_logins.csv`.

Command used:
```bash
python scripts/parse_logs.py
