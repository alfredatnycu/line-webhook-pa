# LINE Bot Webhook Server

這是一個使用 Flask 框架開發的 LINE Bot 應用程式，整合了 ngrok 來創建公開 URL。

## 功能

- 自動使用 ngrok 創建公開 URL
- 處理 LINE webhook 驗證
- 回覆用戶訊息
- 獲取用戶個人資料
- 提供簡單的幫助訊息系統

## 安裝與設置

1. 安裝依賴套件：

```bash
pip install -r requirements.txt
```

2. 創建 `.env` 文件並設置以下環境變數：

```
LINE_CHANNEL_ACCESS_TOKEN=你的LINE頻道訪問令牌
LINE_CHANNEL_SECRET=你的LINE頻道密鑰
PORT=8080
```

3. 運行應用程式：

```bash
python app.py
```

## 使用說明

1. 啟動應用程式後，會自動使用 ngrok 創建公開 URL
2. 將生成的 webhook URL 設置到 LINE Developers 控制台中
3. 開始與您的 LINE Bot 互動

## 注意事項

- 使用 PORT 8080 避免與 macOS AirPlay Receiver 衝突
- 確保已安裝 ngrok 並可在命令行中使用
