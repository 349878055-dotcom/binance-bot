import requests
import time

def main():
    # 验证站点 A: 币安期货 (看是否依然 400)
    binance_url = "https://fapi.binance.com/fapi/v1/allForceOrders"
    # 验证站点 B: Coingecko (第三方公开 API)
    gecko_url = "https://api.coingecko.com/api/v3/ping"

    print("🚀 [逻辑验证启动] 正在进行双向物理链路扫描...", flush=True)

    while True:
        try:
            # 1. 探测币安
            bn_res = requests.get(binance_url, params={'limit': 1}, timeout=5)
            print(f"📡 币安节点反馈: {bn_res.status_code}", flush=True)
            
            # 2. 探测第三方
            gk_res = requests.get(gecko_url, timeout=5)
            print(f"🌐 第三方(Gecko)反馈: {gk_res.status_code} {gk_res.json()}", flush=True)

            if bn_res.status_code == 400 and gk_res.status_code == 200:
                print("❌ [定论] 机房物理通畅，但币安已将该 IP 段永久封锁。必须更换 Region。", flush=True)
                break
                
        except Exception as e:
            print(f"⚠️ 物理震荡: {e}", flush=True)
        
        time.sleep(5)

if __name__ == "__main__":
    main()
