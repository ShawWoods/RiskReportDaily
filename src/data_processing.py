import pandas as pd
import requests
import logging
import yaml

logger = logging.getLogger('RiskReport.Data')

def load_config(config_file='config.yaml'):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)

def load_data(config):
    try:
        logger.info("开始加载数据")
        
        # 加载持仓明细
        holdings = pd.read_excel(config['file_paths']['holdings'], header=2, dtype={'证券代码': str})
        holdings['windcode'] = holdings['证券代码'].apply(lambda x: f"{x}.SH")
        logger.info(f"持仓明细加载完成，记录数：{len(holdings)}")
        
        # 加载产品净值
        netvalue = pd.read_excel(config['file_paths']['netvalue'], header=0)
        logger.info(f"产品净值加载完成，记录数：{len(netvalue)}")
        
        # 加载申赎明细
        transactions = pd.read_excel(config['file_paths']['transactions'], header=2).dropna(subset=['业务名称'])
        logger.info(f"申赎明细加载完成，记录数：{len(transactions)}")
        
        return holdings, netvalue, transactions
    except Exception as e:
        logger.error(f"数据加载失败：{str(e)}", exc_info=True)
        raise

def fetch_bond_data(config, codes, date):
    try:
        # 模拟数据（替换为东方财富 API）
        logger.info("使用模拟数据替代债券数据")
        return pd.DataFrame({
            'windcode': codes,
            'bond_type': ['企业债'] * len(codes),
            'issuer': ['测试发行人'] * len(codes),
            'modified_duration': [3.5] * len(codes),
            'convexity': [0.1] * len(codes)
        })
        # 实际 API 调用（取消注释以使用）
        # logger.info(f"调用东方财富 API，获取债券数据：{codes[:5]}...")
        # url = config['api']['eastmoney_url']
        # params = {
        #     'codes': ','.join(codes),
        #     'fields': 'bond_type,issuer,modified_duration,convexity',
        #     'date': date,
        #     'api_key': config['api']['api_key']
        # }
        # response = requests.get(url, params=params)
        # response.raise_for_status()
        # data = pd.DataFrame(response.json()['data'])
        # logger.info(f"债券数据获取成功，记录数：{len(data)}")
        # return data
    except Exception as e:
        logger.error(f"债券数据获取失败：{str(e)}", exc_info=True)
        raise
