import requests
import time

def main():
    # 路径 A: 币安期货 (看是否依然报 400/451)
    bn_url = "https://fapi.binance.com/fapi/v1/allForceOrders"
    # 路径 B: 欧易 (OKX) 公开接口 (验证物理链路是否通畅)
    okx_url = "https://www.okx.com/api/v5/market/tickers?instType=SWAP"

    print("🚀 [全域对撞验证] 正在扫描：币安 vs 欧易...", flush=True)

    while True:
        # --- 探测 1: 币安 (Binance) ---
        try:
            bn_res = requests.get(bn_url, params={'limit': 10}, timeout=10)
            if bn_res.status_code == 200:
                print(f"🔥 [币安] 并网成功！捕获 {len(bn_res.json())} 条信号", flush=True)
            else:
                print(f"❌ [币安] 拦截：状态码 {bn_res.status_code} | 原因: {bn_res.text[:50]}", flush=True)
        except Exception as e:
            print(f"⚠️ [币安] 链路崩溃: {e}", flush=True)

        # --- 探测 2: 欧易 (OKX) ---
        try:
            okx_res = requests.get(okx_url, timeout=10)
            if okx_res.status_code == 200:
                # OKX 如果通了，说明你的法兰克福节点网络没问题
                data = okx_res.json().get('data', [])
                print(f"✅ [欧易] 验证通过！成功获取 {len(data)} 条行情数据", flush=True)
            else:
                print(f"❌ [欧易] 拦截：状态码 {okx_res.status_code}", flush=True)
        except Exception as e:
            print(f"⚠️ [欧易] 链路崩溃: {e}", flush=True)

        print("-" * 30)
        time.sleep(5)

if __name__ == "__main__":
    main()
