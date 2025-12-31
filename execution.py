import ccxt
import time

def main():
    # 逻辑锁定：初始化实例
    exchange = ccxt.binanceusdm({
        'timeout': 20000,
        'enableRateLimit': True
    })

    # 物理锁定：强制定义基础域名
    # 注意：后面不带 /fapi/v1，由 request 方法自动补全
    exchange.urls['api']['public'] = 'https://fapi.binance.com'

    print("🚀 [主权接管] 链路已重组。目标：期货强平流", flush=True)

    while True:
        try:
            # 暴力穿透：直接调用 /fapi/v1/allForceOrders
            # 这是最稳健的写法，避开了所有 AttributeError 风险
            params = {'limit': 50}
            response = exchange.fapiPublicGetAllForceOrders(params)
            
            if response:
                print(f"🔥 [爆仓信号] 捕获 {len(response)} 条数据", flush=True)
                for o in response[:3]:
                    val = float(o['origQty']) * float(o['price'])
                    print(f"   ∟ {o['symbol']} | {o['side']} | 价值: ${val:,.0f}", flush=True)
            else:
                print("💎 链路正常，当前市场平静...", flush=True)
                
        except Exception as e:
            # 捕获异常，输出真实路径信息
            print(f"⚠️ 链路反馈: {e}", flush=True)
        
        time.sleep(3)

if __name__ == "__main__":
    main()
