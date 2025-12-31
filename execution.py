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
    # 逻辑映射：通过 global 关键字接管外部变量权限
    global exchange 
    try:
        params = {'instType': 'SWAP'}
        # 显式 V5 端点调用
        response = exchange.publicGetMarketPlatformLiquidationOrders(params)
        
        data = response.get('data', [])
        if data:
            print(f"✅ 链路正常 | 捕获到 {len(data)} 条最新清算订单", flush=True)
            for order in data[:3]: # 只打印前3条，降噪
                print(f"🚩 预警: {order['instId']} | 价格: {order['bkPx']}", flush=True)
        else:
            print("🌑 链路正常 | 此时段无大规模清算", flush=True)

    except Exception as e:
        print(f"⚠️ 链路波动: {str(e)}", flush=True)

def main():
    # 强行刷新缓冲区：手动捅破静默
    print("🚀 系统入位，主权接管开始...", flush=True)
    while True:
        try:
            fetch_data()
            time.sleep(15) 
        except Exception as e:
            print(f"🔥 系统溢出: {e}", flush=True)
            time.sleep(30)

if __name__ == "__main__":
    main()

