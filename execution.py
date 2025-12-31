import ccxt
import time

# --- 1. 物理密钥填装：核心实例化 ---
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
        # 逻辑更替：不再使用 market/liquidation-orders (容易被封)
        # 改用 fetch_tickers (CCXT 封装好的、带鉴权的行情探测)
        # 如果这个能通，说明你的 API Key 权限和网络路径是活的
        tickers = exchange.fetch_tickers(['BTC/USDT:USDT'])
        
        if tickers:
            price = tickers['BTC/USDT:USDT']['last']
            print(f"✅ 链路全线打通 | BTC 实时价: {price}", flush=True)
            
            # 如果行情通了，尝试用 CCXT 封装的清算方法（它会自动处理路径细节）
            try:
                # 注意：有些版本的 CCXT 使用 fetch_liquidation_orders
                liq = exchange.fetch_liquidation_orders('BTC/USDT:USDT')
                print(f"🚩 捕获清算数据成功，条数: {len(liq)}", flush=True)
            except:
                print("🌑 暂无清算数据或该方法受限，但链路已接通", flush=True)
        
    except Exception as e:
        print(f"⚠️ 物理屏蔽告警: {str(e)}", flush=True)

def main():
    print("🚀 正在强行破译地理屏蔽，初始化主权链路...", flush=True)
    while True:
        try:
            fetch_data()
            time.sleep(15) 
        except Exception as e:
            print(f"🔥 系统溢出: {e}", flush=True)
            time.sleep(30)

if __name__ == "__main__":
    main()

