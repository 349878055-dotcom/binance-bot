import requests
import time

def main():
    # 物理路径归一化：手动写死币安期货 API 地址
    # 不再给 ccxt 任何乱拼路径的机会
    url = "https://fapi.binance.com/fapi/v1/allForceOrders"
    
    print("🚀 [物理级穿透] 正在绕过所有库，直接打击 API 端点...", flush=True)

    while True:
        try:
            # 逻辑回传：手动指定参数，不带任何身份验证（黄线是公开的）
            params = {'limit': 100}
            response = requests.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                print(f"🔥 [脉冲成功] 捕获 {len(data)} 条爆仓流", flush=True)
                for o in data[:2]:
                    print(f"   ∟ {o['symbol']} | {o['side']} | ${float(o['origQty'])*float(o['price']):,.0f}", flush=True)
            elif response.status_code == 400:
                # 如果还报 400，说明新加坡出口 IP 被币安 WAF 拦截
                print(f"⚠️ 物理拦截: 币安返回 400。判定：新加坡 IP 被标记。请立即更换 Region。", flush=True)
                break
            else:
                print(f"⚠️ 链路震荡: {response.status_code} {response.text}", flush=True)
                
        except Exception as e:
            print(f"⚠️ 网络反馈: {e}", flush=True)
        
        time.sleep(3)

if __name__ == "__main__":
    main()
