import ccxt
import time

def main():
    # 强制指定期货实例
    exchange = ccxt.binanceusdm({
        'timeout': 15000,
        'enableRateLimit': True,
        'options': {'defaultType': 'future'} 
    })

    # 【关键纠偏】显式指定期货域名，防止其自动跳转至 api.binance.com
    exchange.urls['api']['public'] = 'https://fapi.binance.com/fapi/v1'

    print("🚀 [云端主权已锁定] 正在强制并网期货清算流...", flush=True)

    while True:
        try:
            # 使用正确的期货路径：allForceOrders
            # 不需要传 'public' 参数，直接通过底层 request 击穿
            response = exchange.request('allForceOrders', 'public', 'GET', {'limit': 50})
            
            if response:
                print(f"🔥 [脉冲] 捕获 {len(response)} 条实时爆仓信号", flush=True)
                for o in response[:3]:
                    val = float(o['origQty']) * float(o['price'])
                    print(f"   ∟ {o['symbol']} | {o['side']} |规模: ${val:,.0f}", flush=True)
            else:
                print("💎 链路正常，当前市场波动率较低...", flush=True)
                
        except Exception as e:
            # 捕获 404 的具体报错，如果改完还报 404，说明路径前缀依然被篡改
            print(f"⚠️ 链路震荡反馈: {e}", flush=True)
        
        time.sleep(3) # 保持心跳频率

if __name__ == "__main__":
    main()
