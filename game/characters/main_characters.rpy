# 角色定义
define maidenNoble = DynamicynamicCharacter('高贵的少女', color="#0707F3", image="role1")
define maidenMerciful = DynamicynamicCharacter('仁慈的少女', color="#04a136", image="role2")
define maidenCalm = DynamicynamicCharacter('冷静的少女', color="#E66C00", image="role3")
define maidenJustice = DynamicynamicCharacter('正义的少女', color="#878905", image="role4")
define maidenGuilty = DynamicynamicCharacter('怀罪的少女们', color="#f31414", image="role5")
define mistery = DynamicynamicCharacter('？', color="#0c0901", image="role6")
define endoEden = DynamicynamicCharacter('远藤伊甸', color="#8307eb", image="role7")

# 叙述者定义
define narrator_nvl = Character(None, kind=nvl)
define narrator_adv = Character(None, kind=adv)

# 音频配置
define config.voice_filename_format = "audio/{filename}"

# 角色颜色变化函数（用于不同章节）
init python:
    def set_chapter_colors():
        """设置章节特定的角色颜色"""
        role1.what_args["color"] = "#c8c8ff"
        role2.what_args["color"] = "#c8c8ff"
        role3.what_args["color"] = "#c8c8ff"
        role4.what_args["color"] = "#c8c8ff"
        role5.what_args["color"] = "#c8c8ff"
        role6.what_args["color"] = "#c8c8ff"
        role7.what_args["color"] = "#c8c8ff"
    
    def reset_eden_color():
        """重置远藤伊甸的原始颜色"""
        role7.what_args["color"] = "#5151eb"