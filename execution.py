import ccxt
import time
import sys

def main():
    # 付费档享受独享带宽，无需任何代理，直连官方节点
    exchange = ccxt.binanceusdm({
        'timeout': 15000,
        'enableRateLimit': True,
        'options': {'defaultType': 'future'}
    })

    print("🚀 [云端主权接管] 付费通道已建立，开始高频监听...", flush=True)

    while True:
        try:
            # 获取实时清算（黄线）
            orders = exchange.request('allForceOrders', 'public', 'GET', {'limit': 50})
            
            if orders:
                ts = time.strftime('%H:%M:%S', time.localtime())
                print(f"🔥 [{ts}] 实时溢出：{len(orders)} 条强平", flush=True)
                for o in orders[:5]:
                    val = float(o['origQty']) * float(o['price'])
                    print(f"   ∟ {o['symbol']} | {o['side']} | ${val:,.0f}", flush=True)
            
        except Exception as e:
            # 即使有暂时的网络波动，循环也会自动重启
            print(f"⚠️ 链路震荡反馈: {e}", flush=True)
        
        time.sleep(2) # 付费档可以尝试更短的间隔，如 1-2 秒

if __name__ == "__main__":
    main()
