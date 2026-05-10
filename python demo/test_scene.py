
---

## 📄 文件 2：`demo/test_scene.py`

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Home AI Agent - 场景测试脚本
用于测试全屋智能管家的核心功能
"""

import json
import time
import logging
from typing import Dict, List, Optional
from datetime import datetime

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


class MockMiMoAPI:
    """
    MiMo API 模拟器（开发阶段使用）
    待正式 Token 到账后替换为真实 API 调用
    """
    
    def __init__(self):
        self.total_tokens_used = 0
        
    def scene_inference(self, command: str, context: Optional[Dict] = None) -> Dict:
        """
        场景推理 - 模拟 MiMo-V2.5-Pro 的推理能力
        """
        logger.info(f"Processing command: '{command}'")
        
        # 模拟推理耗时
        time.sleep(0.3)
        
        # 基于关键词的场景识别
        command_lower = command.lower()
        
        if "睡觉" in command_lower or "good night" in command_lower:
            return self._bedtime_scene()
        elif "出门" in command_lower or "离家" in command_lower:
            return self._leave_home_scene()
        elif "回家" in command_lower or "进门" in command_lower:
            return self._arrive_home_scene()
        elif "吃饭" in command_lower or "dinner" in command_lower:
            return self._dinner_scene()
        elif "电影" in command_lower or "movie" in command_lower:
            return self._movie_scene()
        else:
            return self._default_scene(command)
    
    def visual_understanding(self, image_description: str) -> Dict:
        """
        视觉理解 - 模拟 MiMo-VL-7B 的视觉能力
        """
        logger.info(f"Analyzing scene: '{image_description}'")
        
        # 模拟视觉推理
        time.sleep(0.2)
        
        if "小孩" in image_description and "写作业" in image_description:
            return {
                "scene": "child_studying",
                "confidence": 0.92,
                "actions": [
                    {"device": "desk_lamp", "action": "set_brightness", "value": 80},
                    {"device": "curtain", "action": "close", "value": 50},
                    {"device": "thermostat", "action": "set_temperature", "value": 24}
                ],
                "message": "检测到孩子正在写作业，已调整灯光和室温"
            }
        elif "老人" in image_description and "摔倒" in image_description:
            return {
                "scene": "emergency_fall",
                "confidence": 0.98,
                "actions": [
                    {"device": "alert", "action": "send_notification", "value": "family_members"},
                    {"device": "speaker", "action": "play_audio", "value": "紧急情况，请检查老人状况"}
                ],
                "message": "⚠️ 检测到老人摔倒，已发送紧急通知"
            }
        else:
            return {
                "scene": "normal",
                "confidence": 0.70,
                "actions": [],
                "message": "未检测到特殊场景"
            }
    
    def _bedtime_scene(self) -> Dict:
        """就寝场景"""
        tokens_used = 1247
        self.total_tokens_used += tokens_used
        
        return {
            "scene": "bedtime",
            "confidence": 0.94,
            "tokens_used": tokens_used,
            "reasoning_steps": [
                "Step 1: 识别意图 → '睡觉' 表示用户准备休息",
                "Step 2: 时间检查 → 当前时间适合就寝模式",
                "Step 3: 环境评估 → 客厅灯亮，卧室灯未开",
                "Step 4: 生成动作序列 → 关客厅灯，开卧室夜灯，调空调"
            ],
            "actions": [
                {"device": "living_room_light", "action": "turn_off", "value": None},
                {"device": "bedroom_light", "action": "set_brightness", "value": 20},
                {"device": "bedroom_curtain", "action": "close", "value": 100},
                {"device": "ac", "action": "set_mode", "value": "sleep_24c"},
                {"device": "door_lock", "action": "check", "value": "locked"}
            ],
            "message": "晚安，已为您准备好舒适的睡眠环境"
        }
    
    def _leave_home_scene(self) -> Dict:
        """离家场景"""
        tokens_used = 893
        self.total_tokens_used += tokens_used
        
        return {
            "scene": "leave_home",
            "confidence": 0.96,
            "tokens_used": tokens_used,
            "reasoning_steps": [
                "Step 1: 识别意图 → '出门' 表示用户即将离家",
                "Step 2: 安全检查 → 检测门窗状态",
                "Step 3: 节能优化 → 关闭非必要设备",
                "Step 4: 安防布防 → 启动离家模式"
            ],
            "actions": [
                {"device": "all_lights", "action": "turn_off", "value": None},
                {"device": "all_ac", "action": "turn_off", "value": None},
                {"device": "air_purifier", "action": "turn_off", "value": None},
                {"device": "security_system", "action": "arm", "value": "away"},
                {"device": "robot_vacuum", "action": "start", "value": "full_clean"}
            ],
            "message": "已开启离家模式，设备已关闭，安防已布防"
        }
    
    def _arrive_home_scene(self) -> Dict:
        """回家场景"""
        tokens_used = 1056
        self.total_tokens_used += tokens_used
        
        return {
            "scene": "arrive_home",
            "confidence": 0.95,
            "tokens_used": tokens_used,
            "reasoning_steps": [
                "Step 1: 识别意图 → '回家' 表示用户即将到家",
                "Step 2: 环境准备 → 提前开启舒适环境",
                "Step 3: 安全验证 → 人脸识别解锁",
                "Step 4: 个性化设置 → 根据用户偏好调整"
            ],
            "actions": [
                {"device": "door_lock", "action": "unlock", "value": "face_id"},
                {"device": "living_room_light", "action": "turn_on", "value": 60},
                {"device": "ac", "action": "set_temperature", "value": 24},
                {"device": "curtain", "action": "open", "value": 80},
                {"device": "speaker", "action": "play_greeting", "value": "welcome_home"}
            ],
            "message": "欢迎回家，已为您准备好舒适的环境"
        }
    
    def _dinner_scene(self) -> Dict:
        """用餐场景"""
        tokens_used = 762
        self.total_tokens_used += tokens_used
        
        return {
            "scene": "dinner",
            "confidence": 0.91,
            "tokens_used": tokens_used,
            "actions": [
                {"device": "dining_light", "action": "set_brightness", "value": 70},
                {"device": "dining_light", "action": "set_color", "value": "warm"},
                {"device": "speaker", "action": "play_music", "value": "dinner_jazz"},
                {"device": "air_purifier", "action": "set_speed", "value": "low"}
            ],
            "message": "已切换到用餐模式，祝您用餐愉快"
        }
    
    def _movie_scene(self) -> Dict:
        """观影场景"""
        tokens_used = 845
        self.total_tokens_used += tokens_used
        
        return {
            "scene": "movie",
            "confidence": 0.93,
            "tokens_used": tokens_used,
            "actions": [
                {"device": "living_room_light", "action": "set_brightness", "value": 10},
                {"device": "curtain", "action": "close", "value": 100},
                {"device": "tv", "action": "turn_on", "value": None},
                {"device": "speaker", "action": "set_volume", "value": 25}
            ],
            "message": "已切换到观影模式，享受您的电影时光"
        }
    
    def _default_scene(self, command: str) -> Dict:
        """默认场景"""
        tokens_used = 324
        self.total_tokens_used += tokens_used
        
        return {
            "scene": "custom",
            "confidence": 0.65,
            "tokens_used": tokens_used,
            "actions": [
                {"device": "speaker", "action": "speak", "value": f"收到指令：{command}，已为您处理"}
            ],
            "message": f"已理解您的指令：{command}"
        }


class DeviceController:
    """设备控制器 - 模拟控制米家/Miloco设备"""
    
    def __init__(self):
        self.device_status = {
            "living_room_light": {"status": "off", "brightness": 0},
            "bedroom_light": {"status": "off", "brightness": 0},
            "ac": {"status": "off", "temperature": 26, "mode": "cool"},
            "curtain": {"status": "open", "percentage": 0},
            "door_lock": {"status": "locked", "battery": 85},
        }
    
    def execute(self, action: Dict) -> bool:
        """执行设备动作"""
        device = action.get("device")
        action_type = action.get("action")
        value = action.get("value")
        
        try:
            if device == "living_room_light":
                if action_type == "turn_off":
                    self.device_status["living_room_light"] = {"status": "off", "brightness": 0}
                    logger.info(f"✓ 执行: 客厅灯 → 关闭")
                elif action_type == "set_brightness":
                    self.device_status["living_room_light"] = {"status": "on", "brightness": value}
                    logger.info(f"✓ 执行: 客厅灯 → 亮度 {value}%")
                    
            elif device == "bedroom_light":
                if action_type == "set_brightness":
                    self.device_status["bedroom_light"] = {"status": "on", "brightness": value}
                    logger.info(f"✓ 执行: 卧室灯 → 亮度 {value}%")
                    
            elif device == "bedroom_curtain" or device == "curtain":
                if action_type == "close":
                    self.device_status["curtain"] = {"status": "closed", "percentage": value}
                    logger.info(f"✓ 执行: 窗帘 → 关闭 {value}%")
                elif action_type == "open":
                    self.device_status["curtain"] = {"status": "open", "percentage": value}
                    logger.info(f"✓ 执行: 窗帘 → 开启 {value}%")
                    
            elif device == "ac":
                if action_type == "set_mode" and "sleep_24c" in str(value):
                    self.device_status["ac"] = {"status": "on", "temperature": 24, "mode": "sleep"}
                    logger.info(f"✓ 执行: 空调 → 睡眠模式 24°C")
                elif action_type == "set_temperature":
                    self.device_status["ac"] = {"status": "on", "temperature": value, "mode": "auto"}
                    logger.info(f"✓ 执行: 空调 → 设置温度 {value}°C")
                elif action_type == "turn_off":
                    self.device_status["ac"] = {"status": "off", "temperature": 26, "mode": "off"}
                    logger.info(f"✓ 执行: 空调 → 关闭")
                    
            elif device == "door_lock":
                if action_type == "unlock":
                    self.device_status["door_lock"]["status"] = "unlocked"
                    logger.info(f"✓ 执行: 门锁 → 已解锁")
                elif action_type == "check":
                    logger.info(f"✓ 检查: 门锁状态 → {self.device_status['door_lock']['status']}")
                    
            elif device == "speaker":
                if action_type == "play_greeting":
                    logger.info(f"✓ 执行: 音箱 → 播放问候语: {value}")
                elif action_type == "play_music":
                    logger.info(f"✓ 执行: 音箱 → 播放音乐: {value}")
                elif action_type == "set_volume":
                    logger.info(f"✓ 执行: 音箱 → 音量设置为 {value}")
                elif action_type == "speak":
                    logger.info(f"✓ 执行: 音箱 → 语音播报: {value}")
                    
            elif device == "security_system":
                if action_type == "arm":
                    logger.info(f"✓ 执行: 安防系统 → 布防模式: {value}")
                    
            elif device == "robot_vacuum":
                if action_type == "start":
                    logger.info(f"✓ 执行: 扫地机器人 → 开始清扫: {value}")
                    
            elif device == "tv":
                if action_type == "turn_on":
                    logger.info(f"✓ 执行: 电视 → 已开启")
                    
            elif device == "air_purifier":
                if action_type == "set_speed":
                    logger.info(f"✓ 执行: 空气净化器 → 风速设置为 {value}")
                    
            elif device == "dining_light":
                if action_type == "set_brightness":
                    logger.info(f"✓ 执行: 餐厅灯 → 亮度 {value}%")
                elif action_type == "set_color":
                    logger.info(f"✓ 执行: 餐厅灯 → 色温设置为 {value}")
                    
            elif device == "desk_lamp":
                if action_type == "set_brightness":
                    logger.info(f"✓ 执行: 台灯 → 亮度 {value}%")
                    
            elif device == "alert":
                if action_type == "send_notification":
                    logger.info(f"✓ 执行: 告警 → 已发送通知给: {value}")
                    
            else:
                logger.warning(f"⚠️ 未知设备或动作: {device}/{action_type}")
                return False
                
            return True
            
        except Exception as e:
            logger.error(f"❌ 执行失败: {device} → {str(e)}")
            return False


class HomeAIAgent:
    """全屋 AI 智能管家 Agent"""
    
    def __init__(self):
        self.mimo_api = MockMiMoAPI()
        self.device_controller = DeviceController()
        self.total_actions_executed = 0
        
    def process_command(self, command: str) -> Dict:
        """处理用户自然语言指令"""
        logger.info("=" * 60)
        logger.info(f"🎤 接收指令: {command}")
        logger.info("=" * 60)
        
        # 1. 调用 MiMo API 进行场景推理
        result = self.mimo_api.scene_inference(command)
        
        # 2. 输出推理过程
        if "reasoning_steps" in result:
            logger.info("🧠 长链推理过程:")
            for step in result["reasoning_steps"]:
                logger.info(f"   {step}")
        
        # 3. 执行动作序列
        logger.info("🔧 执行动作序列:")
        actions = result.get("actions", [])
        for action in actions:
            if self.device_controller.execute(action):
                self.total_actions_executed += 1
        
        # 4. 输出结果
        logger.info("=" * 60)
        logger.info(f"✅ 执行完成 | 场景: {result['scene']} | 置信度: {result['confidence']}")
        logger.info(f"💬 {result.get('message', '执行完毕')}")
        logger.info(f"📊 本次消耗Token: {result.get('tokens_used', 'N/A')}")
        logger.info("=" * 60)
        
        return result
    
    def process_visual(self, image_description: str) -> Dict:
        """处理视觉输入（摄像头画面理解）"""
        logger.info("=" * 60)
        logger.info(f"📷 视觉输入: {image_description}")
        logger.info("=" * 60)
        
        result = self.mimo_api.visual_understanding(image_description)
        
        logger.info(f"🎯 识别场景: {result['scene']} (置信度: {result['confidence']})")
        
        actions = result.get("actions", [])
        for action in actions:
            self.device_controller.execute(action)
        
        logger.info(f"💬 {result.get('message', '处理完毕')}")
        logger.info("=" * 60)
        
        return result
    
    def get_stats(self) -> Dict:
        """获取运行统计"""
        return {
            "total_tokens_used": self.mimo_api.total_tokens_used,
            "total_actions_executed": self.total_actions_executed,
            "timestamp": datetime.now().isoformat()
        }


def main():
    """主测试函数"""
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║     Home AI Agent - 全屋智能管家测试脚本                  ║
    ║     基于 MiMo-VL-7B + Miloco 架构                        ║
    ║                                                          ║
    ║     正在参与 MiMo Orbit 百万亿 Token 计划                ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """)
    
    # 初始化 Agent
    agent = HomeAIAgent()
    
    # 测试场景列表
    test_scenes = [
        ("语音场景", "我准备睡觉了"),
        ("语音场景", "我要出门了"),
        ("语音场景", "我回家了"),
        ("语音场景", "准备吃饭"),
        ("语音场景", "我要看电影"),
        ("视觉场景", "摄像头检测到：一个6岁小孩正在书桌前写作业"),
        ("视觉场景", "摄像头检测到：一位老人摔倒在客厅地板上"),
    ]
    
    # 执行测试
    for scene_type, command in test_scenes:
        if scene_type == "语音场景":
            agent.process_command(command)
        else:
            agent.process_visual(command)
        print("\n" + "⏎" * 40 + "\n")
    
    # 输出统计信息
    stats = agent.get_stats()
    logger.info("📊 测试统计汇总:")
    logger.info(f"   总消耗Token: {stats['total_tokens_used']}")
    logger.info(f"   总执行动作数: {stats['total_actions_executed']}")
    logger.info(f"   测试完成时间: {stats['timestamp']}")
    
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║                    测试完成！                            ║
    ║                                                          ║
    ║  提示: 当前使用 Mock API 进行模拟测试                    ║
    ║  待 MiMo Token 到账后，替换为真实 API 调用               ║
    ║                                                          ║
    ║  MiMo Orbit 计划申请邮箱: [2295178533@qq.com]                     ║
    ╚══════════════════════════════════════════════════════════╝
    """)


if __name__ == "__main__":
    main()
