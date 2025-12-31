import ccxt
import time
import os

def main():
    # 云端环境下，物理链路是天然打通的，无需任何代理配置
    exchange = ccxt.binanceusdm({
        'timeout': 20000,
        'enableRateLimit': True,
        'options': {'defaultType': 'future'}
    })

    print("🚀 [云端主权已锁定] 正在实时同步全球强平订单流...", flush=True)

    while True:
        try:
            # 获取全网实时强平单
            response = exchange.request('allForceOrders', 'public', 'GET', {'limit': 100})
            
            if response:
                print(f"🔥 [脉冲捕获] 实时信号：{len(response)} 条", flush=True)
                for order in response[:5]:
                    symbol = order['symbol']
                    side = "🔴 多头坍缩" if order['side'] == 'SELL' else "🟢 空头炸裂"
                    val = float(order['origQty']) * float(order['price'])
                    print(f"   ∟ [{symbol}] {side} | 规模: ${val:,.0f}", flush=True)
            
        except Exception as e:
            # 如果云端也报错，通常是 API 频率限制，无需担心物理断连
            print(f"⚠️ 系统震荡反馈: {e}", flush=True)
        
        time.sleep(2.5) # 频率锚定，防止 IP 被临时灰度

if __name__ == "__main__":
    main()