import requests
import time

def main():
    # OKX 期货强平接口（无需私钥，公开数据）
    # 逻辑：监听全网永续合约的爆仓单
    url = "https://www.okx.com/api/v5/public/liquidation-orders"
    
    # 锚定变数：只盯永续合约 (SWAP)
    params = {
        'instType': 'SWAP',
        'limit': 100
    }

    print("🚀 [OKX 链路锁定] 物理连接正常，开始高频监听因果流...", flush=True)

    while True:
        try:
            response = requests.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json().get('data', [])
                if data:
                    # 按照因果律排序，展示最新的爆仓能量释放
                    print(f"🔥 [能量释放] 捕获 {len(data)} 条实时强平", flush=True)
                    for o in data[:3]:
                        # 计算爆仓规模：张数 * 每张价值 (需要更精细计算，这里先展示核心维度)
                        posSide = o.get('posSide', '未知')
                        print(f"   ∟ {o['instId']} | {posSide}方向 | 总计: {o['sz']} 张", flush=True)
                else:
                    print("💎 链路正常，OKX 市场当前无大规模坍缩...", flush=True)
            else:
                print(f"⚠️ 链路震荡反馈: {response.status_code}", flush=True)
                
        except Exception as e:
            print(f"⚠️ 物理拦截反馈: {e}", flush=True)
        
        # OKX 限速相对宽松，3秒一次进行降噪
        time.sleep(3)

if __name__ == "__main__":
    main()
