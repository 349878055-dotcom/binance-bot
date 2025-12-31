import requests
import time
import sys

def main():
    url = "https://fapi.binance.com/fapi/v1/allForceOrders"
    print("🚀 [俄勒冈并网] 身份已刷新，开始执行穿透...", flush=True)

    while True:
        try:
            # 在美国西海岸节点，流量特征是干净的
            response = requests.get(url, params={'limit': 100}, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                print(f"🔥 [能量释放] 成功！当前捕获 {len(data)} 条实时强平信号", flush=True)
            else:
                # 即使在俄勒冈也输出状态，确保我们知道发生了什么
                print(f"⚠️ 状态反馈: {response.status_code} - {response.text}", flush=True)
                
        except Exception as e:
            print(f"⚠️ 链路震荡: {e}", flush=True)
        
        # 即使报错也不退出，保持进程驻留
        time.sleep(3)

if __name__ == "__main__":
    main()
