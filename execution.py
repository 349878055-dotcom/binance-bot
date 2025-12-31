import ccxt
import time

def main():
    # 逻辑归零：不依赖 CCXT 的自动寻址，手动强插接口
    exchange = ccxt.binanceusdm({
        'timeout': 15000,
        'enableRateLimit': True
    })

    # 暴力修正：彻底覆盖 CCXT 的所有寻址逻辑，强制指向期货端点
    exchange.urls['api']['fapiPublic'] = 'https://fapi.binance.com/fapi/v1'
    exchange.urls['api']['public'] = 'https://fapi.binance.com/fapi/v1'

    print("🚀 [绝对主权锁定] 目标：fapi.binance.com", flush=True)

    while True:
        try:
            # 使用更底层的 fapiPublicGetAllForceOrders 
            # 这样 ccxt 会强制去匹配 fapi 前缀
            response = exchange.fapiPublic_get_allforceorders({'limit': 50})
            
            if response:
                print(f"🔥 捕获信号: {len(response)} 条", flush=True)
                for o in response[:2]:
                    print(f"   ∟ {o['symbol']} | ${float(o['origQty'])*float(o['price']):,.0f}", flush=True)
            else:
                print("💎 链路正常，无溢出数据...", flush=True)
                
        except Exception as e:
            # 这里的报错如果还包含 api.binance.com，说明你代码压根没改成功
            print(f"⚠️ 实时反馈: {e}", flush=True)
        
        time.sleep(3)

if __name__ == "__main__":
    main()
