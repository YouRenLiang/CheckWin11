Windows 11 Compatibility Check 工具使用說明

📌 功能概述
本工具用於快速檢查電腦是否符合 Windows 11 安裝需求，並彈出結果視窗。
它會檢測以下條件：

CPU 型號（僅顯示，不做判斷）

記憶體 ≥ 4 GB

系統碟容量 ≥ 64 GB

TPM 版本 ≥ 2.0

Secure Boot 是否啟用

若條件符合，會顯示電腦名稱與 CPU 型號，並提示符合需求。

📂 檔案結構

將以下檔案放在同一資料夾：

Win11Check.py（主程式）

（可選）編譯後的 Win11Check.exe

⚙️ 使用方式

方式 1：直接用 Python 執行

安裝必要套件：

pip install psutil wmi pywin32


執行程式：

python Win11Check.py

方式 2：打包成 EXE 執行檔

使用 PyInstaller 打包：

pyinstaller --onefile --noconsole Win11Check.py


生成的 Win11Check.exe 可在無 Python 環境的電腦上執行。

📑 結果範例

若符合需求：

This computer DESKTOP-123456
CPU: Intel(R) Core(TM) i7-8650U CPU @ 1.90GHz
other conditions meets Windows 11 requirements.


若不符合需求：

This computer DESKTOP-123456 does not meet Windows 11 requirements.


⚠️ 注意事項

必須以 Windows 系統管理員 身分執行，否則部分檢查（TPM、Secure Boot）可能失敗。

本工具僅做基礎條件檢查，不會檢查 CPU 是否在 Microsoft 官方支援清單。

若要更完整的檢查，建議搭配 Microsoft 官方工具 PC Health Check。
