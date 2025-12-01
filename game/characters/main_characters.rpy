init python:
    class GameCharacter:
        """角色状态管理类"""
        def __init__(self, base_name, color, image, **kwargs):
            self.base_name = base_name
            self.display_name = base_name
            self.color = color
            self.image = image
            # 核心：创建动态角色对象
            self.character = DynamicCharacter(f'"{self.display_name}"', color=color, image=image, **kwargs)
            
            # === 角色状态变量 ===
            self.is_alive = True          # 存活状态
            self.trust_level = 0          # 对主角信任度 -100~100
            self.suspicion = 0            # 嫌疑值
            self.known_facts = []         # 该角色已知的秘密
            self.sin_type = None          # 罪孽类型（七宗罪）
        
        def say(self, text):
            """让角色说话"""
            return self.character(text)
        
        def set_display_name(self, new_name):
            """动态改变显示名称（用于身份揭示）"""
            self.display_name = new_name
        
        def die(self):
            """角色死亡处理"""
            self.is_alive = False
            self.set_display_name(f"†{self.base_name}†")
            # 死亡时改变颜色为灰色
            self.character.who_args["color"] = "#888888"
        
        def learn_fact(self, fact_id, fact_name):
            """角色学会一个事实（用于解锁对话）"""
            if fact_id not in self.known_facts:
                self.known_facts.append({"id": fact_id, "name": fact_name})
        
        def knows_fact(self, fact_id):
            """检查角色是否知道某个事实"""
            return any(fact["id"] == fact_id for fact in self.known_facts)
        
        def add_trust(self, amount):
            """增加/减少信任度"""
            self.trust_level = max(-100, min(100, self.trust_level + amount))
        
        def reveal_identity(self, true_identity, new_color=None):
            """揭示真实身份（化名->真名）"""
            self.true_identity = true_identity
            self.set_display_name(f"{self.base_name}\n<size=20>{true_identity}</size>")
            if new_color:
                self.character.who_args["color"] = new_color

# === 初始化你的游戏角色（使用GameCharacter类）===

# 七位仪式少女
define maidenNoble = GameCharacter("高贵的少女", "#0707F3", "role1")
define maidenMerciful = GameCharacter("仁慈的少女", "#04a136", "role2")
define maidenCalm = GameCharacter("冷静的少女", "#E66C00", "role3")
define maidenJustice = GameCharacter("正义的少女", "#878905", "role4")
define maidenGuilty = GameCharacter("怀罪的少女们", "#f31414", "role5")
define mistery = GameCharacter("？", "#0c0901", "role6")

# 主角 - 远藤伊甸
define endoEden = GameCharacter("远藤伊甸", "#8307eb", "role7")

# 为角色设置罪孽类型（七宗罪）
init python:
    maidenNoble.sin_type = "pride"       # 傲慢
    maidenMerciful.sin_type = "envy"     # 嫉妒
    maidenCalm.sin_type = "wrath"        # 愤怒
    maidenJustice.sin_type = "sloth"     # 懒惰
    maidenGuilty.sin_type = "greed"      # 贪婪
    mistery.sin_type = "gluttony"        # 暴食
    endoEden.sin_type = "lust"           # 色欲

# 叙述者定义（保持不变）
define narrator_nvl = Character(None, kind=nvl)
define narrator_adv = Character(None, kind=adv)

# 音频配置（保持不变）
define config.voice_filename_format = "audio/{filename}"