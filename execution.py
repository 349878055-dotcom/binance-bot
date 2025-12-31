import ccxt
import time

def main():
    # 逻辑归零：只把 ccxt 当成一个授权和连接工具
    exchange = ccxt.binanceusdm({
        'timeout': 15000,
        'enableRateLimit': True
    })

    print("🚀 [物理接管] 绕过所有封装属性，直接请求底层 API 路径...", flush=True)

    while True:
        try:
            # 【核心修正】不再调用 exchange.xxxx()，直接用 request 手动指定路径
            # 这叫“路径击穿”，是程序员最后的保底手段
            response = exchange.request('allForceOrders', 'fapiPublic', 'GET', {'limit': 100})
            
            if response and isinstance(response, list):
                print(f"🔥 [确定性捕获] 实时强平信号：{len(response)} 条", flush=True)
                for o in response[:3]:
                    val = float(o['origQty']) * float(o['price'])
                    print(f"   ∟ {o['symbol']} | {o['side']} | 价值: ${val:,.0f}", flush=True)
            else:
                print("💎 链路正常，无爆仓能量释放...", flush=True)
                
        except Exception as e:
            # 捕获报错并输出，如果是 429 说明太快了，如果是 404 说明路径写错了
            print(f"⚠️ 物理反馈: {e}", flush=True)
            if "429" in str(e):
                time.sleep(60) # 被限频则静默 1 分钟
        
        time.sleep(3) # 降噪频率

if __name__ == "__main__":
    main()
