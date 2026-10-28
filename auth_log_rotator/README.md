# Auth Log Rotator 

Auth Log Rotator is a Python script that checks a log file to see if it is 1 Megabyte. If the file is larger or equal to 1 megabyte, then it will get copied to a file named "file".old, and clear the file out and say log rotated.

Repo Structure:

```
├── auth_log_rotator.py
└── README.md
```