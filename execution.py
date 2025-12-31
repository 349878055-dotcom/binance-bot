import ccxt
import time

def main():
    # 逻辑初始化
    exchange = ccxt.binanceusdm({
        'timeout': 15000,
        'enableRateLimit': True
    })

    # 【核心修正】强制覆盖所有路径变量。注意：末尾绝对不带斜杠，也不带 /fapi/v1
    exchange.urls['api']['fapiPublic'] = 'https://fapi.binance.com'
    exchange.urls['api']['public'] = 'https://fapi.binance.com'

    print("🚀 [物理接管] 正在执行路径归一化，开始监听...", flush=True)

    while True:
        try:
            # 放弃所有 ccxt 自带的驼峰命名方法（防止 AttributeError）
            # 直接使用最原始的 request，手动写全路径后缀
            response = exchange.request('fapi/v1/allForceOrders', 'public', 'GET', {'limit': 50})
            
            if response and isinstance(response, list):
                ts = time.strftime('%H:%M:%S', time.localtime())
                print(f"🔥 [{ts}] 捕获信号: {len(response)} 条", flush=True)
                for o in response[:2]:
                    val = float(o['origQty']) * float(o['price'])
                    print(f"   ∟ {o['symbol']} | {o['side']} | ${val:,.0f}", flush=True)
            else:
                print("💎 链路正常，等待市场脉冲...", flush=True)
                
        except Exception as e:
            # 如果依然报错，这个输出会显示币安返回的真实原因
            print(f"⚠️ 物理反馈: {e}", flush=True)
        
        time.sleep(3)

if __name__ == "__main__":
    main()
