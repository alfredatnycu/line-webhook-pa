# LINE Bot Webhook Server

這是一個使用 Flask 框架開發的 LINE Bot 應用程式。

## 功能

- 處理 LINE webhook 驗證
- 回覆用戶訊息
- 獲取用戶個人資料
- 支援文字、圖片和檔案訊息處理
- 識別訊息來源（用戶、群組或聊天室）

## 安裝與設置

1. 安裝依賴套件：

```bash
pip install -r requirements.txt
```

2. 創建 `.env` 文件並設置以下環境變數：

```
LINE_CHANNEL_ACCESS_TOKEN=你的LINE頻道訪問令牌
LINE_CHANNEL_SECRET=你的LINE頻道密鑰
```

3. 運行應用程式：

```bash
python app.py
```

## 使用說明

1. 啟動應用程式後，服務將在本地端口 5000 運行
2. 使用 ngrok 或其他工具將本地服務暴露到公網（例如：`ngrok http 5000`）
3. 將生成的 webhook URL 設置到 LINE Developers 控制台中
4. 開始與您的 LINE Bot 互動

## 注意事項

- 如果端口 5000 被 macOS AirPlay Receiver 佔用，可以在 app.py 中修改端口號
- 確保 LINE Developers 控制台中的 Webhook URL 設置正確
