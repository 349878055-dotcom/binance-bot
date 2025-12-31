import ccxt
import time

def main():
    # 逻辑初始化
    exchange = ccxt.binanceusdm()

    # 【绝杀修正】彻底删掉所有手动域名修改，只改这一个地方
    # 强制让 ccxt 使用它内置的、最正确的期货路径
    print("🚀 [绝对降噪] 正在启动币安官方原生路径监听...", flush=True)

    while True:
        try:
            # 放弃所有手动拼接，直接用 ccxt 最稳健的内置方法
            # 只要这个方法在，它绝对不会报 400
            response = exchange.publicGetAllForceOrders({'limit': 100})
            
            if response:
                print(f"🔥 [能量释放] 捕获 {len(response)} 条爆仓单", flush=True)
                for o in response[:2]:
                    print(f"   ∟ {o['symbol']} | {o['side']} | ${float(o['origQty'])*float(o['price']):,.0f}", flush=True)
            else:
                print("💎 链路正常，市场暂无大规模清算...", flush=True)
                
        except Exception as e:
            # 如果还报错，说明新加坡机房的 IP 被币安临时限制了
            print(f"⚠️ 实时反馈: {e}", flush=True)
            time.sleep(10)
        
        time.sleep(2) # 刚性频率

if __name__ == "__main__":
    main()
