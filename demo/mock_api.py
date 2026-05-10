#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MiMo API 模拟器
用于开发阶段的测试，待正式 Token 到账后替换为真实 API
"""

import random
import time
from typing import Dict, Optional


class MiMoMockAPI:
    """MiMo 模型 API 模拟器"""
    
    def __init__(self):
        self.api_calls = 0
        self.total_tokens = 0
        
    def chat_completion(self, prompt: str, context: Optional[str] = None) -> Dict:
        """模拟对话补全接口"""
        self.api_calls += 1
        tokens_used = len(prompt) // 2 + random.randint(50, 200)
        self.total_tokens += tokens_used
        
        # 模拟推理延迟
        time.sleep(0.2)
        
        return {
            "id": f"mock_{self.api_calls}",
            "model": "MiMo-V2.5-Pro",
            "choices": [{
                "message": {
                    "role": "assistant",
                    "content": f"Received: {prompt[:50]}... (mock response)"
                }
            }],
            "usage": {
                "prompt_tokens": len(prompt) // 2,
                "completion_tokens": tokens_used,
                "total_tokens": tokens_used + len(prompt) // 2
            }
        }
    
    def visual_understanding(self, image_base64: str) -> Dict:
        """模拟视觉理解接口"""
        self.api_calls += 1
        self.total_tokens += 800
        
        time.sleep(0.3)
        
        return {
            "scene": "living_room",
            "objects": ["sofa", "tv", "table", "person"],
            "confidence": 0.87,
            "description": "A living room with a person sitting on the sofa"
        }
    
    def get_stats(self) -> Dict:
        return {
            "api_calls": self.api_calls,
            "total_tokens": self.total_tokens
        }


# 使用示例
if __name__ == "__main__":
    api = MiMoMockAPI()
    result = api.chat_completion("打开客厅的灯")
    print(result)
