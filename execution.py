import ccxt
import time

# --- 物理密钥填装：这是你的银行卡和密码 ---
keys = {
    'apiKey': '26a747cf-7bc6-4a73-be7d-52dc56dc8106',
    'secret': 'E897F21E2C4001F8E35B51FF2AB46541',
    'password': 'Jintao0341$',
    'enableRateLimit': True,
    'options': {'defaultType': 'swap'}
}
exchange = ccxt.okx(keys)

def fetch_data():
    global exchange 
    try:
        # 3. 核心重塑：使用通用请求（硬连接）
        # 这是万能钥匙，不吃 CCXT 的版本更新，直接对接 OE 的 V5 接口
        endpoint = 'market/platform-liquidation-orders'
        params = {'instType': 'SWAP'}
        
        # 这种写法在任何 CCXT 版本中都绝对有效
        response = exchange.request(endpoint, 'public', 'GET', params)
        
        data = response.get('data', [])
        if data:
            print(f"✅ 链路接通 | 捕获到 {len(data)} 条清算订单", flush=True)
        else:
            print("🌑 链路接通 | 市场平静，无大规模清算", flush=True)

    except Exception as e:
        print(f"⚠️ 协议波动: {str(e)}", flush=True)

def main():
    print("🚀 系统入位，逻辑全线接通...", flush=True)
    while True:
        try:
            fetch_data()
            time.sleep(15) 
        except Exception as e:
            print(f"🔥 系统溢出: {e}", flush=True)
            time.sleep(30)

if __name__ == "__main__":
    main()

