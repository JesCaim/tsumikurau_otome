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