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
        # 逻辑映射：CCXT 内部会根据 'public' 自动定位到 market 类别
        # 因此端点只需写最后一段，避免路径叠加导致的 404
        endpoint = 'liquidation-orders' 
        params = {
            'instType': 'SWAP',
            'limit': 5
        }
        
        # 显式锁定：使用封装好的 market 公开接口请求
        response = exchange.publicGetMarketLiquidationOrders(params)
        
        data = response.get('data', [])
        if data:
            print(f"✅ 链路接通 | 捕获到 {len(data)} 条最新清算订单", flush=True)
            o = data[0]
            print(f"🚩 实时: {o['instId']} | 价格: {o['bkPx']} | 数量: {o['sz']}", flush=True)
        else:
            print("🌑 链路接通 | 此时段无大规模清算", flush=True)

    except Exception as e:
        # 如果这种写法依然被 Render 里的旧库报 AttributeError，
        # 则使用下面的万能底层命令（注意路径：去掉了开头的 market/）
        try:
            endpoint_fallback = 'liquidation-orders'
            res = exchange.request(endpoint_fallback, 'public', 'GET', params)
            print(f"✅ 万能链路接通 | 数据量: {len(res.get('data', []))}", flush=True)
        except Exception as e2:
            print(f"⚠️ 协议深度波动: {str(e2)}", flush=True)

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

