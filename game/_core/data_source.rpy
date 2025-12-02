init python:
    class GameCharacter:
        """角色状态管理类"""
        def __init__(self, base_name, color, image, **kwargs):
            self.base_name = base_name
            self.display_name = base_name
            self.color = color
            self.image_tag = image
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

        def show(self, expression="normal", transition=dissolve):
            """
            显示角色立绘或切换差分
            expression: 差分属性 (如 "smile", "angry")
            """
            # 组合成 Ren'Py 识别的字符串，例如 "role1 smile"
            image_spec = f"{self.image_tag} {expression}"
            
            # 调用 Ren'Py 内部函数显示图片
            renpy.show(image_spec, at_list=[center], transition=transition)

        def hide(self, transition=dissolve):
            """隐藏角色"""
            renpy.hide(self.image_tag, transition=transition)
        
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

