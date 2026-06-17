"""
    测试：获取API_kEY和BASE_URL
    1、在项目的根目录下创建.env文件，文件中包含：
    OPENAI_API_KEY=xxx
    OPENAI_BASE_URL=xxx
    读取方式：
        import os
        from dotenv import load_dotenv
        # 使用load_dotenv()将.env文件中内容加载到系统的环境变量中
        load_dotenv()
        print(os.getenv("OPENAI_API_KEY"))
        print(os.getenv("OPENAI_BASE_URL"))

    2、在系统的环境变量中设置OPENAI_API_KEY和OPENAI_BASE_URL环境变量，此时可以直接获取环境变量中的数据
        print(os.getenv("OPENAI_API_KEY"))
        print(os.getenv("OPENAI_BASE_URL"))

"""

import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("OPENAI_API_KEY"))
print(os.getenv("OPENAI_BASE_URL"))