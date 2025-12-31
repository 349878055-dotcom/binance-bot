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
        # --- 2. 路径重塑：精确锁定 OE V5 官方端点 ---
        # 修正：去掉了导致 404 的 'platform-'
        endpoint = 'market/liquidation-orders'
        params = {
            'instType': 'SWAP', # 锁定永续合约
            'limit': 10         # 限制返回条数，降噪
        }
        
        # 使用 request 底层通用方法，彻底无视 CCXT 版本代差
        response = exchange.request(endpoint, 'public', 'GET', params)
        
        data = response.get('data', [])
        if data:
            # 逻辑映射：实时数据反馈
            print(f"✅ 链路全通 | 捕获到 {len(data)} 条最新清算记录", flush=True)
            for order in data[:3]: # 打印前三条精简信息
                print(f"🚩 实时清算: {order['instId']} | 价格: {order['bkPx']} | 数量: {order['sz']}", flush=True)
        else:
            print("🌑 链路全通 | 市场平静，无大规模清算", flush=True)

    except Exception as e:
        # 捕获 404/401 等协议层面波动
        print(f"⚠️ 协议波动: {str(e)}", flush=True)

def main():
    # 捅破缓冲区：实时输出
    print("🚀 系统入位，逻辑全线接通，开始监控市场脉动...", flush=True)
    while True:
        try:
            fetch_data()
            # 锁定频率：15秒一次，防止触发限频
            time.sleep(15) 
        except Exception as e:
            print(f"🔥 系统溢出: {e}", flush=True)
            time.sleep(30)

if __name__ == "__main__":
    main()
