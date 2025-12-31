import ccxt
import time

# --- 物理密钥填装：这是你的银行卡和密码 ---
keys = {
    'apiKey': '26a747cf-7bc6-4a73-be7d-52dc56dc8106',
    'secret': 'E897F21E2C4001F8E35B51FF2AB46541',
    'password': 'Jintao0341$',
    'enableRateLimit': True,
    'options': {'defaultType': 'swap'}
}

def fetch_liquidation_orders():
    """
    针对 OKX V5 协议的硬核重写
    摒弃旧的 public_get_public_liquidation_orders
    """
    try:
        # 显式映射：OE V5 市场清算数据端点
        params = {'instType': 'SWAP'} # 监控永续合约
        
        # 1.0 刚性调用：使用当前版本 CCXT 支持的显式方法
        response = exchange.publicGetMarketPlatformLiquidationOrders(params)
        
        data = response.get('data', [])
        if data:
            for order in data:
                print(f"📡 清算预警: 币种={order['instId']} | 数量={order['sz']} | 价格={order['bkPx']}")
        else:
            print("📭 当前无清算订单数据溢出")
            
    except AttributeError:
        print("❌ 协议映射失效：请检查 CCXT 版本，建议执行 pip install --upgrade ccxt")
    except Exception as e:
        print(f"⚠️ 链路波动: {str(e)}")

def main():
    print("🚀 系统入位，主权接管开始...")
    while True:
        try:
            # 逻辑映射：验证余额与清算数据
            # balance = exchange.fetch_balance() # 如需监控余额可开启
            fetch_liquidation_orders()
            
            # 强行留白：防止请求过快导致 IP 被锁
            time.sleep(10) 
            
        except Exception as e:
            print(f"🔥 核心逻辑溢出: {e}")
            time.sleep(30)

if __name__ == "__main__":
    main()
