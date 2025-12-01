# 角色定义
define role1 = Character('高贵的少女', color="#700c40", image="role1")
define role2 = Character('仁慈的少女', color="#04a136", image="role2")
define role3 = Character('冷静的少女', color="#0f96d9", image="role3")
define role4 = Character('正义的少女', color="#bcdf11", image="role4")
define role5 = Character('怀罪的少女们', color="#f31414", image="role5")
define role6 = Character('？', color="#fcbf07", image="role6")
define role7 = Character('远藤伊甸', color="#5151eb", image="role7")

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