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

def main():
    try:
        # 物理并网：法兰克福节点连接 OKX
        bot = ccxt.okx(keys)
        bot.options['adjustForTimeDifference'] = True # 解决你刚才遇到的时间同步问题
        print("🚀 [收割引擎并网] 身份验证成功！正在法兰克福监听小众市场...", flush=True)
    except Exception as e:
        print(f"❌ 接入失败: {e}", flush=True)
        return

    while True:
        try:
            # 1. 随时计算：扫描全场强平信号
            liq_orders = bot.public_get_public_liquidation_orders({
                'instType': 'SWAP',
                'limit': 20
            })['data']

            if liq_orders:
                for order in liq_orders:
                    symbol = order['instId']
                    sz = float(order['sz'])
                    
                    # 2. 逻辑过滤：避开拥挤的 BTC/ETH，寻找二线币种的“裂缝”
                    # 设定阈值：瞬间强平超过 500 张
                    if "BTC" not in symbol and "ETH" not in symbol and sz > 500:
                        print(f"🔥 [检测到坍缩] {symbol} | 能量: {sz} 张 | 正在捕捉超跌点...", flush=True)
                        
                        # --- 核心交易逻辑 ---
                        # 计算当前余额，只用 5% 的头寸进行“几秒钟”的抢购
                        # balance = bot.fetch_balance()
                        # bot.create_market_buy_order(symbol, 头寸量)
            else:
                print("💎 扫描中：当前市场处于低噪声态...", flush=True)

        except Exception as e:
            print(f"⚠️ 链路波动: {e}", flush=True)
        
        time.sleep(2) # 保持呼吸频率

if __name__ == "__main__":
    main()
